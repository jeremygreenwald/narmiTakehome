import sys

from schedule import display_schedule

if __name__ == '__main__':
    print(sys.argv[1])
    display_schedule(sys.argv[1])
