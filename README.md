# Fireblocks Investigation Agent

Fireblocks Investigation Agent is a local proof-of-concept AI investigation agent created as part of a **Fireblocks home assignment**.

The goal of the project is to investigate a given subject, such as a person, company, domain, or other entity, collect relevant evidence, and generate a structured investigation report using an LLM.

The project is intentionally lightweight and designed to run locally from the command line.

---

## Architecture

For the full system design, implementation details, current limitations, and future development plan, see:

[ARCHITECTURE.md](ARCHITECTURE.md)

---

## What the Agent Does

The agent accepts a subject and performs a small autonomous investigation flow:

1. Receives a subject from the user.
2. Detects whether the subject looks like a domain or a person/company.
3. Runs relevant tools.
4. Collects evidence.
5. Sends the evidence to an LLM.
6. Generates a structured Markdown investigation report.
7. Saves the report under the `reports/` directory.

#### Examples:

```
python main.py --subject example.com
python main.py --subject "Fireblocks"
python main.py --subject "Elon Musk"
```
## Demo Video

A short demo video is included to show the agent running locally from the command line.

[Watch the demo video](assets/demo.mp4)

The video demonstrates:

- Running the investigation agent locally
- Providing a subject with `--subject`
- Collecting evidence from available tools
- Generating a structured investigation report
- Saving the report under the `reports/` directory


---
## Current Capabilities

The current agent supports:

* Domain investigation
* Person/company investigation
* DNS lookup
* IP resolution
* WHOIS lookup
* Brave Search web search
* Google News search
* NewsData.io search
* Claude API support
* Ollama local model fallback
* Markdown report generation
* Local report storage

### Fireblocks-Investigation-Agent/
```
├── main.py
├── tools.py
├── prompts.py
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── .env.example
├── .gitignore
└── reports/
    └── .gitkeep
    └── reports.md
```

### File Overview

| File             | Purpose                                                             |
|------------------|---------------------------------------------------------------------| 
| main.py          | 	Main CLI entry point and investigation flow                        |
| tools.py         | 	DNS, WHOIS, IP, and web search tools                               |
| prompts.py	      | System and final report prompts                                     |
| requirements.txt | 	Python dependencies                                                |
| README.md        | 	Setup and usage guide                                              |
| ARCHITECTURE.md  | 	Full architecture and design documentation                         |
| .env.example     | 	Example environment variable file                                  |
| .gitignore       | 	Prevents secrets, venv, and generated reports from being committed |
| reports/	        | Stores generated Markdown reports                                   |

### Requirements
* Python 3.10+
* Windows, macOS, or Linux
* Claude API key for Claude mode
* Ollama installed locally for Ollama mode
* Optional Brave Search API key for web search

## Installation
### 1. Clone the repository
```
git clone https://github.com/perzibel/Fireblocks-Investigation-Agent.git
cd Fireblocks-Investigation-Agent
```
### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Create a .env file in the project root.
```
copy .env.example .env
```

## LLM Options

The project supports two LLM modes:

1. Claude API
2. Ollama local model

This allows the project to meet the assignment requirement for Claude API usage while still supporting free local development when Claude API credits are unavailable.

### Option 1: Claude API Mode

Claude is the default LLM provider for the assignment.

Use this when you have available Anthropic API.

In .env:
```
LLM_PROVIDER=claude
ANTHROPIC_API_KEY=your_claude_api_key_here
CLAUDE_MODEL=claude-sonnet-4-6
```

### Option 2: Ollama Local Mode

Ollama mode allows the agent to run locally without paid API credits.


#### Install Ollama

Download and install Ollama from:
```
https://ollama.com/
```
Pull a model:
```
ollama pull llama3.1:8b
```
Test the model:
```
ollama run llama3.1:8b
```
Then configure .env:
```
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.1:8b

ANTHROPIC_API_KEY=
CLAUDE_MODEL=
```


### Choosing Between Claude and Ollama

Change the LLM_PROVIDER value in .env.

Use Claude:
```
LLM_PROVIDER=claude
```
Use Ollama:
```
LLM_PROVIDER=ollama
```

### Important
Dont forget to fill the Brave API and NewsData,io API

## Output

The final report is printed to the terminal and saved under:

```reports/```

#### Example generated file:

reports/provider_example_com_20260505_113000.md

The report includes:

* Subject
* Executive summary
* Key findings
* Evidence collected
* Risk assessment
* Indicators / technical details
* Gaps and limitations
* Recommended next steps
* Final verdict
* Errors