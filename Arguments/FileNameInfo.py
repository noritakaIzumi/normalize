from Arguments.AbstractArgumentsInfo import *


class FileNameInfo(AbstractArgumentsInfo):

    inputFileName = None
    outputFileName = None

    @classmethod
    def set_file_name(cls, fileNames: Dict[str, str]):
        cls.inputFileName = fileNames['input']
        cls.outputFileName = fileNames['output']
