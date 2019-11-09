import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)
try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected! at: " + time.strftime('%d/%m/%Y %H:%M:%S'))
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
