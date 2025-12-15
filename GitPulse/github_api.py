import requests
import json
import sys

from . import config


def fetch_repos(date_range: str, language: str = None, limit: int = 10):
    query = f"pushed:{date_range}"
    if language:
        query += f" language:{language}"

    url = (
        f"{config.GITHUB_API_BASE_URL}?q={query}&sort=stars&order=desc&per_page={limit}"
    )

    try:
        res = requests.get(url)

        if res.status_code != 200:
            print(
                f"Error: Unable to fetch data from GitHub API (Status Code: {res.status_code})"
            )
            sys.exit(1)

        if res.status_code == 200:
            repo_data = res.json()
            items = repo_data["items"]

            if language and items:
                has_match = any(
                    item.get("language", "").lower() == language.lower()
                    for item in items
                )
                if not has_match:
                    print(
                        f"⚠️  Warning: No repositories found for language '{language}'. Showing results without language filter.\n"
                    )
            return items
    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        return []
