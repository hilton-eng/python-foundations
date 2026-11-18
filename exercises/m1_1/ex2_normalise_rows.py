"""write normalise_rows(rows). 
It takes a list of dicts, like rows from a CSV, and returns a new list of new dicts where:
each key has its whitespace stripped and is lowercased;
string values have their whitespace stripped;
any other value (numbers, for example) is left as it is;
the input is not changed at all.  """

def normalise_rows(rows):
    normalised_rows = []
    for row in rows:
        new_row = {}
        for key, value in row.items():
            clean_key = key.strip().lower()
            if isinstance(value, str):
                clean_value = value.strip()
            else:
                clean_value = value
            new_row[clean_key] = clean_value
        normalised_rows.append(new_row)
    return normalised_rows


def test_basic():
    rows = [{" Name ": " Ada ", "AGE": 36}]
    assert normalise_rows(rows) == [{"name": "Ada", "age": 36}]

"""test_input_unchanged, proving the original rows is exactly as it was afterwards.
 (Hint: what do you compare it against, and when do you need to make that thing?)"""

import copy

def test_input_unchanged():
    rows = [{" Name ": " Ada ", "AGE": 36}]
    original_rows_copy = copy.deepcopy(rows)
    normalise_rows(rows)
    assert rows == original_rows_copy

"""test_returns_new_dicts, 
proving the output dicts aren't the input dicts. (Which operator checks that?)"""

def test_returns_new_dicts():
    rows = [{" Name ": " Ada ", "AGE": 36}]
    output_rows = normalise_rows(rows)
    for row in rows:
        for output_row in output_rows:
            assert row is not output_row


test_basic()
test_input_unchanged()
test_returns_new_dicts()
print("All tests passed")



    

        