import numpy as np
import random
from constants import DEALLOCATION_RATE, TAX_RATE
from models import Agent
from typing import List, Tuple, Dict, Any

def update_resource_prices(resources: List[Any]) -> None:
    """Updates the prices of all resources."""
    for resource in resources:
        resource.update_price()

def get_resource_prices(resources: List[Any]) -> np.ndarray:
    """Returns an array of resource prices."""
    return np.array([r.price for r in resources])

def get_resource_availability(resources: List[Any]) -> np.ndarray:
    """Returns an array of resource availability."""
    return np.array([r.capacity - r.current_load for r in resources])

def get_agent_requests(agents: List[Agent], resource_prices: np.ndarray, resource_availability: np.ndarray) -> List[Tuple[Agent, int, float]]:
    """
    Gets resource requests from agents.

    Args:
        agents (List[Agent]): List of agents.
        resource_prices (np.ndarray): Array of resource prices.
        resource_availability (np.ndarray): Array of resource availability.

    Returns:
        List[Tuple[Agent, int, float]]: List of agent requests.
    """
    active_agents = [agent for agent in agents if not agent.is_bankrupt]
    all_requests = []
    for agent in active_agents:
        agent_requests = agent.request_resources(resource_prices, resource_availability)
        all_requests.extend([(agent, resource_id, amount) for resource_id, amount in agent_requests])
    random.shuffle(all_requests)
    return all_requests

def allocate_resources(resources: List[Any], requests: List[Tuple[Agent, int, float]]) -> None:
    """Allocates resources to agents based on their requests."""
    for agent, resource_id, amount in requests:
        resource = resources[resource_id]
        allocated = resource.allocate(amount)
        cost = allocated * resource.price
        if agent.ctx_balance >= cost:
            agent.ctx_balance -= cost

def deallocate_resources(resources: List[Any]) -> None:
    """Deallocates resources based on the deallocation rate."""
    for resource in resources:
        deallocate_amount = resource.current_load * DEALLOCATION_RATE
        resource.deallocate(deallocate_amount)

def regenerate_resources(resources: List[Any], avg_agent_balance: float) -> None:
    """Regenerates resources based on the average agent balance."""
    for resource in resources:
        resource.regenerate(avg_agent_balance)

def adjust_agent_needs(agents: List[Agent]) -> None:
    """Adjusts the needs of all agents."""
    for agent in agents:
        agent.adjust_needs()

def adjust_agent_demand_multiplier(agents: List[Agent], step_num: int) -> None:
    """Adjusts the demand multiplier of all agents."""
    for agent in agents:
        agent.adjust_demand_multiplier(step_num)

def add_agent_income(agents: List[Agent], avg_resource_price: float) -> None:
    """Adds income to all agents."""
    for agent in agents:
        agent.add_income(avg_resource_price)

def add_agent_expense(agents: List[Agent]) -> None:
    """Adds expense to all agents."""
    for agent in agents:
        agent.add_expense()

def check_agent_bankruptcies(agents: List[Agent]) -> List[Agent]:
    """Checks for agent bankruptcies and returns a list of bankrupt agents."""
    bankrupt_agents = []
    for agent in agents:
        if agent.check_bankrupt():
            bankrupt_agents.append(agent)
    return bankrupt_agents

def tax_agents(agents: List[Agent], tax_rate: float, resources: List[Any]) -> float:
    """Taxes agents and returns the total taxes collected."""
    total_taxes = 0
    for agent in agents:
        tax_amount = agent.ctx_balance * tax_rate
        agent.tax(tax_amount)
        total_taxes += tax_amount
    return total_taxes

def redistribute_wealth(agents: List[Agent], total_taxes: float, resources: List[Any]) -> None:
    """Redistributes wealth among agents."""
    active_agents = [agent for agent in agents if not agent.is_bankrupt]
    if len(active_agents) > 0:
        redistribution_per_agent = total_taxes / len(active_agents)
        for agent in active_agents:
            agent.ctx_balance += redistribution_per_agent

def adjust_resource_capacity(resources: List[Any], total_economic_output: float) -> None:
    """Adjusts the capacity of resources based on the total economic output."""
    for resource in resources:
        resource.adjust_capacity(total_economic_output)

def get_agent_balances(agents: List[Agent]) -> List[float]:
    """Returns a list of agent balances."""
    return [agent.ctx_balance for agent in agents]

def get_resource_load_and_prices(resources: List[Any]) -> Tuple[List[float], List[float]]:
    """Returns a tuple of resource prices and loads."""
    return [r.price for r in resources], [r.current_load for r in resources]

def get_total_economic_output(agents: List[Agent], resources: List[Any]) -> float:
    """Calculates the total economic output."""
    total_balances = sum(get_agent_balances(agents))
    resource_prices = get_resource_prices(resources)
    resource_load, _ = get_resource_load_and_prices(resources)
    total_resource_value = sum(resource_prices * resource_load)
    return total_balances + total_resource_value

def calculate_gini_coefficient(balances: List[float]) -> float:
    """Calculates the Gini coefficient."""
    balances = sorted(balances)
    n = len(balances)
    if n < 2:
        return 0.0
    numerator = sum((i + 1) * balance for i, balance in enumerate(balances)) - sum((n - i) * balance for i, balance in enumerate(balances))
    denominator = n * sum(balances)
    return numerator / denominator if denominator else 0.0