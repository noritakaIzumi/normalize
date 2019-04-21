import csv
import sys

from Arguments.FileNameInfo import *


def unique_by_row():
    with open(FileNameInfo.outputFileName, 'w', newline='\n') as g:
        writer = csv.writer(g, delimiter=',', lineterminator='\n')
        with open(FileNameInfo.inputFileName, 'r', newline='\n') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                writer.writerow(list(set(row)))


def main():
    if len(sys.argv) == 3:
        file_names = {
            'input': str(sys.argv[1]),
            'output': str(sys.argv[2])
        }
        FileNameInfo.set_file_name(fileNames=file_names)
        unique_by_row()
        return 0
    else:
        print('you need 2 arguments')
        print('Command: python uniqueByRow.py [inputFileName] [outputFileName]')
        return 1


if __name__ == '__main__':
    main()
