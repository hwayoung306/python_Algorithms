# shift+ctrl+p -> start repl

from audioop import add


print("hello world")
print("안녕")
print("처음 해보는거야")

# 파이썬 2장 연습문제
 # Q1
average = (80+75+55)/3
print(average)

 # Q2
if 13%2 != 0 :
    print("홀수입니다.")
else :
    print("짝수입니다.")

# Q3
pin = "881120-1068234"
yyyymmdd = "19" + pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(':','#')
print(b)

# Q6
c=[1,3,5,4,2]
c.sort()
c.reverse()
print(c)

# Q7
d = ['Life', 'is', 'too', 'short']
result = " ".join(d)
print(result)

# Q8
f = (1,2,3)
result2 = f + (4,)
print(result2)

# Q10
g = {'A':90, 'B':80, 'C':70}
result = g.pop('B')
print(g)
print(result)

# Q11
h = {1,1,1,2,2,3,3,3,4,4,5}
hSet = set(h)
b = list(hSet)
print(b)
