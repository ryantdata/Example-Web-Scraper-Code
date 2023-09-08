import json
from _ScraperBaseClass.ParserBaseClass import (
    ParsedEntityBaseClass,
    ParserBaseClass
)




class ParsedEntity(ParsedEntityBaseClass):

    def __init__(self):
        # REMOVED



class Parser(ParserBaseClass):



    @classmethod
    def parse_extracted_data(cls, dependencies):
        json_data = json.loads(dependencies.extracted_data)
        dependencies.parsed_data = list(map(cls.create_parsed_entity, json_data))
        return dependencies
    


    @classmethod
    def create_parsed_entity(cls, json_data):
        parsed_entity = ParsedEntity()
        # REMOVED
        return parsed_entity
    
    @staticmethod
    def __parse_data(data, key):
        try:
            return data[key]
        except KeyError:
            return

    