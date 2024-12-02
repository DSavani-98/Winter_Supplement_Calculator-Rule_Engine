# Tests Directory

### Overview

The `tests` folder has detailed unit tests to check the system’s reliability and accuracy. They cover MQTT communication and the Winter Supplement calculation logic.

---

### Test Files

`test_broker_handler.py`

Contains tests for MQTT broker interaction, connection lifecycle, and message processing logic.

`test_supplement_core_logic.py`
   
  Includes tests for validating input data and calculating the Winter Supplement eligibility and amounts.

---

#### 1. Test Cases under `test_broker_handler.py`

- *`test_connect_success`*:

  Confirms that the MQTT client connects to the broker and subscribes to the correct topic.
  Checks the connection status and ensures proper cleanup after execution.

- *`test_connect_failure`*:

  Mocks connection errors to simulate failure scenarios.
  Verifies that no subscriptions are created when the connection is unsuccessful.

- *`test_valid_message_processing`*: 
  
  Publishes valid JSON messages to the input topic to test message handling.
  Ensures the correct response is published to the output topic.

- *`test_bad_message_handling`*: 
  
  Sends invalid JSON to the input topic to test error handling.
  Confirms that no responses are published for invalid messages.

- *`test_startup_and_shutdown`*:  
  
  Checks the proper initialization and cleanup of MQTT client lifecycle methods (loop_start, loop_stop, and disconnect).
  Ensures smooth system startup and shutdown.
---
<br>

#### 2. Test Cases under `test_supplement_core_logic.py`

- *`test_validation_passes`*:

  Verifies that valid input data passes all schema checks without errors.

- *`test_validation_fails_missing_field`*:  

  Confirms that missing required fields trigger appropriate validation errors.

- *`test_validation_fails_invalid_composition`*:  

  Validates that a single individual without children receives a benefit of $60.

- *`test_single_person_calculation`*:

  Verifies that ineligible families correctly receive a benefit amount of $0.

- *`test_couple_with_children_calculation`*:

  Confirms that a couple with two children receives a total benefit of $160.


- *`test_ineligible_returns_zero`*: 

  Verifies that ineligible families correctly receive a benefit amount of $0.


- *`test_validation_fails_negative_children`*:

  Tests that negative values for numberOfChildren trigger validation errors.


- *`test_single_with_children`*:

Confirms that a single individual with one child gets $80 ($60 base + $20 for the child).


- *`test_childless_couple`*:

  Validates that a couple without children receives the base amount of $120.
---
<br>

### Notes:

- All tests require an active MQTT broker (test.mosquitto.org) running on port 1883.
- Ensure all dependencies listed in requirements.txt are installed before running the tests.
