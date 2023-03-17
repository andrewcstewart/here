from pathlib import Path

def here(file_path: str = None) -> Path:
    """
    Find the path to the directory containing the pyproject.toml file, 
    or to a file in the parent directory hierarchy if specified.

    Args:
        file_path (str, optional): A relative path to a file in the 
            parent directory hierarchy of the pyproject.toml file. 
            Defaults to None.

    Returns:
        Path: A Path object pointing to the directory or file.
    
    Raises:
        FileNotFoundError: If pyproject.toml file not found in directory hierarchy.
    """
    current_dir = Path.cwd()
    while current_dir != Path("/"):
        pyproject_path = current_dir / "pyproject.toml"
        if pyproject_path.exists():
            if file_path is not None:
                return (current_dir / file_path).resolve()
            else:
                return current_dir
        current_dir = current_dir.parent
    raise FileNotFoundError("pyproject.toml file not found in directory hierarchy")
