import hashlib


def A3(Ki, RAND):
    return hashlib.sha256((Ki + RAND + "A3").encode()).hexdigest()[:8]


def A8(Ki, RAND):
    return hashlib.sha256((Ki + RAND + "A8").encode()).hexdigest()[:16]


def A5(text, key):
    answer = ""
    for i in range(len(text)):
        answer += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return answer


Ki = "secret"
RAND = "1234"

print("Authentication:", A3(Ki, RAND) == A3(Ki, RAND))

Kc = A8(Ki, RAND)
message = "Hello GSM"
encrypted = A5(message, Kc)

print("Encrypted:", [ord(x) for x in encrypted])
print("Decrypted:", A5(encrypted, Kc))
