print("Welcome to the quiz...")
score = 0
question = input("Hello, Are you ready for the quiz? ").lower()
if question == 'yes':
    print("Oh... Good... Let's go.....")

    q1 = input("what is the full meaning of CPU? ").lower()
    if q1 == 'central processing unit':
        print('correct! ')
        score+=1
    else:
        print("incorrect!")
   
    q2 = input("what is the full meaning of HDD? ").lower()
    if q2 == 'harddisk':
        print('correct!')
        score+=1
    else:
        print("incorrec!")

    q3 = input("what is the full meaning of SSD? ").lower()
    if q3 == "solid state drives":
        print('correct!')
        score+=1
    else:
        print("incorrec!")

    q4 = input("what is the full meaning of CD? ").lower()
    if q4 == "compact disk":
        print('correct!')
        score+=1
    else:
        print("incorrec!")

    q5 = input("what is the full meaning of PC? ").lower()
    if q5 == "personal computer":
        print('correct!')
        score+=1
    else:
        print("incorrec!")

else:
    print('Ops, bye for now...........')
score = str(score)
print(f"Your score is {score} thanks")
