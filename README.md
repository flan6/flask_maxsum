# REST API TO CALCULATE MAX SUBSTRING

This is an example REST api built in Flask-RESTful to receive a POST request with a json containing an integer array and calculate a subarray of the biggest sum possible and return its indexes as a new json.

## EXAMPLES

The json on the POST request should follow the format

```json:
{
    "list": [-1000, -1, -1, -1, -1000]
}
```

then the return would be

```json:
{
    "sum": -1,
    "positions": [2]
}
```

**note:** the indexes are starting at 1 **not** 0

## HOW TO RUN

To start the python virtual enviroment run in terminal:

 > `$ source venv/bin/activate`

To start this api just run in terminal:

> `$ python api.py`

## REQUERIMENTS

Requeriments are listed in `requeriments.txt`

simply run inside the virtual envirement:

>`pip install -r requeriments.txt`

## TESTS

A test file is included as `tests.py` it has a list of lists to be sent and a dictionary of expected results.

To run the tests the api must be running then call in another window:
> `$ python tests.py`
