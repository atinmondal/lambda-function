# lambda_function.py

import json
import datetime

def lambda_handler(event, context):
    """
    Simple example Lambda that echoes the event and returns timestamp.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from GitHub->AWS Lambda integration! Atin Mondal.v1",
            "received_event": event,
            "invoked_at": datetime.datetime.utcnow().isoformat() + "Z"
        })
    }
