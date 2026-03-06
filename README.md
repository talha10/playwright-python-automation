# Playwright Python Automation Framework

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-1.40.0-green.svg)
![pytest](https://img.shields.io/badge/pytest-7.4.3-yellow.svg)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF.svg)

## 📌 Project Overview
This repository contains an industry-standard, fully scalable automated testing framework built from scratch using **Python**, **Playwright**, and **pytest**. It implements the **Page Object Model (POM)** design pattern for optimal maintainability and readability.

The target application under test is [Automation Exercise](https://automationexercise.com), a comprehensive e-commerce sandbox designed specifically for test automation practice.

## 🏗️ Folder Structure
```
playwright-python-automation/
├── tests/                 # Business logic tests by functionality
├── pages/                 # Page Object Model (POM) classes
├── utils/                 # Configuration and helper functions
├── .github/workflows/     # CI/CD pipelines
├── conftest.py            # Pytest fixtures and browser setup
├── pytest.ini             # Pytest configuration and markers
└── requirements.txt       # Project dependencies
```

## 🚀 Tech Stack
- **Language**: Python 3.11+
- **Browser Automation**: Playwright for Python
- **Test Runner**: pytest
- **Reporting**: pytest-html
- **Configuration**: python-dotenv
- **CI/CD**: GitHub Actions

## ⚙️ Local Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/talhakhattak/playwright-python-automation.git
   cd playwright-python-automation
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**:
   ```bash
   playwright install chromium
   ```

## 🧪 Running Locally

By default, tests run in **headless** mode pointing to the production URL.

- **Run all tests**: 
  ```bash
  pytest
  ```
- **Run a specific test file**:
  ```bash
  pytest tests/test_login.py
  ```
- **Run tests in headed mode** (opens browser):
  ```bash
  set HEADLESS=false
  pytest
  ```
- **Generate HTML Report**:
  ```bash
  pytest --html=reports/report.html
  ```

## 🤖 Continuous Integration
This repository is configured with **GitHub Actions**. On every push to `main` or upon pull request creation, the CI pipeline automatically:
1. Sets up Python 3.11
2. Installs requirements and Playwright binaries
3. Executes the full test suite in headless mode
4. Uploads the generated standard `pytest-html` report as a build artifact.

*See `.github/workflows/playwright-tests.yml` for exact configurations.*

---

## 👤 Author
**Talha Khan** | Senior Software Quality Assurance Engineer  
[LinkedIn](https://www.linkedin.com/in/talha-khan-khattak/) | *Engineered for highly reliable, parallelized E2E test automation.*
