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
           "y": [13745.6,
                 3996.76666666667,
                 1000.91666666667,
                 655.5,
                 414.05,
                 1392,
                 2083.66666666667,
                 878.533333333333,
                 670,
                 2802.01666666667,
                 2700.71666666667,
                 967.916666666667,
                 1546.06666666667,
                ],
            "type": "bar"}

PerfCloudServers = {"name": "Performance Cloud Servers",
           "x": categories,
           "y": [20460.66,
                 4219.04,
                 1362.02,
                 688.9,
                 414.92,
                 1724.8,
                 2368,
                 1152.48,
                 917.3,
                 3800.2,
                 3695.94,
                 1725.5,
                 1974.24,
                ],
            "type": "bar"}

PerfCloudServersHVM = {"name": "Performance Cloud Servers (HVM)",
           "x": categories,
           "y": [20564.5333333333,
                 4219.11666666667,
                 4846.51666666667,
                 1817.38333333333,
                 1226.31666666667,
                 4058.48333333333,
                 10849.2166666667,
                 4269.68333333333,
                 4879.43333333333,
                 10825.6166666667,
                 10730.9166666667,
                 2320.2,
                 4976.26666666667,
                ],
            "type": "bar"}

legend_style = {"font": {"size": 10}}

layout = {"title": "Unixbench on 30GB Servers (8 CPUs, 8 processes)",
          "barmode": "group",
          "xaxis": {"type": "category"},
          "yaxis": {"name": "Index"},
          "categories": categories,
          "legend": legend_style}

response = py.plot([CloudServers, PerfCloudServers, PerfCloudServersHVM],
                   layout=layout,
                   filename="unixbench_30gb_8procs",
                   fileopt="overwrite")

print "url=", response["url"]
print "filename=", response["filename"]

