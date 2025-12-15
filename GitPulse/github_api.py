import requests
import json
import sys


if (args_count := len(sys.argv)) != 2:
    print("Usage: python github_api.py <language>")
    sys.exit(1)
lang_name = sys.argv[1]


url=f"https://api.github.com/search/repositories?q=stars:>1 language:{lang_name}&sort=stars&order=desc"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error: Unable to fetch data from GitHub API (Status Code: {res.status_code})")
    sys.exit(1)

if res.status_code == 200:
    repo_data = res.json()
    
    
    for item in repo_data['items'][:5]:
        print(f"Repository Name: {item['name']}")
        print(f"Language: {item['language']}")
        print(f"Stars: {item['stargazers_count']/1000}k")
        print(f"Forks: {item['forks_count']/1000}k")
        print(f"Open Issues: {item['open_issues_count']}")
        print(f"URL: {item['html_url']}")
        print("-" * 40)
    
