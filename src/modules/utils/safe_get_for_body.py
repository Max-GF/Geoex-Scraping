"""
    This module provides a utility function to safely access nested dictionary or list elements.
"""
def safe_get(
    response_dict : dict | None,
    keys : list[str],
    default:str | None =None
    ):
    """
    Safely get a value from a nested dictionary or list using a list of keys.
    This function allows for safe traversal of nested structures, returning a default value if any key is not found.

    Args:
        d (dict): The dictionary or list to traverse.
        keys (string): A list of keys or indices to traverse the dictionary or list.
        default (str | None, optional): Defalt value for not found keys. Defaults to None.

    Returns:
        _type_: _description_
    """
    if response_dict is None:
        return default
    for key in keys:
        if isinstance(response_dict, dict):
            response_dict = response_dict.get(key)
        elif isinstance(response_dict, list) and isinstance(key, int) and len(response_dict) > key:
            response_dict = response_dict[key]
        else:
            return default
        if response_dict is None:
            return default
    return response_dict
