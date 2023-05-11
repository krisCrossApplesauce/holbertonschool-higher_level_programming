#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1

    if argc == 0:
        end = "s."
    elif argc == 1:
        end = ":"
    else:
        end = "s:"

    print("{} argument{}".format(argc, end))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
