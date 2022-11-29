#!/usr/bin/python3
"""
main
"""
import sys

if __name__ == '__main__':
    num_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the reddit to search.")
    else:
        print("{:d}".format(num_subscribers(sys.argv[1])))
