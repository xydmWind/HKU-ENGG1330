Code=int(input())
Turns=int(input())
Target=int(input())
Attemps_Left=int(input())
Code1=Code//100%10
Code2=Code//10%10
Code3=Code%10
Code1=(Code1+Turns)%10
Code2=(Code2+Turns)%10
Code3=(Code3+Turns)%10
Code=(Code1*100+Code2*10+Code3)
print(str(Code)+"\n"+str(Code==Target and Attemps_Left>0))