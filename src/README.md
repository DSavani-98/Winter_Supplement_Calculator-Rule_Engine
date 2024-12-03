# src Directory

## Overview
The `src` directory holds the main implementation of the Winter Supplement Eligibility Calculator. It includes modules for MQTT communication, request processing, and rule-based eligibility calculations. The design focuses on integration, modularity, and scalability.

---

### Modules

#### rule_engine.py

- Acts as the main entry point for the system.
- Initializes the PaymentEligibilityService from broker_handler.py.
- Starts and manages the MQTT service to handle messages until interrupted.

#### broker_handler.py

- Manages MQTT communication and message handling.
- Subscribes to request topics and publishes responses dynamically based on the environment.
- Processes incoming messages to calculate the Winter Supplement using the logic from supplement_core_logic.py.

	##### Key Features:
	- Handles connections, disconnections, and reconnections to the MQTT broker.
	- Dynamically uses topic IDs for flexible communication.
	- Ensures smooth operation with lifecycle management (start, stop, and error handling).

#### client.py
- Provides an interactive client interface to send test requests and receive responses.
- Allows users to input family details such as:
- Number of children.
- Family composition (single or couple).
- Eligibility for December payments.
- Publishes data to the input topic and listens for responses on the output topic.

	##### Key Features:
	- Input validation for user-friendly error handling.
	- Supports testing multiple scenarios through an interactive menu.

#### supplement_core_logic.py
- Contains the core logic for calculating the Winter Supplement.
- Validates input data against a predefined schema using jsonschema.

	##### Key Features:
	- Validation:
	- Ensures data integrity and correctness (e.g., non-negative children, valid family composition).
	
	##### Calculation:
	- Determines eligibility and computes supplement amounts:
	- Base amount: $60 (single) or $120 (couple).
	- Additional $20 for each child.
	- Returns $0 if not eligible for December payments.
	

---
<br>

### Usage:

1.	Start the rule_engine.py to launch the MQTT service.
2.	Use client.py to send test requests and validate responses.
3.	Modify topics and configurations using environment variables for flexible deployments.
