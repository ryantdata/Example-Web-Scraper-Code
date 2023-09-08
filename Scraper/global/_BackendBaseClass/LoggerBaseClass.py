import logging







class LoggerBaseClass:



    def __init__(self):
        logging.basicConfig(level=logging.INFO, format=f'\n  >>>> %(message)s <<<< \n')
        self.logger = logging.getLogger("logger")


    
    @staticmethod
    def __progress_prefix(dependencies):
        percent_progress = round((dependencies.state.input/dependencies.state.input_count)*100,2)
        return f"INPUT ({dependencies.state.input}/{dependencies.state.input_count}) (%{percent_progress})"
    


    def current_input_log(self, dependencies):
        self.logger.info(f"{self.__progress_prefix(dependencies)} :: Current Input {dependencies.state.current_url}")


    
    def no_prices_log(self, dependencies):
        self.logger.info(f"{self.__progress_prefix(dependencies)} :: No prices for current url!")



    def current_page_log(self, dependencies):
        self.logger.info(f"{self.__progress_prefix(dependencies)} :: Page ({dependencies.state.current_page}/{dependencies.state.page_count})")


    
    def request_response_log(self, dependencies, request_type, status_code, url):
        self.logger.info(f"{self.__progress_prefix(dependencies)} :: Request ({request_type}) :: Response ({status_code}) {url}")


    
    def price_count_log(self, dependencies):
        self.logger.info(f"{self.__progress_prefix(dependencies)} :: Price count {dependencies.state.price_count} (+{len(dependencies.validated_data)})")



    def sqs_message_log(self):
        self.logger.info(f"Scraper Finished. SQS Message sent!")