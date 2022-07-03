import time
#產生不重複數字的random值
while True:
    quiz = time.time()
    quiz = str(int((quiz*(10**4))%(10**4)))
    if len(quiz) <4:
        num = 4-len(quiz)
        series_0="0"
        series_0= series_0*num
        quiz = series_0+quiz
    test_set=set()
    for ele in quiz:
        if ele  not in  test_set:
                test_set.add(ele)
        else :
            break
    else: 
        break
quiz_set = set(quiz)
# print(quiz)
# print(quiz_set)
str_in =""
while  str_in != quiz:
    str_in =str(input("Guess number=>"))
    if len(str_in) != 4:
        print("you should input 4 digits.")
        continue
    if (str_in.count(str_in[0])+str_in.count(str_in[1])+str_in.count(str_in[2])+str_in.count(str_in[3]))>4:
        print("you can't repeat key same numbers.")
        continue
    A = 0 
    error_set = set()
    correct_set =set()
    for i in range(0,len(quiz)):
        if str_in[i] == quiz[i]:
            A += 1
            correct_set.add(str_in[i])
        else: 
            error_set.add(str_in[i])
    # print(error_set)
    # print(correct_set)
    # print(quiz_set)
    B = len((error_set-correct_set)&quiz_set)
    print(A,"A",B,"B")
print("clear")
print("The answer is ",quiz)
