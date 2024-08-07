from pathlib import Path

def get_file_paths_in_dir(dir, ex = "jpg"):
    print(dir, ex)
    return list(Path(dir).glob('**/*.'+ex))