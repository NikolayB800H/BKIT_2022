import json
import pytest
import re
import sys
from process_data_to_test.process_data import f1, f2, f3, f4

f1_to_f2 = ["преподаватель языка C", "программист на языке A", "Программист на языке B", "программист на языке C"]
f2_to_f3 = ["программист на языке A", "Программист на языке B", "программист на языке C"]
f3_to_f4 = ["программист на языке A с опытом Python", "Программист на языке B с опытом Python", "программист на языке C с опытом Python"]
path = 'process_data_to_test/data.json'
with open(path) as f:
    data = json.load(f)

def test_f1():
    assert f1(data) == f1_to_f2

def test_f2():
    assert f2(f1_to_f2) == f2_to_f3

def test_f3():
    assert f3(f2_to_f3) == f3_to_f4

def test_f4():
    ans = f4(f3_to_f4)
    assert len(ans) == len(f3_to_f4)
    for i in range(len(f3_to_f4)):
        assert ans[i][0] == f3_to_f4[i]
        assert re.match(r"зарплата\s+\d+\s+руб\.", ans[i][1])
        assert 100000 <= int(re.search(r"\d+", ans[i][1]).group()) <= 200000
