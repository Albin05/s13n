# Data vs Information

## Key Concepts
* **Data:** Raw facts and figures without context (e.g., `10110`, `34.5`).
* **Information:** Processed data that conveys meaning (e.g., `Price: $34.50`).
* **Relationship:** Information depends on data; data does not depend on information.

## The Transformation Process
To turn Data into Information, we typically perform:
1.  **Collection:** Gathering raw facts.
2.  **Organization:** Sorting or categorizing.
3.  **Analysis:** Calculating or interpreting.

## Comparison Table
| Feature | Data | Information |
| :--- | :--- | :--- |
| **State** | Raw, Unprocessed | Processed, Organized |
| **Context** | None | Specific context |
| **Decision Making** | Cannot be used directly | Used for decisions |
| **Example** | `[255, 0, 0]` | "The pixel is Red" |

## Code Snippet: Raw vs Processed
```python
# Raw Data
sensor_readings = [0, 0, 1, 0, 1, 1]

# Information (Interpretation)
active_count = sum(sensor_readings)
status = "Active" if active_count > 3 else "Inactive"
print(f"System Status: {status}")
