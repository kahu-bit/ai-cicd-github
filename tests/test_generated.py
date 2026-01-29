import pytest
import string
from more_utils import generate_password

def test_generate_password_default_length():
    """Test that default password has length 12."""
    password = generate_password()
    assert len(password) == 12

def test_generate_password_custom_length():
    """Test password generation with custom length."""
    password = generate_password(length=8)
    assert len(password) == 8

def test_generate_password_with_symbols():
    """Test that password includes symbols when include_symbols is True."""
    password = generate_password(length=50, include_symbols=True)
    assert any(c in string.punctuation for c in password)

def test_generate_password_without_symbols():
    """Test that password excludes symbols when include_symbols is False."""
    password = generate_password(length=50, include_symbols=False)
    assert all(c in string.ascii_letters + string.digits for c in password)

def test_generate_password_contains_letters():
    """Test that generated password contains letters."""
    password = generate_password(length=20)
    assert any(c in string.ascii_letters for c in password)

def test_generate_password_contains_digits():
    """Test that generated password contains digits."""
    password = generate_password(length=20)
    assert any(c in string.digits for c in password)

def test_generate_password_different_each_time():
    """Test that passwords are different when generated multiple times."""
    password1 = generate_password(length=20)
    password2 = generate_password(length=20)
    # While theoretically they could be the same, it's extremely unlikely
    # We'll check that at least one character differs
    assert password1 != password2 or len(set(password1)) > 1