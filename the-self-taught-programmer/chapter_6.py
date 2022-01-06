# challenge1
author = "Camus"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])


# challenge2
answer1 = input("What did you write yesterday? ")
answer2 = input("Who did you send it yesterday? ")
new_string = "Yesterday I wrote a {}, I send it to {}!".format(answer1, answer2)
print(new_string)


# challenge3
print("aldous Huxley was born in 1894.".capitalize())


# challenge4
print("Where now? Who now? When now? ".split('?'))


# challenge5
lst = ["The", "fox", "jumped", "over", "the", "fence", "."]
string = " ".join(lst)
print(string[:-2] + string[-1])


# challenge6
print("A screaming comes across the sky.".replace('s', '$'))


# challenge7
print("Hemingway".index('m'))


# challenge8
quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"


# challenge9
string = 'three '
print(string * 3)
print(string + string + string)


# challenge10
slce = "It was bright cold day in April, and the clocks were strikingthirteen.".split(',')
print(slce[0])
