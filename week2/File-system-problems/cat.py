import sys

def file_content():
    filename = sys.argv
    textfile = open(filename, "r")
    print(textfile.read())
    textfile.close()

def main():
    file_content()



if __name__ == "__main__":
    main()
