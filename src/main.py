import logging
from typing import Dict, Any, List

from experimentation import experiment_results
from simulation import run_simulation
from config import *

# --- Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main entry point for the parameter experimentation.
    """
    logging.info("Starting parameter experimentation...")

    # The experimentation and analysis are now in experimentation.py

    logging.info("Performing further analysis...")

    if 'tax_rate' in experiment_results:
        tax_results: List[Dict[str, Any]] = experiment_results['tax_rate']
        best_tax_rate_data: Dict[str, Any] = min(tax_results, key=lambda x: x['num_bankruptcies'])
        logging.info(f"Tax rate that minimizes bankruptcies: {best_tax_rate_data['param_value']}")

    if 'resource_regen_rate' in experiment_results:
        regen_results: List[Dict[str, Any]] = experiment_results['resource_regen_rate']
        best_regen_rate_data: Dict[str, Any] = max(regen_results, key=lambda x: x['avg_final_balance'])
        logging.info(f"Regen rate that maximizes average final balance: {best_regen_rate_data['param_value']}")

    logging.info("Experimentation and analysis complete.")

if __name__ == "__main__":
    main()