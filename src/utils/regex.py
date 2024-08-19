import re

def is_file_path(target):
    print(target)
    print(re.match('.*\.[a-zA-Z]*$', target))
    return re.match('.*\.[a-zA-Z]*$', target)