from inter2 import intersect, union

s1, s2, s3 = "SPAM", "SCAM", "SLAM"

print(intersect(s1, s2))
print(union(s1, s2))
print(intersect([1, 2, 3], (1, 4)))
print(intersect(s1, s2, s3))
print(union(s1, s2, s3))
print("\n")
