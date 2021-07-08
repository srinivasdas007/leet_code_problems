# x=[10,2,5,3]
# m=max(x)
# for i in x:
#     if i*2==m:
#         print(True)
def f(n):
    m=max(n)
    for i in n:
        if i*2==m:
            return True
    return False

print(f([10,2,5,3]))
print(f([7,1,14,11]))
print(f([3,1,7,11]))