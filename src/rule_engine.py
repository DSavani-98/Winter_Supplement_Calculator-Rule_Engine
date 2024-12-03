import logging
import time
from broker_handler import PaymentEligibilityService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("\nStarting MQTT Service...")
    service = PaymentEligibilityService()
    
    try:
        service.start()
        # Keep the service running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("\nShutting down service...")
    finally:
        service.stop()
        logger.info("Service shutdown complete")

if __name__ == "__main__":
    main()