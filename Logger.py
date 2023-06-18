import serial
import time
import csv
import datetime

calibration_value = 21.34 - 0.7
ser = serial.Serial('COM8', 9600)
while True:
    volt = float(ser.readline().decode("utf-8").strip())
    pH = -5.70 * volt + calibration_value
    print(volt, pH)
    # Open file
    with open(f"Data.csv", "a", newline='') as file:

        # Write naar file
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), pH, volt])

    # Clos file
    file.close()
