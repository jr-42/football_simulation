#!/bin/bash
echo -----
echo Running FM Test Suite
echo -----
echo Install
pip install -U -e .[develop]
echo -----
echo Preliminary tests
echo Check Compile
python -m compileall src/football/
echo -----
echo Check type stuff
mypy src/football/
echo -----
echo Pylint
pylint src/football
echo -----
echo -----
echo Run tests
pytest --cov=football --cov-report html tests/
echo -----
echo ALL TESTS COMPLETED

