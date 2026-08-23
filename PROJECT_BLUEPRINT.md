# AI SDLC Assistant - Project Blueprint

This document defines what the AI SDLC Assistant is, the problem it solves, its major components, and the high-level architecture.

The purpose of this document is to keep the entire team aligned on the same solution before implementation.

---

## 1. What Are We Building?

We are building an AI-powered multi-agent SDLC Assistant.

The system will take a software requirement provided by a user and help transform it into common software development lifecycle artifacts.

The system acts like a virtual software development team.

The user provides:

- Requirement text
- PDF
- DOCX
- TXT

The system processes the requirement and generates:

- Requirement Analysis
- Clarification Questions
- User Stories
- Acceptance Criteria
- High-Level Architecture
- API Specification
- Database Design
- QA Test Cases
- Review Results
- Final SDLC Report

---

## 2. Problem We Are Solving

In a traditional software project, requirements move through multiple people and teams.

Typical flow:

Business Analyst
    ↓
Architect
    ↓
Developer
    ↓
QA

This creates several problems:

- Requirements may be incomplete.
- Important business rules may be missed.
- Different teams may interpret the same requirement differently.
- Requirements may not be properly converted into user stories.
- Architecture may not fully match the requirement.
- API and database design may miss important requirements.
- QA may not have complete requirement coverage.
- A lot of repetitive SDLC documentation is created manually.

The AI SDLC Assistant aims to reduce this manual effort and provide a consistent starting point for the development team.

---

## 3. Core Idea

The core idea is not to create one large AI chatbot.

Instead, we create multiple specialized AI agents.

Each agent has one responsibility.

For example:

Requirement Agent
    ↓
Understands the requirement

User Story Agent
    ↓
Creates user stories

Architect Agent
    ↓
Creates architecture

API + DB Agent
    ↓
Creates API and database design

QA / Reviewer
    ↓
Creates tests and validates the outputs

An Agent Orchestrator controls the overall workflow.

---

## 4. High-Level Architecture

The expected architecture is:

User
  ↓
React UI
  ↓
FastAPI
  ↓
Agent Orchestrator
  ↓
Specialized Agents
  ↓
OpenAI LLM
  ↓
Project State / Database
  ↓
Review
  ↓
Final SDLC Report

Additional services such as RAG and external tools will be introduced later.

---

## 5. Document Input

The system will support:

- PDF
- DOCX
- TXT

Maximum file size:

5 MB

Document flow:

User Upload
    ↓
File Validation
    ↓
File Type Validation
    ↓
File Size Validation
    ↓
Document Parser
    ↓
Text Extraction
    ↓
Clean Requirement Text
    ↓
Requirement Analyst Agent

The application should not blindly send the uploaded file to the LLM.

The document-processing layer first extracts the relevant text.

---

## 6. MVP Agents

The MVP will contain five specialized agents.

### Agent 1 - Requirement Analyst

Purpose:

Understand and analyze the original requirement.

Responsibilities:

- Identify business objective.
- Identify actors.
- Identify functional requirements.
- Identify non-functional requirements.
- Identify business rules.
- Identify assumptions.
- Identify missing information.
- Generate clarification questions when necessary.

Input:

Requirement text.

Output:

Structured requirement analysis.

---

### Agent 2 - User Story Agent

Purpose:

Convert validated requirements into user stories.

Responsibilities:

- Create epics where required.
- Create user stories.
- Create acceptance criteria.
- Maintain traceability to requirements.

Input:

Validated requirement analysis.

Output:

Structured user stories and acceptance criteria.

---

### Agent 3 - Architect Agent

Purpose:

Create the high-level technical architecture.

Responsibilities:

- Identify major components/services.
- Define communication between components.
- Recommend appropriate technologies.
- Identify external systems.
- Identify important architectural considerations.

Input:

Requirement analysis and user stories.

Output:

High-level architecture.

---

### Agent 4 - API + Database Agent

Purpose:

Translate the requirement and architecture into API and database design.

Responsibilities:

- Define REST APIs.
- Define request structures.
- Define response structures.
- Identify database entities.
- Define tables.
- Define relationships.
- Identify important indexes and constraints.

Input:

Requirement analysis, user stories and architecture.

Output:

API specification and database design.

---

### Agent 5 - QA / Reviewer Agent

Purpose:

Validate the generated SDLC artifacts.

Responsibilities:

- Create test scenarios.
- Create test cases.
- Check requirement coverage.
- Identify inconsistencies.
- Identify missing information.
- Check whether generated artifacts agree with each other.
- Produce review findings.

Input:

All relevant previous artifacts.

Output:

QA test cases and review results.

---

## 7. Agent Orchestrator

The Agent Orchestrator acts like the team lead.

It controls:

- Which agent runs.
- When an agent runs.
- What information is passed to an agent.
- What happens when an agent fails.
- How the workflow progresses.
- How the project state is updated.

Conceptually:

User
  ↓
Orchestrator
  ↓
Requirement Agent
  ↓
Project State
  ↓
User Story Agent
  ↓
Project State
  ↓
