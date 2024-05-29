"""Common filesystem"""

import os
from typing import Any
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
import box.exceptions as be

from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """ reads a yaml file and returns

    Args:
        Path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except be.BoxValueError as exc:
        raise exc.ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_driectories(path_to_directories: list, verbose=True):
    """create list if directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_logs (bool, optional): ignore if multiple dirs is to be created. Defaults to False.    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of the file

    Returns:
        str: size in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
