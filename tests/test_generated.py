import pytest

# Tests for is_palindrome from more_utils.py
```python
import pytest

def test_is_palindrome_simple_true():
    """Test with a simple lowercase palindrome."""
    assert is_palindrome("madam") is True

def test_is_palindrome_with_spaces_and_mixed_case_true():
    """Test with a palindrome that includes spaces and mixed casing."""
    assert is_palindrome("Race car") is True
    assert is_palindrome("Was it a car or a cat I saw") is True

def test_is_palindrome_simple_false():
    """Test with a simple non-palindrome string."""
    assert is_palindrome("hello") is False
    assert is_palindrome("python") is False

def test_is_palindrome_empty_string_true():
    """Test with an empty string, which is considered a palindrome."""
    assert is_palindrome("") is True
    assert is_palindrome("   ") is True # String with only spaces should also be true

def test_is_palindrome_single_character_true():
    """Test with a single character string."""
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True # Should be true after lowercasing

def test_is_palindrome_none_input_raises_attribute_error():
    """Test that passing None raises an AttributeError."""
    with pytest.raises(AttributeError):
        is_palindrome(None)
```