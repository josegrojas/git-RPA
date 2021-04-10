import pyautogui as robot
import time
lista_canciones = ["can't stop", "Take on me"]
google = 45, 148
direc = 179, 53
buscar = 470, 129
cancion = 526, 317
cerrar = 1571, 7
mintodo = 1599, 873

def abrir(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#abrir google
abrir(mintodo, click=1)
time.sleep(1)
abrir(google, click=2)
time.sleep(2)
robot.hotkey("alt", "space")
time.sleep(1)
robot.typewrite("x")

#ubicarse en el buscador
time.sleep(3)
abrir(direc)
robot.typewrite("www.youtube.com")
robot.hotkey("enter")
time.sleep(3)

#Elegir la cancion
for elemento in range(len(lista_canciones)):
    abrir(buscar, click=3)
    robot.typewrite(lista_canciones[elemento])
    robot.hotkey("enter")
    time.sleep(3)
    abrir(cancion)
    time.sleep(5)

abrir(cerrar)
print("PROCESO TERMINADO")
