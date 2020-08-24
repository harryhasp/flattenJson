# flattenJson - Unit tests

### General

- use of Python3
- use of pytest
- all unit tests under unit_tests folder


### Setup

For pytest and pytest coverage:
```python
pip install pytest
pip install pytest-cov
```


### Execution

After making the above setup, execute one of the following:

- For simple execution
```python
pytest flattenJson/
```

- For provide code coverage report
```python
pytest flattenJson/ --cov-report term-missing --cov flattenJson/
```
