from abc import (
    ABC,
    abstractclassmethod
)





class ParsedEntityBaseClass:

    def __init__(*args, **kwargs):
        NotImplementedError




class ParserBaseClass(ABC):



    @abstractclassmethod
    def parse_extracted_data(*args, **kwargs):
        NotImplementedError



    @abstractclassmethod
    def create_parsed_entity(*args, **kwargs):
        NotImplementedError

        