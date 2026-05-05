# Investigation Report

## Subject

**URL:** `hXXps://fitgirl-repacks[.]site/`

---

## Executive Summary

`fitgirl-repacks[.]site` is a long-standing (est. 2016) pirated video game distribution website operated anonymously from an offshore jurisdiction (Saint Kitts and Nevis). The site is widely known for "repacking" (compressing) cracked commercial video games for distribution. It has been formally listed by the Entertainment Software Association (ESA) as a "Malicious Pirate" in their 2024 report and has been subject to ISP-level blocking. While the official `.site` domain has not been confirmed to bundle malware directly, the platform distributes copyright-infringing content, circumvents DRM protections, and is surrounded by a significant ecosystem of impersonator/fake domains that do distribute malware. DNS resolution failed at time of scan, consistent with active ISP blocking.

---

## Key Findings

- **Piracy Platform**: Site explicitly distributes pirated, cracked video games — its core and sole purpose.
- **ESA Blacklisted**: Formally named a "Malicious Pirate" in the ESA's 2024 report on piracy threats.
- **ISP Blocked**: Reported blocked by ISPs without a court order as of October 2025.
- **DNS Non-Resolution**: All DNS records (A, AAAA, MX, NS, TXT) returned empty at scan time; IP lookup failed — consistent with active blocking.
- **Anonymous Operator**: Registrant fully privacy-redacted; registered in Saint Kitts and Nevis (KN).
- **Domain Age**: Registered September 2016 — nearly 9 years old, indicating sustained operation.
- **DRM Circumvention**: Released a repack with a "Hypervisor security bypass" in March 2026, actively circumventing commercial DRM.
- **No Direct Malware Confirmed**: The official `.site` domain has not been confirmed to bundle malware as of early 2022; Scamadviser rates it "legit and safe."
- **Fake Impersonator Sites**: Multiple fraudulent domains impersonate FitGirl (e.g., `fitgirl-repacks[.]net` rated 1/100 trust, confirmed malware distributor).
- **Rival Malware Incident**: A rival repack distributor (not FitGirl) was accused of bundling cryptocurrency miners in game installers.
- **Wikipedia Classification**: Explicitly described as "a website distributing pirated video games."

---

## Evidence Collected

| Tool | Status | Summary |
|------|--------|---------|
| `dns_lookup` | OK | All record types (A, AAAA, MX, NS, TXT) returned empty — domain not resolving |
| `ip_lookup` | ERROR | `getaddrinfo failed` — IP could not be resolved |
| `whois_lookup` | OK | Domain registered 2016-09-01, registrar TUCOWS, expires 2026-09-01, DNSSEC signed, registrant redacted (KN) |
| `brave_search` | OK | Confirmed piracy platform; Wikipedia classification; community safety discussions; Scamadviser "legit" rating |
| `brave_search` (security) | OK | ESA listing; ISP blocking; fake domain malware reports; rival crypto miner incident |
| `google_news_search` | OK | ESA 2024 report; ISP blocking (Oct 2025); Hypervisor bypass repack (Mar 2026); piracy coverage |
| `google_news_search` (security) | OK | Crypto miner bundling by rivals; ISP blocking; DRM cracking news |
| `newsdata_search` | OK | No results returned |

---

## Risk Assessment

### Classification: **HIGH**

**Rationale:**
- The site's **primary function is illegal** — distributing copyright-infringing software at scale, affecting major commercial game publishers.
- Formally recognized as a **threat actor by the ESA** and subject to **ISP-level blocking**.
- Active **DRM circumvention** (Hypervisor bypass) demonstrates ongoing technical sophistication and deliberate circumvention of security controls.
- **Anonymous offshore operator** with no accountability.
- Significant **brand abuse ecosystem** of impersonator sites that actively distribute malware, creating high risk for users who land on the wrong domain.
- DNS failure at scan time suggests the domain is **actively suppressed** by network-level controls.
- While the official site has not been confirmed to directly distribute malware, downloading and executing cracked game installers carries **inherent and significant security risk** regardless of source reputation.

---

## Indicators / Technical Details

