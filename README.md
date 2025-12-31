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

## 📂 Project Structure

playwright-pom-framework/
│
├── pages/
│ ├── login_page.py
│ ├── register_user_page.py
│ ├── product_page.py
│
├── tests/
│ ├── test_login.py
│ ├── test_register_user.py
│ ├── test_product_page.py
│ ├── test_logout.py
│
├── utils/
│ └── config.py
│
├── screenshots/ # Auto-generated on test failure
│
├── conftest.py # Fixtures & hooks
├── pytest.ini # Pytest configuration
├── requirements.txt
├── README.md


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

## ⚠️ Important Notes

- Avoid test order dependency in real projects
- Use fixtures for setup (login, state)
- Prefer stable locators (`data-*`, scoped locators)
- Avoid `time.sleep()` → Playwright auto-waits

---

## 🏆 Interview Ready Highlights

- POM Architecture
- Fixture-based login
- Screenshot on failure
- Strict mode locator handling
- Clean test isolation
- CI/CD ready structure

---

## 📌 Future Enhancements

- Storage-state based login
- Parallel execution (`pytest-xdist`)
- Allure reporting
- Environment switching (dev / staging / prod)
- CI pipeline integration (GitHub Actions)

---

## 👤 Author

**Navneet Harsh**  
Playwright | Pytest | Automation
