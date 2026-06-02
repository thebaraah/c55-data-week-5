"""
Week 5 assignment: containerised data pipeline.

Tasks:
- Task 1: confirm this script runs locally before touching the Dockerfile.
- Task 5: read all configuration from environment variables (no hardcoded values).

Replace every `raise NotImplementedError` below with a real implementation.
"""
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def get_config() -> dict:
    """
    Return configuration read from environment variables.

    Required variable: API_KEY
    Optional variable: OUTPUT_DIR (default "output")

    Raise RuntimeError with a clear message if a required variable is missing.
    """
    api_key = os.getenv("API_KEY")
    output_dir = os.getenv("OUTPUT_DIR", "output")

    if not api_key:
        raise RuntimeError("ERROR: API_KEY is not set in environment variables")


    return {
        "api_key": api_key,
        "output_dir": output_dir,
       
    }
    raise NotImplementedError("Task 5: read API_KEY and OUTPUT_DIR from the environment")

def clean_name(name: str) -> str:
    return name.strip()

def fetch_data(api_key: str) -> list[dict]:
    """
    Simulate fetching records from an external API.

    Return a list of at least one dict representing a record.
    In a real pipeline you would call requests.get(...) here.
    """
    logger.info("fetching data")

    return [
        {"id": 1, "name": "Alice", "value": 100},
        {"id": 2, "name": "Bob", "value": 200},
    ]

def save_results(records: list[dict], output_dir: Path) -> None:
    """
    Write each record as a line to output_dir/results.txt.

    Create output_dir if it does not exist.
    Log the number of records written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "results.txt"

    with file_path.open("w") as f:
        for record in records:
            f.write(f"{record}\n")
    logger.info(f"saved {len(records)} records to {file_path}")
     #raise NotImplementedError("Task 1: write records to output_dir/results.txt")


def run() -> None:
    config = get_config()
    logger.info("starting pipeline")
    records = fetch_data(config["api_key"])
    output_dir = Path(config["output_dir"])
    save_results(records, output_dir)
    logger.info("pipeline complete")


if __name__ == "__main__":
    run()
