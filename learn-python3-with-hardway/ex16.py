from sys import argv

script, filename = argv

print(f"\nWe're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
# KeyboardInterrupt键盘中断
print("If you do want that, hitRETURN.")
# 让用户选择
input("? ")

print("Opening the file...")
# Open文件，the mode is 'w',只写模式，清空内容然后新建，不可以read，赋值给fileobject
target = open(filename, 'w')

print("Truncating the file. Goodbey! ")
target.truncate()

print("Now I'm going to aks you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
lines = f"{line1}\n{line2}\n{line3}\n"
target.write(lines)

# target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
# 关闭文件，这样就把文件写入磁盘里头，而不是在内存里缓冲
target.close()