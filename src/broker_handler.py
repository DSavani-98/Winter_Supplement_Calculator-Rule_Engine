import logging
import json
import paho.mqtt.client as mqtt
import os
from typing import Any, Dict
from src.supplement_core_logic import calculate_winter_supplement
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class PaymentEligibilityService:
    """
    Handles MQTT communication for payment eligibility and calculations.
    """
    
    def __init__(self, broker: str = "test.mosquitto.org", port: int = 1883):
        """
        Initialize MQTT client and setup topics.
        
        Args:
            broker: MQTT broker address (default: test.mosquitto.org)
            port: MQTT broker port
        """
        # Get topic ID from environment variable, default to "default" if not set
        self.topic_id = os.getenv('MQTT_TOPIC_ID', 'default')
        
        # MQTT setup
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        
        # Configure callback handlers
        self.client.on_connect = self.handle_connect
        self.client.on_message = self.handle_message
        self.client.on_disconnect = self.handle_disconnect
        
        # Topic configuration with dynamic topic ID
        self.request_topic = f"BRE/calculateWinterSupplementInput/{self.topic_id}"
        self.response_topic = f"BRE/calculateWinterSupplementOutput/{self.topic_id}"

    def start(self) -> None:
        """Start the MQTT client and connect to broker."""
        try:
            self.client.connect(self.broker, self.port)
            self.client.loop_start()
            logger.info("Connected to MQTT broker")
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            raise

    def stop(self) -> None:
        """Stop the MQTT client and disconnect."""
        try:
            self.client.loop_stop()
            self.client.disconnect()
        except Exception as e:
            logger.error(f"Error during shutdown: {e}")

    def handle_disconnect(self, client: mqtt.Client, userdata: Any, rc: int) -> None:
        """Handle disconnection from MQTT broker."""
        if rc != 0:
            logger.warning(f"Unexpected disconnection, return code: {rc}")
            # Attempt to reconnect using connect instead of reconnect
            try:
                self.client.connect(self.broker, self.port)
            except Exception as e:
                logger.error(f"Reconnection failed: {e}")
        else:
            logger.info("Disconnected from MQTT broker")

    def handle_connect(self, client: mqtt.Client, userdata: Any, flags: Dict, rc: int) -> None:
        """Handle connection to MQTT broker."""
        if rc == 0:
            self.client.subscribe(self.request_topic)
            logger.info(f"Subscribed to topic: {self.request_topic}")
        else:
            logger.error(f"Connection failed with code {rc}")

    def handle_message(self, client: mqtt.Client, userdata: Any, message: mqtt.MQTTMessage) -> None:
        """Process incoming MQTT messages."""
        try:
            request = json.loads(message.payload.decode())
            
            # Display incoming request
            print("\n=== Request Data ===")
            print(json.dumps(request, indent=2))
            
            # Calculate supplement
            result = calculate_winter_supplement(request)
            
            # Display response before sending
            print("\n=== Response Data ===")
            print(json.dumps(result, indent=2))
            
            # Send response
            self.client.publish(self.response_topic, json.dumps(result))
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")


