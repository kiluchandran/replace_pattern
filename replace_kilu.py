import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("-f", "--find")
parser.add_argument("-r", "--replace")
args = parser.parse_args()


def main():
    file_name = args.input_file
    if args.find and args.replace:
        search_word = args.find
        replace_word = args.replace


main()
