import pytest
from unittest.mock import patch
from app.operations import Addition, Subtraction, Multiplication, Division
from app.calculator import Calculator


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
])
def test_addition(a, b, expected):
    assert Addition.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (1.5, 0.5, 1.0),
])
def test_subtraction(a, b, expected):
    assert Subtraction.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (1.5, 2, 3.0),
])
def test_multiplication(a, b, expected):
    assert Multiplication.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (-6, 2, -3.0),
    (1, 4, 0.25),
])
def test_division(a, b, expected):
    assert Division.execute(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Division.execute(10, 0)


def test_get_number_valid():
    with patch("builtins.input", return_value="42"):
        assert Calculator().get_number("Enter: ") == 42.0


def test_get_number_invalid_then_valid():
    with patch("builtins.input", side_effect=["abc", "5"]):
        with patch("builtins.print"):
            assert Calculator().get_number("Enter: ") == 5.0


def test_get_operation_valid():
    with patch("builtins.input", return_value="add"):
        assert Calculator().get_operation() == "add"


def test_get_operation_quit():
    with patch("builtins.input", return_value="quit"):
        assert Calculator().get_operation() == "quit"


def test_get_operation_invalid_then_valid():
    with patch("builtins.input", side_effect=["blah", "multiply"]):
        with patch("builtins.print"):
            assert Calculator().get_operation() == "multiply"


def test_run_quit_immediately():
    with patch("builtins.input", side_effect=["quit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_one_operation_then_quit():
    with patch("builtins.input", side_effect=["add", "3", "4", "quit"]):
        with patch("builtins.print"):
            Calculator().run()


def test_run_divide_by_zero_then_quit():
    with patch("builtins.input", side_effect=["divide", "5", "0", "quit"]):
        with patch("builtins.print"):
            Calculator().run()