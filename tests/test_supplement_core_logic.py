import pytest
from src.supplement_core_logic import calculate_winter_supplement, validate_input

@pytest.fixture
def valid_single_request():
    return {
        "id": "WS001",
        "numberOfChildren": 0,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }

@pytest.fixture
def valid_couple_request():
    return {
        "id": "WS002",
        "numberOfChildren": 2,
        "familyComposition": "couple",
        "familyUnitInPayForDecember": True
    }

def test_validation_passes(valid_single_request):
    validate_input(valid_single_request)

def test_validation_fails_missing_field():
    invalid_request = {
        "id": "WS003",
        "numberOfChildren": 0,
        "familyUnitInPayForDecember": True
    }
    with pytest.raises(ValueError):
        validate_input(invalid_request)

def test_validation_fails_invalid_composition():
    invalid_request = {
        "id": "WS004",
        "numberOfChildren": 0,
        "familyComposition": "invalid",
        "familyUnitInPayForDecember": True
    }
    with pytest.raises(ValueError):
        validate_input(invalid_request)

def test_single_person_calculation(valid_single_request):
    result = calculate_winter_supplement(valid_single_request)
    assert result["supplementAmount"] == 60.0

def test_couple_with_children_calculation(valid_couple_request):
    result = calculate_winter_supplement(valid_couple_request)
    assert result["supplementAmount"] == 160.0

def test_ineligible_returns_zero():
    ineligible_request = {
        "id": "WS005",
        "numberOfChildren": 0,
        "familyComposition": "single",
        "familyUnitInPayForDecember": False
    }
    result = calculate_winter_supplement(ineligible_request)
    assert result["isEligible"] == False
    assert result["supplementAmount"] == 0.0

# New test cases for better coverage
def test_single_with_children():
    request = {
        "id": "WS006",
        "numberOfChildren": 1,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }
    result = calculate_winter_supplement(request)
    assert result["supplementAmount"] == 120.0 + 20.0

def test_childless_couple():
    request = {
        "id": "WS007",
        "numberOfChildren": 0,
        "familyComposition": "couple",
        "familyUnitInPayForDecember": True
    }
    result = calculate_winter_supplement(request)
    assert result["supplementAmount"] == 120.0

def test_validation_fails_negative_children():
    invalid_request = {
        "id": "WS008",
        "numberOfChildren": -1,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }
    with pytest.raises(ValueError):
        validate_input(invalid_request)