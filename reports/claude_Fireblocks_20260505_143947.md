# Investigation Report

## Subject

**Fireblocks** — Enterprise Digital Asset Infrastructure Company
Website: `hXXps://www[.]fireblocks[.]com`
Console: `hXXps://console[.]fireblocks[.]io/v2/`
LinkedIn: `hXXps://www[.]linkedin[.]com/company/fireblocks/`
Twitter/X: `hXXps://x[.]com/FireblocksHQ`

---

## Executive Summary

Fireblocks is a well-established, enterprise-grade digital asset infrastructure company offering MPC-secured custody, stablecoin infrastructure, DeFi/CEX connectivity, and blockchain-based product tooling. The investigation found no evidence of fraud, sanctions, active lawsuits, or malicious activity attributable to Fireblocks. Historical security incidents were minor, limited to non-production systems, or involved third parties — all handled with public transparency. Fireblocks actively operates as a **defender** in the cybersecurity space, having disrupted a North Korean Lazarus Group recruitment scam. Recent business activity reflects strong institutional growth, including a high-profile partnership with Western Union.

---

## Key Findings

- **Legitimate enterprise company**: Provides MPC security, digital asset custody, and stablecoin infrastructure to financial institutions.
- **Western Union partnership (May 2026)**: Powers Western Union's first stablecoin (USDPT) on the Solana blockchain, deployed in Bolivia and the Philippines.
- **Terra DeFi expansion (May 2026)**: Expanded institutional access to Terra's DeFi ecosystem.
- **Thales collaboration (Feb 2026)**: Joint effort to deliver bank-grade digital asset security.
- **Mastercard & Coinbase alliance (Apr 2026)**: Member of the Blockchain Security Standards Council.
- **Agentic AI Infrastructure (Apr 2026)**: Actively building AI-driven infrastructure for digital assets.
- **Security Posture Management product (Oct 2025)**: New product launch targeting enterprise crypto security.
- **Sha1-Hulud 2.0 incident**: Suspicious activity detected in **non-production systems only**; no customer funds affected; platform remained operational.
- **Fortress Trust hack**: A third-party analytics vendor was breached; Fireblocks was **not** the direct breach source and responded publicly.
- **Operation Contagious Interview**: Fireblocks' security team **proactively identified and disrupted** a Lazarus Group-linked fake recruitment malware campaign — acting as defender, not victim.
- **No evidence of sanctions, fraud, or litigation** found across all sources.

---

## Evidence Collected

| Tool | Query | Key Results |
|------|-------|-------------|
| `brave_search` | "Fireblocks" | Official website, LinkedIn, console, PeerSpot reviews — all confirm legitimate enterprise identity |
| `brave_search` | "Fireblocks security incident OR scam OR malware OR breach" | Fortress Trust (third-party breach), Sha1-Hulud 2.0 (non-production), Operation Contagious Interview (Fireblocks as defender) |
| `google_news_search` | "Fireblocks" | Western Union USDPT stablecoin launch, Terra DeFi expansion, Agentic AI infrastructure news |
| `google_news_search` | "Fireblocks security OR breach OR investigation OR fraud OR sanctions OR lawsuit" | Security Posture Management product, Thales collaboration, Mastercard/Coinbase council — no negative findings |
| `newsdata_search` | "Fireblocks" | Western Union USDPT stablecoin on Solana; DTCC tokenization participation |
| `newsdata_search` | "Fireblocks security OR breach OR investigation OR fraud OR sanctions OR lawsuit" | No relevant negative results returned; results dominated by Western Union stablecoin news |

---

## Risk Assessment

### 🟢 **LOW**

**Rationale:**
- No evidence of fraud, sanctions, regulatory action, or active litigation.
- Security incidents identified were either in non-production environments (Sha1-Hulud 2.0) or attributable to third parties (Fortress Trust).
- Fireblocks actively exposes and counters threat actors (Lazarus Group/Operation Contagious Interview), demonstrating a mature security posture.
- Strong institutional partnerships (Western Union, Mastercard, Thales, Coinbase) indicate high trust from regulated financial entities.
- Transparent public disclosure of all known incidents.

---

## Indicators / Technical Details

