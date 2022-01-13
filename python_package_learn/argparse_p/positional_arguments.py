import argparse

parser = argparse.ArgumentParser()
# help 指定输出help 时的内容
# type 指定获得的参数的类型
parser.add_argument("echo", help="echo the string you use here", type=int)
args = parser.parse_args()
print(args.echo**2)

