while 1:
    try:
        s=input()
        des=[0,0,0,0]
        for i in s:
            if i.islower():
                des[0]+=1
            elif i.isnumeric():
                des[2]+=1
            elif i.isupper():
                des[1]+=1
        des[3]=s.count(' ')

        print(*des)        
    except:
        break