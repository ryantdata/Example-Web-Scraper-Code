from abc import (
    ABC,
    abstractclassmethod
)



class ValidatorBaseClass(ABC):



    @classmethod
    def  validate_parsed_data(cls, dependencies):
        dependencies.validated_data = [cls.create_validated_entity(dependencies, parsed_entity) for parsed_entity in dependencies.parsed_data]
        dependencies.validated_data = list(filter(cls.__is_not_null, dependencies.validated_data))
        dependencies.state.update_price_count(len(dependencies.validated_data))
        dependencies.logger.price_count_log(dependencies)
        return dependencies



    @staticmethod
    def __is_not_null(validated_result):
        is_not_null = [False if validated_result.__dict__[f'{field}'] is None else True for field in validated_result.NOT_NULLABLE] 
        if all(is_not_null) is True:    
            return True
        else:                           
            return False



    @abstractclassmethod
    def create_validated_entity(*args, **kwargs):
        NotImplementedError



