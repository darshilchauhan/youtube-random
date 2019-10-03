from apiclient.discovery import build
import random
import json
import subprocess, sys, argparse

def main():
    args = get_arguments()
    searchString = get_search_string()
    video = get_video(searchString, args.numOfResults, args.apiKey)
    resultUrl = "https://youtube.com/watch?v="+video['id']['videoId']
    print(searchString+"\n"+resultUrl)    
    if not args.printOnly:
        open_video(resultUrl)

def get_video(searchString, numOfResults, apiKey):
    if (numOfResults<=0):
        print("argument for number of search results is " + str(numOfResults) + ", invalid")
        exit(1)
    youtube = get_youtube_resource(apiKey)
    req = youtube.search().list(q=searchString, part='snippet', type='video', maxResults=numOfResults)
    res=req.execute()
    if not res['items']:
        print('Search results were empty')
        exit(1)
    return random.choice(res['items'])

def open_video(resultUrl):
    bashCommand = "python3 -m webbrowser -t " + resultUrl
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    if not process.returncode:
        print('Browser link opened successfully')
    else:
        print('Error opening link in browser, error code:' + str(process.returncode))

def get_youtube_resource(apiKey):
    youtube = build('youtube','v3',developerKey=apiKey)
    return youtube

def get_search_string():
    with open('keywords.json') as f:
        data = json.load(f)
    return random.choice(data['prefixes'])+' '+random.choice(data['topics'])+' '+random.choice(data['suffixes'])

def get_api_key():
    with open('apikey.json') as f:
        keydata = json.load(f)
    return keydata['key']

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numOfResults", type=int, default=20, help="number of search results")
    parser.add_argument("-p", "--printOnly", action="store_true", help="Only print result, do not open link")
    parser.add_argument("-k", "--apiKey", default=get_api_key(), help="Youtube api key, store defualt in apikey.json in same directory")
    # parser.add_argument("--addPrefix", help="add to prefix list")
    # parser.add_argument("--addSuffix", help="add to suffix list")
    # parser.add_argument("--addTopic", help="add to topic list")
    # parser.add_argument("--removePrefix", help="remove from prefix list")
    # parser.add_argument("--removeSuffix", help="remove from suffix list")
    # parser.add_argument("--removeTopic", help="remove from topic list")
    # parser.add_argument("--removePrefixContaining", help="remove from prefix list containing given string")
    # parser.add_argument("--removeSuffixContaining", help="remove from suffix list containing given string")
    # parser.add_argument("--removeTopicContaining", help="remove from topic list containing given string")
    return parser.parse_args()

if __name__== "__main__":
    main()

