# Advent of Code Visualizations

Few simple visualizations with Python and Blessed.

Developed in Lubuntu with Python 3.10.

Uses [virtual environment](https://docs.python.org/3.10/tutorial/venv.html).

## Setup

Required in Lubuntu:
```
sudo apt install python3.10-venv
```

Create virtual environment:
```
$ python3 -m venv .venv
```

Activate virtual environment:
```
$ source .venv/bin/activate
```

Install required packages:
```
python -m pip install blessed numpy
```

TODO freeze requirements.

## Visualizations

File naming pattern:

* `<YEAR>-<DAY>-<PART>-0.py` is my Python solution without visualizations
* `<YEAR>-<DAY>-<PART>-1.py` is first visualisation

Run:
```
python <PROGRAM>.py <INPUT>
```
