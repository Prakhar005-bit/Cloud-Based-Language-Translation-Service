import json, requests

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    text = body.get('text', '')
    target = body.get('target_language', 'hi')
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target}"
    response = requests.get(url).json()
    translated = response['responseData']['translatedText']
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"translated_text": translated})
    }
