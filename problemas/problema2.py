limite=1000000
nsuma=0
suma=1
nprimero=1
nsegundo=2
while (nsuma<=limite):
    nsuma=nprimero+nsegundo
    nprimero=nsegundo
    nsegundo=nsuma
    if (nsuma%2==1) and (nsuma<=limite):
        suma=suma+nsuma
print(suma)