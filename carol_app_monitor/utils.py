from typing import Dict, List


def _check_intersection(list_A: List, list_B: List) -> bool:
    """Check if there is any intersection between two lists.

    Args:
        list_A (List): A list to be checked for intersection.
        list_B (List): A list to be checked for intersection.

    Returns:
        bool: `True` if there is any intersection, `False` otherwise.

    Examples:
        >>> _check_intersection([1,2,3], [3,4,5])
        True
        >>> _check_intersection([1,2,3], [4,5,6])
        False
    """
    if any(item in list_B for item in list_A):
        return True
    else:
        return False


def filter_dicts_by_values(
    raw_dicts: List[Dict],
    filter_value: str | List | None,
    keep: bool | None = None,
    drop: bool | None = None,
) -> List[Dict]:
    """Filters a list of dicts based whether contain a specific value.

    Args:
        raw_dicts (List[Dict]): The list of dicts to filter.
        filter_value (str | List | None): The value or a list of values to filter by.\
        Can be `None` if you want to drop all dictionaries with empty values.

        keep (bool | None, optional): Whether to keep the dictionaries that\
        contain the `filter_value`. Defaults to None.

        drop (bool | None, optional): Whether to exclude the dictionaries that\
        contain the `filter_value`. Defaults to None.

    Raises:
        ValueError: If `keep` and `drop` are `None`, raises: keep and drop\
        cannot be both None.
        ValueError: If `keep` and `drop` are `True`, raises: keep and drop\
        cannot be both True.
        ValueError: If `keep` and `drop` are `False`, raises: keep and drop\
        cannot be both False.
        TypeError: If `keep` is `True` or `drop` is `False` and`filter_value`\
        isn't a `str` or a `list`, raises: To keep the `filter_value` it must\
        be a `str` or a `list`.
        TypeError: If `keep` is `False` or `drop` is `True` and `filter_value`\
        isn't a `str`, `list` or `None`, raises: filter_value must be a str, list\
        or None.

    Returns:
        List[Dict]: The filtered list of dictionaries.

    Examples:
        >>> filter_dicts_by_values([{"A": "1", "B": "2"}, {"C": "3", "D": "4"}], filter_value="3", keep=False)
        [{'A': '1', 'B': '2'}]

        >>> filter_dicts_by_values([{"A": "1", "B": "2"}, {"C": "3", "D": "4"}], filter_value="3", keep=True)
        [{'C': '3', 'D': '4'}]

        >>> filter_dicts_by_values([{"A": "1", "B": "2"}, {"C": "3", "D": "4"}], filter_value="3", drop=False)
        [{'C': '3', 'D': '4'}]

        >>> filter_dicts_by_values([{"A": "1", "B": "2"}, {"C": "3", "D": "4"}], filter_value="3", drop=True)
        [{'A': '1', 'B': '2'}]
    """
    if keep is None and drop is None:
        raise ValueError("`keep` and `drop` cannot be both `None`.")

    if keep and drop:
        raise ValueError("`keep` and `drop` cannot be both `True`.")

    if keep is False and drop is False:
        raise ValueError("`keep` and `drop` cannot be both `False`.")

    match keep, drop:
        case [True, False] | [True, None] | [None, False]:
            if isinstance(filter_value, str):
                filtered_dicts = [
                    raw_dict
                    for raw_dict in raw_dicts
                    if filter_value in raw_dict.values()
                ]
            elif isinstance(filter_value, list):
                filtered_dicts = [
                    raw_dict
                    for raw_dict in raw_dicts
                    if _check_intersection(filter_value, raw_dict.values())
                ]
            else:
                raise TypeError(
                    "To keep the `filter_value` it must be a `str` or a `list`."
                )

        case [False, True] | [None, True] | [False, None]:
            if isinstance(filter_value, (str, type(None))):
                filtered_dicts = [
                    raw_dict
                    for raw_dict in raw_dicts
                    if filter_value not in raw_dict.values()
                ]
            elif isinstance(filter_value, list):
                filtered_dicts = [
                    raw_dict
                    for raw_dict in raw_dicts
                    if not _check_intersection(filter_value, raw_dict.values())
                ]
            else:
                raise TypeError(
                    "`filter_value` must be a `str`, `list` or `None`."
                )

    return filtered_dicts


def merge_dicts(*dicts: Dict) -> Dict:
    """Merge dicts into unique dict.

    Raises:
        TypeError: If any args aren't a dict, raises:\
        Args must be a `dict`.

    Returns:
        Dict: Merged dict.

    Examples:
        >>> merge_dicts({"A": 1, "B": 2},{"C": 3, "D": 4})
        {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    """
    merged_dicts = {}

    for raw_dict in dicts:
        if not isinstance(raw_dict, dict):
            raise TypeError("Args must be `dict`.")
        merged_dicts.update(raw_dict)
    return merged_dicts
