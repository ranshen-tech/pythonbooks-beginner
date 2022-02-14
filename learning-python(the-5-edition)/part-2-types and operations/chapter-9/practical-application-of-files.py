myfile = open("myfile.txt", "w")
# print(help(myfile.write))
print(myfile.write("hello text file\n"))
print(myfile.write("goodbye text file\n"))
myfile.close()
print("\n")

myfile = open("myfile.txt")
# print(help(open))
a = myfile.readline()
print(a)
b = myfile.readline()
print(b)
print(myfile.readline())

x = open("myfile.txt").read()
print(x)
print(open("myfile.txt").read())
print("\n")

for line in open("myfile.txt"):
    print(line, end="")
print("\n")

# data = open("data.bin", "rb").read()
# print(data)
# print("\n")

x, y, z = 43, 44, 45
s = "spam"
d = {"a": 1, "b": 2}
l = [1, 2, 3]

f = open("datafile.txt", "w")
f.write(s + "\n")
f.write("%s,%s,%s\n" % (x, y, z))
f.write(str(l) + "$" + str(d) + "\n")
f.close()

chars = open("datafile.txt").read()
print(chars)
print("\n")

f = open("datafile.txt")
line = f.readline()
print(line)
print(line.rstrip())
print("\n")
