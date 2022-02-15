from python_questdb_client.row import Row


def test_builder():
    instance = Row.table("a")
    assert isinstance(instance, Row)


def test_timestamp():
    instance = Row.table("a").timestamp_column("timestamp", 1)
    assert str(instance) == "a timestamp=1t"


def test_string():
    instance = Row.table("a").string_column("string", "123")
    assert str(instance) == 'a string="123"'


def test_long():
    instance = Row.table("a").long_column("long", 123)
    assert str(instance) == "a long=123i"


def test_bool():
    instance = Row.table("a").bool_column("bool", True)
    assert str(instance) == "a bool=True"


def test_double():
    instance = Row.table("a").double_column("double", 123.0)
    assert str(instance) == "a double=123.0"


def test_raw_column():
    instance = Row.table("a").raw_column("raw", 123)
    assert str(instance) == "a raw=123"


def test_symbol():
    instance = Row.table("a").symbol("symbol", 123)
    assert str(instance) == "a,symbol=123"


def test_at():
    instance = Row.table("a").raw_column("raw", 123).at(1234)
    assert str(instance) == "a raw=123 1234"


def test_at_now():
    instance = Row.table("a").raw_column("raw", 123).at_now()
    timestamp = str(instance).split(" ")[2]
    assert timestamp


def test_combined():
    instance = (
        Row.table("a")
        .symbol("symbol", "a")
        .timestamp_column("timestamp", 1)
        .string_column("string", "1")
        .long_column("long", 123)
        .bool_column("bool", False)
        .double_column("double", 123.0)
        .raw_column("raw", 123)
        .at(1234)
    )
    assert (
        str(instance)
        == 'a,symbol=a timestamp=1t,string="1",long=123i,bool=False,double=123.0,raw=123 1234'
    )
