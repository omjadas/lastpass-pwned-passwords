#!/usr/bin/env python
import requests
import hashlib
import csv
import sys

url = "https://api.pwnedpasswords.com/range/{}"


def main():
    if len(sys.argv) < 2:
        print("The file containing your passwords must be provided", file=sys.stderr)
        exit()
    elif len(sys.argv) > 2:
        print("Only one argument can be provided", file=sys.stderr)
        exit()
    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if ','.join(row) == "url,username,password,extra,name,grouping,fav":
                continue
            hash = hashlib.sha1(row[2].encode('utf-8')).hexdigest()

            r = requests.get(url.format(hash[:5]))

            if hash[5:].upper() in r.text:
                print("{}'s password for {} has been leaked.".format(row[1], row[4]))


if __name__ == "__main__":
    main()
