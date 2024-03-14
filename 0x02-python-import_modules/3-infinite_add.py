#!/usr/bin/python3

if __name__ == "__main__":
    """add infinite number on cLD arg"""
    import sys

    argv = sys.argv
    arg = len(argv) - 1

    sum = 0

    if arg == 0:
        print(sum)
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])
        print(sum)
