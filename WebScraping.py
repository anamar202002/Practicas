from email import header
import requests
import time
import csv
import re
from bs4 import BeautifulSoup
import pandas as pd
import urllib

""" htmlejemplo = urllib.request.urlopen("https://ciencia.lasalle.edu.co/sistemas_informacion_documentacion/")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
articulos=sopita.find_all("p",class_="article-listing")
links=[]
for articulo in articulos:
  links.append(articulo.a["href"])

for i in range(2, 9):
    url='https://ciencia.lasalle.edu.co/sistemas_informacion_documentacion/index.'+str(i)+'.html'
    htmlejemplo = urllib.request.urlopen(url)
    sopita = BeautifulSoup(htmlejemplo, "html.parser")
    articulos=sopita.find_all("p",class_="article-listing")
    for articulo in articulos:
        links.append(articulo.a["href"]) """ #Se recolectan los links

""" l=pd.read_excel("links_salle.xlsx")
links=list(l[0])
cols=[]
obs=[]
data=[]
x=0
for l in links:
    dict={}
    print(l)
    html=urllib.request.urlopen(l)
    soup = BeautifulSoup(html, "html.parser")
    columnas=soup.find_all("div", class_="element")
    for col in columnas:
        if col["id"]!="attach_additional_files":
            cols.append(col.h4.text)
            obs.append(col.p.text)
    for i in range(x, len(cols)):
        valor=str(obs[i])
        if cols[i] == 'Autor':
            aux=valor.split(", ")
            valor=aux[0]
        
        dict[str(cols[i])]=valor
        
    data.append(dict)
    x=i

c = list(dict.fromkeys(cols))
df=pd.DataFrame(columns=c)

for dc in data:
    new=dc
    df=df.append(new, ignore_index=True)

df.to_excel("datos_salle.xlsx") """



#nueva_fila = {'name':'Geo', 'physics':87, 'chemistry':92, 'algebra':97}
#df_marks = df_marks.append(nueva_fila, ignore_index=True)
#print(df)

#df.to_excel("texto.xlsx")

""" import requests

def link_a_pdf(link,nombre):
  html = urllib.request.urlopen(link)
  soup=BeautifulSoup(html, "html.parser")
  pdf_url=soup.find("div", class_="aside download-button")
  pdf_url=pdf_url.a["href"]
  nombre=nombre+".pdf"
  file = requests.get(pdf_url, stream = True)
  
  with open(nombre,"wb") as pdf: #abre el archivo
    for chunk in file.iter_content(chunk_size=1024):

        if chunk:
            pdf.write(chunk)
  #urllib.request.urlretrieve(pdf_url, nombre)
  #file = req.get(pdf_url, allow_redirects=True)
  #open(nombre, 'wb').write(file.content)


#link_a_pdf('https://ciencia.lasalle.edu.co/sistemas_informacion_documentacion/778/', 'sallePrueba2')
#print("hi")
l=pd.read_excel("links_salle.xlsx")
links=list(l[0])
cont=0
for l in links:
    print(l)
    titulo="Salle "+str(cont)
    titulo=str(titulo)
    link_a_pdf(l,titulo)
    cont+=1 """

#UNIANTIOQUIA

""" pag=0
links=[]
for i in range(19):
    link="https://bibliotecadigital.udea.edu.co/handle/10495/13405?offset="+str(pag)
    pag+=20
    df_list = pd.read_html(link)[0]
    df=pd.DataFrame(df_list)
    html = urllib.request.urlopen(link)
    soup=BeautifulSoup(html, "html.parser")
    table=soup.find("table", class_="table")
    tds = table.find_all('tr')
    for t in tds:
        if t.a != None:
            l='https://bibliotecadigital.udea.edu.co/'+str(t.a['href'])
            links.append(l)
        
        #links.append(t.a["href"])

    #df_list.columns = df_list.iloc[0]
    #df_list=df_list.drop(index=0)
df=pd.DataFrame(links)
df.to_excel("antioquia_archivo.xlsx") """

""" df_list=pd.DataFrame()
l=pd.read_excel("antioquia_bibliotecologia.xlsx")
lista_links=list(l[0])
x=0
#for link in lista_links:

for link in lista_links:
    df=pd.DataFrame()
    metadato = link+"?show=full"
    print(link)
    htmlmetadato=(requests.get(metadato).content).decode()
    df = (pd.read_html(htmlmetadato)[0])
    df=df.T
    df.columns = df.iloc[0]
    df=df.drop([0],axis=0)

    df_list=pd.concat([df, df_list])

df_list=df_list.reset_index(drop=True)
print(df)
#df_list=df_list.T
df_list.to_excel("antioquia_bibliotecologia_datos.xlsx") """

""" def link_a_pdf(link,nombre):
  nombre=nombre+".pdf"
  file = requests.get(link, stream = True)
  
  with open(nombre,"wb") as pdf: #abre el archivo
    for chunk in file.iter_content(chunk_size=1024):

        if chunk:
            pdf.write(chunk) """
  #urllib.request.urlretrieve(pdf_url, nombre)
  #file = req.get(pdf_url, allow_redirects=True)
  #open(nombre, 'wb').write(file.content)

