# 将argv解包，与之前的形式不太一样，但内容相同，
import sys

script, encoding, error = sys.argv             

# 定义main函数，含三个变量
def main(language_file, encoding, errors): 
    # 每次读取文件的一行，赋值给line变量    
    line = language_file.readline()            

    # 做line的if语句，若语句为真，运行以下两行语句。若语句为假，跳过
    if line:      
        # 调用print_line函数                                         
        print_line(line, encoding, errors)    
        # 返回main函数【在main里调用main函数，利用if函数终止循环】              
        return main(language_file, encoding, errors)         


# 定义print_line函数，含三个参数
def print_line(line, encoding, errors):    
    # .strip()用来移除换行符                            
    next_lang = line.strip()   
    # 将移除换行符后得到的字符串编码成字节串，赋值给raw_bytes                                         
    raw_bytes = next_lang.encode(encoding, errors = errors)   
    # 将刚才得到的字节串解码          
    cooked_string = raw_bytes.decode(encoding, errors = errors)         

    # 打印字节串和对应的字符串
    print(raw_bytes, "<===>", cooked_string)                            


# 打开目标文件，编码方式为utf-8
languages = open("languages.txt", encoding = "utf-8")                   

# 对打开的文件对象调用main函数
main(languages, encoding, error)                                        


## 回到第7行运行main函数，languages对应language_file, encoding对应encoding, error对应errors
## 此处的languages是打开文件“languages.txt”得到的文件对象，encoding和error都是最开始解包导入的参数
## 阅读languages文件的内容并将其赋值给line
## 因为line返回内容，所以第12行if语句判断为真，继续运行接下来的语句，运行print_line函数
## 跳到14行运行print_line函数，将第9行得到的line变量去掉换行符得到next_lang变量
## 将next_lang变量编码成字节串，得到新变量raw_bytes
## 将raw_bytes解码得到新变量cooked_string
## 打印raw_bytes及对应的cooked_string
## print_line函数运行完毕，回到第16行返回main函数
## 重新回到第7行，进行循环
## 直到文件读取至最后一行后，line不返回内容，所以第12行if语句判断为假，停止执行return语句。
## 循环结束，代码执行完毕

