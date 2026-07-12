"""Planner node (Task 1.2).

TODO: Implement `make_planner(llm)` returning a node that:
  - reads the user question from state["messages"],
  - asks the LLM (PLANNER_PROMPT) for a JSON list of 2-5 steps,
  - parses it robustly (fallback to a single step on parse failure),
  - returns {"plan": [...], "current_step_index": 0, "step_results": []}.
"""

from __future__ import annotations

from agent.state import AnalystState


def make_planner(llm):
    def planner(state: AnalystState) -> dict:
        user_question = state["messages"][-1].content
        response = (
            llm.invoke([
                ("system", "Break down the user's question into 2-5 atomic steps. Return only a JSON list of strings."),
                ("user", user_question)
            ])
        )

        state["plan"] = response[0].content
        
    


    return planner
