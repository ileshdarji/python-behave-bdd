# python-behave-bdd

This is an Automation Testing framework built on Python libraries using [Behave](https://behave.readthedocs.io/en/latest/) (BDD - Behavior Driven Development for Python) for testing UI and API features
## Installation

[![Python 3.7](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-399/)

### It is highly recommended installing and activating Python Virtual environment before installing the requirements.
visit here for more info on [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

After activating Virtual environment, install dependencies by running this command:
```
pip3 install -r autotests/requirements.txt
```
## Running the tests

To run full regression test including API and UI tests:

```bash
behave --tags="regression"
```

To run UI regression test:

```bash
behave --tags="regression_ui"
```

List of available tags:

* @regression (for all file type backfeed scenarios )
* @regression_ui
* @regression_api
* @post
* @login
* @navigate
* @login_error_handling