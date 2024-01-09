#!/usr/bin/env python3
"""Unittests_and_integration_tests module"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Access nested map with key path
        Parameterize a unit test"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Mock HTTP calls
        Get JSON from remote URL.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        results = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(results, test_payload)


class TestMemoize(unittest.TestCase):
    """memoized function "remembers" the results
    corresponding to some set of specific inputs."""

    def test_memoize(self):
        """test the cache the results of expensive function calls
        to avoid redundant computations. """

        class TestClass:
            """test class to text memoise"""
            def a_method(self):
                """a method that returns when on ly called once"""
                return 42

            @memoize
            def a_property(self):
                """a method that returns same results when called twice"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            obj = TestClass()

            results1 = obj.a_property
            results2 = obj.a_property

            mock.assert_called_once()

            self.assertEqual(results1, 42)
            self.assertEqual(results2, 42)


if __name__ == "__main__":
    unittest.main()
