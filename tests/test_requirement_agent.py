from src.agents.requirement_agent import RequirementAgent


def test_requirement_agent_analyze():
    agent = RequirementAgent()

    result = agent.analyze("The system should allow users to upload requirements.")

    assert result["requirement"] == "The system should allow users to upload requirements."
    assert result["length"] > 0
    assert result["has_requirement"] is True
