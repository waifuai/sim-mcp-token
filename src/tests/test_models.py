import unittest
import numpy as np
from models import Agent, Resource
from constants import NUM_RESOURCES, BASE_RESOURCE_COST

class TestModels(unittest.TestCase):

    def setUp(self):
        self.agent = Agent(0)
        self.resource = Resource(0)

    def test_agent_initialization(self):
        self.assertEqual(self.agent.agent_id, 0)
        self.assertTrue(self.agent.ctx_balance > 0)
        self.assertEqual(len(self.agent.resource_demand_preference), NUM_RESOURCES)
        self.assertFalse(self.agent.is_bankrupt)

    def test_resource_initialization(self):
        self.assertEqual(self.resource.resource_id, 0)
        self.assertTrue(self.resource.capacity > 0)
        self.assertEqual(self.resource.current_load, 0)
        self.assertEqual(self.resource.price, BASE_RESOURCE_COST)

    def test_agent_request_resources(self):
        resource_prices = np.array([1.0, 2.0, 3.0])
        resource_availability = np.array([100.0, 50.0, 25.0])
        requests = self.agent.request_resources(resource_prices, resource_availability)
        # Basic check: should return a list
        self.assertIsInstance(requests, list)

    def test_agent_adjust_needs(self):
        initial_needs = self.agent.resource_demand_preference.copy()
        self.agent.adjust_needs()
        self.assertFalse(np.array_equal(self.agent.resource_demand_preference, initial_needs))

    def test_agent_add_income(self):
        initial_balance = self.agent.ctx_balance
        self.agent.add_income(1.0)
        self.assertGreater(self.agent.ctx_balance, initial_balance)

    def test_agent_add_expense(self):
        initial_balance = self.agent.ctx_balance
        self.agent.add_expense()
        self.assertLess(self.agent.ctx_balance, initial_balance)

    def test_agent_tax(self):
        initial_balance = self.agent.ctx_balance
        tax_amount = 10
        self.agent.tax(tax_amount)
        self.assertEqual(self.agent.ctx_balance, initial_balance - tax_amount)

    def test_agent_check_bankrupt(self):
        self.agent.ctx_balance = -100
        self.agent.check_bankrupt()
        self.assertTrue(self.agent.is_bankrupt)

    def test_resource_update_price(self):
        initial_price = self.resource.price
        self.resource.current_load = self.resource.capacity
        self.resource.update_price()
        self.assertGreater(self.resource.price, initial_price)

    def test_resource_allocate(self):
        amount = 10
        allocated = self.resource.allocate(amount)
        self.assertEqual(allocated, amount)
        self.assertEqual(self.resource.current_load, amount)

    def test_resource_deallocate(self):
        amount = 10
        self.resource.allocate(amount)
        self.resource.deallocate(5)
        self.assertEqual(self.resource.current_load, 5)

    def test_resource_regenerate(self):
        initial_capacity = self.resource.capacity
        self.resource.regenerate(100)
        self.assertGreaterEqual(self.resource.capacity, initial_capacity)

    def test_resource_adjust_capacity(self):
        initial_capacity = self.resource.capacity
        self.resource.adjust_capacity(100)
        self.assertGreaterEqual(self.resource.capacity, initial_capacity)

if __name__ == '__main__':
    unittest.main()