# -*- coding: utf-8 -*-
from time import sleep
import pyautogui as mouse
import pyperclip as cp
import keyboard

""" cord_x, cord_y = mouse.position()
print(str(cord_x)+";"+str(cord_y)) """


""" mouse.moveTo(124,194)
mouse.click()
mouse.write("DTH HISTORIAS LABORALES")
mouse.press('enter')
mouse.moveTo(115,400) """
while keyboard.is_pressed("esc")==False:

    if keyboard.is_pressed('+'):
        
        mouse.click(98,237)

        keyboard.wait('F2')    
        

        res=mouse.locateOnScreen("fd.png", grayscale=True, region=(0,252,318,347))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.doubleClick()
        mouse.hotkey('ctrl', 'c')


        res=mouse.locateOnScreen("f.png", grayscale=True, region=(0,361, 312, 481))
        if res != None:
            ps=mouse.center(res)
            mouse.moveTo(ps[0], ps[1]+20)
            mouse.click()
            mouse.hotkey('ctrl', 'v')

        res=mouse.locateOnScreen("NoID.png", grayscale=True, region=(0,350,350,726))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.click()
        mouse.write("51866410")

        res=mouse.locateOnScreen("n&a.png", grayscale=True, region=(0,350,350,726))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.click()
        cp.copy("NORA ÁNGELA AFANADOR ORTEGÓN")
        mouse.click()
        mouse.hotkey('ctrl', 'v') 
        #mouse.write("NORA ÁNGELA AFANADOR ORTEGÓN")
        
        """ 
        HISTORIA LABORAL-80021314-JAIRO DANIEL GONZÁLEZ REYES
        mouse.press("down")
        sleep(0.5)
        mouse.press("down")
        mouse.press("enter") """
        res=mouse.locateOnScreen("en.png", grayscale=True, region=(0,365,258,573))
        if res != None:
            mouse.moveTo(mouse.center(res))
            mouse.click()
            mouse.write("FOGAFIN")
            mouse.press('down')
            sleep(0.5)
            mouse.press('down')
            mouse.press('enter')
            """ cp.copy("BANCO DE LA REPÚBLICA")
            mouse.hotkey('ctrl', 'v') """

        res=mouse.locateOnScreen("crg.png", grayscale=True, region=(0,365,258,573))
        if res != None:
            mouse.moveTo(mouse.center(res))
            mouse.click()
            mouse.write("SECRETARIA")
            #mouse.write("PROFESIONAL DEL DEPARTAMENTO DE OPERACIONES DE TESORERIA Y PAGOS")
            #mouse.write("CONTADOR")
            #mouse.hotkey('ctrl', 'v')
            res1=mouse.locateOnScreen("LdA.png", grayscale=True, region=(0,365,258,573))
            if res1 != None:
                mouse.moveTo(mouse.center(res1))
                mouse.click()
                mouse.write("JAIRO ENRIQUE OSORIO BUSTAMANTE")
                #cp.copy("JAIRO ENRIQUE OSORIO BUSTAMANTE")
                #mouse.hotkey('ctrl', 'v')

        mouse.moveTo(115,475)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)
        mouse.scroll(-1)

        mouse.moveTo(10,10)
        res=mouse.locateOnScreen("ne.png", grayscale=True, region=(0,350,350,726))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.click()
        """ cp.copy("")
        mouse.hotkey('ctrl', 'v') """
        mouse.write("HISTORIA LABORAL-51866410-NORA")
        
        mouse.press('down')
        sleep(1)
        mouse.press('down')
        mouse.press('enter')
        
        sleep(0.5)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)

        res=mouse.locateOnScreen("csb.png", grayscale=True, region=(0,350,350,726))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.click()
        mouse.press('tab')

        mouse.moveTo(442,280)
        sleep(0.5)
        mouse.click()


        keyboard.wait('enter')

        mouse.moveTo(115,475)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        mouse.scroll(1)
        

        keyboard.wait('F2')

        mouse.moveTo(380,737)
        mouse.click()
        """ mouse.moveTo(492,669)
        mouse.click() """

        keyboard.wait('enter')

        mouse.moveTo(442,269)
        mouse.click()

        mouse.hotkey('ctrl', 'o')    
        
    elif keyboard.is_pressed('F3'):
        res=mouse.locateOnScreen("fd.png", grayscale=True, region=(0,252,318,347))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.doubleClick()

        keyboard.wait('enter')
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.doubleClick()
        mouse.hotkey('ctrl', 'c')


        res=mouse.locateOnScreen("f.png", grayscale=True, region=(0,361, 312, 481))
        ps=mouse.center(res)
        mouse.moveTo(ps[0], ps[1]+20)
        mouse.click()
        mouse.hotkey('ctrl', 'v')

        keyboard.wait('F2')

        mouse.moveTo(380,737)
        mouse.click()
        """ mouse.moveTo(492,669)
        mouse.click() """

        keyboard.wait('enter')

        mouse.moveTo(442,269)
        mouse.click()

        mouse.hotkey('ctrl', 'o')
