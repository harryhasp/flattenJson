import pytest


def test_json_flatten_1():
    from flattenJson.main import json_flatten
    import json

    key = json.loads(
        """{
                "a": 1,
                "b": true,
                "c": {
                    "d": 3,
                    "e": "test"
                }
            }"""
        )

    result = json_flatten(key)

    expected_result = '{"a": 1, "b": true, "c.d": 3, "c.e": "test"}'

    assert expected_result == json.dumps(result, sort_keys=True)


def test_json_flatten_2():
    from flattenJson.main import json_flatten
    import json

    key = json.loads(
        """{
                "a": 1
            }"""
        )

    result = json_flatten(key)

    expected_result = '{"a": 1}'

    assert expected_result == json.dumps(result, sort_keys=True)


def test_json_flatten_3():
    from flattenJson.main import json_flatten
    import json

    key = json.loads(
        """{}"""
        )

    result = json_flatten(key)

    expected_result = '{}'

    assert expected_result == json.dumps(result, sort_keys=True)


def test_json_flatten_4():
    from flattenJson.main import json_flatten
    import json

    key = json.loads(
        """{
                "a": 1,
                "b": true,
                "c": {
                    "d": 3,
                    "e": "test"
                },
                "e": "hello"
            }"""
        )

    result = json_flatten(key)

    expected_result = '{"a": 1, "b": true, "c.d": 3, "c.e": "test", "e": "hello"}'

    assert expected_result == json.dumps(result, sort_keys=True)
