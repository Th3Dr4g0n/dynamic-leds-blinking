#Importing GPIO and sleep libraries
import RPi.GPIO as GPIO
from time import sleep

#Setting up GPIO
def init(gpio_pins):
	#Setup GPIO using Board numbering
    GPIO.setmode(GPIO.BOARD)
	#Loop through the GPIO pins
    for pin in gpio_pins:
		#Set the current pin for output
        GPIO.setup(pin, GPIO.OUT)
        print "Preparing pin %s for output" % pin
    return 1

#Send on output command to the pi's GPIO pin
def led_on(gpio_pin):
    GPIO.output(gpio_pin, GPIO.HIGH)
    print "pin %s is on" % gpio_pin

#Send off output command to the pi's GPIO pin
def led_off(gpio_pin):
    GPIO.output(gpio_pin, GPIO.LOW)
    print "pin %s is off" % gpio_pin

#Controlling the output of each pin
def blink(gpio_pins, interval):
    try:
		#Make sure there is at least one GPIO pin set, and pin(s) were set
        if(len(gpio_pins) > 0 and init(gpio_pins) == 1):
			#Initiate an index and set it to 0
            index = 0
            while 1:
				#Command current pin to turn on
                led_on(gpio_pins[index])
				#Increase index by 1
                index = index + 1
				#Make sure the index is not greater than the provided pins length to avoid commanding wrong pins
                if(index >= len(gpio_pins)):
					#Reset index
                    index = 0
				#Command current pin to turn off
                led_off(gpio_pins[index])
				#Wait before proceeding with a provided interval
                sleep(interval)
	#Check in there is a keyboard interruption (Ctrl+Alt+Del)
    except KeyboardInterrupt:
		#Clean up the pi's GPIO
        GPIO.cleanup()

#Registring GPIO pins 11, 12, and 13
connected_gpio_pins = [11, 12, 13]

#Setting up blinking interval
interval = 0.3

#Running the program
blink(connected_gpio_pins, interval)
