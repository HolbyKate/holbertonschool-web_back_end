#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Work with map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        output = access_nested_map(map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 1),
        ({"a": 1}, ("a", "b"), 1),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_output):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), expected_output)


class TestGetJson(unittest.TestCase):
    """Class that inherit from unittest.TestCase"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test that utils.get_json returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        """call the function with test input"""
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase): 
    """Class to test memoization decorator"""
    def test_memoize(self):
        """Test_memoize method"""
        
        
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

if __name__ == "__main__":
    unittest.main()
