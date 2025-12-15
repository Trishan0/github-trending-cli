import argparse
import utils

parser = argparse.ArgumentParser()

parser.add_argument('-t', type=str, choices=['day', 'week','month','year'], help='Time duration to filter repositories')

args = parser.parse_args()

print(f"args : {args.t}")

date_range = utils.get_date_ranges(args.t)
print(f"Date Range: {date_range}")