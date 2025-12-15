def format_repos(repos: list):
    """
    Display repository information in a readable format.

    Args:
        repos: List of repository dictionaries from GitHub API
    """
    if not repos:
        print("No repositories found for the given criteria.")
        return

    print(f"\n📊 Found {len(repos)} trending repositories:\n")

    for item in repos:
        print(f"Repository Name: {item['name']}")
        print(f"Language: {item.get('language', 'N/A')}")
        print(f"Stars: {item['stargazers_count']}")
        print(f"Forks: {item['forks_count']}")
        print(f"Description: {item.get('description', 'No description')}")
        print(f"URL: {item['html_url']}")
        print("-" * 60)
