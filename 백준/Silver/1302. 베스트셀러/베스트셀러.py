from collections import Counter
n=int(input())
Book=[input() for i in range(n)]
R=sorted(Book)
max_item=Counter(R).most_common(n=1)
print(max_item[0][0])

#https://hengbokhan.tistory.com/184