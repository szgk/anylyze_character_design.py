import re

def is_file_path(target):
    print(target)
    result = re.match('.*\.[a-zA-Z]*$', target)
    print('is file path' if result else 'is not file path')
    return re.match('.*\.[a-zA-Z]*$', target)