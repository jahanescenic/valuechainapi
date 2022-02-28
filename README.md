API Test for Value chain api automation testing
================================================

This repository contains automated API tests of "adequateshop.com"

*Pre-requisites*: `python3`, `python3-pip` `python3-venv`, `git` should be installed in your local machine.


Run API tests
================

Clone the repository with `git clone https://github.com/jahanescenic/valuechainapi.git`

From the repository root, Run following commands to create a python virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Finally, you're ready to run some tests.  

```
pytest Tests --html=report.html --self-contained-html -s
```

The following files will be created automatically to facilitate test run -

- `TestData` directory to store user related test data.
- `report.html` html test report

Future Improvements
================

- These API tests can be run on a docker container to avoid environment dependency (python3).

