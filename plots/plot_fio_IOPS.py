import os
import plotly

py = plotly.plotly(username=os.getenv("PLOTLY_USERNAME"),
                   key=os.getenv("PLOTLY_APIKEY"))

categories = ["1GB Server",
              "30GB Server"]

CloudServers = {"name": "Cloud Servers",
           "x": categories,
           "y": [393.333333333333,
                 1064
                ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [20134.5,
                 21666.1666666667
                ],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Servers (HVM)",
           "x": categories,
           "y": [19791.6666666667,
                 22437
                ],
            "type": "bar"}

legend_style = {"font": {"size": 10},
                "x": 0, "y": 1}

layout = {"title": "IOPS (16K blocks)",
          "barmode": "group",
          "xaxis": {"type": "category"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="fio_IOPS",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

