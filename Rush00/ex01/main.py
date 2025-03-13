from checkmate import check_file
import sys

def main():
    if len(sys.argv) <= 1:
        print("No file")
        return


    filename = sys.argv[1]

    check_file(filename)

if __name__ == "__main__":
    main()
    

