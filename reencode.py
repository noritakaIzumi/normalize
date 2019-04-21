# import csv
import sys

from Arguments.FileNameInfo import *


def re_encode():
    with open(FileNameInfo.outputFileName, 'w', newline='\n') as g:
        with open(FileNameInfo.inputFileName, 'r', newline='\n', encoding='utf-8_sig') as f:
            for row in f:
                g.write(row)


def main():
    if len(sys.argv) == 3:
        file_names = {
            'input': str(sys.argv[1]),
            'output': str(sys.argv[2])
        }
        FileNameInfo.set_file_name(fileNames=file_names)
        re_encode()
        return 0
    else:
        print('you need 2 arguments')
        print('Command: python uniqueByRow.py [inputFileName] [outputFileName]')
        return 1


if __name__ == '__main__':
    main()
