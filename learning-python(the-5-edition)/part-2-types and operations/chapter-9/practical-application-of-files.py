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

line = f.readline()
print(line)
parts = line.split(",")
print(parts)
# print(help(line.split))
print("\n")

print(int(parts[1]))
numbers = [int(p) for p in parts]
print(numbers)
print("\n")

line = f.readline()
# print(help(f.readline))
print(line)
parts = line.split("$")
print(parts)
print(eval(parts[0]))
print(type(eval(parts[0])))
objects = [eval(p) for p in parts]
print(objects)
print("\n")


# 存储 Python 原生对象：pickle
d = {"a": 1, "b": 2}
f = open("datafile.pkl", "wb")
import pickle

pickle.dump(d, f)
f.close()

f = open("datafile.pkl", "rb")
e = pickle.load(f)
print(e)
print("\n")
