# AI SDLC Assistant - Development Plan

This document tracks the implementation order and current development status of the AI SDLC Assistant.

The project will be built incrementally.

Do not build the complete system at once.

Each phase should be completed, tested and understood before moving to the next major phase.

---

## 1. Development Strategy

Our development approach is:

Understand
    ↓
Plan
    ↓
Implement
    ↓
Test
    ↓
Demonstrate
    ↓
Commit
    ↓
Move to next phase

Each feature should be small enough that the team can explain:

- Why it exists.
- What input it receives.
- What output it produces.
- How it works.
- How it is tested.
- How it connects to the rest of the system.

---

## 2. Current Status

### Completed

- GitHub repository
- Project baseline branch
- Python 3.12 environment
- VS Code project setup
- .env configuration
- .env.example
- .gitignore
- requirements.txt
- OpenAI API connectivity test
- GitHub Copilot instructions
- README.md
- SETUP.md
- PROJECT_BLUEPRINT.md

### Currently Working On

Document Ingestion

### Next

Requirement Analyst Agent

---

## 3. Phase 1 - Project Foundation

Status:

COMPLETED

Objective:

Create a clean and shareable project foundation.

Completed:

- Git repository
- Branch structure
- Python virtual environment
- requirements.txt
- .env
- .env.example
- .gitignore
- OpenAI connectivity test
- README
- Setup guide
- Copilot instructions

Expected result:

A new developer can checkout the project, open it in VS Code and run the basic OpenAI test.

---

## 4. Phase 2 - Document Ingestion

Status:

CURRENT

Objective:

Allow the application to receive software requirement documents.

Supported formats:

- PDF
- DOCX
- TXT

Maximum size:

5 MB

Implementation flow:

File
    ↓
Validate File Size
    ↓
Validate File Type
    ↓
Extract Text
    ↓
Clean Text
    ↓
Return Requirement Text

Technologies:

- PyMuPDF
- python-docx
- Python standard library for TXT

Expected result:

We can give the system a PDF, DOCX or TXT requirement document and successfully extract its text.

Testing should include:

- Valid PDF
- Valid DOCX
- Valid TXT
- Unsupported file type
- File larger than 5 MB
- Empty document
- Document with multiple pages

---

## 5. Phase 3 - Requirement Analyst Agent

Status:

NEXT

Objective:

Create the first real AI agent.

Input:

Clean requirement text.

Output:

Structured requirement analysis containing:

- Business objective
- Actors
- Functional requirements
- Non-functional requirements
- Business rules
- Assumptions
- Missing information

Basic flow:

Requirement Text
    ↓
Requirement Analyst Agent
    ↓
OpenAI
    ↓
Structured Analysis

Expected result:

The agent can analyze a real requirement document instead of a hardcoded string.

---

## 6. Phase 4 - Structured Requirement Output

Status:

PLANNED

Objective:

Ensure the Requirement Analyst returns predictable structured data.

Example structure:

project_id
business_objective
actors
functional_requirements
non_functional_requirements
business_rules
assumptions
missing_information

The output should be machine-readable so future agents can consume it.

Expected result:

The User Story Agent can consume the Requirement Analyst output without parsing uncontrolled natural-language text.

---

## 7. Phase 5 - Clarification Workflow

Status:

PLANNED

Objective:

Allow the system to identify missing information and ask the user clarification questions.

Flow:

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
Updated Context
    ↓
Requirement Analyst
    ↓
Validated Requirement

Expected result:

The system does not simply guess missing requirements.

It asks the user for important missing information before continuing.

---

## 8. Phase 6 - User Story Agent

Status:

PLANNED

Objective:

Convert validated requirements into user stories.

Input:

- Requirement analysis
- Clarification answers

Output:

- Epics
- User stories
- Acceptance criteria

Example:

As a customer,
I want to transfer money to a beneficiary,
so that I can send money from my account.

Acceptance criteria:

- Beneficiary must be valid.
- Account balance must be sufficient.
- Transfer amount must be positive.
- Successful transfer must generate confirmation.

Expected result:

Requirements become structured development-ready user stories.

---

## 9. Phase 7 - Architect Agent

Status:

PLANNED

Objective:

Generate the high-level technical architecture.

Input:

- Requirement analysis
- User stories

Output:

- Components
- Services
- Communication flow
- External systems
- Technology recommendations
- Important architectural decisions

Expected result:

The team receives a technical architecture based on the analyzed requirements.

---

## 10. Phase 8 - API + Database Agent

Status:

PLANNED

Objective:

Translate requirements and architecture into API and database design.

Output:

API:

- Endpoint
- HTTP method
- Request
- Response
- Validation
- Error handling

Database:

- Entities
- Tables
- Columns
- Relationships
- Primary keys
- Foreign keys
- Indexes

Expected result:

The generated API and database design should align with the requirement and architecture.

---

## 11. Phase 9 - QA / Reviewer Agent

Status:

PLANNED

Objective:

Validate the generated SDLC artifacts.

Responsibilities:

- Generate test scenarios.
- Generate test cases.
- Check requirement coverage.
- Find inconsistencies.
- Find missing requirements.
- Check cross-artifact consistency.

Example:

Requirement says:

Customer can transfer money.

QA should verify that:

