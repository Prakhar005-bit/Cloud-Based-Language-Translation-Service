import json
import requests

def lambda_handler(event, context):
    # Get text + target language from API Gateway POST body
    body = json.loads(event.get("body", "{}"))
    
    text = body.get("text", "")
    target = body.get("target_language", "hi")  # default Hindi

    # Free Translation API
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target}"
    response = requests.get(url).json()

    translated_text = response["responseData"]["translatedText"]

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"translated_text": translated_text})
    }
