import csv
import sys


def main():
	debug = False # Change True to print debug statement 
	data = []
	match = []
	with open(sys.argv[1],'r') as csvfile:
		#variable for CSV handler
		reader = csv.reader(csvfile)
		csv_headings = next(reader)
		target_price = float(csv_headings[1][1:].strip())


		if (debug):
			print(reader)

		for rows in reader:
			data.append(rows)

		for firstArray in data:
			if (debug): print ("firstArray " + firstArray[0])
			results = target_price - float(firstArray[1][1:].strip())
			for secondArray in data:
				if (debug): print ("secondArray " + secondArray[0])
				if results == float(secondArray[1][1:].strip()):
					match.append((firstArray[0],secondArray[0]))

	if (match == []):
		print ("There is no combination of dishes that is equal to target price.")

	else:
		print(match)

main();
			
