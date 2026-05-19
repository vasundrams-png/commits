# Supply Chain Vulnerability Visualizer

## Problem Statement
Modern organizations depend heavily on third-party libraries, APIs, SaaS platforms, and cloud providers. A single vulnerable dependency can expose the entire system to major cybersecurity threats.

Security teams often lack a unified view of:
- Dependency relationships
- Vulnerable packages
- Trust-chain depth
- High-risk exposure points

Our project aims to solve this problem through an interactive visualization and risk analysis platform.

---

## Our Solution
Supply Chain Vulnerability Visualizer is a web-based cybersecurity dashboard that helps organizations analyze their software supply chain security.

The platform allows users to:
- Input their tech stack manually or through JSON/SBOM upload
- Visualize dependency relationships through an interactive graph
- Detect known CVEs and vulnerabilities
- Analyze trust-chain depth
- Identify high-risk components
- Generate prioritized remediation recommendations

---

## Core Features

### Tech Stack Input
- Manual entry of libraries, APIs, SaaS tools, and cloud services
- JSON/SBOM file upload support

### Interactive Dependency Graph
- Visual node-based dependency mapping
- Relationship tracking between services and packages
- Risk-highlighted dependency chains

### CVE Vulnerability Overlay
- Integration with public vulnerability databases
- Detection of known security issues
- Vulnerability severity indication

### Risk Scoring Engine
- Calculates risk score based on:
  - Vulnerability severity
  - Dependency depth
  - Exposure level
  - Breach history

### Recommendations Dashboard
- Suggests remediation actions
- Highlights critical exposure points
- Prioritizes urgent fixes

### Exportable Risk Report
- Downloadable summary report
- Security overview for organizations

---

## Proposed Workflow
1. User enters company tech stack
2. System analyzes dependencies
3. Vulnerable components are identified
4. Dependency graph is generated
5. Risk scores are calculated
6. Recommendations are displayed
7. Risk report is exported

---

## Tech Stack

### Frontend
- React.js
- Tailwind CSS
- React Flow / Cytoscape.js

### Backend
- Python Flask

### APIs & Data Sources
- NVD CVE Database
- OSV API

---

## Repository Structure

project/
│
├── frontend/
├── backend/
├── assets/
└── README.md

---

## Team Members
- M S Vasundra
- Vijayalakshmi V
- S Sandhya

---

## Future Scope
- Real-time vulnerability monitoring
- AI-powered threat prediction
- Automatic dependency scanning from GitHub repositories
- Cloud infrastructure risk analysis
- Enterprise dashboard with multi-user support
- Integration with DevSecOps pipelines
- Historical risk trend analytics
- Email alerts for newly discovered vulnerabilities

---

## Current Status
- Problem statement analysis completed
- Initial architecture planning completed
- Repository initialized
- Development in progress
