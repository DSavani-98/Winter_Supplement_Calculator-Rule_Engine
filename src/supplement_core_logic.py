import logging
from jsonschema import validate, ValidationError

logger = logging.getLogger(__name__)

REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "numberOfChildren": {"type": "integer", "minimum": 0},
        "familyComposition": {"type": "string", "enum": ["single", "couple"]},
        "familyUnitInPayForDecember": {"type": "boolean"}
    },
    "required": ["id", "numberOfChildren", "familyComposition", "familyUnitInPayForDecember"]
}

def calculate_winter_supplement(data: dict) -> dict:
    """Calculate winter supplement amount."""
    try:
        validate(instance=data, schema=REQUEST_SCHEMA)
    except ValidationError as e:
        logger.error(f"Validation failed: {e.message}")
        raise ValueError(f"Invalid input: {e.message}")

    # If not eligible for December payments, return 0
    if not data["familyUnitInPayForDecember"]:
        return {
            "id": data["id"],
            "isEligible": False,
            "supplementAmount": 0.0
        }

    # Determine the base amount based on family composition
    if data["numberOfChildren"] > 0:  # Families with children
        base_amount = 120.0
    else:  # Childless single or couple
        base_amount = 120.0 if data["familyComposition"] == "couple" else 60.0

    # Add the child amount
    child_amount = data["numberOfChildren"] * 20.0

    # Calculate total supplement
    total_amount = base_amount + child_amount

    return {
        "id": data["id"],
        "isEligible": True,
        "supplementAmount": total_amount
    }

def validate_input(data: dict) -> None:
    """Validate the input data against the schema."""
    try:
        validate(instance=data, schema=REQUEST_SCHEMA)
    except ValidationError as e:
        logger.error(f"Validation failed: {e.message}")
        raise ValueError(f"Invalid input: {e.message}")