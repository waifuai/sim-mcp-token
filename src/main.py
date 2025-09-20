import logging
from typing import Dict, Any, List

from experimentation import run_experiments, analyze_results, experiment_results
from constants import *

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main entry point for the parameter experimentation.
    """
    run_experiments()
    analyze_results()

if __name__ == "__main__":
    main()