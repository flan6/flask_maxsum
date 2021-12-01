"""api.py

Accepts requests HTTP POST with an integer list and returns
the biggest sum of a non-empty substring and its indexes

To start the python virtual enviroment run in terminal
    $ source venv/bin/activate

To start this api just run in terminal
    $ python api.py
and make requests POST to http://127.0.0.1:8080/maxsum/
as the example in test.http
note: press 'ctrl+c' to stop running

Requirements are listed in requeriments.txt
To install requirements just run in terminal
    $ pip install -r requeriments.txt
"""


from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Maxsum(Resource):
    """A class to manage /maxsum/ route requests.

    Methods:
    post() -- handles HTTP POST requests to /maxsum/
    maximum_subarray(ls: list) --Given a list of integers,
        compute the best sum of a non-empty sublist.
        params:
            ls -- list to be computed
    """

    def post(self):
        """Handles HTTP POST requests to endpoint /maxsum/"""

        json_data = request.get_json(force=True)
        ls_of_integers = json_data['list']
        return self.maximum_subarray(ls_of_integers)

    def maximum_subarray(self, ls_of_integers: list):
        """Return the max sum of a substring and it indexes"""

        # variables used to compare the sum of possible sublists
        best_sum = cur_sum = 0
        # variables used to store starting and ending index of sublist
        cur_sum_index = start_index = best_sum_index = 0
        # list to build all indexes of elements of the sublist
        pos = []

        # if the list only contains negative numbers
        # get the biggest number and return its index
        if max(ls_of_integers) < 0:
            best_sum = max(ls_of_integers)
            pos_i = ls_of_integers.index(best_sum) + 1
            pos.append(pos_i)
        else:

            # otherwise find the best sum of a sublist
            # and the indexes
            for ind, i in enumerate(ls_of_integers):
                if cur_sum+i > 0:
                    cur_sum += i
                else:
                    cur_sum, cur_sum_index = 0, ind+1

                if cur_sum > best_sum:
                    start_index = cur_sum_index
                    best_sum_index = ind+1
                    best_sum = cur_sum

            # build a list of indexes starting from 1 not 0
            # NOTE: these indexes are based from 1 TO N
            pos = list(range(start_index+1, best_sum_index+1))

        # dictionary used in the HTTP response
        response = {
            "sum": best_sum,
            "positions": pos
            }
        return response


# creating the route to endpoint /maxsum/
api.add_resource(Maxsum, "/maxsum/")

if __name__ == "__main__":
    # change port from default 5000 to 8080 as required
    app.run(port=8080, debug=True)
