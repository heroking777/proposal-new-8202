import re

def validate_and_map_data(data):
    # Define the expected structure of the data
    expected_structure = {
        "user_id": str,
        "username": str,
        "email": str,
        "role": str,
        "is_active": bool,
        "created_at": str,
        "updated_at": str
    }

    # Check if all required keys are present in the data
    for key, expected_type in expected_structure.items():
        if key not in data:
            raise ValueError(f"Missing key: {key}")

    # Validate and map each field according to the expected structure
    mapped_data = {}
    for key, value in data.items():
        if not isinstance(value, expected_structure[key]):
            raise TypeError(f"Invalid type for key '{key}': Expected {expected_structure[key]}, got {type(value).__name__}")
        
        # Additional validation rules can be added here
        if key == "email":
            if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                raise ValueError(f"Invalid email format for key '{key}': {value}")

        mapped_data[key] = value

    return mapped_data

# Example usage:
data = {
    "user_id": "12345",
    "username": "new_user",
    "email": "example@example.com",
    "role": "admin",
    "is_active": True,
    "created_at": "2023-04-01T12:00:00Z",
    "updated_at": "2023-04-01T12:00:00Z"
}

try:
    validated_data = validate_and_map_data(data)
    print("Validated and mapped data:", validated_data)
except (ValueError, TypeError) as e:
    print("Validation error:", e)