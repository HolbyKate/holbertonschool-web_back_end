#!/usr/bin/env python3

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """Function to access a value in a nested dictionary along a given path."""
    current = nested_map
    for key in path:
        current = current[key]
    return current


class TestAccessNestedMap(unittest.TestCase):
    """Work with map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        output = acces_nested_map(map, path)
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
