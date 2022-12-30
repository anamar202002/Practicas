import pandas as pd
registros=[]

with open("HL.txt") as archivo:
    for linea in archivo:
        linea=str(linea)
        aux=linea.split(": ")
        r=str(aux[1])
        r=r.replace('\n', '')
        r1=r.split(".")
        for i in r1:
            i=i.replace(' ', '')
            if i != '':
                registros.append(i)
df=pd.DataFrame(registros)
df.to_excel("HL.xlsx")