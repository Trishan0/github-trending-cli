import requests
import json
import sys


def fetch_repos(date_range: str, language: str = None):
    url = f"https://api.github.com/search/repositories?q=pushed:{date_range} language:{language}&sort=stars&order=desc"

    res = requests.get(url)

    if res.status_code != 200:
        print(
            f"Error: Unable to fetch data from GitHub API (Status Code: {res.status_code})"
        )
        sys.exit(1)

    if res.status_code == 200:
        repo_data = res.json()

        for item in repo_data["items"][:5]:
            print(f"Repository Name: {item['name']}")
            print(f"Language: {item['language']}")
            print(f"Stars: {item['stargazers_count']}")
            print(f"Forks: {item['forks_count']}")
            print(f"Open Issues: {item['open_issues_count']}")
            print(f"Created At: {item['created_at']}")
            print(f"Updated At: {item['updated_at']}")
            print(f"Pushed At: {item['pushed_at']}")
            print(f"URL: {item['html_url']}")
            print("-" * 40)
