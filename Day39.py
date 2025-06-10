# Kaun Bnaega crore patti
questions= [["what is your name?","shivam","pullu","gullu","tillu",1],
           ["what is your work?","python","pullu","gullu","tillu",1],
           ["what is your place?","lpu","pullu","gullu","tillu",1],
           ["what is your imp?","family","pullu","gullu","sillu",1],]
money=0

i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n{question[0]}")
    print(f"a.{question[1]}  b.{question[2]}")
    print(f"c.{question[3]}  d.{question[4]}")
    answer=int(input("Enter you answer 1 to 4"))
    if(answer==question[-1]):
        print("you won first question")
    else:
        print("you lost the game")
        break