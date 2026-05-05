import os
import socket
from typing import Any

import requests
import whois
import dns.resolver
from dotenv import load_dotenv

load_dotenv()


def brave_search(query: str, count: int = 5) -> dict[str, Any]:
    api_key = os.getenv("BRAVE_API_KEY")

    if not api_key:
        return {
            "tool": "brave_search",
            "status": "skipped",
            "reason": "BRAVE_API_KEY is not configured",
            "query": query,
            "results": []
        }

    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": api_key
    }
    params = {
        "q": query,
        "count": count
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("web", {}).get("results", []):
            results.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "description": item.get("description")
            })

        return {
            "tool": "brave_search",
            "status": "ok",
            "query": query,
            "results": results
        }
    except Exception as e:
        return {
            "tool": "brave_search",
            "status": "error",
            "query": query,
            "error": str(e),
            "results": []
        }


def whois_lookup(domain: str) -> dict[str, Any]:
    try:
        data = whois.whois(domain)

        return {
            "tool": "whois_lookup",
            "status": "ok",
            "domain": domain,
            "registrar": str(data.registrar),
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "name_servers": data.name_servers,
            "emails": data.emails,
            "raw": str(data)
        }

    except Exception as e:
        return {
            "tool": "whois_lookup",
            "status": "error",
            "domain": domain,
            "error": str(e)
        }


def dns_lookup(domain: str) -> dict[str, Any]:
    records = {}

    for record_type in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(answer) for answer in answers]
        except Exception:
            records[record_type] = []

    return {
        "tool": "dns_lookup",
        "status": "ok",
        "domain": domain,
        "records": records
    }


def ip_lookup(domain: str) -> dict[str, Any]:
    try:
        _, _, ips = socket.gethostbyname_ex(domain)

        return {
            "tool": "ip_lookup",
            "status": "ok",
            "domain": domain,
            "ips": ips
        }

    except Exception as e:
        return {
            "tool": "ip_lookup",
            "status": "error",
            "domain": domain,
            "error": str(e)
        }


def run_tools(subject):
    evidence = []

    looks_like_domain = "." in subject and " " not in subject

    if looks_like_domain:
        evidence.append(dns_lookup(subject))
        evidence.append(ip_lookup(subject))
        evidence.append(whois_lookup(subject))
        evidence.append(brave_search(subject))
        evidence.append(brave_search(f"{subject} security incident OR scam OR malware OR breach"))
    else:
        evidence.append(brave_search(subject))
        evidence.append(brave_search(f"{subject} security incident OR scam OR fraud OR breach"))

    return evidence
