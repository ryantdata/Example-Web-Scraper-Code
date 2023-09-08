from _ScraperBaseClass.InitializerBaseClass import InitializerBaseClass
import re



class Initializer(InitializerBaseClass):



    @classmethod
    def initialize_scraper(cls, dependencies):
        dependencies = cls.crash_check(dependencies)
        if dependencies.state.status != "Running":
            dependencies.state.remaining_urls = cls.__generate_urls(dependencies) 
            dependencies.state.input_count = len(dependencies.state.remaining_urls)
            dependencies.state.save_state(dependencies)
        return dependencies



    @staticmethod
    def __generate_urls(dependencies):
        remaining_urls = []
        for inputs in dependencies.input_list:
            try:
                remaining_urls.append(# REMOVED)
            except KeyError:
                pass
        return remaining_urls
    


