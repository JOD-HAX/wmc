network = {
    "3G": "UE -> Node B -> RNC -> Core",
    "4G": "UE -> eNodeB -> EPC",
    "5G": "UE -> gNB -> 5GC"
}

for generation in network:
    print(generation, "=", network[generation])

print("RSRP = Signal power")
print("RSRQ = Signal quality")
