# Winter Supplement Eligibility Calculator

## Overview
This project implements a **Winter Supplement Eligibility Calculator** for determining a client’s eligibility and calculating their benefit amount based on predefined rules. The application uses an event-driven architecture with an MQTT broker for seamless message exchange. It integrates a dynamic rule engine for real-time processing of eligibility criteria and calculations.

---

## Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-repo-name>.git
   cd <your-repo-name>

	2.	Create a Virtual Environment:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows


	3.	Install Dependencies:

pip install -r requirements.txt


	4.	Set Environment Variables:
	•	Copy .env:

cp .env.example .env


	•	Update MQTT_TOPIC_ID and other variables in the .env file if necessary.

How to Run the Engine

	1.	Start the Rule Engine:

python src/rule_engine.py

This connects to the MQTT broker, subscribes to the input topic, and dynamically processes incoming requests.

	2.	Run the Client Interface:

python src/client.py

Use the interactive CLI to send test requests for calculating the Winter Supplement. This tool allows manual testing of the rule engine.

How to Run Tests

	1.	Execute Unit Tests:

pytest tests/ --cov=src --cov-report=term-missing

This command runs all unit tests and generates a coverage report for the src folder.

	2.	Sample Coverage Report Output:

Name                            Stmts   Miss  Cover
-----------------------------------------------
src/broker_handler.py              61      0   100%
src/supplement_core_logic.py       42      0   100%
-----------------------------------------------
TOTAL                             103      0   100%

Prerequisites

	•	Python 3.8 or higher
	•	MQTT broker (e.g., test.mosquitto.org)
	•	Internet connection for MQTT broker communication
	•	Git for cloning the repository

Recorded Videos

	1.	Establishing Connection with the MQTT Broker:
Demonstrates the process of connecting the application to the MQTT broker and passing data in the exact JSON format received from the web application.
	2.	Interactive Testing with Step-by-Step User Input:
Showcases an additional feature that imitates user input step by step. This feature facilitates better usability and allows for manual testing of the application.
	3.	Executing All Tests:
Displays the process of running all test cases using the command:

pytest -v --color=yes

The video highlights the successful execution of tests with detailed results.

	4.	Running Tests with Coverage Report:
Illustrates running tests with the coverage command:

pytest -v --color=yes --cov=src

The video shows the generated coverage report, ensuring complete test coverage of the core functionality.
