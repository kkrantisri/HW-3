import pytest
import answer

def test_calculate():
    c, q, type_q = answer.calculate()
    assert c == 7
    assert q == (7 - 1) / 5.0
    assert type_q == type((7 - 1) / 5.0)

def test_string_formating():
    string_pi, comma_string, exp_string, center_string, left_string = answer.string_formating()
    assert string_pi == '{0:.6f}'.format(3.141592653589793)
    assert comma_string == "{:,}".format(100000000)
    assert exp_string == "{:.2e}".format(100000000)
    assert center_string == "{:^10d}".format(13)
    assert left_string == "{:0>2d}".format(13)

def test_build_in():
    math_pi, math_e, sin_pi, square_root_2, abs_2 = answer.build_in()
    assert math_pi == math.pi
    assert math_e == math.e
    assert sin_pi == math.sin(math.pi)
    assert square_root_2 == math.sqrt(2)
    assert abs_2 == abs(-2)

def test_set_op():
    S1, union_s, sum_s = answer.set_op()
    assert S1 == {0, 1, 2, 3, 4}
    assert union_s == {0, 1, 2, 3, 4, 5, 6}
    assert sum_s == sum({0, 1, 2, 3, 4, 5, 6})
