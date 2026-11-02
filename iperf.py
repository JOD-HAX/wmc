data = float(input("Data in MB: "))
time = float(input("Time in seconds: "))

speed = data * 8 / time

print("Throughput =", round(speed, 2), "Mbps")
print("iPerf3 port = 5201")
print("Ping measures latency")
