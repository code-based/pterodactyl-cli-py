import requests

ver = "testrelease"
response = requests.get("https://api.github.com/repos/code-based/pterodactyl-cli-py/releases/latest")
gitver = print(response.json()["name"])
if gitver == ver:
    print('yes')
else:
    print ('no')