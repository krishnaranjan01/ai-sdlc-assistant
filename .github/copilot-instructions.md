# AI SDLC Assistant - Copilot Instructions

## Project Purpose

This project is an AI-powered SDLC Assistant.

The system takes a software requirement and helps convert it into SDLC artifacts such as:

- Requirement Analysis
- Clarification Questions
- User Stories
- Architecture
- API Specification
- Database Design
- QA Test Cases
- Final Review Report

The goal is to demonstrate a practical multi-agent AI software development workflow.

---

## MVP Agents

The MVP will contain five specialized agents:

1. Requirement Analyst Agent
2. User Story Agent
3. Architect Agent
4. API + Database Agent
5. QA / Reviewer Agent

Each agent must have a clearly defined responsibility.

Do not make one agent responsible for the entire SDLC.

---

## Agent Communication

Agents should not directly depend on each other's implementation.

The system will use a shared project state and an orchestrator.

Conceptually:

User
↓
FastAPI
↓
Agent Orchestrator
↓
Specialized Agent
↓
Shared Project State
↓
Next Agent

Use structured outputs between agents.

---

## Technology Direction

Current technology direction:

- Python
- OpenAI
- FastAPI
- React
- PostgreSQL
- CrewAI for agent orchestration
- PyMuPDF for PDF processing
- python-docx for DOCX processing
- Pytest for testing
- GitHub for source control
- Docker for deployment

Do not introduce every technology at the beginning.

Add dependencies incrementally when they are required.

---

## Document Input

The system must support:

- PDF
- DOCX
- TXT

Maximum upload size:

5 MB

The document-processing layer must:

1. Validate file type.
2. Validate file size.
3. Extract text.
4. Return clean text to the Requirement Analyst.

Do not send raw files directly to agents unless explicitly required.

---

## Development Order

Build the system in this order:

1. Document ingestion
2. Requirement Analyst Agent
3. Structured requirement output
4. Clarification workflow
5. User Story Agent
6. Architect Agent
7. API + Database Agent
8. QA / Reviewer Agent
9. Agent Orchestrator
10. PostgreSQL persistence
11. RAG / Knowledge Base
12. FastAPI APIs
13. React UI
14. Docker / deployment

Do not skip ahead unless explicitly requested.

---

## Current Development Status

Already completed:

- Git repository
- GitHub branch
- Python virtual environment
- `.env` configuration
- `.gitignore`
- `requirements.txt`
- OpenAI API connectivity test

The next development task is:

Document ingestion supporting PDF, DOCX and TXT files up to 5 MB.

---

## Security Rules

Never hardcode API keys.

Never commit `.env`.

Use environment variables for secrets.

`.env.example` may contain placeholder values but must never contain real credentials.

Do not print API keys in logs or responses.

---

## Coding Guidelines

Keep the code simple and readable.

Prefer small modules with one responsibility.

Do not create unnecessary abstractions.

Do not introduce unnecessary dependencies.

Use type hints where practical.

Add tests for important functionality.

Do not mix UI logic with business logic.

Do not put LLM calls directly into unrelated modules.

Keep agent instructions/prompts separate from reusable infrastructure where practical.

---

## AI / LLM Guidelines

The LLM is a capability used by the agents.

Do not describe the LLM itself as an agent.

An agent should have:

- A clear role
- A clear goal
- Defined input
- Defined output
- Limited responsibility

Do not assume information that is missing from the requirement.

When information is missing, identify it explicitly and ask clarification questions.

Prefer structured outputs for data that will be consumed by another agent.

---

## MVP Scope

The MVP should focus on:

Requirement
→ Analysis
→ Clarification
→ User Stories
→ Architecture
→ API / Database
→ QA
→ Review
→ Final Report

The following are future enhancements unless specifically included:

- Production deployment
- Advanced enterprise authentication
- Complex autonomous coding
- Automatic production deployment
- Large-scale distributed execution
- Advanced long-term memory
- Extensive enterprise RAG
- Fully autonomous software development

---

## Important Development Rule

Work incrementally.

Before implementing a new module:

1. Understand its purpose.
2. Define its input.
3. Define its output.
4. Implement the smallest working version.
5. Test it.
6. Explain why it exists.
7. Then integrate it with the next module.

Do not generate the entire project at once.

The developer should be able to understand and demonstrate every major component.
