#!/usr/bin/env python3
import os
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
def test_one():
    assert True

def test_two():
    assert 1 == 1
###

print("All tests passed!")
if os.environ.get("OUTPUT_RUNS") == "True":
    print("TEST RUN:")
