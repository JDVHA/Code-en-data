import serial
import time
import csv
import datetime


ser = serial.Serial('COM5', 9600)
while True:
    command = input("Input: ")
    ser.write(command.encode("utf-8"))
    print(ser.readline().decode("utf-8").strip())
