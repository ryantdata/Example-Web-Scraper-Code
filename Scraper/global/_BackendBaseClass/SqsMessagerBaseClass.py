import boto3
from botocore.exceptions import ClientError
import time
import json


class SqsMessagerBaseClass:

    def send_completion_message_to_aws(self, logger, worker_queue_url):

        session = boto3.Session()
        sqs = session.client('sqs')
        max_attempts = 3
        attempt = 0
        while attempt < max_attempts:

            messageBody = {
                'controller': # REMOVED,
                'action': 'index',
                'scheduled': True,
                'pass': {
                    'outlet': outlet_id
                },
            }

            try:
                response = sqs.send_message(
                    QueueUrl=worker_queue_url,
                    DelaySeconds=10,
                    MessageAttributes={
                        'Action': {
                            'DataType': 'String',
                            'StringValue': 'requestAction'
                        },
                    },
                    MessageBody=json.dumps(messageBody)
                )
                break
            except ClientError as error:
                logger.warning("Unable to send SQS message to the SQS queue. Retrying...", error)
                attempt += 1
                time.sleep(1)

        if attempt >= max_attempts:
            logger.error("Unable to send SQS message to the SQS queue", error)     
        
        return None
