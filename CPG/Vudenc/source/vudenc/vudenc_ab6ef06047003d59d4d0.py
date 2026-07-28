def test_escape(self):...
assert escape_literal("'") == "'\\''"
assert escape_literal(date(2001, 1, 1)) == "toDate('2001-01-01')"
assert escape_literal(datetime(2001, 1, 1, 1, 1, 1)
    ) == "toDateTime('2001-01-01T01:01:01')"
assert escape_literal([1, 'a', date(2001, 1, 1)]
    ) == "(1, 'a', toDate('2001-01-01'))"
