#!/usr/bin/env python3
''' Test utils '''
import unittest
import unittest.mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    ''' Test access for nested map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' Test access for nested map function'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected, msg):
        ''' Test access for nested map function'''
        with self.assertRaises(expected, msg=msg):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' Test get json '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected):
        ''' Test get json function'''
        with unittest.mock.patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)


class TestMemoize(unittest.TestCase):
    ''' Test memoize '''

    class TestClass:
        ''' Test class '''

        def a_method(self):
            ''' Test method '''
            return 42

        @memoize
        def a_property(self):
            ''' Test property '''
            return self.a_method()

    def test_memoize(self):
        ''' Test memoize function'''
        test_class = TestMemoize.TestClass()
        with unittest.mock.patch.object(
                TestMemoize.TestClass, 'a_method', return_value=42
        ) as mock_method:
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
