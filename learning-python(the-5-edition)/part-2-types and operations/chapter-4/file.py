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

text = open("unidata.txt", encoding="utf-8").read()
print(text)
print(len(text))

raw = open("unidata.txt", "rb").read()
print(raw)
print(len(raw))

print(text.encode("utf-8"))
print(raw.decode("utf-8"))

print(text.encode("latin-1"))
print(text.encode("utf-16"))

print(len(text.encode("latin-1")), len(text.encode("utf-16")))
print(text.encode("utf-16").decode("utf-16"))

import codecs

print(codecs.open("unidata.txt", encoding="utf-8").read())
print(open("unidata.txt", "rb").read())
print(open("unidata.txt").read())
