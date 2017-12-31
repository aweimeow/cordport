#! /usr/bin/python3

import argparse
from cordport.core import parser as PortParser


def main():
    parser = argparse.ArgumentParser(description="cordport")
    parser.add_argument('-v', '--view', type=str,
                        help="View of the output", default="ovs")
    parser.add_argument('-i', '--ip', type=str,
                        help="Filter by IP address")
    parser.add_argument('-m', '--mac', type=str,
                        help="Filter by MAC address")
    parser.add_argument('-n', '--name', type=str,
                        help="Filter by Name")

    args = parser.parse_args()

    port = PortParser(args)


if __name__ == '__main__':
    main()
