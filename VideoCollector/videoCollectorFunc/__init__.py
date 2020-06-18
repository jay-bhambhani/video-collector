import json
import logging
import requests
import azure.functions as func

ARGO_EVENTS_ENDPOINT = 'http://20.185.11.147:12000/labeling'

def main(event: func.EventGridEvent):
    logging.info('')
    blob_data = event.get_json()
    blob_url = blob_data['url']
    logging.info(f"Python event trigger function processed blob \n"
                 f"Name: {blob_url}")
    payload = dict(blob_url=blob_url)
    requests.post(ARGO_EVENTS_ENDPOINT, json=payload)
    logging.info('Python EventGrid sent blob {payload} to endpoint {endpoint}'.format(payload=payload, endpoint=ARGO_EVENTS_ENDPOINT))
