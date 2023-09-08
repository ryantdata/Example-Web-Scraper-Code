from abc import (
    ABC, 
    abstractclassmethod
)


class InitializerBaseClass(ABC):



    @abstractclassmethod
    def initialize_scraper(*args, **kwargs):
        NotImplementedError



    @staticmethod
    def crash_check(dependencies):
        data = dependencies.database_api.fetch_s3_log(
            aws_log_filename=dependencies.settings.aws_log_filename,
            bucket_name=dependencies.settings.bucket_name,
            local_log_filename=dependencies.settings.local_log_filename
        )
        if data is not None:
            if data['status'] == "Running":
                dependencies.state.__dict__ = data
        return dependencies


