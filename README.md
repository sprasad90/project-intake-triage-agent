# Project Intake & Triage Agent

An AI-powered agent that automates the first pass of project intake reading, incoming project requests, categorizing them, assigning a priority level, and explaining its reasoning, using the Anthropic Claude API.

## The Problem

Every organization deals with a steady stream of incoming requests, bug reports, feature asks, security issues, process improvement ideas arriving in inconsistent formats from different requesters. Someone has to read each one and make a judgment call: how urgent is this, what category does it belong to, and what's the risk of letting it sit. That first-pass triage is repetitive, time consuming, and easy to do inconsistently across a busy intake queue.

This project automates that first pass using an LLM, so a human reviewer starts from a structured, reasoned first opinion instead of a blank inbox.

## What It Does

Given a batch of project requests (currently read from a CSV), the agent:
- **Categorizes** each request (Bug, Feature Request, Security Issue, Process Improvement, or Other)
- **Assigns a priority level** (Critical, High, Medium, Low)
- **Explains its reasoning** in one sentence, so the output is auditable, not just a black-box label

## Example Output

\```
--- Request #1: Mobile app crash on login ---
Category: Bug
Priority: Critical
Reasoning: The crash affects a significant portion of the active user base (15%)
and completely blocks access to core functionality (login), making the app
unusable for those users.

--- Request #4: Data breach in customer export tool ---
Category: Security Issue
Priority: Critical
Reasoning: Exposure of Social Security Numbers constitutes a severe data breach
with immediate legal, regulatory, and reputational risks that requires urgent
remediation.
\```

## Tech Stack

- Python 3.14
- [Anthropic Claude API](https://docs.claude.com) (`claude-sonnet-4-5`)
- CSV-based intake (current version)


## Roadmap

- [x] **Phase 1** — Core intake and triage logic (this version)
- [ ] **Phase 2** — Risk Heat Map: a visual view of open requests by risk level
- [ ] **Phase 3** — Release Readiness module: surface whether outstanding requests indicate readiness (or risk) ahead of a release
- [ ] **Phase 4** — Move from CSV input to a more realistic intake format (e.g., form submissions or a lightweight database)

## Running It Locally

\```bash
# Clone the repo
git clone https://github.com/sprasad90/project-intake-triage-agent.git
cd project-intake-triage-agent

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install anthropic

# Set your API key (get one at console.anthropic.com)
export ANTHROPIC_API_KEY="your-key-here"

# Run it
python3 triage_agent.py
\```
