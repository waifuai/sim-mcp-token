"""
Manim-based visualization for the agent-based economic simulation.

This module creates animated visualizations of the economic simulation using
the Manim mathematical animation engine. It provides visual representations
of agent behaviors, wealth distributions, and economic dynamics over time.

The animation includes:
- Visual representation of agents with wealth-based coloring
- Real-time wealth updates and position changes
- Agent type categorization and legend
- Step-by-step simulation progression
- Final statistics display
- Economic metrics visualization

This module requires Manim to be installed and is designed to be run
with the Manim command-line interface rather than as a standalone script.
"""
from manim import *
import numpy as np
from src.constants import *
from src.models import Agent, Resource
from src.simulation import run_simulation

class EconomicSimulationScene(Scene):
    def construct(self):
        # Title
        title = Text("Agent-Based Economic Simulation", font_size=36)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Create simulation data
        agents = [Agent(i) for i in range(NUM_AGENTS)]
        resources = [Resource(i) for i in range(NUM_RESOURCES)]

        if INITIAL_IMBALANCE:
            for agent in agents:
                if agent.agent_id < NUM_AGENTS * IMBALANCE_STRENGTH:
                    agent.ctx_balance *= 2
                else:
                    agent.ctx_balance *= 0.5

        # Create visual representations
        agent_circles = VGroup()
        wealth_texts = VGroup()
        legend = VGroup()

        # Colors for different agent types
        colors = [BLUE, GREEN, RED, YELLOW, PURPLE]

        # Create legend
        legend_title = Text("Agent Types:", font_size=20).to_edge(DOWN + LEFT)
        legend.add(legend_title)
        for i, agent_type in enumerate(["Producer", "Consumer", "Trader", "Banker", "Investor"]):
            dot = Dot(color=colors[i], radius=0.1)
            text = Text(agent_type, font_size=16)
            text.next_to(dot, RIGHT)
            legend.add(VGroup(dot, text).arrange(RIGHT).next_to(legend_title, DOWN, buff=0.2).shift(DOWN * i * 0.3))

        # Create agent circles and wealth texts
        for i, agent in enumerate(agents):
            circle = Circle(radius=0.3, color=colors[i % len(colors)], fill_opacity=0.6)
            x_pos = np.random.uniform(-4, 4)
            y_pos = np.random.uniform(-2, 2)
            circle.move_to([x_pos, y_pos, 0])
            agent_circles.add(circle)

            wealth_text = Text(f"${agent.ctx_balance:.0f}", font_size=16)
            wealth_text.next_to(circle, DOWN, buff=0.1)
            wealth_texts.add(wealth_text)

        self.play(Create(agent_circles), Create(wealth_texts), Create(legend))
        self.wait(2)

        # Simulation loop
        for step in range(min(50, SIMULATION_STEPS)):  # Show first 50 steps for animation
            # Update simulation
            from src.simulation import simulation_step
            step_metrics = simulation_step(agents, resources, step, {})

            # Update positions and wealth displays
            animations = []
            for i, (agent, circle, wealth_text) in enumerate(zip(agents, agent_circles, wealth_texts)):
                # Move agents slightly
                current_pos = circle.get_center()
                move_vec = np.random.uniform(-0.5, 0.5, 2)
                new_pos = [np.clip(current_pos[0] + move_vec[0], -6, 6),
                          np.clip(current_pos[1] + move_vec[1], -3, 3),
                          current_pos[2]]
                animations.append(circle.animate.move_to(new_pos))

                # Update wealth text
                new_wealth = Text(f"${agent.ctx_balance:.0f}", font_size=16)
                new_wealth.move_to(wealth_text.get_center())
                animations.append(Transform(wealth_text, new_wealth))

                # Update color based on wealth
                if agent.ctx_balance > 1000:
                    new_color = GREEN
                elif agent.ctx_balance > 500:
                    new_color = YELLOW
                else:
                    new_color = RED
                animations.append(circle.animate.set_color(new_color))

            self.play(*animations, run_time=0.5)

            # Show step counter
            step_text = Text(f"Step: {step + 1}", font_size=24).to_edge(DOWN + RIGHT)
            self.add(step_text)
            self.wait(0.3)
            self.remove(step_text)

        # Final statistics
        self.play(FadeOut(agent_circles), FadeOut(wealth_texts), FadeOut(legend))

        # Show final results
        results_title = Text("Final Results", font_size=36)
        self.play(Write(results_title))
        self.wait(1)

        # Calculate final statistics
        final_wealths = [agent.ctx_balance for agent in agents]
        avg_wealth = np.mean(final_wealths)
        max_wealth = np.max(final_wealths)
        min_wealth = np.min(final_wealths)

        stats = VGroup(
            Text(f"Average Wealth: ${avg_wealth:.2f}", font_size=24),
            Text(f"Max Wealth: ${max_wealth:.2f}", font_size=24),
            Text(f"Min Wealth: ${min_wealth:.2f}", font_size=24),
            Text(f"Total Transactions: {sim.total_transactions}", font_size=24)
        ).arrange(DOWN, buff=0.3)

        self.play(Write(stats))
        self.wait(3)

        # End with thank you
        thank_you = Text("Thank you for watching!", font_size=32)
        self.play(Transform(results_title, thank_you))
        self.play(FadeOut(stats))
        self.wait(2)

if __name__ == "__main__":
    pass  # This file is meant to be run with manim