import pytest
import json
import paho.mqtt.client as mqtt
import time
from src.broker_handler import PaymentEligibilityService
from unittest.mock import patch, MagicMock

@pytest.fixture
def mqtt_setup():
    """Setup real MQTT client for testing"""
    processor = PaymentEligibilityService(broker="test.mosquitto.org", port=1883)
    # Allow time for connection
    time.sleep(2)
    return processor

def test_connect_success(mqtt_setup):
    """Test successful MQTT connection"""
    # Start the service
    mqtt_setup.start()
    time.sleep(2)  # Allow time for connection
    
    # Verify connection by checking client is connected
    assert mqtt_setup.client.is_connected()
    mqtt_setup.stop()

def test_connect_failure(mqtt_setup):
    """Test failed MQTT connection"""
    # Create a mock for subscribe method
    mqtt_setup.client.subscribe = MagicMock()
    
    with patch.object(mqtt_setup.client, 'connect', side_effect=Exception("Connection failed")):
        try:
            mqtt_setup.start()
        except Exception as e:
            assert str(e) == "Connection failed"
        
        # Verify subscribe was not called
        assert not mqtt_setup.client.subscribe.called

    mqtt_setup.stop()

def test_valid_message_processing(mqtt_setup):
    """Test processing of valid supplement request"""
    mqtt_setup.start()
    time.sleep(2)  # Allow time for connection
    
    test_data = {
        "id": "test123",
        "numberOfChildren": 1,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }
    
    # Create a separate client to receive the response
    received_messages = []
    
    def on_message(client, userdata, message):
        received_messages.append(json.loads(message.payload.decode()))
    
    test_client = mqtt.Client()
    test_client.on_message = on_message
    test_client.connect("test.mosquitto.org", 1883)
    test_client.subscribe(mqtt_setup.response_topic)
    test_client.loop_start()
    
    # Publish test message
    test_client.publish(mqtt_setup.request_topic, json.dumps(test_data))
    
    # Wait for response
    time.sleep(2)
    
    # Verify response was received
    assert len(received_messages) > 0
    response = received_messages[0]
    assert response["id"] == "test123"
    assert "supplementAmount" in response
    
    # Cleanup
    test_client.loop_stop()
    test_client.disconnect()
    mqtt_setup.stop()

def test_bad_message_handling(mqtt_setup):
    """Test handling of invalid JSON message"""
    mqtt_setup.start()
    time.sleep(2)
    
    # Create test client
    test_client = mqtt.Client()
    test_client.connect("test.mosquitto.org", 1883)
    
    # Send invalid message
    test_client.publish(mqtt_setup.request_topic, "invalid json")
    time.sleep(2)
    
    test_client.disconnect()
    mqtt_setup.stop()

def test_startup_and_shutdown(mqtt_setup):
    """Test service startup and shutdown sequence"""
    # Create mocks for the client methods
    mqtt_setup.client.loop_start = MagicMock()
    mqtt_setup.client.loop_stop = MagicMock()
    mqtt_setup.client.disconnect = MagicMock()
    
    # Test startup
    mqtt_setup.start()
    mqtt_setup.client.loop_start.assert_called_once()
    
    # Test shutdown
    mqtt_setup.stop()
    mqtt_setup.client.loop_stop.assert_called_once()
    mqtt_setup.client.disconnect.assert_called_once()
