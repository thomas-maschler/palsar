import os
import shutil
from pathlib import Path
from typing import List


def extract_archive(archive: str, output_directory: str = '') -> str:
    """
    Extract tar.gz or zip
    return the folder
    """
    if output_directory == '':
        output_directory = f"{Path(archive).parent}/{Path(archive).stem.split('.')[0]}"
    shutil.unpack_archive(archive, output_directory)

    return output_directory


def palsar_name_parse(filename: str):
    """
    Parse palsar file name into components
    TileName (NLat ELong) - LLLLLLL
    Year - YY
    Band - sl_HH, sl_HV, date, linci, mask
    F02DAR - constant:
        F- Full Beam,
        02 Beam number,
        D - Dual polarization,
        O - ascending oribit,
        R right observation
    """


def palsar_folder_parse(directory: str) -> List:
    """
    Given a 1x1 tile folder, parse files that need conversion, return list of paths
    """
    matches = []
    for file in os.listdir(directory):
        if file.endswith(".hdr"):
            matches.append(file.split(".")[0])
        elif file.endswith(".tif"):
            matches.append(file)
    return matches
