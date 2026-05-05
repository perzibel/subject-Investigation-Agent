import os
import socket
import requests
import whois
import dns.resolver
from dotenv import load_dotenv
import time
from urllib.parse import quote_plus
import xml.etree.ElementTree as ET

load_dotenv()


def brave_search(query, count=5):
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
        response = requests.get(url, headers=headers, params=params)
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


def whois_lookup(domain):
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


def dns_lookup(domain):
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


def ip_lookup(domain):
    try:
        a, b, ips = socket.gethostbyname_ex(domain)

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


def google_news_search(query, count=5):
    encoded_query = quote_plus(query)

    url = (
        f"https://news.google.com/rss/search"
        f"?q={encoded_query}"
        f"&hl=en-US"
        f"&gl=US"
        f"&ceid=US:en"
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            return {
                "tool": "google_news_search",
                "status": "rate_limited",
                "query": query,
                "error": "HTTP 429 Too Many Requests",
                "results": []
            }

        response.raise_for_status()

        root = ET.fromstring(response.content)

        articles = []

        channel = root.find("channel")
        if channel is None:
            return {
                "tool": "google_news_search",
                "status": "error",
                "query": query,
                "error": "RSS channel not found in response",
                "results": []
            }

        for item in channel.findall("item")[:count]:
            title = item.findtext("title")
            link = item.findtext("link")
            pub_date = item.findtext("pubDate")
            source = item.find("source")

            articles.append({
                "title": title,
                "link": link,
                "published": pub_date,
                "source": source.text if source is not None else None,
                "source_url": source.attrib.get("url") if source is not None else None
            })

        return {
            "tool": "google_news_search",
            "status": "ok",
            "query": query,
            "results": articles
        }

    except Exception as e:
        return {
            "tool": "google_news_search",
            "status": "error",
            "query": query,
            "error": str(e),
            "results": []
        }


def newsdata_search(query, count=5):
    api_key = os.getenv("NEWSDATA_API_KEY")

    if not api_key:
        return {
            "tool": "newsdata_search",
            "status": "skipped",
            "reason": "NEWSDATA_API_KEY is not configured",
            "query": query,
            "results": []
        }

    url = "https://newsdata.io/api/1/latest"

    params = {
        "apikey": api_key,
        "q": query,
        "language": "en",
        "size": count
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        articles = []
        for item in data.get("results", []):
            articles.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "source_id": item.get("source_id"),
                "pub_date": item.get("pubDate"),
                "country": item.get("country"),
                "category": item.get("category"),
                "description": item.get("description")
            })

        return {
            "tool": "newsdata_search",
            "status": "ok",
            "query": query,
            "results": articles
        }

    except Exception as e:
        return {
            "tool": "newsdata_search",
            "status": "error",
            "query": query,
            "error": str(e),
            "results": []
        }


def run_tools(subject):
    evidence = []

    looks_like_domain = "." in subject and " " not in subject
    security_query = f"{subject} security incident OR scam OR malware OR breach"
    news_query = f"{subject} security OR breach OR investigation OR fraud OR sanctions OR lawsuit"

    if looks_like_domain:
        evidence.append(dns_lookup(subject))
        evidence.append(ip_lookup(subject))
        evidence.append(whois_lookup(subject))

        evidence.append(brave_search(subject))
        evidence.append(brave_search(security_query))

        evidence.append(google_news_search(subject))
        evidence.append(google_news_search(news_query))

        evidence.append(newsdata_search(subject))
        evidence.append(newsdata_search(news_query))
    else:
        evidence.append(brave_search(subject))
        evidence.append(brave_search(security_query))

        evidence.append(google_news_search(subject))
        evidence.append(google_news_search(news_query))

        evidence.append(newsdata_search(subject))
        evidence.append(newsdata_search(news_query))

    return evidence
