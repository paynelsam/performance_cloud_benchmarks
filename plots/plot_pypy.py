import os
import plotly

py = plotly.plotly(username=os.getenv("PLOTLY_USERNAME"),
                   key=os.getenv("PLOTLY_APIKEY"))

categories = ["30GB Server",]

CloudServers = {"name": "Cloud Servers",
           "x": categories,
           "y": [7509.5, ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [6150.13333333333,],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Servers (HVM)",
           "x": categories,
           "y": [6217.28333333333,],
            "type": "bar"}

legend_style = {"font": {"size": 10},}
                #"x": 0, "y": 1}

layout = {"title": "PyPy Translation Time",
          "barmode": "group",
          "xaxis": {"type": "category",
                    "name": "Server Type"},
          "yaxis": {"name": "Seconds"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="pypy_translate",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

