import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, FINAL_REPORT_PROMPT
from tools import run_tools

load_dotenv()


def call_llm(system_prompt, user_prompt):
    provider = os.getenv("LLM_PROVIDER", "claude").lower()

    if provider == "ollama":
        import ollama

        model = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        return response["message"]["content"]

    if provider == "claude":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        model = os.getenv("CLAUDE_MODEL", "claude-3-5-haiku-latest")

        if not api_key:
            raise ValueError("Missing ANTHROPIC_API_KEY in .env")

        client = Anthropic(api_key=api_key)

        response = client.messages.create(
            model=model,
            max_tokens=2500,
            temperature=0,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
        )

        return response.content[0].text

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")


def make_safe_filename(text):
    safe_text = ""

    for character in text:
        if character.isalnum() or character == "-" or character == "_":
            safe_text += character
        else:
            safe_text += "_"

    return safe_text


def save_report(subject, report):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    provider = os.getenv("LLM_PROVIDER", "claude").lower()

    safe_subject = make_safe_filename(subject)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"{provider}_{safe_subject}_{timestamp}.md"

    with report_path.open("w", encoding="utf-8") as f:
        f.write(report)

    return report_path


def investigate(subject):
    print(f"[+] Starting investigation for: {subject}")
    provider = os.getenv("LLM_PROVIDER", "claude").lower()

    evidence = []
    notes = []

    print("[+] Running investigation tools...")
    tool_results = run_tools(subject)
    evidence.extend(tool_results)

    print(f"[+] Asking {provider} to analyze collected evidence...")

    analysis_prompt = f"""
Subject:
{subject}

Collected evidence:
{json.dumps(evidence, indent=2, ensure_ascii=False)}

Previous notes:
{json.dumps(notes, indent=2, ensure_ascii=False)}

Analyze the evidence and decide:
1. What are the key findings?
2. What risk signals exist?
3. What information is missing?
4. Is this enough for a final report?

Return your answer as concise investigation notes.
"""

    investigation_notes = call_llm(SYSTEM_PROMPT, analysis_prompt)
    notes.append(investigation_notes)

    print("[+] Generating final report...")

    final_prompt = f"""
Subject:
{subject}

Evidence:
{json.dumps(evidence, indent=2, ensure_ascii=False)}

Investigation notes:
{json.dumps(notes, indent=2, ensure_ascii=False)}

{FINAL_REPORT_PROMPT}
"""

    final_report = call_llm(SYSTEM_PROMPT, final_prompt)

    return final_report


def main():
    parser = argparse.ArgumentParser(
        description="Fireblocks Investigation Agent - Claude powered local POC"
    )

    parser.add_argument(
        "--subject",
        required=True,
        nargs="+",
        help="Subject to investigate, for example: example.com, company name, person name"
    )

    args = parser.parse_args()

    subject = " ".join(args.subject)

    report = investigate(subject)
    report_path = save_report(subject, report)

    print("\n========== FINAL REPORT ==========\n")
    print(report)
    print(f"\n[+] Report saved to: {report_path}")


if __name__ == "__main__":
    main()
