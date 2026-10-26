# Project Overview
The primary goal of this project is to build a reliable and maintainable automation testing suite for Sauce Demo, a standard e-commerce practice platform.<br>
This framework mimics real-world business scenarios, ensuring that critical user journeys function seamlessly. It incorporates custom fixtures, centralized test configurations, and advanced UI synchronization techniques (auto-waiting) to achieve high execution stability and eliminate flaky test behaviors common in web automation.

# Tech Stack
The framework leverages a modern, efficient tech stack tailored:<br>
• Programming Language: Python <br>
• Automation Tool: Playwright for headless/headed browser execution across Chromium, Firefox,...<br>
• Test Runner: Pytest<br>
• Dependency Management: Pip & requirements.txt<br>
• IDE: Visual Studio Code

# Test Coverage
The suite targets high-risk, core user flows on the target site to validate critical test cases: login, cart updates, checkout and API response validation.

# Setup Instructions
1. Clone the repository
2. Setup a virtual environment:
Windows:
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies & Playwright Browsers
pip install -r requirements.txt
playwright install
4. Run the Playwright tests locally

<i>Note: the project hasn't finished and needs to be updated for features like Allure report, CI/CD intergration in the future.</i>