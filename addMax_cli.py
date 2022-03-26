import argparse


def calc(args):
    if args.max != "NULL":
        return max(args.numbers)
    else:
        return sum(args.numbers)


def main():
    parser = argparse.ArgumentParser(description="Addition of numbers and finding largest of given numbers")
    parser.add_argument(
        "numbers", metavar="numbers", nargs="*", type=int, help="list of numbers"
    )
    parser.add_argument(
        "--max", type=str, default="NULL", help="write max for printing largest number"
    )
    args = parser.parse_args()
    print(str(calc(args)))


if __name__ == "__main__":
    main()
