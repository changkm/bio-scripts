import shutil
from pathlib import Path
from typing import List

ASSEMBLIES_FOLDER_PATH = "/Users/kchang/test/test_dir/"  # Needs to have trailing /
FILTER_FOLDER_PATH = "/Users/kchang/test/filter/"      # Needs to have trailing /
FILE_NAMES_FILE = "/Users/kchang/test/keep.txt"


def should_copy(file: Path, files_to_keep: List[str]):
    # file.name = only the file name, not the parent folder path.
    # .split('.')[0] is split the string at every dot and only keep the first bit.
    stem = file.name.split('.')[0]
    if stem in files_to_keep:
        return True
    else:
        return False


if __name__ == '__main__':
    with open(FILE_NAMES_FILE) as f:
        files_to_keep = f.readlines()
    files_to_keep = [item.strip() for item in files_to_keep] # get rid of trailing \n, etc

    source_dir = Path(ASSEMBLIES_FOLDER_PATH)
    dest = Path(FILTER_FOLDER_PATH)
    # .glob finds all child files that match the given regex
    files_to_copy = [f for f in source_dir.glob('**/*') if f.is_file() and should_copy(f, files_to_keep)]

    for f in files_to_copy:
        shutil.copy(f, dest / f.name)
