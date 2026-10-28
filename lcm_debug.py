# LCM
# num1 = int(input())
# num2 = int(input())
# if num1 > num2:
#     lcm = num2
# else:
#     lcm = num1
# while True:
#     if lcm % num1 == 0 and lcm % num2 != 0:
#         break
#     lcm += 1
# print(lcm)

# Debug
num1 = int(input())
num2 = int(input())
if num1 > num2:
    lcm = num1
else:
    lcm = num2
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1
print(lcm)