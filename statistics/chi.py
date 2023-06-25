def chi(x, y):
    return (x-y)**2/y

lst1 = [0.61, 0.99, 0.40, 0.98, 0.94, 0.70, 0.84, 0.68, 0.93, 0.44]
lst2 = [86.24, 45.76, 44, 109.76, 58.24, 56]

lst = []

for i in range(len(lst1)):
    lst.append(chi(lst1[i], 0.5))
len(lst)
sum(lst)
