# lambda_function.py
# deployed via GitHub Actions - v1.0.2
import json
import datetime

def lambda_handler(event, context):
    """
    Simple example Lambda that echoes the event and returns timestamp.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from GitHub->AWS Lambda integration! Atin Mondal.",
            "received_event": event,
            "invoked_at": datetime.datetime.utcnow().isoformat() + "Z"
        })
    }
