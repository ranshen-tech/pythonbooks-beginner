L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# i = 0
# while i < len(L):
#     if 2**X == L[i]:
#         print("at index", i)
#         break
#     i += 1
# else:
#     print(X, "not found")

# for num in L:
#     if 2**X == num:
#         print(L.index(num))
#         break
# else:
#     print("not found")

if 2**X in L:
    print("found at", L.index(2**X))
else:
    print("not found")
