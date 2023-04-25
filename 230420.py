def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
        return a


# from sys import stdin
def index_array(n):
    n = int(stdin.readline())
    lst = [0] * 10001

    for i in range(n):
        a = int(stdin.readline())
        lst[a] += 1

    for i in range(10001):
        if lst[i] != 0:
            for j in range(lst[i]):
                print(i)
                stdin.stdout.write(lst[i]+'\n')

# from sys import stdin
# n = int(stdin.readline())
# lst = []
# x = 2
#
# while n != 1:
#     if n % x == 0:
#         print(x)
#         n = n / x
#     else:
#         x += 1


# import sys
# n = int(sys.stdin.readline())
# lst = [0] * 10001
#
# for i in range(n):
#     a = int(sys.stdin.readline())
#     lst[a] += 1
#
# for i in range(10001):
#     if lst[i] != 0:
#         for j in range(lst[i]):
#             sys.stdout.write(str(i)+'\n')
# 1-31, 2-28, 3-3

# import sys
# x, y = map(int, sys.stdin.readline().split())
# cal = [[31, 1, 3, 5, 7, 8, 10], [30, 4, 6, 9, 11], [28, 2]]
# week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# days = 0
# for i in range(1, x):
#     for j in range(len(cal)):
#         if i in cal[j]:
#             days += cal[j][0]
# days += y
# days -= 1
# days = days % 7
# print(week[days])

# import itertools
# import sys

# lst = []
# for i in range(9):
#     x = int(sys.stdin.readline())
#     lst.append(x)
#
# gps = list(itertools.combinations(lst, 7))
# for gp in gps:
#     if sum(gp) == 100:
#         for p in sorted(gp):
#             print(p)
#         break


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    return x * y // gcd(x, y)

def solution(array):
    lst = [0] * (len(array)+1)
    for i in array:
        lst[i] +=1
    if lst.count(max(lst)) != 1:
        ans = -1
    else:
        ans = lst.index(max(lst))
    return ans


print('hihi')
print('hihi')
print('hihi')
print('hihi')

print('byebye')
print('byebye')
print('byebye')
print('byebye')
print('byebye')
print('byebye')