f = open("data.txt", "w")
print(f.write("Hello\n"))
print(f.write("world\n"))
f.close()

f = open("data.txt")
text = f.read()
print(text)
print(text.split())

for line in open("data.txt"):
    print(line)

# print(dir(f))
# print(help(f.seek))


# 二进制字节文件
import struct

packed = struct.pack(">i4sh", 7, b"spam", 8)
print(packed)

file = open("data.bin", "wb")
print(file.write(packed))
file.close()

data = open("data.bin", "rb").read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack(">i4sh", data))


# unicode 文本文件
S = "sp\xc4m"
print(S)
print(S[2])

file = open("unidata.txt", "w", encoding="utf-8")
print(file.write(S))
file.close()
