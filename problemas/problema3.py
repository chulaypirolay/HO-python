numero=13195
nmayor=1
for div in range(1,numero):
    print div
    for i in range(1,div):
        if (div%i==0) and (numero%div==0):
            nmayor=div
print nmayor