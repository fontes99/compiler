import sys

conta = sys.argv[1]

res = 0

nums = []
op = []

num = ''

for i in conta:

    if i == ' ':
        pass
    elif i !='+' and i != '-':
        num += i
    else:
        op.append(i)
        nums.append(int(num))
        num = ''

nums.append(int(num))

res += nums[0]

print(op)
print(nums)

for i in range(len(op)):
    if op[i] == '+':
        res += nums[i+1]
    if op[i] == '-':
        res -= nums[i+1]

print(res)
