import csv
import random
import string
import sys

from Arguments.DataGenerationInfo import *

letters = string.ascii_uppercase


def generate_data():
    with open(DataGenerationInfo.outputFileName, mode='w', newline='\n') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        for i in range(DataGenerationInfo.rowCount):
            row = []
            for j in range(DataGenerationInfo.colCount):
                cell = ''.join(random.sample(letters, DataGenerationInfo.cellSize))
                row.append(cell)
            writer.writerow(row)


def main():
    if len(sys.argv) == 5:
        file_names = {
            'output': str(sys.argv[1])
        }
        DataGenerationInfo.set_file_name(fileNames=file_names)
        data_sizes = {
            'rowCount': int(sys.argv[2]),
            'colCount': int(sys.argv[3]),
            'cellSize': int(sys.argv[4])
        }
        DataGenerationInfo.set_data_amount(dataSizes=data_sizes)
        generate_data()
        return 0
    else:
        print('you need 4 arguments')
        print('Command: python generateData.py [outputFileName] [rowCount] [colCount] [cellSize]')
        return 1


if __name__ == '__main__':
    main()
