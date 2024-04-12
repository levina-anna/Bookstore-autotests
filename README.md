# Bookstore-autotests

This project contains automated tests for the Bookstore application. It's designed to validate the functionality of the Bookstore's web interface.

## Features
- Emulates user actions within the browser.
- Tests the functionality of category filters in the web application.

## Running the Tests
```shell
pip install -r requirements.txt
pytest -s tests/test_cost_table.py
```

## Running on a Server
```shell
docker build -t bookstore-autotests .
docker run --rm bookstore-autotests
```

## Configuration
The test scripts are configured to run against the Bookstore application deployed at http://127.0.0.1:8000. To change the test environment, update the DOMAIN variable in the .env file (note that .env is included in .gitignore to prevent sensitive information from being committed to version control).

## Technologies Used
- Python 3
- Selenium WebDriver
- Pytest
- Docker