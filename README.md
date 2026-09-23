# Selenium Automation Project

A sample Selenium automation framework built with:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model

## Prerequisites

Install:

- Python 3.10 or newer
- Google Chrome

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the tests

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_selenium_home_page.py::test_selenium_home_page_title
```

Run tests with browser output:

```bash
pytest -s
```

## How it works

- `pages/selenium_home_page.py` contains page interactions.
- `tests/test_selenium_home_page.py` contains test cases.
- Selenium Manager automatically finds and manages the ChromeDriver.
- The browser is closed automatically after every test.