import copy
import sys

def get_args():
    args = copy.deepcopy(sys.argv)
    args.pop(0)
    return args
