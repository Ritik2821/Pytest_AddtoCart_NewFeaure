# Add to Cart Feature Test with Pytest

This test verifies the functionality of the "Add to Cart" feature on an e-commerce website.

## Features Tested
1. **Login with valid and invalid configurations**.
2. **Add an item to the cart**.
3. **Verify if the item is added to the cart**.
4. **Proceed to checkout**.
5. **Verify the confirmation text on the screen after checkout**.

## Prerequisites
- Python 3.x should be installed on your machine.
- **Selenium** WebDriver and **pytest** should be installed.
- A working internet connection to access the test URL.

## Steps to Execute the Test


### 1. Install Required Dependencies
You will need to install the necessary libraries to run the test.

- First, create a `requirements.txt` file (or use the one below) with all required dependencies:


To install these dependencies, run the following command:

```bash
pip install -r requirements.txt
```
### 2. Run the Test
- Once the dependencies are installed, you can run the test using pytest.

- Run the following command in your terminal or command prompt:
```bash
pytest test_demo_site.py --html=HtmlReport.html
```
#### Explanation: This command will:

- Run the test in the test_demo_site.py file.
- Generate an HTML report with the name HtmlReport.html in the current directory.

### 3. Test Steps
Below are the steps that the test will perform:

- Step 1: Go to the URL of the e-commerce website (e.g., https://www.saucedemo.com/).
- Step 2: Log in with valid credentials and attempt to add an item to the cart.
- Test invalid login configurations to verify error handling.
- Step 3: Select an item and click on it to add it to the cart.
- Verify whether the item appears in the cart.
- Step 4: Click on the cart icon and proceed to checkout.
- Step 5: Check for a confirmation message that the item has been successfully added and proceed to checkout.

### 4. Viewing the HTML Report
- After the test completes, an HTML report (HtmlReport.html) will be generated in your current directory.
- Open the report in your browser to view the detailed test results.