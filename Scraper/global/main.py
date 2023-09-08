from Backend.Entities import (
    DependenciesEntity, 
    ScraperLogEntity
)
from GlobalSettings import (
    GlobalSettings,
    Settings
)
from Backend.DatabaseAPI import DatabaseAPI
from Backend.Entities import ValidatedEntity
from Backend.InputList import InputList
from Backend.SqsMessager import SqsMessager
from Backend.Logger import Logger
from Scraper.Extractor import Extractor
from Scraper.Initializer import Initializer
from Scraper.Parser import Parser
from Scraper.Runner import Runner
from Scraper.StateEntity import StateEntity
from Scraper.Terminator import Terminator
from Scraper.Validator import Validator
from settings import LocalSettings



def main():
    dependencies = DependenciesEntity()
    dependencies.database_api       = DatabaseAPI()
    dependencies.logger             = Logger()
    dependencies.extractor          = Extractor()
    dependencies.initializer        = Initializer()
    dependencies.inp_list           = InputList()
    dependencies.parser             = Parser()
    dependencies.settings           = Settings()
    dependencies.settings.merge_settings(GlobalSettings(), LocalSettings())
    dependencies.scraper_log        = ScraperLogEntity(dependencies.settings.scraper_id) 
    dependencies.sqs_messager       = SqsMessager()
    dependencies.state              = StateEntity()
    dependencies.validated_entity   = ValidatedEntity()
    dependencies.validator          = Validator()
    dependencies.extracted_data     = None
    dependencies.input_list         = []
    dependencies.parsed_data        = []
    dependencies.validated_data     = []
    
    dependencies = Initializer.initialize_scraper(dependencies)
    dependencies = Runner.run_scraper(dependencies)
    Terminator.terminate_scraper(dependencies)
    return



if __name__=="__main__":
    main()


