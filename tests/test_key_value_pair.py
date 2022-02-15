from python_questdb_client.key_value_pair import KeyValuePair, BOOLEAN_VALUE_MAP

RESTRICTED_TEST_SET = [
    ".",
    "?",
    ",",
    ":",
    "/",
    "\\",
    "\0",
    ")",
    "(",
    "_",
    "+",
    "*",
    "~",
    "%",
]


def test_init_key_throws_error_if_using_restricted_alphabet():
    for item in RESTRICTED_TEST_SET:
        try:
            KeyValuePair(item)
        except ValueError as e:
            assert str(e) == f"key contains invalid character.value: {item}"


def test_eq():
    first_pair = KeyValuePair()
    first_pair.set_key("a")

    second_pair = KeyValuePair()
    second_pair.set_key("a")

    third_pair = KeyValuePair()
    third_pair.set_key("b")

    assert first_pair == second_pair
    assert second_pair != third_pair
    assert first_pair != third_pair


def test_key_throws_error_if_using_restricted_alphabet():
    kv = KeyValuePair()
    for item in RESTRICTED_TEST_SET:
        try:
            kv.set_key(item)
        except ValueError as e:
            assert str(e) == f"key contains invalid character.value: {item}"


def test_string_value():
    pair = KeyValuePair()
    pair.set_key("a")
    pair.set_string_value("b")
    assert str(pair) == 'a="b"'


def test_long_value():
    pair = KeyValuePair()
    pair.set_key("a")
    pair.set_long_value(1)
    assert str(pair) == "a=1i"


def test_bool_value():
    pair = KeyValuePair()
    pair.set_key("a")
    for original_value, normalised_value in BOOLEAN_VALUE_MAP.items():
        pair.set_bool_value(original_value)
        assert str(pair) == f"a={normalised_value}"


def test_timestamp_value():
    pair = KeyValuePair()
    pair.set_key("a")
    pair.set_timestamp_value(1)
    assert str(pair) == "a=1t"


def test_raw_value():
    pair = KeyValuePair()
    pair.set_key("a")
    pair.set_raw_value(1)
    assert str(pair) == "a=1"


def test_escaped_value():
    pair = KeyValuePair()
    pair.set_key("a")
    pair.set_raw_value("test\ 123")
    assert str(pair) == "a=test\ 123"
