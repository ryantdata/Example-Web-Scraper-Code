import boto3
import os
import pandas as pd
from random import shuffle
from botocore.exceptions import (
    ClientError,
    ParamValidationError,
)
import time
import sys


class InputListBaseClass:



    @classmethod
    def get_input_list(cls, dependencies):
        response = cls.__get_missing_inputs(dependencies.settings.scraper_id)

        if response is None: 
            dependencies.input_list = cls.__get_input_list_from_database(dependencies)
            return dependencies
        
        dependencies.input_list = response["input_list"]
        dependencies.settings.aws_log_filename = dependencies.settings.aws_log_filename.replace("0", response["batch_id"])
        dependencies.settings.local_log_filename = dependencies.settings.local_log_filename.replace("0", response["batch_id"])
        dependencies.input_list = list(map(cls.__convert_decimal_values_to_int, dependencies.input_list))
        shuffle(dependencies.input_list)
        return dependencies
    


    @classmethod
    def __get_input_list_from_database(cls, dependencies):
        input_list = dependencies.database_api.fetch_table(
            table_name=dependencies.settings.inputs_table_name, 
            condition= # REMOVED, 
            fields= # REMOVED
        )
        input_list = list(map(cls.__convert_decimal_values_to_int, input_list))
        shuffle(input_list)
        return input_list
    


    @staticmethod
    def __get_missing_inputs(scraper_id):
        handler = MissingInputsHandler(scraper_id)
        response = handler.get_missing_inputs()
        return response
    


    @staticmethod
    def __convert_decimal_values_to_int(input_dict):
        input_dict[# REMOVED] = int(float(input_dict[# REMOVED]))
        input_dict[# REMOVED] = int(float(input_dict[# REMOVED]))
        input_dict[# REMOVED] = int(float(input_dict[# REMOVED]))
        return input_dict



class MissingInputsHandler:

    def __init__(self, scraper_id):
        self.queue_name = # REMOVED
        self.queue_url = None
        self.sqs = boto3.client("sqs")
        self.s3 = boto3.client("s3")
        self.scraper_id = scraper_id
        self.root_filepath = os.path.dirname(os.path.abspath(__file__))
        self.bucket_name =         # REMOVED
        self.local_item_filename = None
        self.aws_item_filename = None



    def get_batch_id_if_exists():
        if "BATCH_ID" in os.environ:
            return os.environ.get("BATCH_ID")
        else:
            return



    def get_input_list(self):

        try:
            missing_inputs = pd.read_csv(self.local_item_filename)
        
        except FileNotFoundError:
            return
        
        input_list = missing_inputs.to_dict("records")
        shuffle(input_list)

        self.s3.delete_object(Bucket=self.bucket_name, Key=self.aws_item_filename)
        
        return input_list



    def get_missing_inputs(self, count=0):
        batch_id = None
        if "BATCH_ID" in os.environ:
            batch_id = os.environ.get("BATCH_ID")
        
        if batch_id is None:
            return

        if count > 5:
            print(f"Could not download missing inputs file for batch id {batch_id}! Shutting down task...")
            sys.exit()

        self.aws_item_filename =         # REMOVED
        self.local_item_filename =        # REMOVED

        try:
            self.s3.download_file(
                Bucket=self.bucket_name, 
                Key=self.aws_item_filename, 
                Filename=self.local_item_filename
            )
            input_list = self.get_input_list()
            return {"input_list": input_list, "batch_id": batch_id}

        except (ClientError, ParamValidationError) as error:
            print(f"Could not download missing inputs file for batch_id {batch_id}! Retrying... :: {error}")
            count += 1
            time.sleep(1)
            return self.get_missing_inputs(count)

    

