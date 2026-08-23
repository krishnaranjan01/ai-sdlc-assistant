# AI SDLC Assistant - Local Setup Guide

This guide is for a developer who has checked out the project from GitHub and opened the project folder in VS Code.

Follow the steps in order.

The goal is to get the project running locally.

---

## Step 1 - Open the Project in VS Code

After checking out the project from GitHub:

1. Open VS Code.
2. Select:

   File → Open Folder

3. Select the `AI-SDLC-ASSISTANT` project folder.

You should see the project structure in the VS Code Explorer.

---

## Step 2 - Open the VS Code Terminal

In VS Code select:

Terminal → New Terminal

Make sure the terminal is opened inside the project root.

You should be in:

    AI-SDLC-ASSISTANT

You can verify with:

    pwd

or on Windows PowerShell:

    Get-Location

---

## Step 3 - Verify Python

The project requires Python 3.12.

Run:

    python --version

Expected:

    Python 3.12.x

If Python 3.12 is not installed, install Python 3.12 before continuing.

---

## Step 4 - Create the Virtual Environment

From the project root run:

    python -m venv venv

This creates:

    venv/

The virtual environment is local to your machine and should not be committed to Git.

---

## Step 5 - Activate the Virtual Environment

### Windows PowerShell

Run:

    .\venv\Scripts\Activate.ps1

After successful activation, you should see:

    (venv)

at the beginning of the terminal.

Example:

    (venv) PS C:\...\AI-SDLC-ASSISTANT>

### Windows CMD

Run:

    venv\Scripts\activate

---

## Step 6 - Select the Python Interpreter in VS Code

This step is important.

In VS Code:

1. Press:

   Ctrl + Shift + P

2. Search:

   Python: Select Interpreter

3. Select the Python interpreter from:

    venv

On Windows it will normally look similar to:

    venv\Scripts\python.exe

After selecting it, VS Code should use the project's virtual environment.

---

## Step 7 - Install Project Dependencies

Make sure `(venv)` is visible in the terminal.

Run:

    pip install -r requirements.txt

Wait until installation completes successfully.

---

## Step 8 - Create the Local Environment File

The repository contains:

    .env.example

Create your local `.env` file.

On Windows PowerShell:

    Copy-Item .env.example .env

The project should now contain:

    .env
    .env.example

---

## Step 9 - Add Your OpenAI API Key

Open:

    .env

Add your own OpenAI API key:

    OPENAI_API_KEY=your_openai_api_key_here

Replace the placeholder with your real API key.

Important:

Never commit `.env`.

Never share your API key.

`.env.example` is the file that is committed to GitHub.

`.env` is local to each developer.

---

## Step 10 - Verify the Environment File

Make sure `.env` contains:

    OPENAI_API_KEY=your_actual_key

Do not put quotes around the key unless the project specifically requires them.

---

## Step 11 - Run the OpenAI Connection Test

The project contains:

    tests/test_openai.py

Run:

    python tests/test_openai.py

The purpose of this test is only to confirm that:

    VS Code
       ↓
    Python
       ↓
    .env
       ↓
    OpenAI API
       ↓
    Response

is working.

If the test returns a successful response, the OpenAI configuration is ready.

---

## Step 12 - Run the Application

The current application entry point is:

    src/main.py

Run:

    python src/main.py

If the application starts successfully, the basic local project setup is complete.

---

## Step 13 - Verify the Project Is Ready

At this point verify:

- Python 3.12 is working.
- Virtual environment is active.
- VS Code is using the `venv` interpreter.
- Dependencies are installed.
- `.env` exists.
- OpenAI API key is configured.
- OpenAI connection test passes.
- `src/main.py` runs successfully.

If all of the above work:

    PROJECT SETUP COMPLETE

---

## Important

Do not create another virtual environment if `venv/` already exists.

Do not commit:

    .env
    venv/

Do not change project dependencies unless required.

Do not modify the project architecture during initial setup.

After the project is successfully running, read:

    README.md

and:

    .github/copilot-instructions.md

Then proceed with the current development task.

---

## Current Development Task

The next development task is:

    Document Ingestion

The document ingestion module will support:

    PDF
    DOCX
    TXT

Maximum file size:

    5 MB
