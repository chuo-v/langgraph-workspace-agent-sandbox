import sys


def main():
    multiplier = 2

    if len(sys.argv) > 1:
        try:
            val = int(sys.argv[1])
            print(f"Result: {val * multiplier}")
        except ValueError:
            print("Please provide an integer.")
    else:
        print(f"Default Result: {10 * multiplier}")


if __name__ == "__main__":
    main()
