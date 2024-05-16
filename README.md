# API TESTING WITH PYTHON

The API tetsing with python project was used to follow the tutorial on API Testing in Python on Test Automation University. This course exposes testers to using Python, Pytest for automating API test.

## Table of Contents
- [SetUp](#Setup)
- [IMPORTANT NOTE](#NOTE)
- [Purpose](#Purpose)


### NOTE

- #### Create Account with Test Automation University
  - To follow the tutorial, create an account on TestAutomation University [here](https://testautomationu.applitools.com/login.html)
  - Go to the Learning Path page [here](https://testautomationu.applitools.com/learningpaths.html?id=python-testing-path) and select Python path follow the courses in the order they are arranged. If you are familiar with python programming, you can skip the python tutorial and start with Introduction to pytest
- #### Important information to use this code
  - You need to have the Applications under Test for this project. There are two AUT used: people-api and covid_tracker
  - You can fork or clone the people-api repo [here](https://github.com/victoriaajuwon/python-people-api)
  - You can fork or clone the covid-tracker repo [here](https://github.com/victoriaajuwon/python-covid-tracker)
- Now fork/clone the aoi-testing-in-python github repo [here](https://github.com/victoriaajuwon/tau-api-testing-in-python)!

### Purpose
The purpose of this project is to learn and understand how to use python to automate API testing.

### Setup

1. Clone the repository.
    ```sh
    cd backend
    ```
2.On another terminal, navigate to the root directory in your terminal
    ```sh
    cd tau-api-testing-in-python
    ```
3. You need to ensure you have virtual environment set up for the project
4. You can either use pipenv or pip, to use pipenv is installed. To install pipenv follow this [link](https://pipenv.pypa.io/en/latest/installation.html). To install pip, follow this [link](https://pip.pypa.io/en/stable/installation/)
4. Install dependencies using pipenv
    ```sh
    # Activate virtualenv
    pipenv shell
    # install
    pipenv install
    ```
5. Install dependencies using pip
    ```sh
    # Create virtualenv, inside the root directory, use the code below
    python -m venv venv
    # Activate virtualenv for windows
    .\venv\Scripts\activate
    # Activate virtualenv for Linux/MacOS
    source venv/bin/activate
    ```
