"""tests.py

Make test POST requests and assert the responses of the api.py
Currently there are 5 tests in a single method.

To start the python virtual enviroment run in terminal
    $ source venv/bin/activate

To start this script just run in terminal
    $ python tests.py
note: api must be running and this script called in a second terminal window

Requirements are listed in requeriments.txt
To install requirements just run in terminal
    $ pip install -r requeriments.txt
"""

import unittest
import json
import requests


class MaxsumTestCase(unittest.TestCase):
    """Test cases for unit testing of the POST request to
    endpoint http://127.0.0.1:8080/maxsum/

    variables:
        BASE -- base url for the request
        lists_to_send_to_maxsum -- arguments for POST request
        expected_responses_from_maxsum -- expected responses
            key: index of integer list counterpart in lists_to_send_to_maxsum
            values: dictionary expected to be recieved from api.py

    Methods:
        test_maxsum_endpoint -- Make POST request and compare its result to
        expected values"""

    BASE = "http://127.0.0.1:8080/"
    lists_to_send_to_maxsum = [
        [-2, 3, 5, -1, 4, -5],
        [-1000, -1, -1, -1, -1000],
        [1, 2, 3, 4, -1000],
        [-1000, 1, 2, 3, 4],
        [-1000, 2, -1, 2, -1000],
    ]
    expected_responses_from_maxsum = {
        0: {"sum": 11, "positions": [2, 3, 4, 5]},
        1: {"sum": -1, "positions": [2]},
        2: {"sum": 10, "positions": [1, 2, 3, 4]},
        3: {"sum": 10, "positions": [2, 3, 4, 5]},
        4: {"sum": 3, "positions": [2, 3, 4]},
    }

    def test_maxsum_endpoint(self):
        """For each list makes a request and compare its result"""

        for index, _list in enumerate(self.lists_to_send_to_maxsum):

            # as using subtest if any fail during the loop
            # print its traceback and continue the loop
            with self.subTest(index=index, _list=_list):
                data = {"list": _list}
                response = requests.post(
                                        self.BASE + "maxsum/",
                                        data=json.dumps(data))
                res = response.json()
                self.assertEqual(res,
                                 self.expected_responses_from_maxsum[index])


# calls all tests when script is executed
if __name__ == "__main__":
    unittest.main()
