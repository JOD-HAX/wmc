barker = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
data = input("Binary data: ")
spread = []

for number in data:
    chips = []
    for bit in barker:
        chips.append(bit ^ int(number))
    spread.append(chips)

answer = ""
for chips in spread:
    answer += str(chips[0] ^ barker[0])

print("Spread:", spread)
print("Recovered:", answer)
