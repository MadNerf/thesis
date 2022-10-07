import RPi.GPIO as GPIO
import time
from tkinter import *
from smbus2 import SMBus
from mlx90614 import MLX90614

INFRARED_SENSOR_PIN_ENTRANCE = 8
INFRARED_SENSOR_PIN_EXIT = 40


GPIO.setmode(GPIO.BOARD)
GPIO.setup(INFRARED_SENSOR_PIN_ENTRANCE, GPIO.IN)
GPIO.setup(INFRARED_SENSOR_PIN_EXIT, GPIO.IN)


count=0
window = Tk()
window.title("Thesis GUI")
window.configure(width=500, height=300)
window.geometry("500x300")
count_label=Label(window, text="counter:")
count_label.grid(row=0,column=0)

    
def counter_func():
    global count
    counter=GPIO.input(INFRARED_SENSOR_PIN_ENTRANCE)

    if counter==False:
        time.sleep(0.5)
        count+=1
        print(count)
    else:
        print("")
        time.sleep(0.5)

    return count

def negacounter_func():
    global count
    counter=GPIO.input(INFRARED_SENSOR_PIN_EXIT)

    if counter==False:
        time.sleep(0.5)
        count-=1
        print(count)
    else:
        print("")
        time.sleep(0.5)

    return count

def reset_count():
    global count
    count=0
    count_label.configure(text="counter:"+ str(count))
    window.update()

counter_rst= Button(window, text="Reset", command=reset_count)
counter_rst.grid(row=0,column=1)

def temperature_sensor():
    bus = SMBus(1)
    tempsensor = MLX90614(bus, address=0x5A)
    #print tempsensor.get_amb_temp()
    #print tempsensor.get_obj_temp()
    bus.close()


def app_window():
    
    global count
    count_label.configure(text="counter:"+ str(count))
    counter_func()
    negacounter_func()
    window.update()

while True:
    app_window()