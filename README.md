# 🎭 Playwright Pytest POM Framework

A scalable **Playwright + Pytest automation framework** using the **Page Object Model (POM)** design pattern.  
This framework is designed for **real-world UI automation** with login, register, product (add-to-cart), and logout flows.

---

## 🚀 Tech Stack

- Python 3.10+
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest Fixtures
- Pytest Hooks (Screenshots on Failure)

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

    python -m venv venv
    source venv/bin/activate # Linux / Mac
    venv\Scripts\activate # Windows

---

### 2️⃣ Install Dependencies

    pip install -r requirements.txt

---

### 3️⃣ Install Playwright Browsers

    playwright install

---

## ▶️ How to Run Tests

### 🔹 Run all tests

    pytest

### 🔹 Run a specific test file

    pytest -v tests/test_product_page.py

### 🔹 Run tests in verbose mode

    pytest -v

---

## 🔐 Login Handling Strategy

- Login is handled via a **fixture (`logged_in_page`)**
- Product & logout tests **do not depend on login test**
- Each test is **independent and reusable**

✅ Industry best practice  
❌ No test dependency

---

## 📸 Screenshot on Failure

- Screenshots are **automatically captured**
- Stored inside the `screenshots/` folder
- Triggered via `pytest_runtest_makereport` hook

---

## 🧪 Pytest Markers

Markers are defined in `pytest.ini`:

    [pytest]
    markers =
    order: test execution order
    
    Example usage:
    
    @pytest.mark.order(3)
    def test_add_to_cart():


---

## 🧠 Design Principles Followed

- Page Object Model (POM)
- Single Responsibility Principle
- Reusable fixtures
- No hard dependency between tests
- Clean and readable locators
- Strict-mode safe Playwright locators

---

## 🌐 Test Website Used

Automation Exercise  
https://automationexercise.com

---

## 👤 Author

**Navneet Harsh**  
Playwright | Pytest | Automation
