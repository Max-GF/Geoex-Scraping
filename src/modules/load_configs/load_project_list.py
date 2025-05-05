"""
    Load project from given file.
"""
def load_project_list(file_path: str = "projects.txt") -> list[str]:
    """
    Load project from a file.

    Args:
        file_path (str, optional): File with projects to consult.
        Defaults to local "projects.txt" file.

    Raises:
        FileNotFoundError: If the file is not found.

    Returns:
        list[str]: Project numbers to be consulted as lists.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Project list file not found: {file_path}") from error