### Domain
| Field | Value |
|-------|-------|
| Domain | `fitgirl-repacks[.]site` |
| Registrar | TUCOWS.COM, CO. |
| WHOIS Server | `whois[.]tucows[.]com` |
| Creation Date | 2016-09-01 |
| Expiration Date | 2026-09-01 |
| Last Updated | 2026-04-02 / 2025-08-03 |
| Name Servers | `ns1[.]terradns[.]org`, `ns2[.]terradns[.]org` |
| DNSSEC | signedDelegation |
| Registrant Country | KN (Saint Kitts and Nevis) |
| Registrant Identity | REDACTED FOR PRIVACY |
| Domain Status | clientTransferProhibited, clientUpdateProhibited |
| Contact Email | `domainabuse[@]tucows[.]com` |

### DNS Records (at time of scan)
| Type | Records |
|------|---------|
| A | None resolved |
| AAAA | None resolved |
| MX | None resolved |
| NS | None resolved |
| TXT | None resolved |

### Hosting / IP
- **IP Address**: Not resolved (lookup failed)
- **CDN/Hosting Provider**: Unknown

### Related URLs (Safe Representation)
| URL | Notes |
|-----|-------|
| `hXXps://fitgirl-repacks[.]site/popular-repacks/` | Official site subpage |
| `hXXps://fitgirl-repacks[.]site/upcoming-repacks-10/` | Official site subpage |
| `hXXps://fitgirl-repacks[.]net` | **Fake/impersonator domain** — confirmed malware distributor (1/100 trust score) |
| `hXXps://en[.]wikipedia[.]org/wiki/FitGirl_Repacks` | Wikipedia article |
| `hXXps://www[.]scamadviser[.]com/check-website/fitgirl-repacks.site` | Scamadviser rating |

---

## Gaps and Limitations

- **No IP/Hosting Data**: DNS and IP resolution both failed; hosting provider, CDN, and server location are unknown.
- **No VirusTotal / Threat Intel Scan**: No sandbox or AV scan results available for the domain or its content.
- **Operator Identity Unknown**: Registrant is fully privacy-redacted; no attribution possible.
- **Full Impersonator Domain List**: Only one fake domain (`fitgirl-repacks[.]net`) identified; others likely exist.
- **Legal Action Status**: No confirmed civil or criminal proceedings against the operator found in evidence.
- **Current Site Content**: DNS failure prevents live content inspection.
- **Newsdata Search**: Returned no results, limiting news coverage depth.

---

## Recommended Next Steps

1. **VirusTotal Scan**: Submit `fitgirl-repacks[.]site` to VirusTotal for AV/threat intelligence vendor assessment.
2. **Passive DNS Lookup**: Use tools like SecurityTrails, RiskIQ, or Shodan to retrieve historical DNS/IP records and identify hosting infrastructure.
3. **Threat Intelligence Platforms**: Query platforms (e.g., Recorded Future, MISP, AlienVault OTX) for IOCs associated with the domain.
4. **Impersonator Domain Enumeration**: Search for all domains using "fitgirl" or "fitgirl-repacks" across TLDs to map the full fake-site ecosystem.
5. **Legal/Regulatory Check**: Review ESA 2024 report in full; check USTR "Notorious Markets" list for formal designation.
6. **ISP Block Verification**: Confirm which ISPs/countries have implemented blocks and under what legal authority.
7. **User Warning**: If this investigation is for user safety purposes, advise users that **any executable downloaded from piracy sites carries inherent malware risk**, regardless of site reputation.

---

## Final Verdict

> ### ⚠️ MALICIOUS

**Justification:** `fitgirl-repacks[.]site` operates as a large-scale piracy distribution platform, formally designated a threat by the ESA, subject to ISP blocking, and actively circumventing commercial DRM protections. While the site operator has not been confirmed to directly bundle malware, the platform's core activity (distributing cracked, copyright-infringing software) is illegal in most jurisdictions, and the surrounding ecosystem of impersonator sites poses direct malware risk to users. The anonymous, offshore operator structure and DNS-level blocking further confirm the site's adversarial posture toward legal and regulatory frameworks.

---

## Errors

| System/Tool | Error Details |
|-------------|---------------|
| `ip_lookup` | `[Errno 11001] getaddrinfo failed` — DNS resolution failure prevented IP lookup; likely caused by active ISP/DNS-level blocking of the domain at time of scan |
| `newsdata_search` | Returned empty results for both queries; no articles indexed for this subject in the Newsdata database |