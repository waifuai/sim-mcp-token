import unittest
from constants import NUM_AGENTS, NUM_RESOURCES, SIMULATION_STEPS, INITIAL_CTX_BALANCE, RESOURCE_CAPACITY, BASE_RESOURCE_COST, PRICE_ELASTICITY, DEALLOCATION_RATE, AGENT_INCOME, RESOURCE_REGEN_RATE, MAX_RESOURCE_CAPACITY, AGENT_EXPENSE_RATE, MIN_AGENT_BALANCE, BANKRUPTCY_THRESHOLD, DYNAMIC_INCOME_MULTIPLIER, DYNAMIC_REGEN_MULTIPLIER, AGENT_INCOME_CEILING, TAX_RATE, RESOURCE_CAPACITY_MULTIPLIER, INITIAL_IMBALANCE, IMBALANCE_STRENGTH

class TestConstants(unittest.TestCase):

    def test_constants_defined(self):
        self.assertIsInstance(NUM_AGENTS, int)
        self.assertIsInstance(NUM_RESOURCES, int)
        self.assertIsInstance(SIMULATION_STEPS, int)
        self.assertIsInstance(INITIAL_CTX_BALANCE, int)
        self.assertIsInstance(RESOURCE_CAPACITY, int)
        self.assertIsInstance(BASE_RESOURCE_COST, int)
        self.assertIsInstance(PRICE_ELASTICITY, float)
        self.assertIsInstance(DEALLOCATION_RATE, float)
        self.assertIsInstance(AGENT_INCOME, float)
        self.assertIsInstance(RESOURCE_REGEN_RATE, float)
        self.assertIsInstance(MAX_RESOURCE_CAPACITY, int)
        self.assertIsInstance(AGENT_EXPENSE_RATE, float)
        self.assertIsInstance(MIN_AGENT_BALANCE, int)
        self.assertIsInstance(BANKRUPTCY_THRESHOLD, int)
        self.assertIsInstance(DYNAMIC_INCOME_MULTIPLIER, float)
        self.assertIsInstance(DYNAMIC_REGEN_MULTIPLIER, float)
        self.assertIsInstance(AGENT_INCOME_CEILING, float)
        self.assertIsInstance(TAX_RATE, float)
        self.assertIsInstance(RESOURCE_CAPACITY_MULTIPLIER, float)
        self.assertIsInstance(INITIAL_IMBALANCE, bool)
        self.assertIsInstance(IMBALANCE_STRENGTH, float)

if __name__ == '__main__':
    unittest.main()