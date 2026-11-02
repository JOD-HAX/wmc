wifi = [
    ["HomeWiFi", -48, 6],
    ["CollegeWiFi", -70, 11]
]

ble = [
    ["Watch", "AA:BB:CC:11:22:33", -55],
    ["No Name", "11:22:33:AA:BB:CC", -80]
]

print("Wi-Fi scan")
for device in wifi:
    print(device[0], device[1], "dBm", "Channel", device[2])

print("\nBLE scan")
for device in ble:
    print(device[0], device[1], device[2], "dBm")
