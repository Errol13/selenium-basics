# Selenium Basics

This project is a basic introduction to web automation using Selenium. 

## Demonstrated Knowledge
- Site under testing is `Swag Labs` [https://www.saucedemo.com/]
- Open a browser using Selenium WebDriver
- Locate and interact with web elements (e.g., input fields, buttons)
- Automate a login workflow
- Use Python `assert` statements for validation
- Structure tests using `pytest` for test automation

## Run this project 

### Clone the repository
```bash
git clone https://github.com/Errol13/selenium-basics.git
cd selenium-basics
```

### Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Run the test
```bash
pytest test_swaglabs.py # less detailed
pytest test_swaglabs.py -v # more detailed
```