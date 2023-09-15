num = int(input("please enter a number between 50 and 100 :"))
for i in range(num):
    output=[]
    output.append(i)
    if i % 2 == 1 and i % 3 != 0:
      print(output,end=" ")




