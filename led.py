import RPi.GPIO as GPIO
import time
import psutil
# blinking function  



def blink(pin):
        # to use Raspberry Pi board pin numbers
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        # set up GPIO output channel  
        GPIO.setup(16, GPIO.OUT)
        # blink GPIO17 50 tim
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        return






def main():
    old_value = 0


    while True:



        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counter$

        if old_value:
            a=new_value - old_value
            if a<100000:
                  print "nothing"
                  #GPIO.cleanup()
                  print a
            else:
                  print "sth"
                  print a
                  for i in range(0,5):
                      blink(16)
                      GPIO.cleanup()





                  #GPIO.cleanup()
        old_value = new_value

        time.sleep(1)
        #GPIO.cleanup()

b= main()
print "a is:"+ b

