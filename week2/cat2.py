import sys


def multiple_files():
    if len(sys.argv) > 1:
        for index in range(1, len(sys.argv)):
            filename = sys.argv[index]
            textfile = open(filename, 'r')
            print(textfile.read())
            textfile.close()
    else:
        print('There is no file')

def main():
    multiple_files()


if __name__ == '__main__':
    main()
