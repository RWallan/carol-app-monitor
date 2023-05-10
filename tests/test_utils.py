from pytest import mark, raises

from carol_app_monitor import utils


def test_merge_dicts_with_no_primary_key_with_two_dicts():
    dict_a = {"A": 1, "B": 2}
    dict_b = {"C": 3, "D": 4}

    expected_dict = {"A": 1, "B": 2, "C": 3, "D": 4}

    result_dict = utils.merge_dicts(dict_a, dict_b)

    assert result_dict == expected_dict


def test_merge_dicts_with_no_primary_key_with_more_than_two_dicts():
    dict_a = {"A": 1, "B": 2}
    dict_b = {"C": 3, "D": 4}
    dict_c = {"E": 5, "F": 6}
    dict_d = {"G": 7, "H": 8}

    expected_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
    }

    result_dict = utils.merge_dicts(dict_a, dict_b, dict_c, dict_d)

    assert result_dict == expected_dict


def test_merge_dicts_with_a_non_dict_must_raises():
    arg_a = {"A": 1, "B": 2}
    arg_b = [1, 2, 3, 4]

    error_message = "Args must be `dict`."

    with raises(TypeError) as error:
        utils.merge_dicts(arg_a, arg_b)

    assert error.value.args[0] == error_message


def test_check_intersections_with_intersection_must_return_true():
    response = utils._check_intersection([1, 2, 3], [3, 4, 5])

    assert response is True


def test_check_intersections_with_no_intersection_must_return_false():
    response = utils._check_intersection([1, 2, 3], [4, 5, 6])

    assert response is False


@mark.parametrize(
    "raw_dicts, filter_value, keep, drop, expected",
    [
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            False,
            None,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            True,
            None,
            [{"C": "3", "D": "4"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            None,
            False,
            [{"C": "3", "D": "4"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            None,
            True,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            False,
            True,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            True,
            False,
            [{"C": "3", "D": "4"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            "3",
            False,
            True,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}, {"E": "3", "F": "5"}],
            ["3", "5"],
            False,
            None,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}, {"E": "3", "F": "5"}],
            ["3", "5"],
            True,
            None,
            [{"C": "3", "D": "4"}, {"E": "3", "F": "5"}],
        ),
    ],
)
def test_filter_dicts_by_value_must_return_correct_list_of_dictionaries(
    raw_dicts, filter_value, keep, drop, expected
):
    result = utils.filter_dicts_by_values(raw_dicts, filter_value, keep, drop)

    assert result == expected


@mark.parametrize(
    "raw_dicts, filter_value, keep, drop, expected",
    [
        (
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}],
            None,
            False,
            None,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}],
            None,
            None,
            True,
            [{"A": "1", "B": "2"}],
        ),
        (
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}],
            None,
            False,
            True,
            [{"A": "1", "B": "2"}],
        ),
    ],
)
def test_filter_dicts_by_value_must_return_correct_list_of_dictionaries_if_want_to_drop_None(
    raw_dicts, filter_value, keep, drop, expected
):
    result = utils.filter_dicts_by_values(raw_dicts, filter_value, keep, drop)

    assert result == expected


def test_filter_dicts_by_value_must_raises_value_error_if_keep_drop_is_none():
    error_message = "`keep` and `drop` cannot be both `None`."

    with raises(ValueError) as error:
        utils.filter_dicts_by_values(
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}], "3", None, None
        )

    assert error.value.args[0] == error_message


def test_filter_dicts_by_value_must_raises_value_error_if_keep_drop_is_true():
    error_message = "`keep` and `drop` cannot be both `True`."

    with raises(ValueError) as error:
        utils.filter_dicts_by_values(
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}], "3", True, True
        )

    assert error.value.args[0] == error_message


def test_filter_dicts_by_value_must_raises_value_error_if_keep_drop_is_false():
    error_message = "`keep` and `drop` cannot be both `False`."

    with raises(ValueError) as error:
        utils.filter_dicts_by_values(
            [{"A": "1", "B": "2"}, {"C": None, "D": "4"}], "3", False, False
        )

    assert error.value.args[0] == error_message


@mark.parametrize(
    "raw_dicts, filter_value, keep, drop, expected",
    [
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            3,
            True,
            None,
            "To keep the `filter_value` it must be a `str` or a `list`.",
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            3.2,
            True,
            None,
            "To keep the `filter_value` it must be a `str` or a `list`.",
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            None,
            True,
            None,
            "To keep the `filter_value` it must be a `str` or a `list`.",
        ),
    ],
)
def test_filter_dicts_by_value_must_raises_type_error_if_keep_is_true_and_filter_value_is_not_str_list(
    raw_dicts, filter_value, keep, drop, expected
):
    with raises(TypeError) as error:
        utils.filter_dicts_by_values(raw_dicts, filter_value, keep, drop)

    assert error.value.args[0] == expected


@mark.parametrize(
    "raw_dicts, filter_value, keep, drop, expected",
    [
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            3,
            False,
            None,
            "`filter_value` must be a `str`, `list` or `None`.",
        ),
        (
            [{"A": "1", "B": "2"}, {"C": "3", "D": "4"}],
            3.2,
            False,
            None,
            "`filter_value` must be a `str`, `list` or `None`.",
        ),
    ],
)
def test_filter_dicts_by_value_must_raises_type_error_if_keep_is_true_and_filter_value_is_not_str_list(
    raw_dicts, filter_value, keep, drop, expected
):
    with raises(TypeError) as error:
        utils.filter_dicts_by_values(raw_dicts, filter_value, keep, drop)

    assert error.value.args[0] == expected
