import RPi.GPIO as GPIO
import time
from my_vars import TRIG_PIN, ECHO_PIN, BUTTON_CONTAINS_MEAT, BUTTON_CONTAINTS_DANGER

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUTTON_CONTAINS_MEAT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_CONTAINTS_DANGER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global contain_danger
contain_danger = False
global contain_meat
contain_meat = False


def my_callback_contains_danger(channel):
    print("INTERUPT: DANGER CALLED")
    global contain_danger
    contain_danger = not bool(contain_danger)
    return 

def my_callback_contains_meat(channel):
    print("INTERUPT: MEAT CALLED")
    global contain_meat
    contain_meat = not bool(contain_meat)
    return

GPIO.add_event_detect(BUTTON_CONTAINS_MEAT, GPIO.FALLING, callback=my_callback_contains_meat)
GPIO.add_event_detect(BUTTON_CONTAINTS_DANGER, GPIO.FALLING, callback=my_callback_contains_danger)

def measure_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2

    return round(distance, 2)
print "Calibrating trash depths... Make sure trash is empty."
time.sleep(2)
empty_distance = measure_distance()
print "Calibrated empty trash distance: {} cm".format(empty_distance)

def get_trash_fill_percentage():
   current_distance = measure_distance()

   if current_distance >= empty_distance:
      fill_percentage = 0
   else:
      fill_percentage = round(((empty_distance - current_distance) / empty_distance) * 100, 2)

   print "Measured Distance: {} cm | Trash fill percentage: {}%".format(current_distance, fill_percentage)

   return fill_percentage


   