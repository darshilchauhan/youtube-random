"""
TODO 
turn this into a cli tool with options:
    numOfResults
    add, remove and removeContaining for prefix, suffix and topic from keywords.json
    -p only for printing and not opening the link
    repeatDuration : after how many videos can a video be chosen again

make sure none of the last 50 selected videos get played
"""


from apiclient.discovery import build
import random
import json
import subprocess

def getYoutubeResource():
    # read api key
    with open('apikey.json') as f:
        keydata = json.load(f)
    api_key = keydata['key']
    youtube = build('youtube','v3',developerKey=api_key)
    return youtube

def getSearchString():
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
    return prefix+' '+topic+' '+suffix

def main():
    youtube = getYoutubeResource()
    searchString = getSearchString()
    
    req = youtube.search().list(q=searchString, part='snippet', type='video', maxResults=20)
    res=req.execute()
    results=[]
    for item in res['items']:
        results.append(item)
    choice = random.choice(results)
    resultUrl = "https://youtube.com/watch?v="+choice['id']['videoId']

    print(searchString)
    print(resultUrl)
    

    bashCommand = "python3 -m webbrowser -t " + resultUrl
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__== "__main__":
    main()

