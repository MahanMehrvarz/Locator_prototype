GPIO.setup(11, GPIO.OUT)
p=GPIO.PWM(11,50)
p.start(0)


def main():
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counter$

        if old_value:
            a=new_value - old_value
            if a<5000:
                  print "nothing"
                  #GPIO.cleanup()
                  print a
            else:
                  print "sth"
                  print a
                  p.ChangeDutyCycle(2.5)
                  time.sleep(0.5)
                  p.ChangeDutyCycle(7.5)
                  time.sleep(0.5)
                  p.ChangeDutyCycle(12.5)
                  time.sleep(0.5)
                  #GPIO.cleanup()
        old_value = new_value

        time.sleep(1)
        #GPIO.cleanup()


b= main()
print "a is:"+ b

