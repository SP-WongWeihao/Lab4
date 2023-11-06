import socket
import hal.hal_input_switch as input_switch
from hal import hal_led as led
import time
from time import sleep

def check_switch_state_1():
    ret = 0
    if input_switch.read_slide_switch() == 1:
        ret = 1
    return ret

def blink_led():
    while input_switch.read_slide_switch() == 1:
        led.set_output(0, 1)
        sleep(0.1)
        led.set_output(0, 0)
        sleep(0.1)
    if input_switch.read_slide_switch() == 0:
        start_time = time.time()
        while time.time() - start_time < 5.0:
            led.set_output(0, 1)
            sleep(0.05)
            led.set_output(0, 0)
            sleep(0.05)
            #if check_switch_state_1(): #Turn on interrupt for change of switch state during 5 seconds
                #break

        while input_switch.read_slide_switch() != 1:
            led.set_output(0, 0)


def main():
    local_ip_address = socket.gethostbyname("raspberrypi")
    led.init()
    input_switch.init()
    while 1:
        blink_led()


if __name__ == "__main__":
    main()
