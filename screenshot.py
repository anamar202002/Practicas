#Toma pantallazos y sube las imagenes a la página de la biblioteca de wix
import pyautogui
import keyboard
import webbrowser 
from time import sleep
import pandas as pd

""" cord_x, cord_y = pyautogui.position()
print(str(cord_x)+";"+str(cord_y)) """

#tomar los pantallazos
""" df=pd.read_excel("resoluciones.xlsx")
print(df)

for i, row in df.iterrows():
    titulo=row['Título']
    link=row['Link']
    webbrowser.open(link)
    res=None
    while res == None:
        print("no está ancho")
        res=pyautogui.locateOnScreen("ancho.png", grayscale=True)

    res1=pyautogui.locateOnScreen("x.png", grayscale=True)
    if res1 !=None:
        ps=pyautogui.center(res1)
        pyautogui.click(ps)
    
    ps=pyautogui.center(res)
    pyautogui.click(ps)
    sleep(1)
    pyautogui.click(ps)     
    ss=pyautogui.screenshot(region=(439,114,909-439,720-114))
    s=titulo+".png"
    ss.save(s) """


#poner las imagenes en wix

""" import clipboard
resimage=pyautogui.locateOnScreen("imagen.png", grayscale=True)
while resimage !=None:
    ps=pyautogui.center(resimage)
    #pyautogui.click(ps)
    pyautogui.moveTo(ps)
    pyautogui.move(-300, 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    h=clipboard.paste()
    pyautogui.doubleClick(ps)

    res=None
    while res == None:
        print("no está buscar")
        res=pyautogui.locateOnScreen("buscar.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.click(ps)
    pyautogui.write('"')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write('"')
    pyautogui.press('enter')

    res=None
    while res == None:
        print("no está archivo")
        res=pyautogui.locateOnScreen("archivos.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.moveTo(ps)
    pyautogui.move(-10, 100)
    pyautogui.doubleClick()
    pyautogui.move(-100,0)
    sleep(2)
    resimage=pyautogui.locateOnScreen("imagen.png", grayscale=True)
    if resimage==None:
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1)
        pyautogui.scroll(-1) """

#links de las resoluciones
""" import clipboard
import pandas as pd

df=pd.DataFrame()
restres=pyautogui.locateOnScreen("trespuntos.png", grayscale=True)
lista=[]
while restres !=None:
    pstres=pyautogui.center(restres)
    pyautogui.click(pstres)
    sleep(1)
    res=None
    while res==None:
        print("no esta nombre")
        res=pyautogui.locateOnScreen("nombre.png", grayscale=True, region=(430,129,652,719))

    ps=pyautogui.center(res)
    pyautogui.click(ps)

    pyautogui.hotkey('ctrl', 'c')
    resolucion=clipboard.paste()

    pyautogui.click(pstres)
    sleep(0.5)
    pyautogui.click(pstres)
    sleep(1)
    rescop=None
    while rescop==None:
        print("no esta copiar")
        rescop=pyautogui.locateOnScreen("copiar.png", grayscale=True, region=(430,129,652,719))

    ps=pyautogui.center(rescop)
    pyautogui.click(ps)

    res=None
    while res==None:
        print("no esta acceso")
        res=pyautogui.locateOnScreen("acceso.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.click(ps)

    res=None
    while res==None:
        print("no esta USUARIOS FOGAFIN")
        res=pyautogui.locateOnScreen("fogafin.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.click(ps)

    res=pyautogui.locateOnScreen("aplicar.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.click(ps)

    sleep(2)
    pyautogui.hotkey('ctrl','c')

    link=clipboard.paste()
    print(link)
    print(resolucion)
    lista.append([resolucion, link])

    pyautogui.moveTo(pstres)
    pyautogui.move(-100,60)
    pyautogui.click()
    sleep(1)
    pyautogui.click()
    sleep(2)
    pyautogui.move(0,-60)
    restres=pyautogui.locateOnScreen("trespuntos.png", grayscale=True)
    if restres==None:
        pyautogui.click()
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        restres=pyautogui.locateOnScreen("trespuntos.png", grayscale=True)

df=pd.DataFrame(lista)
df.to_excel("resoluciones1.xlsx") """

    
#Screenshots
""" df=pd.read_excel("resoluciones.xlsx")
print(df)
for i, row in df.iterrows():
    titulo=row['Título']
    link=row['Link']
    webbrowser.open(link)
    sleep(2)
    res=None
    j=0
    while res == None:
        print("no está lupa")
        print(j)
        res=pyautogui.locateOnScreen("lupa.png", grayscale=True)
        j+=1
   
    ps=pyautogui.center(res)
    pyautogui.moveTo(ps)
    pyautogui.move(0,200)
    pyautogui.click()
    
    sleep(1)
      
    ss=pyautogui.screenshot(region=(439,114,909-439,720-114))
    s=titulo+".png"
    ss.save(s) """

#buscar y subir a wix
import clipboard
resimage=pyautogui.locateOnScreen("imagen.png", grayscale=True)
while resimage !=None:
    ps=pyautogui.center(resimage)
    #pyautogui.click(ps)
    pyautogui.moveTo(ps)
    pyautogui.move(-300, 0)
    pyautogui.doubleClick()
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    h=clipboard.paste()
    pyautogui.doubleClick(ps)

    res=None
    while res == None:
        print("no está buscar")
        res=pyautogui.locateOnScreen("buscar.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.click(ps)
    pyautogui.write('"')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write('"')
    pyautogui.press('enter')

    res=None
    while res == None:
        print("no está archivo")
        res=pyautogui.locateOnScreen("archivos.png", grayscale=True)
    ps=pyautogui.center(res)
    pyautogui.moveTo(ps)
    pyautogui.move(-10, 100)
    pyautogui.doubleClick()
    pyautogui.move(-100,0)
    sleep(2)
    resimage=pyautogui.locateOnScreen("imagen.png", grayscale=True)
    if resimage==None:
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        pyautogui.scroll(-20)
        resimage=pyautogui.locateOnScreen("imagen.png", grayscale=True)
