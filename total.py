total = 0
for i in range(1,101):
    total += i 
    print("The sum is:", total)
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
## 更簡潔的寫法
print(sum(range(1,101)))