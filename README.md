# AI SDLC Assistant

AI-powered multi-agent assistant that helps convert software requirements into SDLC artifacts.

## 1. What Are We Building?

We are building a virtual AI software-development team.

A user provides a software requirement through text or by uploading a PDF, DOCX or TXT document.

The system analyzes the requirement and generates useful SDLC artifacts.

### High-Level Flow

User
↓
React UI
↓
FastAPI
↓
Agent Orchestrator
↓
Specialized AI Agents
↓
OpenAI LLM
↓
SDLC Artifacts
↓
Review
↓
Final Report

---

## 2. Problem We Are Solving

Software development involves multiple teams and repeated handoffs:

Business Analyst → Architect → Developer → QA

Requirements can be incomplete, unclear or inconsistent.

The AI SDLC Assistant helps automate the initial SDLC work and provides a common starting point for the team.

---

## 3. What Will The System Produce?

From one requirement, the system can produce:

- Requirement Analysis
- Clarification Questions
- User Stories
- Acceptance Criteria
- High-Level Architecture
- REST API Specification
- Database Design
- QA Test Cases
- Review / Validation Report
- Final SDLC Report

---

## 4. MVP Agents

The MVP contains five specialized agents.

### 1. Requirement Analyst Agent

Understands the requirement and identifies:

- Actors
- Functional requirements
- Non-functional requirements
- Business rules
- Assumptions
- Missing information

### 2. User Story Agent

Converts validated requirements into:

- Epics
- User Stories
- Acceptance Criteria

### 3. Architect Agent

Creates:

- High-level architecture
- Services/components
- Communication flow
- Technology recommendations

### 4. API + Database Agent

Creates:

- REST API specifications
- Request/response structures
- Database tables
- Relationships
- Important indexes

### 5. QA / Reviewer Agent

Creates:

- Test scenarios
- Test cases
- Requirement coverage
- Consistency checks
- Review findings

---

## 5. How Agents Communicate

Agents do not directly depend on each other's implementation.

The system uses an Agent Orchestrator and shared project state.

Conceptually:

User
↓
Orchestrator
↓
Requirement Agent
↓
Shared Project State
↓
User Story Agent
↓
Shared Project State
↓
Architect Agent
↓
Shared Project State
↓
API / DB Agent
↓
QA / Reviewer

Each agent reads the information it needs and adds its own structured output.

---

## 6. Document Input

The MVP supports:

- PDF
- DOCX
- TXT

Maximum file size:

**5 MB**

Document flow:

File
↓
File validation
↓
Text extraction
↓
Requirement text
↓
Requirement Analyst

The system does not blindly send the uploaded file to the LLM.

---

## 7. Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | Python + FastAPI |
| LLM | OpenAI |
| Agent Orchestration | CrewAI / LangGraph |
| Database | PostgreSQL |
| RAG | Vector Database |
| PDF Processing | PyMuPDF |
| DOCX Processing | python-docx |
| Testing | Pytest |
| Source Control | Git + GitHub |
| Deployment | Docker |

Technologies will be introduced incrementally during development.

---

## 8. Database

PostgreSQL will be used in the full MVP.

It will store information such as:

- Projects
- Requirements
- Agent executions
- Requirement analysis
- User stories
- Architecture
- API specifications
- Database design
- QA results
- Review results

The first prototype does not require the database.

---

## 9. RAG / Knowledge Base

RAG will allow agents to use project or company-specific knowledge.

Possible knowledge:

- Architecture standards
- API standards
- Security guidelines
- Coding standards
- Existing project documentation

RAG will be introduced after the basic multi-agent workflow works.

---

## 10. UI

The React UI will allow users to:

1. Create a project
2. Upload a requirement
3. Start analysis
4. See agent progress
5. View requirement analysis
6. Answer clarification questions
7. View user stories
8. View architecture
9. View APIs
10. View database design
11. View QA results
12. Export the final report

The UI should make the agent workflow visible.

---

## 11. Development Phases

We will build the project incrementally.

### Phase 1
OpenAI connection and project foundation

### Phase 2
Document ingestion

### Phase 3
Requirement Analyst Agent

### Phase 4
Structured requirement output

### Phase 5
Clarification workflow

### Phase 6
User Story Agent

### Phase 7
Architect Agent

### Phase 8
API + Database Agent

### Phase 9
QA / Reviewer Agent

### Phase 10
Agent Orchestrator

### Phase 11
PostgreSQL persistence

### Phase 12
RAG / Knowledge Base

### Phase 13
FastAPI APIs

### Phase 14
React UI

### Phase 15
Docker / Deployment / Final Demo

---

## 12. Current Project Status

Completed:

- GitHub repository
- Git branches
- Python virtual environment
- `.env`
- `.env.example`
- `.gitignore`
- `requirements.txt`
- OpenAI API connectivity test
- Copilot project instructions

### Current task

Build document ingestion supporting:

- PDF
- DOCX
- TXT
- Maximum 5 MB

---

## 13. Project Structure

Current structure:

```text
AI-SDLC-ASSISTANT/
│
├── .github/
│   └── copilot-instructions.md
│
├── src/
│   ├── agents/
│   ├── config/
│   ├── tasks/
│   ├── tools/
│   └── main.py
│
├── tests/
│   └── test_openai.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
