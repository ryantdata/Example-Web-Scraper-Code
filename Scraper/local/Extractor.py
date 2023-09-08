import requests
import time
from _ScraperBaseClass.ExtractorBaseClass import ExtractorBaseClass



class Extractor(ExtractorBaseClass):


    @classmethod
    def request_data(cls, dependencies):
        http_proxy = {"http":f"{dependencies.proxy.get_random_proxy().http_proxy}"}
        response = requests.get(dependencies.state.current_url, proxies=http_proxy)
        dependencies.logger.request_response_log(dependencies, request_type="GET", status_code=response.status_code, url=dependencies.state.current_url)
        dependencies.extracted_data = response.text
        time.sleep(1)
        return dependencies


        