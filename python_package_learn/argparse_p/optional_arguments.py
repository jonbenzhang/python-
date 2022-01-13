import argparse

parser = argparse.ArgumentParser()
# help 指定输出help 时的内容
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
