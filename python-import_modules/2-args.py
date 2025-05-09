#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of the list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("Number of argument(s): 0.")
    elif count == 1:
        print("Number of argument(s): 1 argument:")
    else:
        print("Number of argument(s):{} arguments:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
