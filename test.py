import os
import re
import sys
import glob
from argparse import ArgumentParser

def parse():
    usage = 'python {} -s "DIR" -b "YYYYMMDD" [--help]'.format(os.path.basename(__file__))

    argparser = ArgumentParser(usage=usage)
    argparser.add_argument("-s", "--source",   required=True, help="target directory")
    argparser.add_argument("-b", "--basedate", required=True, help="basedate")
    argparser.add_argument("-p", "--pattern", required=False, help="search pattern, default={}".format(DEFALUT_SEARCH_PATTERN))

    return argparser.parse_args()


def file_search(dir ,basedate):
    res = [f for f in glob.glob(os.path.abspath(dir)+"/**/*.log", recursive=True) if basedate in f]
    return res

def filter(contents, pattern):
    regex = re.compile(pattern)
    res = ""

    for line in contents.splitlines(True):
      if(regex.search(line)):
         res += line

    return res

DEFALUT_SEARCH_PATTERN = "ERROR|WARN"

if __name__ == "__main__":

    args = parse()

    pattern = args.pattern if None else DEFALUT_SEARCH_PATTERN
    isError = False

    contents = ""
    try:
        for f in file_search(args.source, args.basedate):
            with open(os.path.abspath(f), "r") as log:
                contents += "checking... " + f + "\n"

                result = filter(log.read(), pattern)
                if result:
                    contents += result
                    isError = True

    except Exception as err:
        print("error occured while analyzing.")
        sys.exit(1)

    if isError:
        print(contents)
        logfile = open('./errorlog.txt','a')
        logfile.write(contents)
        sys.exit(1)
    else:
        sys.exit(0)


