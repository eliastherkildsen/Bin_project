import RPi.GPIO as GPIO
import time
import threading
from my_vars import GREEN_LED_PIN, RED_LED_PIN, YELLOW_LED_PIN, debug, SAMPLE_RATE, BUTTON_CONTAINS_MEAT, BUTTON_CONTAINTS_DANGER, SERVER_IP, SERVER_PORT, BIN_ID
import ultra_sonic_service
import server_service  
from datetime import datetime


def debug(text):
    if debug: 
        print("[debug] " + str(text))

red_yellow_green = [RED_LED_PIN, YELLOW_LED_PIN, GREEN_LED_PIN]
yellow_blinking = False
blink_thread = None
last_emptied = datetime.now().strftime("%Y-%m-%D")

def init_pin(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def turn_on_pin(pin):
    GPIO.output(pin, True);

def turn_off_pin(pin):
    GPIO.output(pin, False)

def blink_light(pin, interval=0.5):
    global yellow_blinking
    yellow_blinking = True
    while yellow_blinking:
        turn_on_pin(pin)
        time.sleep(interval)
        turn_off_pin(pin)
        time.sleep(interval)

def start_blinking(pin, interval=0.5):
    global blink_thread
    if blink_thread is None or not blink_thread.is_alive():
        blink_thread = threading.Thread(target=blink_light, args=(pin, interval))
        blink_thread.start()

def stop_blinking():
    global yellow_blinking
    yellow_blinking = False
    if blink_thread:
        blink_thread.join()

def turn_off_pins(pins):
    stop_blinking()
    for pin in pins:
        GPIO.output(pin, False)

def set_bin_lights(bin_occupied, contain_danger, contain_meat):
    turn_off_pins(red_yellow_green)

    if bin_occupied > 33:
        start_blinking(red_yellow_green[1])

    if bin_occupied > 90:
        turn_on_pin(red_yellow_green[0])
    else:
        turn_on_pin(red_yellow_green[2])

    if contain_danger == True:
        turn_on_pin(red_yellow_green[0])
    if contain_meat == True:
        blink_light(red_yellow_green[1])   



def main(): 

    WS = server_service.init_ws(SERVER_IP, SERVER_PORT)

    debug("Program has started.....")
    init_pin(red_yellow_green)

    try:
        while True:
            fill_percentage = ultra_sonic_service.get_trash_fill_percentage()
            
            set_bin_lights(fill_percentage, ultra_sonic_service.contain_danger, ultra_sonic_service.contain_meat)
            print("danger: " + str(ultra_sonic_service.contain_danger))
            print("meat: " + str(ultra_sonic_service.contain_meat))

            # SEND DATA TO SERVER
            server_service.send_data(WS, BIN_ID, fill_percentage, last_emptied, ultra_sonic_service.contain_meat, ultra_sonic_service.contain_danger)

            time.sleep(7)
            

    except KeyboardInterrupt:
       print("\nMeasurement stopped by user.")
       GPIO.cleanup()

   
if __name__ == "__main__": 
    main()


