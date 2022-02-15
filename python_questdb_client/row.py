import time
from python_questdb_client.key_value_pair import KeyValuePair


class Row:
    def __init__(self, table):
        self._symbol_set = {}
        self._column_set = {}
        self._table = table
        self._at = None

    @classmethod
    def table(cls, table):
        return cls(table)

    def at(self, timestamp):
        self._at = timestamp
        return self

    def at_now(self):
        self.at(timestamp=time.time_ns())
        return self

    def symbol(self, key, value):
        pair = KeyValuePair(key)
        pair.set_raw_value(value)
        self._symbol_set[key] = pair
        return self

    def string_column(self, key, value):
        pair = KeyValuePair(key)
        pair.set_string_value(value)
        self._column_set[key] = pair
        return self

    def long_column(self, key, value):
        pair = KeyValuePair(key)
        pair.set_long_value(value)
        self._column_set[key] = pair
        return self

    def bool_column(self, key, value):
        pair = KeyValuePair(key)
        pair.set_bool_value(value)
        self._column_set[key] = pair
        return self

    def double_column(self, key, value):
        pair = KeyValuePair(key)
        pair.set_raw_value(value)
        self._column_set[key] = pair
        return self

    def timestamp_column(self, key, value):
        pair = KeyValuePair(key)
        pair.set_timestamp_value(value)
        self._column_set[key] = pair
        return self

    def raw_column(
        self,
        key,
        value,
    ):
        pair = KeyValuePair(key)
        pair.set_raw_value(value)
        self._column_set[key] = pair
        return self

    def __str__(self):
        symbols = ""
        symbol_set_values = [str(x) for x in self._symbol_set.values()]
        if len(symbol_set_values) > 0:
            symbols = ",".join(symbol_set_values)

        columns = ""
        column_set_values = [str(x) for x in self._column_set.values()]
        if len(column_set_values) > 0:
            columns = ",".join(column_set_values)

        point_str = self._table
        if symbols != "":
            point_str = point_str + f",{symbols}"

        if columns != "":
            point_str = point_str + f" {columns}"

        if self._at:
            point_str = point_str + f" {self._at}"

        return point_str
