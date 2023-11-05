import requests

def translate(text, source_language, target_language):
    """Translates text from one language to another using the Google Translate API.

    Args:
        text: The text to be translated.
        source_language: The language code of the source language.
        target_language: The language code of the target language.

    Returns:
        A string containing the translated text.
    """


    
    url = 'https://translation.googleapis.com/translate_v2/languages/detect'
    params = {
        'q': text,
        'key': 'AIzaSyDWef1w0wUciYILTM3qj6ahhgKPjaPNrD4'
    }
    
#    response = requests.post(url, params=params)
#    json_response = response.json()
    
#   source_language = json_response['data']['detection'][0][0]['language']


    
    url = 'https://translation.googleapis.com/translate_v2/translate'
    params = {
        'q': text,
        'source': source_language,
        'target': target_language,
        'key': 'AIzaSyDWef1w0wUciYILTM3qj6ahhgKPjaPNrD4'
    }
    
    response = requests.post(url, params=params)
    print("The status code of Translate API response is: ", response.status_code)
    
    json_response = response.json()
    
    translated_text = json_response['data']['translations'][0]['translatedText']
    
    return translated_text


translated_text = translate('Hello world!', 'en', 'es')