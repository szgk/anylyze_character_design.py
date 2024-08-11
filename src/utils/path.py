from pathlib import Path

def get_file_paths_in_dir(dir, ex = "jpg"):
    return list(Path(dir).glob('**/*.'+ex))