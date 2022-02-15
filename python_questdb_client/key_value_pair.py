import re


RESTRICTED_ALPHABET_REGEX = re.compile(r"[.?,:\/\\\0)(_+*~%]+")
BOOLEAN_VALUE_MAP = {
    "t": "t",
    "T": "T",
    "true": "true",
    "True": "True",
    True: "True",
    "f": "f",
    "F": "F",
    "false": "false",
    "False": "False",
    False: "False",
}


class KeyValuePair:
    def __init__(self, key=None, value=None):
        if key:
            self.set_key(key)
        self._value = value

    def __eq__(self, other):
        return self.key() == other.key()

    def __str__(self):
        return f"{self._key}={self._value}"

    def key(self):
        return self._key

    def set_key(self, key):
        match = RESTRICTED_ALPHABET_REGEX.match(key)
        if match:
            raise ValueError(f"key contains invalid character.value: {key}")
        self._key = key

    def set_string_value(self, value):
        self._value = f'"{value}"'

    def set_long_value(self, value):
        self._value = f"{value}i"

    def set_bool_value(self, value):
        if value not in BOOLEAN_VALUE_MAP:
            raise ValueError(f"invalid boolean value.key: {self._key} value: {value}")
        self._value = BOOLEAN_VALUE_MAP[value]

    def set_timestamp_value(self, value):
        self._value = f"{value}t"

    def set_raw_value(self, value):
        self._value = value
