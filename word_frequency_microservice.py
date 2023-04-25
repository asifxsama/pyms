import requests
import re
import json

def get_word_frequency(url):
    response = requests.get(url)
    html = response.content.decode('utf-8')
    text = re.sub('<[^<]+?>', '', html)
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
    words = text.split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    word_counts_list = [{'word': word, 'count': count} for word, count in word_counts.items()]
    json_data = json.dumps(word_counts_list)
    return json_data
