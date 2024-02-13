import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("search_word")
parser.add_argument("replace_word")
parser.add_argument("-f", "--find", action="store_true")
parser.add_argument("-r", "--replace", action="store_true")
args = parser.parse_args()


def search_replace(file_name, search_word, replace_word):
    with open(file_name, "r") as file:
        file_contents = file.read()
        updated_contents = file_contents.replace(search_word, replace_word)
        print(updated_contents)

    # with open(file_name, "w") as file:
    #     file.write(updated_contents)


def main():
    file_name = args.input_file
    if args.find and args.replace:
        search_word = args.search_word
        replace_word = args.replace_word
        search_replace(file_name, search_word, replace_word)


main()
