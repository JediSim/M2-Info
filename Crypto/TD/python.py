file = open("c0", "rb")

data = file.read()

print(data)

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def getPoidsFort(byte):
    return byte >> 6




file.close()