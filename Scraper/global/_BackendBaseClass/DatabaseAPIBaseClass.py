from botocore.exceptions import ClientError
import boto3
import json
import os
import boto3
import pymysql



class DatabaseAPIBaseClass:



    def __init__(self):
        pass



    @classmethod
    def save_initialized_state(cls, dependencies):
        cls.__insert_scraper_log(
            live_status=dependencies.settings.live_status, 
            scraper_log=dependencies.scraper_log
        )   
        cls.__create_file_locally(
            data=dependencies.state.__dict__, 
            local_log_filename=dependencies.settings.local_log_filename
        )
        return cls.__fetch_scraper_log_id(
            live_status=dependencies.settings.live_status,
            scraper_id=dependencies.settings.scraper_id
        )
    


    @classmethod
    def save_running_state(cls, dependencies):
        cls.__update_scraper_log(
            live_status=dependencies.settings.live_status, 
            scraper_log_id=dependencies.state.scraper_log_id, 
            scraper_log=dependencies.scraper_log
        )
        cls.__create_file_locally(
            data=dependencies.state.__dict__, 
            local_log_filename=dependencies.settings.local_log_filename
        )
        cls.__upload_file_to_s3(
            aws_log_filename=dependencies.settings.aws_log_filename,
            bucket_name=dependencies.settings.bucket_name,
            local_log_filename=dependencies.settings.local_log_filename
        )



    @classmethod
    def save_finished_state(cls, dependencies):
        cls.__update_scraper_log(
            live_status=dependencies.settings.live_status, 
            scraper_log_id=dependencies.state.scraper_log_id, 
            scraper_log=dependencies.scraper_log
        )
        cls.__create_file_locally(
            data=dependencies.state.__dict__, 
            local_log_filename=dependencies.settings.local_log_filename
        )
        cls.__upload_file_to_s3(
            aws_log_filename=dependencies.settings.aws_log_filename,
            bucket_name=dependencies.settings.bucket_name,
            local_log_filename=dependencies.settings.local_log_filename
        )



    @classmethod
    def fetch_s3_log(cls, aws_log_filename, bucket_name, local_log_filename):
        file_exists = cls.download_file_from_s3(
            aws_log_filename=aws_log_filename,
            bucket_name=bucket_name,
            local_log_filename=local_log_filename
        )
        if file_exists is True:     
            return cls.__read_file_from_local(
                local_log_filename=local_log_filename, 
                json_data=True
            )
        else:                       
            return



    @classmethod
    def fetch_table(cls, table_name, condition="", fields="*", live_status=True):
        query = f"SELECT {fields} FROM {table_name} {condition};"
        connection = cls.__connect_to_db(live_status)
        return cls.__fetch_records(connection=connection, query=query)



    @classmethod
    def insert_validated_data(cls, live_status, validated_data):
        if validated_data == []:
            return
        values = [tuple(result.__dict__.values()) for result in validated_data]
        fields = list(validated_data[0].__dict__.keys())
        query = cls.__create_insert_query(fields=fields, table_name=# REMOVED)
        connection = cls.__connect_to_db(live_status=live_status)
        cls.__insert_records(connection=connection, query=query, values=values)
        return



    @classmethod
    def insert_validated_reference_data(cls, live_status, validated_data, table_name):
        if validated_data == []:
            return
        values = [tuple(result.__dict__.values()) for result in validated_data]
        fields = list(validated_data[0].__dict__.keys())
        query = cls.__create_insert_query(fields=fields, table_name=table_name)
        connection = cls.__connect_to_db(live_status=live_status)
        cls.__insert_records(connection=connection, query=query, values=values)
        return
    


    @classmethod
    def insert_url(cls, live_status, url_data, table_name):
        if url_data == []:
            return
        values = [tuple(result.__dict__.values()) for result in url_data]
        fields = list(url_data[0].__dict__.keys())
        query = cls.__create_insert_query(fields=fields, table_name=table_name)
        connection = cls.__connect_to_db(live_status=live_status)
        cls.__insert_records(connection=connection, query=query, values=values)
        return
    


    @staticmethod
    def __connect_to_db(live_status):
        # REMOVED



    @staticmethod
    def __insert_records(connection, query, values):
        cursor = connection.cursor()
        if isinstance(values, tuple):
            cursor.execute(query, values)
            connection.commit()
        if isinstance(values, list):
            cursor.executemany(query, values)
            connection.commit() 
        cursor.close()
        connection.close()
        return 



    @staticmethod
    def __fetch_records(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data



    @classmethod
    def __insert_scraper_log(cls, live_status, scraper_log):
        values = tuple(scraper_log.__dict__.values())
        fields = list(scraper_log.__dict__.keys())
        query = cls.__create_insert_query(fields=fields, table_name=# REMOVED)
        connection = cls.__connect_to_db(live_status=live_status)
        cls.__insert_records(connection=connection, query=query, values=values)
        return



    @classmethod
    def __update_scraper_log(cls, live_status, scraper_log_id, scraper_log):
        values = list(scraper_log.__dict__.values())
        values.append(scraper_log_id)
        values = tuple(values)
        fields = list(scraper_log.__dict__.keys())
        query = cls.__create_update_query(fields=fields, table_name=# REMOVED)
        connection = cls.__connect_to_db(live_status=live_status)
        cls.__insert_records(connection=connection, query=query, values=values)
        return
    

 
    @classmethod
    def __fetch_scraper_log_id(cls, live_status, scraper_id):
        query = # REMOVED
        connection = cls.__connect_to_db(live_status=live_status)
        data = cls.__fetch_records(connection=connection, query=query)
        return data[0]['max(id)']



    @staticmethod
    def __create_insert_query(fields, table_name):
        values  = r'%s,' * len(fields)
        fields  = ",".join(fields)
        return f"INSERT INTO {table_name} ({fields}) VALUES ({values[:-1]});"



    @staticmethod
    def __create_update_query(fields, table_name):
        fields = [field + r"= %s" for field in fields]
        fields = ",".join(fields)
        return f"UPDATE {table_name} SET {fields} WHERE id = %s;"



    @staticmethod
    def __delete_file_from_local(local_log_filename):
        try:                       
            os.remove(local_log_filename)
        except FileNotFoundError:   
            return


 
    @staticmethod
    def __read_file_from_local(local_log_filename, json_data=False):
        if json_data is True:
            try:
                with open(local_log_filename, 'r', encoding='utf8') as f:
                    data = json.loads(f.read())
            except FileNotFoundError:
                data = None
        else:
            try:
                with open(local_log_filename, 'r', encoding='utf8') as f:
                    data = f.read()
            except FileNotFoundError:
                data = None
        return data



    @staticmethod
    def __create_file_locally(data, local_log_filename):
        with open(local_log_filename, 'w', encoding='utf8') as f:
            f.write(json.dumps(data))
        return



    @staticmethod
    def delete_file_from_s3(bucket_name, aws_log_filename):
        client = boto3.client("s3")
        client.delete_object(Bucket=bucket_name, Key=aws_log_filename)
        return
    


    @staticmethod
    def __upload_file_to_s3(aws_log_filename, bucket_name, local_log_filename):
        "Returns True if succcessful, False otherwise."
        client = boto3.client("s3")
        return client.upload_file(Filename=local_log_filename, Bucket=bucket_name, Key=aws_log_filename)



    @staticmethod
    def download_file_from_s3(aws_log_filename, bucket_name, local_log_filename):
        client = boto3.client("s3")
        try:        
            client.download_file(Bucket=bucket_name, Key=aws_log_filename, Filename=local_log_filename)
            return True
        except ClientError:
            return False