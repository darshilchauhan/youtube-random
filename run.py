from apiclient.discovery import build
import webbrowser
import random
import json

def main():
    # read api key
    with open('apikey.json') as f:
        keydata = json.load(f)
    api_key = keydata['key']
    youtube = build('youtube','v3',developerKey=api_key)

    # read keywords
    with open('keywords.json') as f:
        data = json.load(f)
    prefixes = data['prefixes']
    topics = data['topics']
    suffixes = data['suffixes']

    # select keyword randomly
    prefix = random.choice(prefixes)
    topic = random.choice(topics)
    suffix = random.choice(suffixes)
    print(prefix+' '+topic+' '+suffix)
    req = youtube.search().list(q=prefix+' '+topic+' '+suffix, part='snippet', type='video', maxResults=20)
    res=req.execute()
    results=[]
    for item in res['items']:
    #     print(item['id']['videoId'])
        results.append(item)
    choice = random.choice(results)
    print("https://youtube.com/watch?v="+choice['id']['videoId'])

if __name__== "__main__":
    main()

