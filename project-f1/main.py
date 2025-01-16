import json
from tabulate import tabulate

class F1LapAnalyzer:
    def __init__(self, driver_file="f1drivers.json"):
        self.driver_file = driver_file
        self.driver_data = self._load_driver_data()

    def _load_driver_data(self):
        """Load driver information from the specified JSON file."""
        try:
            with open(self.driver_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Driver file '{self.driver_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{self.driver_file}'.")
            return {}

    @staticmethod
    def _read_json(file_name):
        """Generic method to read a JSON file."""
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON format in '{file_name}'.")
            return {}

    def analyze_lap_file(self, lap_file):
        """Process a single lap times file."""
        lap_data = self._read_json(lap_file)
        grand_prix = lap_data.get("grand_prix_location", "Unknown")
        lap_times = lap_data.get("lap_times", {})

        # if not lap_times:
        #     print(f"No lap data in '{lap_file}'. Skipping...")
        #     return None

        return grand_prix, self._evaluate_lap_times(lap_times)

    def _evaluate_lap_times(self, lap_times):
        """Evaluate the lap times to find metrics for each driver."""
        fastest_time = float('inf')
        top_driver = None
        metrics = []

        for driver, times in lap_times.items():
            best_time = min(times)
            avg_time = sum(times) / len(times)

            metrics.append({
                "driver": driver,
                "fastest_time": best_time,
                "average_time": avg_time
            })

            if best_time < fastest_time:
                fastest_time = best_time
                top_driver = driver

        return top_driver, fastest_time, metrics

    def generate_log(self, grand_prix, top_driver, top_time, metrics, log_file):
        """Save the analysis results to a JSON file."""
        log = {
            "grand_prix_location": grand_prix,
            "top_driver": top_driver,
            "fastest_time": top_time,
            "driver_statistics": []
        }

        for metric in metrics:
            driver_info = self.driver_data.get(metric["driver"], {"name": "Unknown", "team": "Unknown"})
            log["driver_statistics"].append({
                "code": metric["driver"],
                "name": driver_info["name"],
                "team": driver_info["team"],
                "best_time": metric["fastest_time"],
                "average_time": metric["average_time"]
            })

        with open(log_file, "w") as file:
            json.dump(log, file, indent=4)
        print(f"Results saved to '{log_file}'.")

    def display_results(self, grand_prix, top_driver, top_time, metrics):
        """Present the analysis results in a table format."""
        print(f"Grand Prix: {grand_prix}")
        print(f"Top Driver: {top_driver} with {top_time:.3f}s\n")

        # Prepare rows for the table
        rows = [
            [
                metric["driver"],
                self.driver_data.get(metric["driver"], {}).get("name", "Unknown"),
                self.driver_data.get(metric["driver"], {}).get("team", "Unknown"),
                f"{metric['fastest_time']:.3f}",
                f"{metric['average_time']:.3f}"
            ]
            for metric in sorted(metrics, key=lambda m: m["fastest_time"])
        ]

        # Print the table
        print(tabulate(rows, headers=["Driver", "Name", "Team", "Fastest Time", "Average Time"], tablefmt="fancy_grid"))

def process_files():
    """Main processing function for analyzing lap files."""
    analyzer = F1LapAnalyzer()
    lap_files = ["laptimes1.json", "laptimes2.json", "laptimes3.json"]

    for lap_file in lap_files:
        print(f"\nProcessing: {lap_file}")
        analysis_result = analyzer.analyze_lap_file(lap_file)

        if analysis_result is None:
            continue

        grand_prix, (top_driver, top_time, metrics) = analysis_result
        analyzer.display_results(grand_prix, top_driver, top_time, metrics)

        log_name = f"{lap_file.split('.')[0]}_log.json"
        analyzer.generate_log(grand_prix, top_driver, top_time, metrics, log_name)

if __name__ == "__main__":
    process_files()
