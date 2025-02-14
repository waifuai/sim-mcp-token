import unittest
from typing import Dict, Any
from simulation import run_simulation, simulation_step
from models import Agent, Resource
from constants import NUM_AGENTS, NUM_RESOURCES

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.params: Dict[str, Any] = {}
        self.agents = [Agent(i) for i in range(NUM_AGENTS)]
        self.resources = [Resource(i) for i in range(NUM_RESOURCES)]

    def test_simulation_step(self):
        step_metrics = simulation_step(self.agents, self.resources, 0, self.params)
        self.assertIsInstance(step_metrics, dict)
        self.assertIn("step", step_metrics)
        self.assertIn("gini", step_metrics)
        self.assertIn("median_balance", step_metrics)
        self.assertIn("resource_utilization", step_metrics)
        self.assertIn("price_variance", step_metrics)
        self.assertIn("bankruptcy_rate", step_metrics)
        self.assertIn("tax_redistribution", step_metrics)
        self.assertIn("economic_output", step_metrics)

    def test_run_simulation(self):
        results = run_simulation(self.params)
        self.assertIsInstance(results, dict)
        self.assertIn("avg_final_balance", results)
        self.assertIn("gini_coefficient", results)
        self.assertIn("num_bankruptcies", results)
        self.assertIn("avg_final_resource_price", results)
        self.assertIn("step_metrics", results)

if __name__ == '__main__':
    unittest.main()