"""Write merge_config(base, overrides). 
It returns a new dict containing everything in base, 
with any keys in overrides replacing base's values. 
Requirements:
- neither base nor overrides is changed;
- if base has a list value, such as {"features": ["age"]}, 
  appending to that list in the result must not affect base. """

import copy

def merge_config(base, overrides):
    new_base = copy.deepcopy(base)
    new_overrides = copy.deepcopy(overrides)
    for key, value in new_overrides.items():
        new_base[key] = value
    return new_base

def test_base_overriden():
    b = {"lr": 0.01, "epochs": 10, "tags": ["a"]}
    o = {"lr": 0.1, "seed": 42}
    result = merge_config(b,o)
    assert result == {"lr": 0.1, "epochs": 10, "tags": ["a"], "seed": 42}

def test_base_unchanged():
    b = {"lr": 0.01, "epochs": 10, "tags": ["a"]}
    o = {"lr": 0.1, "seed": 42}
    merge_config(b,o)
    assert b == {"lr": 0.01, "epochs": 10, "tags": ["a"]}

def test_overrides_unchanged():
    b = {"lr": 0.01, "epochs": 10, "tags": ["a"]}
    o = {"lr": 0.1, "seed": 42}
    merge_config(b,o)
    assert o == {"lr": 0.1, "seed": 42}

def test_list_independence():
    b = {"lr": 0.01, "epochs": 10, "tags": ["a"]}
    o = {"lr": 0.1, "seed": 42}
    result = merge_config(b,o)
    result["tags"].append("b") 
    assert b["tags"] == ["a"]



test_base_overriden()
test_base_unchanged()
test_overrides_unchanged()
test_list_independence()
print('all tests passed')




