# F1 Lap Analyzer

The **F1 Lap Analyzer** is a Python-based tool designed to process and analyze lap time data from Formula 1 races. It evaluates lap times, determines the fastest driver, and generates statistical reports for further insights.

---

## Features

1. **Driver Information Integration**: Combines driver codes with metadata (e.g., name, team) from a driver configuration file.
2. **Lap Time Analysis**: Processes lap time data, computes the fastest and average lap times for each driver, and identifies the top performer.
3. **Logging**: Saves detailed results to a JSON file for future reference.
4. **Tabulated Display**: Presents analysis results in a readable table format using the `tabulate` library.
5. **Multi-File Processing**: Handles multiple lap time files in sequence.
6. **Error Handling**: Gracefully handles missing or malformed input files.

---

## Files

- `f1drivers.json`: A JSON file containing metadata about drivers (e.g., names, teams, and codes).
- `laptimesX.json`: JSON files containing lap time data for specific races.
- `f1_lap_analyzer.py`: Main script for analyzing lap data.

---

## Data Format

### `f1drivers.json`
This file provides metadata about drivers. It should be structured as follows:
```json
{
    "DRIVER_CODE": {
        "name": "Driver Name",
        "team": "Team Name"
    },
    "HAM": {
        "name": "Lewis Hamilton",
        "team": "Mercedes"
    }
}
```

### Lap Time Files (`laptimesX.json`)
Lap time data files contain information about the Grand Prix and lap times. Example structure:
```json
{
    "grand_prix_location": "Silverstone",
    "lap_times": {
        "HAM": [89.123, 88.456, 87.789],
        "VER": [88.321, 87.654, 87.012]
    }
}
```

---

## How to Run

1. **Install Dependencies**:
   Ensure Python 3.x is installed. The `tabulate` library is required. Install it using:
   ```bash
   pip install tabulate
   ```

2. **Prepare Input Files**:
   - Create or update `f1drivers.json` with driver details.
   - Add lap time files (`laptimesX.json`) for analysis.

3. **Run the Script**:
   ```bash
   python f1_lap_analyzer.py
   ```

4. **View Results**:
   - Results are displayed in the console as a table.
   - Logs are saved as JSON files (e.g., `laptimes1_log.json`).

---

## Example Output

### Console Output
```
Processing: laptimes1.json
Grand Prix: Silverstone
Top Driver: VER with 87.012s

╒══════════╤══════════════════╤═════════════╤═══════════════╤═══════════════╕
│ Driver   │ Name             │ Team        │ Fastest Time  │ Average Time  │
╞══════════╪══════════════════╪═════════════╪═══════════════╪═══════════════╡
│ VER      │ Max Verstappen   │ Red Bull    │ 87.012        │ 87.662        │
│ HAM      │ Lewis Hamilton   │ Mercedes    │ 87.789        │ 88.456        │
╘══════════╧══════════════════╧═════════════╧═══════════════╧═══════════════╛
```

### Log File (`laptimes1_log.json`)
```json
{
    "grand_prix_location": "Silverstone",
    "top_driver": "VER",
    "fastest_time": 87.012,
    "driver_statistics": [
        {
            "code": "VER",
            "name": "Max Verstappen",
            "team": "Red Bull",
            "best_time": 87.012,
            "average_time": 87.662
        },
        {
            "code": "HAM",
            "name": "Lewis Hamilton",
            "team": "Mercedes",
            "best_time": 87.789,
            "average_time": 88.456
        }
    ]
}
```

---

## Customization

1. **Driver Data**:
   Add or modify driver information in `f1drivers.json`.

2. **Lap Data**:
   Add new lap time files following the required structure.

3. **Disabling Log Generation**:
   Comment or remove the `generate_log` call in the `process_files` function.

---

## Known Limitations

1. **Error Handling**:
   Missing or malformed JSON files may cause partial functionality.

2. **Scalability**:
   Designed for single-race analysis and might require adjustments for large datasets.

---

## Future Improvements

1. **Enhanced Error Reporting**: Add detailed logging for file and JSON-related errors.
2. **Web Interface**: Build a front-end for easier interaction.
3. **Advanced Statistics**: Include additional metrics, such as median lap times.
4. **Batch Processing**: Support simultaneous analysis of multiple races.

---

## License
This project is open-source and available for use and modification under the MIT License.

