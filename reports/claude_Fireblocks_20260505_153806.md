# Investigation Report

## Subject
**Fireblocks** — `hXXps://www[.]fireblocks[.]com`

---

## Executive Summary
Fireblocks is a legitimate, enterprise-grade digital asset infrastructure company providing secure storage, transfer, and issuance of digital assets using MPC (Multi-Party Computation) security technology. The company serves major financial institutions, banks, and crypto organizations globally. Investigation found no evidence of fraud, sanctions, regulatory violations, or malicious activity attributable to Fireblocks itself. The company has been a **target** of threat actors (notably North Korea's Lazarus Group) due to its prominence in the crypto security space, and has responded proactively with public disclosures and active threat disruption. Recent business activity is strong, including a high-profile partnership with Western Union for a Solana-based stablecoin launch in May 2026.

---

## Key Findings

- **Legitimate Enterprise Company:** Fireblocks provides enterprise digital asset infrastructure (MPC custody, DeFi/CEX connectivity, stablecoin issuance) to financial institutions worldwide.
- **Western Union Partnership (May 2026):** Selected to power Western Union's first stablecoin (USDPT) on Solana, launched in Philippines and Bolivia.
- **Lazarus Group Impersonation (Jan 2026):** North Korean threat actors impersonated Fireblocks recruiters on LinkedIn to deliver malware — Fireblocks was the **victim of impersonation**, not the perpetrator; their security team actively disrupted the campaign ("Operation Contagious Interview").
- **Sha1-Hulud 2.0 Incident (Dec 2025):** Suspicious activity detected in **non-production systems only**; no customer funds accessed; proactively disclosed.
- **Fortress Trust Vendor Hack:** A third-party data analytics provider (not Fireblocks) was breached; Fireblocks published a public response clarifying their infrastructure was not the source.
- **Proactive Security Posture:** Launched "Security Posture Management" product (Oct 2025) and "Fireblocks Trust" qualified custody service (Oct 2025).
- **Agentic AI Infrastructure:** Actively building AI-integrated infrastructure for digital assets (Apr 2026).
- **No Regulatory/Legal Actions Found:** No evidence of OFAC sanctions, FinCEN actions, lawsuits, or fraud investigations against Fireblocks.
- **UpGuard Security Report Exists:** A vendor risk report for `fireblocks[.]com` exists on UpGuard but detailed score/findings were not retrieved.

---

## Evidence Collected

| Tool | Query | Key Results |
|------|-------|-------------|
| `brave_search` | "Fireblocks" | Official website, LinkedIn (82,916+ followers), X/Twitter (`@FireblocksHQ`), PeerSpot reviews — all consistent with a legitimate enterprise company |
| `brave_search` | "Fireblocks security incident OR scam OR malware OR breach" | Fortress Trust vendor hack response; Sha1-Hulud 2.0 non-production incident; Lazarus Group impersonation scam disrupted by Fireblocks; UpGuard security rating page referenced |
| `google_news_search` | "Fireblocks" | Western Union USDPT stablecoin launch (May 2026); Terra DeFi expansion; Agentic AI infrastructure development |
| `google_news_search` | "Fireblocks security OR breach OR investigation OR fraud OR sanctions OR lawsuit" | Security Posture Management product launch; Sha1-Hulud 2.0 update; Operation Contagious Interview disruption; Fireblocks Trust custody service |
| `newsdata_search` | "Fireblocks" / "Fireblocks security OR breach..." | Western Union stablecoin coverage; DTCC tokenization participation — no negative findings returned |

---

## Risk Assessment

### Classification: **Low**

**Rationale:**
- No evidence of fraud, sanctions, regulatory violations, or malicious conduct by Fireblocks.
- Security incidents identified were either: (a) third-party breaches where Fireblocks was not the compromised vendor, (b) limited to non-production systems with no customer fund impact, or (c) external threat actors **impersonating** Fireblocks (making Fireblocks a victim, not a threat).
- The company demonstrates a mature, proactive security disclosure culture.
- Active, high-profile institutional partnerships (Western Union) indicate continued trust from major financial entities.
- Residual low risk exists due to the company's high-value target profile in the crypto security space, attracting sophisticated threat actors.

---

## Indicators / Technical Details

| Type | Value | Notes |
|------|-------|-------|
| Primary Domain | `hXXps://www[.]fireblocks[.]com` | Official company website |
| Console URL | `hXXps://console[.]fireblocks[.]io/v2/` | Customer-facing management console |
| Twitter/X | `hXXps://x[.]com/FireblocksHQ` | Official social media handle |
| LinkedIn | `hXXps://www[.]linkedin[.]com/company/fireblocks/` | 82,916+ followers |
| Blog (Security) | `hXXps://www[.]fireblocks[.]com/blog/` | Source of security disclosures |
| UpGuard Report | `hXXps://www[.]upguard[.]com/security-report/fireblocks-com` | Vendor risk report (score not retrieved) |
| News Source | `hXXps://blockchain[.]news/news/fireblocks-exposes-north-korean-hackers-fake-crypto-job-scam` | Lazarus Group impersonation coverage |
| Threat Actor | Lazarus Group (North Korea) | Impersonated Fireblocks recruiters; Fireblocks disrupted the campaign |
| Malware Campaign | "Operation Contagious Interview" | Fake LinkedIn recruiting → malware via coding assignments |
| Incident | Sha1-Hulud 2.0 | Non-production system suspicious activity, Dec 2025 |
| Partner | Western Union | USDPT stablecoin on Solana, May 2026 |

---

## Gaps and Limitations

- **UpGuard Security Rating Score:** The UpGuard vendor risk report for `fireblocks[.]com` was referenced but detailed scores/findings were not retrieved — actual technical security posture rating is unconfirmed.
- **Regulatory/Compliance Status:** No OFAC, FinCEN, SEC, or other regulatory filings or compliance certifications were confirmed (absence of negative findings is noted, but positive confirmation of compliance status was not obtained).
- **Ownership & Funding Structure:** Investor details, funding rounds, and ownership structure were not retrieved.
- **Full Fortress Trust Incident Scope:** The exact nature of Fireblocks' involvement (if any) in the Fortress Trust hack chain was not fully detailed.
- **Customer List:** Only Western Union and Fortress Trust were identified as customers; full client base is unknown.
- **Sha1-Hulud 2.0 Full Details:** The nature of the suspicious activity and the "Sha1-Hulud 2.0" threat actor/tool were not fully described in available evidence.
- **Legal/Lawsuit History:** No active or historical lawsuits were found, but a comprehensive legal database search was not performed.

---

## Recommended Next Steps

1. **Retrieve UpGuard Security Rating:** Access the full vendor risk report at `hXXps://www[.]upguard[.]com/security-report/fireblocks-com` to obtain technical security scores across website, email, network, and phishing/malware categories.
2. **Regulatory Compliance Verification:** Check SEC EDGAR, OFAC SDN list, FinCEN, and relevant state/national financial regulators for any filings, actions, or registrations related to Fireblocks.
3. **Legal Database Search:** Search PACER (US federal courts) or equivalent for any active or historical lawsuits involving Fireblocks.
4. **WHOIS/DNS Lookup:** Perform WHOIS and DNS enumeration on `fireblocks[.]com` and `fireblocks[.]io` to verify domain registration details, hosting infrastructure, and certificate transparency.
5. **Funding/Ownership Research:** Review Crunchbase or PitchBook for investor details, funding rounds, and corporate structure.
6. **Sha1-Hulud 2.0 Threat Intelligence:** Query threat intelligence platforms (e.g., VirusTotal, Recorded Future, MISP) for details on the "Sha1-Hulud 2.0" threat actor or toolset.
7. **LinkedIn Impersonation Monitoring:** If Fireblocks is being evaluated as a vendor/partner, verify recruiter identities independently given the confirmed Lazarus Group impersonation campaign targeting developers via LinkedIn.

---

## Final Verdict

### ✅ **Clean**

Fireblocks is a legitimate, well-established enterprise digital asset infrastructure company with no evidence of malicious activity, fraud, sanctions, or regulatory violations. The company has been a high-profile target of sophisticated threat actors (Lazarus Group) due to its prominence in the crypto security industry, but has demonstrated proactive threat detection, responsible disclosure, and active disruption of threat campaigns. Major institutional partnerships (Western Union) further validate its standing. Residual low risk exists from its high-value target profile and one unresolved UpGuard security rating detail.

---

## Errors

| System/Tool | Error Information |
|-------------|-------------------|
| None | All tools (`brave_search`, `google_news_search`, `newsdata_search`) returned status `ok` with no errors reported. |