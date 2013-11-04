import os
import plotly

py = plotly.plotly(username=os.getenv("PLOTLY_USERNAME"),
                   key=os.getenv("PLOTLY_APIKEY"))

categories = ["Dhrystone",
              "Whetstone",
              "Execl Throughput",
              "File Copy 1024",
              "File Copy 256",
              "File Copy 4096",
              "Pipe Throughput",
              "Pipe-based Ctx Switch",
              "Process Creation",
              "Shell Scripts (1)",
              "Shell Scripts (8)",
              "Syscall Overhead",
              "System Score",
             ]

CloudServers = {"name": "Cloud Severs",
           "x": categories,
           "y": [2027.7,
                 547.433333333333,
                 279.816666666667,
                 574.3,
                 376.366666666667,
                 1071.2,
                 300.983333333333,
                 155.933333333333,
                 202.933333333333,
                 658.916666666667,
                 613.366666666667,
                 214.6,
                 444.433333333333,
                ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [2579.51666666667,
                 529.95,
                 329.716666666667,
                 780.1,
                 480.266666666667,
                 1808.26666666667,
                 362.083333333333,
                 204.266666666667,
                 240.416666666667,
                 780.8,
                 733.883333333333,
                 306.35,
                 560.1,
               ],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Servers (HVM)",
           "x": categories,
           "y": [2578.53333333333,
                 529.216666666667,
                 918.65,
                 2562.15,
                 1693.1,
                 4718.93333333333,
                 1470.1,
                 769.983333333333,
                 1107.03333333333,
                 1711.11666666667,
                 1601.43333333333,
                 2516.31666666667,
                 1568.45,
               ],
            "type": "bar"}

legend_style = {"font": {"size": 10}}

layout = {"title": "Unixbench on 1GB Servers",
          "barmode": "group",
          "xaxis": {"type": "category"},
          "yaxis": {"name": "Index"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="unixbench_1gb",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

