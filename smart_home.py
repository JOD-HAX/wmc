motion = input("Motion detected? yes/no: ")
temperature = float(input("Temperature: "))

light = "OFF"
fan = "OFF"

if motion.lower() == "yes":
    light = "ON"

if temperature > 30:
    fan = "ON"

print("Light =", light)
print("Fan =", fan)
