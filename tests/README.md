# Tests Directory

## Overview

The `tests` directory contains comprehensive unit tests to ensure the reliability and accuracy of the system. These tests validate the core functionalities of MQTT communication and the Winter Supplement calculation logic.

---

## Test Files

1. **`test_broker_handler.py`**  
   Contains tests for MQTT broker interaction, connection lifecycle, and message processing logic.

2. **`test_supplement_core_logic.py`**  
   Includes tests for validating input data and calculating the Winter Supplement eligibility and amounts.

---

## Test Cases

### 1. `test_broker_handler.py`

This file includes multiple test cases to validate the MQTT client lifecycle and message processing logic.

- **`test_connect_success`**  
  Verifies that the MQTT client connects successfully to the broker and subscribes to the input topic.  
  Asserts the connection state and ensures proper cleanup after testing.

- **`test_connect_failure`**  
  Simulates a connection failure using mocked exceptions.  
  Ensures that no subscriptions are made if the connection fails.

- **`test_valid_message_processing`**  
  Tests the processing of valid JSON messages by publishing to the input topic.  
  Verifies that the calculated response is published to the output topic.

- **`test_bad_message_handling`**  
  Publishes invalid JSON to the input topic.  
  Ensures that invalid messages do not result in a response being published.

- **`test_startup_and_shutdown`**  
  Tests the correct invocation of MQTT client lifecycle methods (`loop_start`, `loop_stop`, and `disconnect`).  
  Ensures smooth startup and cleanup.

---

### 2. `test_supplement_core_logic.py`

This file contains test cases to validate input schema compliance and Winter Supplement calculation logic.

- **`test_validation_passes`**  
  Ensures that valid input data passes schema validation.

- **`test_validation_fails_missing_field`**  
  Verifies that missing required fields raise a validation error.

- **`test_validation_fails_invalid_composition`**  
  Tests that invalid values for `familyComposition` raise validation errors.

- **`test_single_person_calculation`**  
  Confirms that a single person without children receives the correct supplement of $60.

- **`test_couple_with_children_calculation`**  
  Validates that a couple with two children receives the correct supplement of $160.

- **`test_ineligible_returns_zero`**  
  Ensures that families ineligible for December payments receive $0.

- **`test_validation_fails_negative_children`**  
  Tests that negative values for `numberOfChildren` raise a validation error.

- **`test_single_with_children`**  
  Confirms that a single person with one child receives $80 ($60 base + $20 per child).

- **`test_childless_couple`**  
  Validates that a childless couple receives the correct base amount of $120.

---

## How to Run Tests

### Run All Tests

Execute the following command to run all tests:
```bash
pytest -v --color=yes

Run All Tests with Coverage

To check test coverage, run:

pytest --cov=src

Interpret Coverage Report

Example output:

Name                            Stmts   Miss  Cover
-----------------------------------------------
src/broker_handler.py              61      0   100%
src/supplement_core_logic.py       42      0   100%
-----------------------------------------------
TOTAL                             103      0   100%

Notes

	•	All tests require an active MQTT broker (test.mosquitto.org) running on port 1883.
	•	Ensure all dependencies listed in requirements.txt are installed before running the tests.
