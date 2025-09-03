#!/usr/bin/python3
# import name of the file


def main():
    names = dir() # name of the file

    for name in names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
