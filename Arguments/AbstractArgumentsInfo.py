from abc import ABCMeta, abstractmethod
from typing import Dict


class AbstractArgumentsInfo(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def set_file_name(cls, fileNames: Dict):
        pass
