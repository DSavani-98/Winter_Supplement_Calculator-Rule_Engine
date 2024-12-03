import logging
import paho.mqtt.client as mqtt
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def on_message(client, userdata, message):
    """Handle received messages"""
    pass

def run_client():
    """Run client interface"""
    # Get topic ID from environment variable
    topic_id = os.getenv('MQTT_TOPIC_ID', 'default')
    
    client = mqtt.Client()
    client.on_message = on_message
    
    try:
        client.connect("test.mosquitto.org", 1883)
        client.subscribe(f"BRE/calculateWinterSupplementOutput/{topic_id}")
        client.loop_start()
        
        request_count = 1
        while True:
            print("\nOptions:")
            print("1. Calculate Winter Supplement")
            print("2. Exit")
            
            choice = input("\nEnter your choice (1-2): ")
            
            if choice == "1":
                try:
                    children = int(input("Number of children: "))
                    if children < 0:
                        print("Number of children cannot be negative!")
                        continue
                        
                    family_type = input("Family composition (single/couple): ").lower()
                    if family_type not in ["single", "couple"]:
                        print("Invalid family composition!")
                        continue
                        
                    eligible = input("Family unit in pay for December (y/n): ").lower() == 'y'
                    
                    request = {
                        "id": f"WS{request_count:03d}",
                        "numberOfChildren": children,
                        "familyComposition": family_type,
                        "familyUnitInPayForDecember": eligible
                    }
                    
                    client.publish(f"BRE/calculateWinterSupplementInput/{topic_id}", json.dumps(request))
                    request_count += 1
                    time.sleep(1)
                    
                except ValueError:
                    print("Please enter a valid number for children!")
                    continue
                    
            elif choice == "2":
                break
            else:
                print("Invalid choice!")
                continue
                
    except KeyboardInterrupt:
        print("\nShutting down client...")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Client shutdown complete")

if __name__ == "__main__":
    run_client() 