import argparse
import utils
import github_api

parser = argparse.ArgumentParser()

parser.add_argument(
    "-t",
    type=str,
    choices=["day", "week", "month", "year"],
    help="Time duration to filter repositories",
)
parser.add_argument("-c", action="store_true", help="Use calendar-based date ranges")


args = parser.parse_args()

date_range = utils.get_date_ranges(args.t, args.c)

github_api.fetch_repos(date_range)
