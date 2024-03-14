#!/usr/bin/python3

if __name__ == "__main__":
    """print the no. and value of CLD"""
    import sys

    argv = sys.argv
    arg = len(argv) - 1

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("{} argument:".format(arg))
        print("{}: {}".format(arg, argv[arg]))
    elif aarg > 1:
        print("{} arguments:".format(arg))

        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
