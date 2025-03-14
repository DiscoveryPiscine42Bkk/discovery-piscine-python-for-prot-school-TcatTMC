import sys

def downcase_all():
    if len(sys.argv) > 1:
        i = 1
        while i < len(sys.argv):
            print(sys.argv[i].lower())
            i += 1
    else:
        print('none')

downcase_all()