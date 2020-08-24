#!/usr/bin/python3
import sys
import os
import json


def json_flatten(data):
    """
    Flattens the input json object

    :param data: dict -> Represents the json object
    :return: dict -> The flatten json
    """
    result = {}

    def flatten_helper(key, prefix=''):
        """
        Recursively flatten each key with its value

        :param key: str or dict -> The key where we're about to flatten / can be str or dict
        :param prefix: str -> The prefix which will be used for the new key of the flatten json
        :return: No return. Result is being stored at the result variable of the parent function
        """
        if type(key) is dict:
            for value in key:
                new_prefix = prefix + value + '.'
                flatten_helper(key[value], new_prefix)
        else:
            result[prefix[:-1]] = key

    flatten_helper(data)

    return result


def print_result(original, flattened):
    """
    Prints Original and Flattened JSON
    :param original: dict -> input JSON
    :param flattened: dict -> result JSON
    :return: No return. Just prints in stdout
    """
    print("Original JSON:")
    print(json.dumps(original, indent=4))
    print("-------------------------")
    print("Flattened JSON:")
    print(json.dumps(flattened, indent=4))


def streaming(stream):
    """
    Transforms a stream of data to a JSON object and kicks flatten process

    :param stream: Stream of data
    :return: No return.
    """
    data = json.load(stream)

    ret = json_flatten(data)

    print_result(data, ret)


def main():
    """
    Reads from stdin or takes as input a file and kicks off the process

    :return: No return
    """
    if len(sys.argv) == 2:
        # In case the input is given as an argument
        file = sys.argv[1]
        if os.path.isfile(file):
            f = open(file)
            streaming(f)
        else:
            print("--> File doesn't exist")
    else:
        # In case the input is given from stdin
        streaming(sys.stdin)


if __name__ == "__main__":
    main()
