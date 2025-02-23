import csv
import argparse

parser = argparse.ArgumentParser(
    prog='playLog.py',
    description='Replays a sensor data log and applies curtain-closing algorithm.',
    epilog='No other options.')
parser.add_argument('filename')
args = parser.parse_args()
print(f"Trying to open {args.filename}")

with open(args.filename, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)