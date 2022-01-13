import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")
# action 为count 统计-v出现的次数
# args.verbosity 为v出现的次数,如果没有-v则args.verbosity None
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
print(args.verbosity )
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)

#  $ python positional_optional_arguments2.py 4
# 16
#  $ python positional_optional_arguments2.py 4 -v
# 4^2 == 16
#  $ python positional_optional_arguments2.py 4 -vv
# the square of 4 equals 16
#  $ python positional_optional_arguments2.py 4 -vvvvvv
# 16
#  $ python positional_optional_arguments2.py 4 --verbosity --verbosity
# the square of 4 equals 16
