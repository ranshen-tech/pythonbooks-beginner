#-*-  coding:UTF-8  -*-
# consolidation1, 2
# j = int(input('> '))                      #定义一个新的参数，并且该参数从控制台输入值，由str强转为int
# def loop(j):                                 #定义一个循环函数，传参j
# 	i = 0                                    #创建一个新的参数，并赋值为0
# 	numbers = []                             #创建一个空的列表
# 	while i < j:                             #使用while
# 		print(f"At the top i is {i}")	     #打印i值	
# 		numbers.append(i)                    #将i值加入到numbers列表中
# 		i = i + 1	                         #i自增
	
# 		print("numbers now:", numbers)        #打印numbers
# 		print(f"at the bottom i is {i}")     #打印自增后的i值
		
# 	print("the numbers:")                     #打印引号中的话
		
# 	for num in numbers:                      #for循环
# 		print(num)                            #打印num值
		
# loop(j)                                      #调用该函数


# consolidation5
j = int(input("> "))
def loop(j):
    i = 0
    numbers = []

    for i in range(j):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers is:")
    for num in numbers:
        print(num)

loop(j)