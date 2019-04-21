from Arguments.AbstractArgumentsInfo import *


class DataGenerationInfo(AbstractArgumentsInfo):

    outputFileName = None
    rowCount = None
    colCount = None
    cellSize = None

    @classmethod
    def set_file_name(cls, fileNames: Dict[str, str]):
        cls.outputFileName = fileNames['output']

    @classmethod
    def set_data_amount(cls, dataSizes: Dict[str, int]):
        cls.rowCount = dataSizes['rowCount']
        cls.colCount = dataSizes['colCount']
        cls.cellSize = dataSizes['cellSize']
