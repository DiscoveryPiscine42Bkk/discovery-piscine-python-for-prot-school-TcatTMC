from checkmate import check_K
import sys



def main():
    file_name = sys.argv[1]
    file = open(file_name, "r")
    board = file.read()
    check_K(board)

if __name__ == "__main__":
    main()
    