Architect Agent
  ↓
Project State
  ↓
API + DB Agent
  ↓
Project State
  ↓
QA / Reviewer

The first implementation should keep orchestration simple and understandable.

CrewAI or LangGraph can be introduced when the workflow requires it.

---

## 8. Shared Project State

Agents should not directly depend on each other's Python implementation.

Instead, they communicate through structured project state.

A simplified project state may contain:

project_id
requirement
analysis
clarification_questions
user_stories
architecture
api_spec
database_schema
qa_results
review_results

Each agent reads the information it needs and adds its own output.

---

## 9. Clarification Workflow

The system should not assume missing information.

If the Requirement Analyst identifies important missing information:

Requirement
    ↓
Requirement Analyst
    ↓
Missing Information
    ↓
Clarification Questions
    ↓
User Answers
    ↓
Updated Requirement Context
    ↓
Requirement Analysis

The system should limit unnecessary clarification questions.

The goal is to obtain enough information to continue the SDLC workflow.

---

## 10. Output Traceability

The system should maintain traceability.

Example:

Requirement
    ↓
Requirement Analysis
    ↓
User Story
    ↓
Architecture
    ↓
API
    ↓
Database
    ↓
QA Test

This allows the team to understand why a generated artifact exists.

It also helps the Reviewer Agent identify missing coverage.

---

## 11. Database

PostgreSQL will be introduced after the basic workflow is working.

The database will eventually store:

- Projects
- Requirements
- Agent executions
- Requirement analysis
- Clarification questions
- User stories
- Architecture
- API specifications
- Database design
- QA results
- Review results

The first prototype does not require PostgreSQL.

Initially, project state can remain in memory or simple local structures.

---

## 12. RAG / Knowledge Base

RAG is a future enhancement.

It will allow the system to use organization-specific knowledge.

Possible knowledge sources:

- Architecture standards
- API standards
- Security standards
- Coding standards
- Existing project documentation
- Internal development guidelines

Conceptual flow:

Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Relevant Context
    ↓
Agent
    ↓
LLM

RAG is not required for the first working prototype.

---

## 13. UI

The final React UI will provide:

### Project Creation

User creates a new SDLC project.

### Requirement Upload

User uploads:

- PDF
- DOCX
- TXT

or enters requirement text directly.

### Analysis

User starts the SDLC analysis.

### Agent Progress

The UI shows which agent is currently running.

Example:

Requirement Analyst       ✓
User Story Agent           ✓
Architect Agent            ●
API / DB Agent             ○
QA / Reviewer              ○

### Artifact Screens

The user can view:

- Requirement Analysis
- Clarification Questions
- User Stories
- Architecture
- API
- Database
- QA
- Review

### Final Report

The user can export the generated SDLC artifacts into a final report.

---

## 14. Backend

FastAPI will provide the backend APIs.

The backend will eventually handle:

- Project creation
- Requirement upload
- Document processing
- Workflow execution
- Agent execution
- Project state
- Artifact retrieval
- Review
- Report generation

Example API structure:

POST /projects

POST /projects/{project_id}/requirements

POST /projects/{project_id}/analysis/start

GET /projects/{project_id}

GET /projects/{project_id}/results

POST /projects/{project_id}/review

GET /projects/{project_id}/report

The exact API design will be finalized during implementation.

---

## 15. Technology Stack

Frontend:

React

Backend:

Python + FastAPI

LLM:

OpenAI

Agent Orchestration:

CrewAI or LangGraph, introduced when required

Database:

PostgreSQL

Document Processing:

PyMuPDF
python-docx

RAG:

Vector database, selected during the RAG phase

Testing:

Pytest

Source Control:

Git + GitHub

Deployment:

Docker

---

## 16. Security

The system must:

- Never hardcode API keys.
- Never commit .env.
- Keep secrets in environment variables.
- Avoid logging sensitive credentials.
- Validate uploaded files.
- Enforce the 5 MB file limit.
- Validate supported file types.
- Keep user/project data isolated.

Additional authentication and authorization will be added during the production phase.

---

## 17. MVP Scope

The MVP should demonstrate the following complete flow:

Requirement
    ↓
Document Processing
    ↓
Requirement Analysis
    ↓
Clarification
    ↓
User Stories
    ↓
Architecture
    ↓
API + Database Design
    ↓
QA
    ↓
Review
    ↓
Final Report

The MVP does not need to autonomously write and deploy production code.

---

## 18. Future Enhancements

Potential future capabilities:

- RAG
- Company knowledge base
- Advanced memory
- Authentication
- Role-based access
- Jira integration
- GitHub integration
- Automatic ticket creation
- Code generation
- Code review
- CI/CD integration
- Cloud deployment
- Advanced observability
- Agent performance monitoring

These are outside the initial MVP.

---

## 19. One-Line Architecture

React UI
    ↓
FastAPI
    ↓
Agent Orchestrator
    ↓
Specialized SDLC Agents
    ↓
OpenAI / Tools / RAG
    ↓
Project State / PostgreSQL
    ↓
Review
    ↓
Final SDLC Report
