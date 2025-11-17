# Medical Records Validator

Medical Records Validator is a Python program that checks the integrity and correctness of structured medical records.  
Each record represents a patient and is validated for proper structure, required keys, and field-specific constraints.

## How It Works

- The program expects a list or tuple of dictionaries, each representing a patient record.

- Each dictionary must have the following keys:
  `patient_id`, `age`, `gender`, `diagnosis`, `medications`, `last_visit_id`.

- Each record is checked for validity:
  - `patient_id` must match the pattern `P####` (case-insensitive).
  - `age` must be an integer greater than or equal to 18.
  - `gender` must be either `'male'` or `'female'` (case-insensitive).
  - `diagnosis` must be a string or `None`.
  - `medications` must be a list of strings.
  - `last_visit_id` must match the pattern `V####` (case-insensitive).

- For each record:
  - If it’s not a dictionary, an error message is printed.
  - If keys are missing or extra keys exist, an error message is printed.
  - If individual fields violate constraints, an error message is printed showing the key, value, and position.

## Example

Input:

```
    medical_records = [
        {
            'patient_id': 'P1001',
            'age': 34,
            'gender': 'Female',
            'diagnosis': 'Hypertension',
            'medications': ['Lisinopril'],
            'last_visit_id': 'V2301',
        },
        {
            'patient_id': 'p1002',
            'age': 17,
            'gender': 'male',
            'diagnosis': 'Type 2 Diabetes',
            'medications': ['Metformin', 'Insulin'],
            'last_visit_id': 'v2302',
        }
    ]

validate(medical_records)
```

Output:

```
    Unexpected format 'age: 17' at position 1.
    Unexpected format 'last_visit_id: v2302' at position 1.
```

## How to Run

- Save the file as medical_validator.py.

- Run the script using:

    `python medical_validator.py`

- Modify or add more records in the medical_records list to test the validation.