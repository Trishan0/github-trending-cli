import argparse
import utils

import config
import github_api

parser = argparse.ArgumentParser(
    prog="GitPulse",
    description="GitHub Repository Trending CLI Tool",
    epilog="Thank you for using %(prog)s! :)",
)

parser.add_argument("gitpulse", help="GitPulse CLI Tool")

parser.add_argument(
    "-d",
    "--duration",
    type=str,
    choices=config.VALID_DURATIONS,
    help="Time duration to filter repositories",
    default=config.DEFAULT_DURATION,
)
parser.add_argument(
    "-c", "--calendar", action="store_true", help="Use calendar-based date ranges"
)

parser.add_argument(
    "-l", "--language", type=str, help="Programming language to filter repositories"
)

parser.add_argument(
    "--limit",
    type=int,
    help="Number of repositories to display",
    default=config.DEFAULT_LIMIT,
)

args = parser.parse_args()

date_range = utils.get_date_ranges(args.duration, args.calendar)
language = args.language
limit = args.limit

github_api.fetch_repos(date_range, language, limit)
