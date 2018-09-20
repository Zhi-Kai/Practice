# import random
# ans = random.randint(1,100)
# for i in range(1,5):
#     print("Please entry the answer!")
#     player_ans = int(input())
#     if player_ans == ans:
#         print("Bingo!")
#         break
#     else:
#         print("you are wrong~")
# print("Game over",'\n',"The andswer is",ans)

#=====================================================
#try except
import random
ans = random.randint(1,100)

for i in range(0,5,1):
    print("Please entry the answer!")
    try:
        player_ans = int(input())

        if player_ans == ans:
            print("Bingo!")
            break
        else:
            print("you are wrong~")
    except  ValueError:
        i = i+1
        print("Please entry a number!")
print("Game over",'\n',"The andswer is",ans)
