Python tool that picks random keyword from keywords.json, searches youtube and plays a random video from first n results.

usage: run.py [-h][-n numofresults] [-p][-k apikey]

optional arguments:
-h, --help show this help message and exit
-n NUMOFRESULTS, --numOfResults NUMOFRESULTS
number of search results
-p, --printOnly Only print result, do not open link
-k APIKEY, --apiKey APIKEY
Youtube api key, store defualt in apikey.json in same
directory

Store api key in apikey.json as default

Make sure Python's webbrowser library is installed. Try running `python3 -m webbrowser -t www.google.com` to verify.
If the error says no runnable browser found, or if chrome is not the default browser, run the following commands:

```python
# Windows
chrome_path='"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
```
