import os
import plotly

py = plotly.plotly(username=os.getenv("PLOTLY_USERNAME"),
                   key=os.getenv("PLOTLY_APIKEY"))

categories = ["1GB Server",
              "30GB Server"]

CloudServers = {"name": "Cloud Servers",
           "x": categories,
           "y": [867.2285,
                 138.175333333333,
                ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [819.282833333333,
                 114.945666666667,
                ],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Servers (HVM)",
           "x": categories,
           "y": [694.584333333333,
                 97.1143333333333,
                ],
            "type": "bar"}

legend_style = {"font": {"size": 10},}
                #"x": 0, "y": 1}

layout = {"title": "Linux Kernel Compilation Time",
          "barmode": "group",
          "xaxis": {"type": "category",
                    "name": "Server Type"},
          "yaxis": {"name": "Seconds"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="kernel_compile",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

