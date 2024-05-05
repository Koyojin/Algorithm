import itertools

n=int(input())
num=list(map(int,input().split()))
calc_num=list(map(int,input().split()))
calc_ele=['+','-','*','//']
calc=[]

maxi=-1000000000
mini=1000000000

for i in range(4):
    for j in range(calc_num[i]):
        calc.append(calc_ele[i])


for case in itertools.permutations(calc):
    case_cal=num[0]
    for i in range(n-1):
        if case[i]=='+':
            case_cal+=num[i+1]
        elif case[i]=='-':
            case_cal-=num[i+1]
        elif case[i]=='*':
            case_cal*=num[i+1]
        else:
            case_cal=int(case_cal/num[i+1])
        
    if case_cal>maxi:
        maxi=case_cal

    if case_cal<mini:
        mini=case_cal

print(maxi)
print(mini)

        