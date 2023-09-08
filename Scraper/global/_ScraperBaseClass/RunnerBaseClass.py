import time



class RunnerBaseClass:



    @classmethod
    def run_scraper(cls, dependencies):
        dependencies.state.status = "Running"
        dependencies.state.save_state(dependencies)
        while len(dependencies.state.remaining_urls) > 0:
            dependencies.state.update_current_url()
            dependencies.state.increment_input()
            dependencies.logger.current_input_log(dependencies)
            cls.__extract_and_load_data(dependencies)
            dependencies.parsed_data = []
            dependencies.validated_data = []
            dependencies.state.save_state(dependencies)
            time.sleep(1)
        return dependencies



    @staticmethod
    def __extract_and_load_data(dependencies):
        dependencies = dependencies.extractor.request_data(dependencies)
        dependencies = dependencies.parser.parse_extracted_data(dependencies)
        dependencies = dependencies.validator.validate_parsed_data(dependencies)
        dependencies.database_api.insert_validated_data(
            live_status=dependencies.settings.live_status, 
            validated_data=dependencies.validated_data
        )
        return dependencies









class PageRunnerBaseClass:



    @classmethod
    def run_scraper(cls, dependencies):
        dependencies.state.status = "Running"
        dependencies.state.save_state(dependencies)   
        while len(dependencies.state.remaining_urls) > 0:
            dependencies.state.update_current_url()
            dependencies.state.increment_input()
            dependencies.logger.current_input_log(dependencies)
            cls.__page_iterator(dependencies)
            dependencies.parsed_data = []
            dependencies.validated_data = []
            dependencies.state.save_state(dependencies)
            time.sleep(1)
        return dependencies
    


    @classmethod
    def __page_iterator(cls, dependencies):
        while dependencies.state.current_page <= dependencies.state.page_count:
            cls.__extract_and_load_data(dependencies)
            time.sleep(1)
            if dependencies.state.page_count == 0:
                dependencies.logger.no_prices_log(dependencies)
            dependencies.logger.current_page_log(dependencies)
            dependencies.state.increment_current_page()
            dependencies.parsed_data = []
            dependencies.validated_data = []
            dependencies.state.save_state(dependencies)
        dependencies.state.reset_page_counts()
        return dependencies



    @staticmethod
    def __extract_and_load_data(dependencies):
        dependencies = dependencies.extractor.request_data(dependencies)
        dependencies = dependencies.parser.parse_extracted_data(dependencies)
        dependencies = dependencies.validator.validate_parsed_data(dependencies)
        dependencies.database_api.insert_validated_data(
            live_status=dependencies.settings.live_status, 
            validated_data=dependencies.validated_data
        )
        return dependencies



