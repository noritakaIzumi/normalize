import csv
import sys

from Arguments.FileNameInfo import *


def normalize():
    with open(FileNameInfo.outputFileName, 'w', newline='\n') as g:
        writer = csv.writer(g, delimiter=',', lineterminator='\n')
        with open(FileNameInfo.inputFileName, 'r', newline='\n') as f:
            reader = csv.reader(f, delimiter=',')
            current_row_number = 1
            for row in reader:
                for string in row:
                    writer.writerow((current_row_number, string))
                current_row_number += 1


def main():
    if len(sys.argv) == 3:
        file_names = {
            'input': str(sys.argv[1]),
            'output': str(sys.argv[2])
        }
        FileNameInfo.set_file_name(fileNames=file_names)
        normalize()
        return 0
    else:
        print('you need 2 arguments')
        print('Command: python normalize.py [inputFileName] [outputFileName]')
        return 1


if __name__ == '__main__':
    main()
