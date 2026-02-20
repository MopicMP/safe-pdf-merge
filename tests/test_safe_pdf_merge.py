"""Tests for safe-pdf-merge."""

import pytest
from safe_pdf_merge import merge


class TestMerge:
    """Test suite for merge."""

    def test_basic(self):
        """Test basic usage."""
        result = merge("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            merge("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = merge(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
