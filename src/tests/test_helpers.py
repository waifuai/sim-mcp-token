import unittest
import numpy as np
from typing import List, Any
from helpers import update_resource_prices, get_resource_prices, get_resource_availability, get_agent_requests, allocate_resources, deallocate_resources, regenerate_resources, adjust_agent_needs, adjust_agent_demand_multiplier, add_agent_income, add_agent_expense, check_agent_bankruptcies, tax_agents, redistribute_wealth, adjust_resource_capacity, get_agent_balances, get_resource_load_and_prices, get_total_economic_output, calculate_gini_coefficient
from models import Agent, Resource

class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.num_resources = 3
        self.agents = [Agent(i) for i in range(5)]
        self.resources = [Resource(i) for i in range(self.num_resources)]

    def test_update_resource_prices(self):
        update_resource_prices(self.resources)
        for resource in self.resources:
            self.assertGreater(resource.price, 0)

    def test_get_resource_prices(self):
        prices = get_resource_prices(self.resources)
        self.assertEqual(len(prices), self.num_resources)
        self.assertIsInstance(prices, np.ndarray)

    def test_get_resource_availability(self):
        availability = get_resource_availability(self.resources)
        self.assertEqual(len(availability), self.num_resources)
        self.assertIsInstance(availability, np.ndarray)

    def test_allocate_and_deallocate_resources(self):
        agent = self.agents[0]
        resource = self.resources[0]
        amount = 10
        resource.allocate(amount)
        self.assertEqual(resource.current_load, amount)
        deallocate_resources(self.resources)
        self.assertLessEqual(resource.current_load, amount)

    def test_regenerate_resources(self):
        initial_capacity = self.resources[0].capacity
        regenerate_resources(self.resources, 100)
        self.assertGreaterEqual(self.resources[0].capacity, initial_capacity)

    def test_adjust_agent_needs(self):
        initial_needs = self.agents[0].resource_demand_preference.copy()
        adjust_agent_needs(self.agents)
        self.assertFalse(np.array_equal(self.agents[0].resource_demand_preference, initial_needs))

    def test_add_agent_income_and_expense(self):
        initial_balance = self.agents[0].ctx_balance
        add_agent_income(self.agents, 1)
        self.assertGreater(self.agents[0].ctx_balance, initial_balance)
        add_agent_expense(self.agents)
        self.assertLess(self.agents[0].ctx_balance, self.agents[0].ctx_balance + 1)

    def test_check_agent_bankruptcies(self):
        self.agents[0].ctx_balance = -100
        bankrupt_agents = check_agent_bankruptcies(self.agents)
        self.assertEqual(len(bankrupt_agents), 1)
        self.assertTrue(self.agents[0].is_bankrupt)

    def test_tax_and_redistribute_wealth(self):
        initial_balance = self.agents[0].ctx_balance
        tax_rate = 0.1
        total_taxes = tax_agents(self.agents, tax_rate, self.resources)
        self.assertGreater(total_taxes, 0)
        redistribute_wealth(self.agents, total_taxes, self.resources)
        self.assertAlmostEqual(self.agents[0].ctx_balance, initial_balance * (1 - tax_rate) + (total_taxes / len(self.agents)))

    def test_adjust_resource_capacity(self):
        initial_capacity = self.resources[0].capacity
        adjust_resource_capacity(self.resources, 100)
        self.assertGreaterEqual(self.resources[0].capacity, initial_capacity)

    def test_get_agent_balances(self):
        balances = get_agent_balances(self.agents)
        self.assertEqual(len(balances), len(self.agents))
        self.assertIsInstance(balances, list)

    def test_get_total_economic_output(self):
        output = get_total_economic_output(self.agents, self.resources)
        self.assertGreater(output, 0)

    def test_calculate_gini_coefficient(self):
        balances = [10, 20, 30]
        gini = calculate_gini_coefficient(balances)
        self.assertGreaterEqual(gini, 0)
        self.assertLessEqual(gini, 1)

    def test_get_resource_load_and_prices(self):
        prices, loads = get_resource_load_and_prices(self.resources)
        self.assertEqual(len(prices), len(self.resources))
        self.assertEqual(len(loads), len(self.resources))

if __name__ == '__main__':
    unittest.main()