from datetime import datetime
import pytz




class StateEntityBaseClass:



    def __init__(self):
        self.input              = 0
        self.current_url        = 0
        self.remaining_urls     = []
        self.end_time           = None
        self.input_count        = 0
        self.last_updated       = datetime.now(pytz.timezone("Europe/London")).strftime("%Y-%m-%d %H:%M:%S")
        self.input_count        = 0
        self.price_count        = 0
        self.scraper_log_id     = 0
        self.start_time         = datetime.now(pytz.timezone("Europe/London")).strftime("%Y-%m-%d %H:%M:%S")
        self.status             = "Starting"



    def increment_input(self):
        self.input += 1
        return self



    def update_current_url(self):
        self.current_url = self.remaining_urls[-1]
        self.remaining_urls.pop()
        return self



    def update_price_count(self, price_count:int):
        self.price_count += price_count
        return self
    


    def reset_price_count(self):
        self.price_count = 0
        return self


    def reset_input_count(self):
        self.input_count = None
        return self



    def __update_scraper_log(self, dependencies):
        for key in dependencies.scraper_log.__dict__.keys():
            if key in self.__dict__.keys():
                dependencies.scraper_log.__dict__[key] = self.__dict__[key]
        return dependencies



    def __update_state(self):
        self.last_updated = datetime.now(pytz.timezone("Europe/London")).strftime("%Y-%m-%d %H:%M:%S")
        if self.status == "Finished":       
            self.end_time = self.last_updated



    def save_state(self, dependencies):
        self.__update_state()
        dependencies = self.__update_scraper_log(dependencies)
        if self.status == "Starting":   
            self.scraper_log_id = dependencies.database_api.save_initialized_state(dependencies)
        if self.status == "Running":    
            dependencies.database_api.save_running_state(dependencies)
        if self.status == "Finished":   
            dependencies.database_api.save_finished_state(dependencies)
        return self




class PageStateEntityBaseClass(StateEntityBaseClass):

    def __init__(self):
        super().__init__()
        self.current_page = 1
        self.page_count = 1

    def increment_current_page(self):
        self.current_page += 1
        return self
    
    def reset_page_counts(self):
        self.current_page = 1
        self.page_count = 1
        return self


