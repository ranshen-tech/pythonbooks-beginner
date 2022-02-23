def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1

    nested.state = start
    return nested


F = tester(0)
print(F.state)
F("spam")
F("ham")
print(F.state)
print("\n")

# G = tester(42)
# G("eggs")
# F("ham")
# F("ham")
# print(F.state)
# print(G.state)
# print(F is G)