""" df_list=pd.DataFrame()
l=pd.read_excel("antioquia_bibliotecologia.xlsx")
lista_links=list(l[0])
cont=len(lista_links)

for link in lista_links:
    cont-=1
    df_list = pd.read_html(link)[0]
    df=pd.DataFrame(df_list)
    html = urllib.request.urlopen(link)
    soup=BeautifulSoup(html, "html.parser")
    table=soup.find("table", class_="table panel-body")
    tds = table.find_all('td', class_='standard break-all')

    for t in tds:
        if t.i == None:
            if t.a != None:
                l='https://bibliotecadigital.udea.edu.co/'+str(t.a['href'])
                print(cont)
                link_a_pdf(l, 'Uniantioquia_bibliotecologia '+str(cont))
                break #solo tome el primer hipervinculo """

#Página web biblioteca
""" htmlejemplo = urllib.request.urlopen("https://dgcpu1.wixsite.com/biblioteca/copia-de-naturaleza-decretos-1")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
sopita.find('div', attrs={'data-testid': 'price-and-procure-title'})
articulos=sopita.find_all('a', attrs={'data-testid' : 'linkElement'})
links=[]
etiquetas=[]
for articulo in articulos:
  print (articulo)
  if str(articulo["href"]).find("fogafin.sharepoint")!=-1:
    links.append([articulo["href"], articulo["aria-label"]])

df=pd.DataFrame(links)
print(df)
df.to_excel("boletines.xlsx") """

#print(links)
#print(etiquetas)

""" htmlejemplo = urllib.request.urlopen("https://dgcpu1.wixsite.com/biblioteca/copia-de-naturaleza-decretos-1")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
sopita.find('div', attrs={'data-testid': 'price-and-procure-title'})
articulos=sopita.find_all('img')
links=[]
for articulo in articulos:
  print (articulo)
  if str(articulo["src"]).find("static.wixstatic")!=-1:
    links.append([articulo["src"], articulo["alt"]])

df=pd.DataFrame(links)
print(df)
df.to_excel("boletines.xlsx") """
""" 
import json

htmlejemplo = urllib.request.urlopen("https://dgcpu1.wixsite.com/biblioteca/copia-de-bolet%C3%ADn-jur%C3%ADdico")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
all=sopita.find_all('p', class_="font_8")
img=sopita.find_all('wix-image')
links=[]
for i in img:
    print(i.img['alt'])
    data = json.loads(i["data-image-info"])
    link='https://static.wixstatic.com/media/'+str(data['imageData']['uri'])
    links.append([link, i.img['alt']])
    print('https://static.wixstatic.com/media/',data['imageData']['uri'])
for a in all:
    links.append(a.text)
    #links.append([a.a['href'], a.span.text])
    
df=pd.DataFrame(links)
print(df)
df.to_excel("boletines1.xlsx") """
#links=[]
  #print (articulo.get('imageData'))

#Título
""" htmlejemplo = urllib.request.urlopen("https://dgcpu1.wixsite.com/biblioteca/copia-de-informes-de-noticias-coyuntu")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
 """

""" #Imagenes y sus labels
import json

htmlejemplo = urllib.request.urlopen("https://dgcpu1.wixsite.com/biblioteca/copia-de-circulares")
sopita = BeautifulSoup(htmlejemplo, "html.parser")
all=sopita.find_all('p', class_="font_8")
img=sopita.find_all('wix-image')
enlaces=sopita.find_all('h5', class_="font_5")
titulos=sopita.find_all('span', class_="color_15")
links=[]
text=[]
imagenes=[]


titulos_lista=[]
for titulo in titulos:
  print (titulo)
  titulos_lista.append(titulo.text)


for i in img:
    print(i.img['alt'])
    data = json.loads(i["data-image-info"])
    link='https://static.wixstatic.com/media/'+str(data['imageData']['uri'])
    imagenes.append([link, i.img['alt']])
    print('https://static.wixstatic.com/media/',data['imageData']['uri'])
for a in all:
    text.append(a.text)
    #links.append([a.a['href'], a.span.text])

for link in enlaces:
    #print(link.a['href'])
    links.append(link.a['href'])


df=pd.DataFrame(links)
print(df)
df.to_excel("links.xlsx")
df=pd.DataFrame(imagenes)
print(df)
df.to_excel("imagenes.xlsx")
df=pd.DataFrame(text)
print(df)
df.to_excel("text.xlsx")
df=pd.DataFrame(titulos_lista)
print(df)
df.to_excel("titulos_lista.xlsx")
 """
 

pag = urllib.request.urlopen('https://www.fogafin.gov.co/que-es-fogafin/normatividad-y-asuntos-juridicos')
html=pag.read()
soup = BeautifulSoup(html, "html.parser")
all=soup.find_all('div', class_='accordion ui-accordion ui-widget ui-helper-reset')
#all=soup.find_all('h3', class_="ui-accordion-header ui-corner-top ui-state-default ui-accordion-icons ui-accordion-header-collapsed ui-corner-all")
print(all)