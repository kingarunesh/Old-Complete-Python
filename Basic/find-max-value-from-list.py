numbers = input("Input a list of students scores:\n")
score_list = numbers.split(' ')
max_score = 0
min_value = 0


for score in score_list:
    score = int(score)
    if max_score < score:
        max_score = score


print(max_score)

