#We need de webbrowser library module webbrowser. This allows us to open a webbrowser and navigate to a specific URL.	
import webbrowser
#Request import is needed for us to make json get requests
import requests

print("Welcome to the web data program")
#We need to ask the user for a URL
url = input("Let's find an old website. Please enter a URL: ")
era = input("type a year month and day, ex 20150613: ")

#We need to make a request to the URL | Postman could be used to get data aswell

#url EXAMPLE to get json data @http://archive.org/wayback/available?url=example.com&timestamp=20060101
site = "http://archive.org/wayback/available?url=" + url + "&timestamp=" + era;
response = requests.get(site)
data = response.json()

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", url)