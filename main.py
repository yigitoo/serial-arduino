import serial
# For linux
# serial_connection = serial.Serial('/dev/ttyUSB0', 9600)
ser = serial.Serial()

# PLEASE BRING YOUR ARDUINO CARD COM PORT AT HERE!!!
ser.port = "COM4"
ser.open()

string = "Hello, Serial I/O World!"

ser.write(b'{string}')


while ser.in_waiting:
  data = ser.readline().decode('ascii')
  print(f'Data received from card: {data}')
  if data == string:
    break

ser.close()