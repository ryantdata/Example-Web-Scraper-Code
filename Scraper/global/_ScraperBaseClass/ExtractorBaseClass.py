from abc import (
    ABC,
    abstractclassmethod
)



class ExtractorBaseClass(ABC):



    @abstractclassmethod
    def request_data(*args, **kwargs):
        NotImplementedError
    