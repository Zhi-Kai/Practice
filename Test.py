import random
ans = random.randint(1,100)
for i in range(1,5):
    print("Please entry the answer!")
    player_ans = int(input())
    if player_ans == ans:
        print("Bingo!")
        break
    else:
        print("you are wrong~")
print("Game over",'\n',"The andswer is",ans)