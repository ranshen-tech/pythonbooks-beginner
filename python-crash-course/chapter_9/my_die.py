from die import Die

# 创建一个 6 面的骰子，再掷 10 次并显示结果。
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("\n10 rolls of a 6-sided die:")
print(results)