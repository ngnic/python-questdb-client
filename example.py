import datetime as dt
import time

from python_questdb_client.row import Row

from python_questdb_client.client import Client

multiple_rows = [
    Row.table("test_table")
    .at(str(time.time_ns()))
    .symbol("symbol_test", value="test")
    .string_column("string_value", value="test")
    .long_column("long_value", value=1)
    .bool_column("bool_value", value=True)
    .double_column("double_value", value=1.23)
    .timestamp_column("timestamp_value", value=str(time.time_ns()))
    .raw_column("raw_value", value=123),
]

single_row = (
    Row.table("test_table")
    .at_now()
    .symbol("symbol_test", value="test")
    .string_column("string_value", value="test")
    .long_column("long_value", value=1)
    .bool_column("bool_value", value=True)
    .double_column("double_value", value=1.23)
    .timestamp_column("timestamp_value", value=str(time.time_ns()))
    .raw_column("raw_value", value=123)
)

client = Client("localhost", 9009)
client.buffer_rows(multiple_rows)
client.buffer_row(single_row)
client.flush()
