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

CloudServers = {"name": "Cloud Servers",
           "x": categories,
           "y": [2070.26666666667,
                 549.466666666667,
                 197.75,
                 574.25,
                 371.916666666667,
                 1026.91666666667,
                 298.933333333333,
                 74.8666666666667,
                 107.933333333333,
                 753.366666666667,
                 1985.93333333333,
                 213.166666666667,
                 428.166666666667,
               ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [2577.11666666667,
                 529.516666666667,
                 265.916666666667,
                 503.483333333333,
                 340.083333333333,
                 1421.75,
                 305.966666666667,
                 93.3166666666667,
                 193.95,
                 996.883333333333,
                 2652.71666666667,
                 272.083333333333,
                 515.3
                ],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Severs (HVM)",
           "x": categories,
           "y": [2579.85,
                 528.933333333333,
                 694.2,
                 2217.73333333333,
                 1444.3,
                 4307.26666666667,
                 1362.01666666667,
                 708.316666666667,
                 662.25,
                 2070.25,
                 6902.88333333333,
                 2206.15,
                ],
            "type": "bar"}

legend_style = {"font": {"size": 10},
                "x": 0, "y": 1}

layout = {"title": "Unixbench on 30GB Servers (8 CPUs, 1 process)",
          "barmode": "group",
          "xaxis": {"type": "category"},
          "yaxis": {"name": "Index"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="unixbench_30gb_1proc",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

