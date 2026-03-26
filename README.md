# The Trust Paradox: Security Vulnerabilities in Multi-Agent LLM Systems and a Framework for Defensive AI Architecture

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Format](https://img.shields.io/badge/Format-IEEE%20Conference-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Pages](https://img.shields.io/badge/Pages-12--15-orange)

---

## 📌 Overview

This repository contains the dataset, analysis scripts, figures, and 
framework documentation supporting the original research article:

> **"The Trust Paradox: Security Vulnerabilities in Multi-Agent LLM 
> Systems and a Framework for Defensive AI Architecture"**

- **Authors:** [Your Name], [Partner Name]  
- **Institution:** University of Central Punjab (UCP), Lahore, Pakistan  
- **Course:** Introduction to Cloud Computing (ICC)  
- **Format:** IEEE Conference Template — LaTeX (IEEEtran)  
- **Target Length:** 12–15 pages including references  
- **Submission:** ZIP folder containing .tex, PDF, Plagiarism Report, AI Report  

---

## 📚 Benchmark Papers

This article uses the following two papers as benchmarks and baselines:

### Paper 1 — 2025 (Attack Analysis Benchmark)
| Field        | Detail |
|---|---|
| **Title**    | The Dark Side of LLMs: Agent-based Attacks for Complete Computer Takeover |
| **Authors**  | Lupinacci, Pironti, Blefari, Romeo, Arena, Furfaro |
| **Year**     | 2025 (v5 — November 4, 2025) |
| **DOI**      | [10.48550/arXiv.2507.06850](https://doi.org/10.48550/arXiv.2507.06850) |
| **Venue**    | arXiv (cs.CR) — Submitted to Elsevier |
| **Pipeline** | LangChain + LangGraph |

### Paper 2 — 2026 (Defense Benchmark)
| Field        | Detail |
|---|---|
| **Title**    | Many Hands Make Light Work: An LLM-based Multi-Agent System for Detecting Malicious PyPI Packages |
| **Authors**  | Zeshan, Ibiyo, Di Sipio, Nguyen, Di Ruscio |
| **Year**     | 2026 (January 17, 2026) |
| **DOI**      | [10.48550/arXiv.2601.12148](https://doi.org/10.48550/arXiv.2601.12148) |
| **Venue**    | arXiv (cs.SE) — Accepted to Journal of Systems and Software (Elsevier) |
| **Pipeline** | CodeBERT + LLaMA-3 Multi-Agent Pipeline |
| **Dataset**  | D1: 6,000 PyPI files (balanced) / D2: 1,296 multi-file packages (imbalanced) |

---

## 🔍 Identified Research Gaps (8 Points)

| # | Gap | Our Solution |
|---|---|---|
| G1 | Synthetic environments only | Real-world cloud deployment threat model |
| G2 | RAG chunk optimization not explored | RAG Integrity Verification Framework |
| G3 | No defense framework proposed | Security Proxy Layer + LAMPS pipeline |
| G4 | Minimal/unhardened system prompts | Structured Prompt Hardening Framework |
| G5 | No multimodal agents tested | Unified Attack Surface Taxonomy |
| G6 | No distributed multi-agent systems | Hierarchical Trust Architecture |
| G7 | 100% inter-agent trust unexplained | Theoretical trust generalization analysis |
| G8 | Black-box evaluation only | White-box interpretability discussion |

---

## 📁 Repository Structure

trust-paradox-agentic-ai-security/
│
├── README.md
│
├── dataset/
│ ├── attack_results.csv
│ ├── sensitivity_results.csv
│ └── lamps_accuracy_results.csv
│
├── analysis/
│ ├── attack_analysis.py
│ ├── sensitivity_analysis.py
│ └── comparison_analysis.py
│
├── figures/
│ ├── fig1_attack_success_rate.png
│ ├── fig2_sensitivity_heatmap.png
│ ├── fig3_framework_architecture.png
│ └── fig4_defense_comparison.png
│
├── framework/
│ ├── security_proxy_layer.md
│ ├── prompt_hardening.md
│ ├── trust_architecture.md
│ ├── rag_integrity.md
│ └── attack_surface_taxonomy.md
│
├── article/
│ ├── main.tex
│ ├── references.bib
│ └── IEEEtran.cls
│
└── submission/
├── article_final.pdf
├── plagiarism_report.pdf
└── ai_report.pdf

text

---

## 📊 Dataset Description

### `attack_results.csv`
Extracted from Tables 2, 3, 4 of Lupinacci et al. (2025).
DOI: 10.48550/arXiv.2507.06850

| Attack | Vulnerable Models | Success Rate |
|---|---|---|
| Direct Prompt Injection | 17/18 | 94.4% |
| RAG Backdoor | 15/18 | 83.3% |
| Inter-Agent Trust | 18/18 | 100.0% |

### `sensitivity_results.csv`
Extracted from Table 6 of Lupinacci et al. (2025).
Metrics: ASR (Attack Success Rate), FSR (Follow Step Ratio), MIR (Malware Identification Rate)

### `lamps_accuracy_results.csv`
Extracted from Zeshan et al. (2026).
DOI: 10.48550/arXiv.2601.12148

| Dataset | Accuracy |
|---|---|
| D1 (balanced) | 97.7% |
| D2 (imbalanced) | 99.5% |

---

## 🏗️ Proposed Framework

┌─────────────────────────────────────────────────────────┐
│ TRUST PARADOX DEFENSE FRAMEWORK │
├───────────────────┬─────────────────┬───────────────────┤
│ LAYER 1 │ LAYER 2 │ LAYER 3 │
│ Input Guard │ Execution │ Trust Control │
│ │ Proxy │ │
│ - Prompt │ - Static │ - Hierarchical │
│ Hardening │ Analysis │ Trust Levels │
│ - RAG Integrity │ - Sandbox │ - Inter-Agent │
│ Verification │ Execution │ Auth Tokens │
│ - Input │ - Formal │ - Privilege │
│ Sanitization │ Verification │ Boundaries │
└───────────────────┴─────────────────┴───────────────────┘

text

Addresses Gaps: G1, G2, G3, G4, G5, G6, G7, G8

---

## 📝 Article Writing Plan

### Tools (Laptop Only)
| Tool | Purpose | Link |
|---|---|---|
| Overleaf | IEEE LaTeX writing | [overleaf.com](https://www.overleaf.com) |
| elicit.ai | Find supporting references | [elicit.com](https://elicit.com) |
| BibGuru | IEEE BibTeX references | [bibguru.com](https://www.bibguru.com) |
| QuillBot | Paraphrasing | [quillbot.com](https://quillbot.com) |
| StealthWriter.ai | Reduce AI content | [stealthwriter.ai](https://stealthwriter.ai) |
| Turnitin | Plagiarism report | Via UCP student portal |
| GitHub | Host dataset + framework | This repository |

### Writing Phases

#### Phase 1 — Setup ✅
- [x] Title finalized
- [x] Benchmark papers confirmed
- [x] 8 gaps identified
- [x] GitHub repository created
- [x] IEEE template opened on Overleaf

#### Phase 2 — Writing ⏳
- [ ] Step 1: Abstract (200–250 words)
- [ ] Step 2: Introduction (~600 words)
- [ ] Step 3: Background (~500 words)
- [ ] Step 4: Literature Review (~700 words)
- [ ] Step 5: Methodology (~600 words)
- [ ] Step 6: Results and Analysis (~800 words)
- [ ] Step 7: Proposed Framework (~900 words)
- [ ] Step 8: Discussion (~500 words)
- [ ] Step 9: Conclusion (~300 words)
- [ ] Step 10: References (12–15 IEEE citations)

#### Phase 3 — Quality Control ⏳
- [ ] Plagiarism below 10% (Turnitin)
- [ ] AI content below 2% (StealthWriter.ai)
- [ ] Page count 12–15 pages
- [ ] All graphs labeled with captions
- [ ] All references in IEEE format

#### Phase 4 — Submission ⏳
- [ ] Export .tex from Overleaf
- [ ] Export PDF from Overleaf
- [ ] Download plagiarism report
- [ ] Download AI report
- [ ] Pack into ZIP folder
- [ ] Submit before deadline — NO EXTENSION

---

## 📋 Submission Checklist

ZIP Folder:
├── ✅ main.tex
├── ✅ article_final.pdf
├── ✅ plagiarism_report.pdf
└── ✅ ai_report.pdf

text

---

## 🔗 Key Links

| Resource | Link |
|---|---|
| Paper 1 (2025) | https://doi.org/10.48550/arXiv.2507.06850 |
| Paper 2 (2026) | https://doi.org/10.48550/arXiv.2601.12148 |
| IEEE Template | https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn |
| This Repository | https://github.com/[yourusername]/trust-paradox-agentic-ai-security |

---

## ⚠️ Academic Integrity Notice

All data in this repository is extracted and structured from 
publicly available peer-reviewed research papers, properly 
cited according to IEEE standards. No proprietary data, 
malware code, or executable attack scripts are included. 
This repository is for academic research purposes only.

---

## 👥 Authors

| Name | Institution | Email |
|---|---|---|
| [Your Name] | UCP, Lahore, Pakistan | [your email] |
| [Partner Name] | UCP, Lahore, Pakistan | [partner email] |

---

*Last Updated: March 2026*
