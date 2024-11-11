"""Test fastsocket."""

import fastsocket


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(fastsocket.__name__, str)
