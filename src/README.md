# src Directory

## Overview
The `src` directory contains the core implementation of the **Winter Supplement Eligibility Calculator**. This folder includes modules for handling MQTT communication, processing requests, and applying the rules engine logic. The design ensures seamless integration, modularity, and scalability for eligibility determination and supplement calculations.

---

## Modules

### 1. `broker_handler.py`
- **Purpose**: Manages communication with the MQTT broker.
- **Responsibilities**:
  - Connects to the MQTT broker and subscribes to input topics.
  - Processes incoming requests and publishes results to output topics.
  - Handles reconnection scenarios for uninterrupted service.
- **Highlights**:
  - Dynamic topic management using environment variables.
  - Error handling to ensure reliable message processing.

---

### 2. `rule_engine.py`
- **Purpose**: Serves as the application’s entry point for starting the rules engine.
- **Responsibilities**:
  - Initializes the MQTT communication service.
  - Keeps the rules engine running to handle real-time requests.
- **Usage**:
  ```bash
  python src/rule_engine.py

3. client.py

	•	Purpose: Provides an interactive command-line interface for testing the application.
	•	Responsibilities:
	•	Collects user input for family details (e.g., family composition, number of children).
	•	Sends requests to the rules engine and receives responses via MQTT.
	•	Usage:

python src/client.py


	•	Features:
	•	Intuitive prompts for user interaction.
	•	Real-time response display.

4. supplement_core_logic.py

	•	Purpose: Implements the core business logic for determining eligibility and calculating supplement amounts.
	•	Responsibilities:
	•	Validates input requests against a JSON schema.
	•	Determines eligibility and computes the supplement amount based on family composition and rules.
	•	Calculation Rules:
	•	Single Individual: $60.
	•	Childless Couple: $120.
	•	Families with Children: $120 plus $20 per child.
	•	Output:
	•	Structured JSON response with eligibility status and calculated amounts.

How to Extend

	•	Modify Rules: Update supplement_core_logic.py to incorporate new eligibility criteria or benefit calculations.
	•	Add New Topics: Adjust broker_handler.py to include additional MQTT topics for integration with other services.

This README provides a concise yet professional overview of the src folder, focusing on its functionality and modularity. For further details, explore the individual modules or contact the development team.

This Markdown version ensures proper formatting and clear presentation in any Markdown viewer or repository platform. Let me know if further adjustments are needed!