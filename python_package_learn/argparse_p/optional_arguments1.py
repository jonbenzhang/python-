import argparse

parser = argparse.ArgumentParser()
# -v 为短命令,方便使用
# help 指定输出help 时的内容
# action 并赋值为 "store_true"。这意味着，当这一选项存在时，为 args.verbose 赋值为 True。
# 没有指定时则隐含地赋值为 False。
# 当你为其指定一个值时，它会报错
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
print(args.verbose)
if args.verbose:
    print("verbosity turned on")
