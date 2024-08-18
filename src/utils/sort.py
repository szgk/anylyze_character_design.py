def dict_by_value(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda x:x[1])}