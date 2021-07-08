def f(n):
    l=len(n)
    for i in n:
        for j in range(len(n)):
            if i==2*n[j] and i!=n[j]:
                return True
    return False

print(f([-2,0,10,-19,4,6,-8]))
print(f([-20, 8, -6, -14, 0, -19, 14, 4]))
print(f([10,2,5,3]))
print(f([7,1,14,11]))
print(f([3,1,7,11]))