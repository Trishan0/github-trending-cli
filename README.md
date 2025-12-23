# GitPulse 🔥

[Read the Medium Article](https://trishan-fernando.medium.com/gitpulse-github-trending-tool-8ab2c4257da3) 

A beautiful command-line tool to discover trending GitHub repositories. Filter by time range, programming language, and get instant insights into what's hot in the developer community.

## Features ✨

-   📊 View trending repositories based on time ranges (day, week, month, year)
-   🎯 Filter by programming language
-   📅 Support for both rolling and calendar-based date ranges
-   🎨 Beautiful, colorful terminal output using Rich
-   ⚡ Fast and lightweight
-   🔍 Smart error handling and validation

## Installation 🚀

### Prerequisites

-   Python 3.12 or higher
-   pip

### Install from source

1. Clone the repository:

```bash
git clone https://github.com/trishan0/github-trending-cli.git
cd github-trending-cli
```

2. Install the package:

```bash
pip install -e .
```

3. Verify installation:

```bash
gitpulse --help
```

## Usage 💻

### Basic Usage

```bash
# Show trending repos from the last week (default)
gitpulse gitpulse

# Show trending repos from the last month
gitpulse gitpulse --duration month

# Show top 20 trending repos
gitpulse gitpulse --limit 20

# Filter by programming language
gitpulse gitpulse --language python

# Combine options
gitpulse gitpulse --duration month --language javascript --limit 15
```

### Command-Line Arguments

| Argument     | Short | Description                                          | Default | Options                                           |
| ------------ | ----- | ---------------------------------------------------- | ------- | ------------------------------------------------- |
| `--duration` | `-d`  | Time range to filter repositories                    | `week`  | `day`, `week`, `month`, `year`                    |
| `--limit`    |       | Number of repositories to display                    | `10`    | Any positive integer                              |
| `--language` | `-l`  | Filter by programming language                       | None    | Any language (e.g., `python`, `javascript`, `go`) |
| `--calendar` | `-c`  | Use calendar-based ranges (previous week/month/year) | False   | Flag                                              |

### Examples

```bash
# Last 24 hours trending repos
gitpulse gitpulse -d day --limit 5

# Last calendar month's trending Python repos
gitpulse gitpulse -d month -l python --calendar

# Top 50 repos from the last year
gitpulse gitpulse -d year --limit 50

# Trending Go repositories
gitpulse gitpulse -l go
```

## How It Works 🔧

GitPulse uses the GitHub Search API to find repositories that were recently pushed/created and sorts them by star count. This gives you a real-time view of what's trending in the developer community.

**Date Filtering:**

-   **Rolling mode (default)**: Last X days from today

    -   `day`: Last 24 hours
    -   `week`: Last 7 days
    -   `month`: Last 30 days
    -   `year`: Last 365 days

-   **Calendar mode (`--calendar`)**: Previous calendar period
    -   `week`: Previous Monday-Sunday
    -   `month`: Previous calendar month
    -   `year`: Previous calendar year

## Output Format 📋

The tool displays repositories in a beautiful table format showing:

-   Repository rank
-   Repository name
-   Primary programming language
-   Star count (formatted: 1k, 1M)
-   Fork count (formatted: 1k, 1M)
-   Description

## Dependencies 📦

-   `requests` - HTTP library for GitHub API calls
-   `rich` - Beautiful terminal formatting

## Project Structure 📁

```
github-trending-cli/
├── GitPulse/
│   ├── __init__.py
│   ├── cli.py           # CLI argument parsing and main entry point
│   ├── github_api.py    # GitHub API integration
│   ├── formatter.py     # Output formatting with Rich
│   ├── utils.py         # Date range calculations
│   └── config.py        # Configuration constants
├── pyproject.toml       # Project configuration
├── README.md
└── LICENSE
```

## Error Handling 🛡️

The tool handles various error scenarios:

-   Invalid programming languages (shows warning, displays results without filter)
-   Network errors (displays error message)
-   API rate limiting (shows status code)
-   Invalid time ranges (argparse validation)

## Limitations ⚠️

-   GitHub API rate limit: 60 requests/hour for unauthenticated requests
-   No authentication required, but limits apply
-   "Trending" is approximated using recently pushed repos sorted by stars

## Contributing 🤝

Contributions are welcome! Feel free to:

-   Report bugs
-   Suggest new features
-   Submit pull requests

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✍️

Created by [Trishan Fernando] as a Project of [RoadMap.sh](https://roadmap.sh/projects/github-trending-cli)

## Acknowledgments 🙏

-   Built with [Rich](https://github.com/Textualize/rich) for beautiful terminal output
-   Powered by [GitHub REST API](https://docs.github.com/en/rest)

---

**Star this repo if you find it useful! ⭐**