- Transfer API exists.
- Transfer-related user story exists.
- Database supports the transfer.
- Architecture supports the transfer.
- Test cases cover successful transfer.
- Test cases cover insufficient balance.
- Test cases cover invalid beneficiary.

Expected result:

The system identifies gaps before development begins.

---

## 12. Phase 10 - Agent Orchestrator

Status:

PLANNED

Objective:

Connect the individual agents into a controlled workflow.

Initial flow:

Requirement
    ↓
Requirement Agent
    ↓
Clarification
    ↓
User Story Agent
    ↓
Architect Agent
    ↓
API + DB Agent
    ↓
QA / Reviewer

The orchestrator should control:

- Agent order
- Agent input
- Agent output
- Error handling
- Project state
- Workflow status

The first implementation should remain simple and easy to understand.

CrewAI or LangGraph can be introduced if they provide clear value.

---

## 13. Phase 11 - PostgreSQL

Status:

PLANNED

Objective:

Persist projects and generated artifacts.

Expected entities:

- Project
- Requirement
- Agent Execution
- Requirement Analysis
- Clarification
- User Story
- Architecture
- API Specification
- Database Design
- QA Result
- Review

Expected result:

A user can close the application and later reopen the project and its generated artifacts.

---

## 14. Phase 12 - RAG / Knowledge Base

Status:

PLANNED

Objective:

Allow agents to use organizational or project-specific knowledge.

Possible documents:

- Architecture guidelines
- API standards
- Security standards
- Coding standards
- Existing documentation

Flow:

Knowledge Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retrieve Relevant Context
    ↓
Agent
    ↓
LLM

Expected result:

The AI produces outputs aligned with the organization's existing standards.

---

## 15. Phase 13 - FastAPI Backend

Status:

PLANNED

Objective:

Expose the SDLC workflow through backend APIs.

Initial API areas:

Project management

Requirement upload

Analysis

Clarification

Artifacts

Review

Report

Example endpoints:

POST /projects

POST /projects/{project_id}/requirements

POST /projects/{project_id}/analysis/start

GET /projects/{project_id}

GET /projects/{project_id}/results

POST /projects/{project_id}/review

GET /projects/{project_id}/report

Expected result:

The complete SDLC workflow can be triggered and consumed through APIs.

---

## 16. Phase 14 - React UI

Status:

PLANNED

Objective:

Create a simple user-friendly interface.

Main screens:

1. Project creation
2. Requirement upload
3. Analysis progress
4. Requirement analysis
5. Clarification questions
6. User stories
7. Architecture
8. API
9. Database
10. QA
11. Review
12. Final report

The UI should show the progress of the agents.

Example:

Requirement Analyst     ✓
User Story Agent         ✓
Architect Agent          ●
API / DB Agent           ○
QA / Reviewer            ○

Expected result:

A user can operate the complete system without using the command line.

---

## 17. Phase 15 - Docker and Deployment

Status:

PLANNED

Objective:

Make the application easy to run consistently.

Expected components:

- React container
- FastAPI container
- PostgreSQL container
- Supporting services where required

Docker Compose may be used for local development.

Deployment will be handled after the application is stable.

---

## 18. Final MVP Flow

The MVP should demonstrate:

User
    ↓
Upload Requirement
    ↓
Document Processing
    ↓
Requirement Analyst
    ↓
Clarification
    ↓
User Story Agent
    ↓
Architect Agent
    ↓
API + Database Agent
    ↓
QA / Reviewer
    ↓
Final Review
    ↓
Final SDLC Report

---

## 19. Definition of Done

A phase is not complete just because the code works.

Each major phase should have:

- Working implementation
- Unit tests
- Clear input/output
- Basic error handling
- Documentation where required
- Demonstration
- Git commit
- Code review where applicable

The team should be able to explain the feature before moving to the next major phase.

---

## 20. Current Immediate Plan

We will NOT start by building all five agents.

We will proceed in baby steps.

Current sequence:

STEP 1

Document ingestion foundation.

STEP 2

Test PDF, DOCX and TXT extraction.

STEP 3

Connect extracted requirement text to Requirement Analyst Agent.

STEP 4

Test Requirement Analyst with a real requirement.

STEP 5

Make the agent output structured data.

STEP 6

Add clarification questions.

Then continue with:

User Story
→ Architecture
→ API/DB
→ QA
→ Orchestrator
→ Database
→ RAG
→ Backend
→ UI
→ Deployment

---

## 21. Current Immediate Task

The only development task we should focus on right now is:

DOCUMENT INGESTION

Requirements:

- PDF support
- DOCX support
- TXT support
- 5 MB maximum
- File validation
- Text extraction
- Basic tests

Once this is working and demonstrated, we move to the Requirement Analyst Agent.

---

## 22. Project Success Criteria

The final project should demonstrate that:

1. A user can upload a real software requirement.
2. The system can understand the requirement.
3. The system can identify missing information.
4. The user can provide clarification.
5. AI agents can convert the requirement into SDLC artifacts.
6. Agents can use outputs from previous agents.
7. The system can identify inconsistencies.
8. The generated artifacts remain traceable to the original requirement.
9. The user can review the generated results.
10. The user can export a final SDLC report.

The goal is not simply to demonstrate multiple AI agents.

The goal is to demonstrate a meaningful AI-assisted SDLC workflow.
