"""Supervisor node + routing edge (Task 1.3).

TODO:
  - `make_supervisor(llm)`: if current_step_index >= len(plan) -> next_agent =
    'synthesizer'; else classify the current step to 'rag_agent' or 'mcp_tools'.
  - `route_from_supervisor(state)`: return state["next_agent"] for the
    conditional edge.
"""

from __future__ import annotations

from agent.state import AnalystState

RAG = "rag_agent"
MCP = "mcp_tools"
SYNTH = "synthesizer"


def make_supervisor(llm):
    def supervisor(state: AnalystState) -> dict:

        if state["current_step_index"] >= len(state["plan"]):
            return {
                "next_agent": SYNTH
            }
        
        current_step = state["plan"][state["current_step_index"]]
        current_step_lower = current_step.lower()

        if any(word in current_step_lower for word in ["find", "retrieve", "look up", "document", "report"]):
            return{
                "next_agent": RAG
            }
        
        if any(word in current_step_lower for word in ["calculate", "compute", "percentage", "growth", "ratio", "compare"]):
            return{
                "next_agent": MCP
            }
        
        return{
            "next_agent": RAG #just fallback to rag if no keywords found
        }

    return supervisor


def route_from_supervisor(state: AnalystState) -> str:
    supervisor_decision = state["next_agent"] 
    return supervisor_decision