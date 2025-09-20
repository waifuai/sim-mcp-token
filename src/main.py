"""
Entry point for the agent-based economic simulation parameter experimentation.

This module serves as the main entry point for running the complete parameter
experimentation suite. It orchestrates the execution of experiments across
different economic parameter ranges and performs analysis of the results to
identify optimal policy settings.

The main function executes the full experimentation workflow:
1. Parameter space exploration across multiple dimensions
2. Simulation runs for each parameter combination
3. Results collection and statistical analysis
4. Identification of optimal economic policies
"""
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