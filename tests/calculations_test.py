# System Modules
import sys
import os
import pytest

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55

def test_area_of_circle_negative_radius():
    """Test con un raggio negativo."""
    with pytest.raises(ValueError):
        area_of_circle(-1)

def test_area_of_circle_non_numeric():
    """Test con un input non numerico."""
    with pytest.raises(TypeError):
        area_of_circle("abc")

def test_get_nth_fibonacci_negative():
    """Test con n negativo."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)

def test_get_nth_fibonacci_non_integer():
    """Test con n non intero."""
    with pytest.raises(TypeError):
        get_nth_fibonacci(3.5)
# ...existing code...
