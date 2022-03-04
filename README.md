![Pytest](https://warehouse-camo.ingress.cmh1.psfhosted.org/1599e7e4caeaac6ca1a8d4ace3cefa8a0d160925/68747470733a2f2f6769746875622e636f6d2f7079746573742d6465762f7079746573742f7261772f6d61696e2f646f632f656e2f696d672f7079746573745f6c6f676f5f6375727665732e737667)
---

# pytest-project
pytest project to learn pytest for automation testing

## Write test
For writing testcases use following conventions
- Name testcase method as `test_abc()`
- Starting the name of testcase method with `test` is necessary

## Writing testcases in object-oriented way
For writing testcases in object-oriented way
- Name the class as `TestXYZ`
- Starting the name of class with `Test` is mandatory

## Run test
Run tests from terminal by executing `pytest filename.py`

## Run multiple tests
### Using sub-string
Run multiple tests at once using sub-strings.
- Open the terminal
- In terminal run `py.test -k method_name_sub_string -v` i.e., `py.test -k format_data_for -v` for methods in test.py

### Using markers
Run multiple tests by grouping them using markers
- Mark a testcase with marker by using a decorator `@pytest.mark.marker_name` over the test case
- For telling program that a testcase will fail mark it with xfail as `@pytest.mark.xfail`
- Similarly, for skipping a testcase mark it with `@pytest.mark.skip`
- But for custom markers you have to register them first by writing their names in pytest.ini like
  ```
  [pytest]
  markers =
      run_it: only run marked test cases
      serial
  ```
- Open the terminal
- In terminal run `py.test -k marker_name` to run all the test cases decorated with the marker
