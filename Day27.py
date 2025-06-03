question = ["what is your name","what is your age"]
answers=[["shivam","rakesh","vellu","shankar"],[15,25,65,85,]]
for i in question:
    print(i)
    for j in answers:
        print(j)
        useranswer=int(input("Select your answer:"))
        if answers[useranswer] == answers[0]:
            print("5 crore")
        else:
            print("you lose")


            