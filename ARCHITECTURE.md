# Architecture Document - Fireblocks Investigation Agent

## 1. Overview

Fireblocks Investigation Agent is a local proof-of-concept AI investigation agent powered by the Claude API.

The goal of the system is to investigate a given subject, such as a person, company, domain, or other entity, and generate a structured investigation report. The agent autonomously collects available evidence from external tools, sends the collected evidence to an LLM for analysis, and produces a final Markdown report.

The project is intentionally lightweight and designed to be completed and reviewed as a small POC. It runs locally from the command line and does not require a database, web server, or complex infrastructure.

Example usage:

```powershell
python main.py --subject example.com