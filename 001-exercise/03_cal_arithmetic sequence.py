# 根据用户输入的开始数字与结束数字，计算等差数列的和
x = int(input("input 1st number:"))
y = int(input("input last number:"))
sum = int((x + y) * (y - x + 1) / 2)
print("the sum is:", sum)
