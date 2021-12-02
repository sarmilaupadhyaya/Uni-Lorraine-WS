from collections import defaultdict

lex_digit = ["one","two","three", "four","five", "six", "seven", "eight", "nine", "ten"]
f = open("cmudict-en-us.dict", "r")
lex_dict = defaultdict()
data = f.read().split("\n")

for line in data:
    wordlex = line.split(" ")
    for each in lex_digit:
        if wordlex[0].startswith(each):
            if wordlex[0] not in lex_dict:
                lex_dict[wordlex[0]] = " ".join(wordlex[1:])
            else:
                lex_dict[wordlex[0]+"(2)"] = " ".join(wordlex[1:])

print(lex_dict)

