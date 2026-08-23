class RequirementAgent:

    def analyze(self, requirement: str):
        requirement = requirement.strip()

        return {
            "requirement": requirement,
            "length": len(requirement),
            "has_requirement": bool(requirement)
        }
