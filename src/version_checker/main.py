import argparse


def main():
    parser = argparse.ArgumentParser(description="", add_help=True)
    parser.add_argument('-sf', '--setup-file', help="specify the file to check version")

    args = parser.parse_args()

    setup_file = getattr(args, "setup_file", ".")

    print(setup_file)

    return 0
