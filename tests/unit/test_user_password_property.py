# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
import pytest

from app.models.user import User


def test_password_property_hash_and_read_behavior():
    user = User(
        first_name="A",
        last_name="B",
        email="a@example.com",
        username="user1",
        password_hash="initial"
    )

    # writing a pre-hashed value (starts with $) should store as-is
    pre_hashed = "$sha$fakehash"
    user.password = pre_hashed
    assert user.password_hash == pre_hashed

    # writing None should set password_hash to None
    user.password = None
    assert user.password_hash is None

    # read access should raise
    with pytest.raises(AttributeError):
        _ = user.password
