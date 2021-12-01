# challenge1
# challenge1_path = 'the-self-taught-programmer/chapter_9/chap9_challenge1.txt'
# with open(challenge1_path, 'r') as file_object:
#     print(file_object.read())


# challenge2
# challenge2_path = 'the-self-taught-programmer/chapter_9/chap9_challenge2.txt'

# answer = input("What's your favourite color? ")

# with open(challenge2_path, 'w') as file_object:
#     file_object.write(answer)


# challenge3
import csv

with open('st.csv', 'w') as f:
    csv.writer(f, delimiter=',').writerow(['a', 'b', 'c'])
    csv.writer(f, delimiter=',').writerow([1, 2, 3])
    csv.writer(f, delimiter=',').writerow(['x', 'y', 'z'])