| Type | Value | Notes |
|------|-------|-------|
| Domain | `fireblocks[.]com` | Primary company domain |
| Domain | `fireblocks[.]io` | Console/platform domain |
| URL | `hXXps://www[.]fireblocks[.]com/` | Official website |
| URL | `hXXps://console[.]fireblocks[.]io/v2/` | Customer console |
| URL | `hXXps://www[.]fireblocks[.]com/blog/in-response-to-the-fortress-trust-hack/` | Fortress Trust incident response blog |
| URL | `hXXps://www[.]fireblocks[.]com/blog/security-update-sha1-hulud-2-0` | Sha1-Hulud 2.0 security update |
| URL | `hXXps://www[.]fireblocks[.]com/blog/contagious-interview-recruiting-scam` | Operation Contagious Interview disclosure |
| Social | `hXXps://x[.]com/FireblocksHQ` | Official Twitter/X handle |
| Social | `hXXps://www[.]linkedin[.]com/company/fireblocks/` | LinkedIn (82,916+ followers) |
| Third-party review | `hXXps://www[.]peerspot[.]com/products/fireblocks-reviews` | Enterprise product reviews |
| Security rating | `hXXps://www[.]upguard[.]com/security-report/fireblocks-com` | UpGuard vendor risk report (score not retrieved) |
| Threat actor (countered) | Lazarus Group (North Korea) | Targeted crypto developers; disrupted by Fireblocks |
| Blockchain | Solana | Used for Western Union USDPT stablecoin |

> **Note:** No IP addresses, WHOIS records, or DNS data were retrieved in this investigation cycle.

---

## Gaps and Limitations

| Gap | Impact |
|-----|--------|
| **WHOIS / DNS / IP infrastructure** not retrieved | Cannot verify domain ownership or hosting infrastructure |
| **UpGuard security rating score** referenced but not retrieved | Quantitative security posture score unavailable |
| **Regulatory licenses and compliance certifications** not confirmed | Cannot verify jurisdictional compliance (e.g., SOC 2, ISO 27001, FinCEN) |
| **Funding and valuation** not confirmed in current evidence | Last known valuation (~$8B, 2022) is unverified in this dataset |
| **Executive/leadership background** not investigated | No vetting of key personnel |
| **Full customer list** not available | Only Western Union and Midas RWA mentioned explicitly |
| **Ongoing litigation or regulatory investigations** not confirmed absent | Absence of evidence ≠ evidence of absence |
| **newsdata_search** security query returned irrelevant results | Possible indexing gap; no additional negative signals found |

---

## Recommended Next Steps

1. **WHOIS & DNS Lookup**: Query `fireblocks[.]com` and `fireblocks[.]io` for registrant details, nameservers, and hosting infrastructure.
2. **UpGuard Score Retrieval**: Access the full UpGuard vendor risk report for a quantitative security rating.
3. **Regulatory Verification**: Check FinCEN, FCA, MAS, and other relevant regulators for Fireblocks' licensing status.
4. **Leadership Vetting**: Investigate key executives (CEO Michael Shaulov, etc.) for adverse media, sanctions, or PEP status.
5. **Litigation Search**: Search PACER (US courts) and equivalent databases for any civil or regulatory actions.
6. **Funding Verification**: Confirm current valuation and investor list via Crunchbase or PitchBook.
7. **Sha1-Hulud 2.0 Deep Dive**: Obtain full technical disclosure to assess whether non-production exposure could have downstream risks.
8. **Third-Party Dependency Risk**: Review Fireblocks' vendor/supply chain exposure given the Fortress Trust third-party breach pattern.

---

## Final Verdict

### ✅ **CLEAN**

Fireblocks presents as a legitimate, reputable, and institutionally trusted enterprise digital asset infrastructure provider. All identified security incidents were minor, transparently disclosed, and either limited to non-production systems or attributable to third parties. The company actively contributes to the security of the broader crypto ecosystem. No fraud, sanctions, malware attribution, or legal risk signals were identified.

---

## Errors

| System/Tool | Error Information |
|-------------|-------------------|
| `newsdata_search` (security query) | No relevant security/breach/fraud results returned; query returned unrelated Western Union stablecoin articles — possible indexing limitation or lack of relevant indexed content |
| UpGuard security rating | URL referenced in search results (`hXXps://www[.]upguard[.]com/security-report/fireblocks-com`) but full report content and numerical score were **not retrieved** by any tool |