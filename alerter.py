import re
import twilio
import time
import sys
import serial

sys.dont_write_bytecode=True
import config

serial_port = '/dev/tty.usbmodem1411';
serial_bauds = 9600;

last_temperature = 0;

def sendSMS(text):
  account_sid = config.account_sid
  auth_token = config.auth_token
  from_number = config.twilio_number
  to_number = config.my_number
  client = twilio.rest.TwilioRestClient(account_sid, auth_token)
  message = client.messages.create(to=to_number, from_=from_number, body=text)

def read_temperature(s):
  line = s.readline();
  return float(line)

def alert():
  global last_temperature
  temperature = read_temperature(s);
  if temperature >= last_temperature + 2 or temperature <= last_temperature - 2:
    sendSMS(temperature)
    last_temperature = temperature;
    #timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  print(str(temperature) + u' \N{DEGREE SIGN}F');

if __name__ == "__main__":
  s = serial.Serial(serial_port, serial_bauds);
  try:
    while True:
      alert();
      time.sleep(5)
  except KeyboardInterrupt:
      sys.exit()
