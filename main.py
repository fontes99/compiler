import sys

conta = sys.argv[1]

res = 0

nums = []
op = []

num = ''

flag_number = None
flag_space = False

for i in range(len(conta)):

    if conta[i] == ' ':
        flag_space = True
    
    elif conta[i] !='+' and conta[i] != '-':
        
        if (flag_space and flag_number):
            raise ValueError

        num += conta[i]
        flag_space = False
        flag_number = True
    
    else:
        flag_space = False
        flag_number = False
        op.append(conta[i])

        try:
            nums.append(int(num))
        except ValueError:
            print('U need to use numbers, dummy...')
            raise

        num = ''

try:
    nums.append(int(num))
except ValueError:
    print('U need to use numbers, dummy...')
    raise

res += nums[0]

print(op)
print(nums)

for i in range(len(op)):
    if op[i] == '+':
        res += nums[i+1]
    if op[i] == '-':
        res -= nums[i+1]

print(res)
