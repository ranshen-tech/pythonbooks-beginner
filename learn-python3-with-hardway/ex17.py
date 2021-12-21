from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"\nCopying from {from_file} to {to_file}")

# We could do these two on one line, how?
# 赋予文件对象
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
# exists函数返回True or False
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# consolidation exercise1
# from sys import argv

# script, from_file, to_file = argv

# indata = open(from_file).read()
# open(to_file, 'w').write(indata)
# print("Alright, all done.")


# consolidation exercise2
# from sys import argv; script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); out_file.close(); in_file.close(); print("Alright, all done.")

# note
# close()函数，在用完文件后确定写入磁盘，而不是在内存中缓冲；
# len()函数，以数值的形式返回字符串的长度，如果是txt文件，则open()之后，由文件对象转化为字符串变量。