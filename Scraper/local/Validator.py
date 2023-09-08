import pytz
from datetime import datetime
from _ScraperBaseClass.ValidatorBaseClass import ValidatorBaseClass
import json



class Validator(ValidatorBaseClass):



    @classmethod
    def create_validated_entity(cls, dependencies, parsed_entity):
        validated_entity = dependencies.validated_entity.create_new_validated_entity()
        # REMOVED
        return validated_entity



