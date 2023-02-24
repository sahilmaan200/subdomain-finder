#created by Sahil maan
# # finding active urls

import requests
def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
             pass
target_url ="youtube.com"
with open("wordlist file location","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url 
        response = request(test_url)
        if response:
            print("[+]discovered subdomains -->  " + test_url)
