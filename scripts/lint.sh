#!/usr/bin/env bash

EXIT_CODE=0

pylint server || EXIT_CODE=1

pycodestyle server || EXIT_CODE=1

python -m flake8 server || EXIT_CODE=1

exit ${EXIT_CODE}