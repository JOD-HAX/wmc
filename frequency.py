import math

N = int(input("Cluster size: "))
R = float(input("Cell radius: "))
D = R * math.sqrt(3 * N)

print("Reuse distance =", round(D, 2))
