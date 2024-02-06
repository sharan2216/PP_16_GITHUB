import os
import pytest

@pytest.mark.login
def test_regression():
    print("test_regression")


@pytest.mark.login
def test_sanity():
    print("test_sanity")


@pytest.mark.login
def test_functions():
    print("test_functions")

@pytest.mark.login
@pytest.mark.settings
def test_functions1():
    print("test_functions1")


@pytest.mark.settings
def test_api():
    print("test_api")


 # in pytest.ini file add :-------------
 # # ignore : ignore all test cases
 # in Terminal :----------
 # >pytest Tests/test_pyTestOptions.py -m "not ignore" -sv
@pytest.mark.ignore
def test_api():
    print("test_api")


@pytest.mark.skip(reason="skipping as test execution takes more time")
def test_api1():
    print("test_api")


@pytest.mark.skipif(os.name == 'nt',reason="skipping if os is nt")
def test_api11():
    print("test_api11 |" +os.name)



