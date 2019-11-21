from twython import TwythonStreamer
from string import punctuation, whitespace

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
import twitter
import serial
import time




class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            date = data['created_at']
            print("{}, @{}: {}".format(date,username, tweet))
            print("----------")
            writeToArduino(bytes(3))
            print(bytes(3))
            print(bytes(3)-48)

            def writeToArduino(someIntAsByteString):
                ser = serial.Serial(9600)
                time.sleep(5)
                while True:
                    ser.write(someIntAsByteString)
                    ser.close()
            writeToArduino(bytes(3))
            print(bytes(3))
            print(bytes(3)-48)
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track='#SmartGreenMakeathon')

