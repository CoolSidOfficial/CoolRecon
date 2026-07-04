```markdown
# CoolRecon

Modular Python-based reconnaissance framework for automated attack surface discovery.

---

## 🧠 About

CoolRecon is a modular reconnaissance framework designed to automate the process of discovering, validating, and organizing target assets during security reconnaissance.

It combines multiple open-source tools into a structured and extensible pipeline while keeping outputs cleanly separated for analysis.

---

## 🎯 Purpose

The purpose of CoolRecon is to:

- Automate attack surface discovery for bug bounty and security research
- Combine multiple reconnaissance tools into a single workflow
- Standardize output from different tools into structured datasets
- Reduce manual effort in recon by chaining discovery → validation → crawling
- Provide a modular base for building advanced recon automation systems

It is designed for **learning, research, and authorized security testing only**.

---

## ⚙️ Features

### Current:
- Subdomain enumeration
- DNS validation
- HTTP probing
- Modular architecture
- Tool execution engine
- Organized output storage
- Clean logging system

### Planned:
- Port scanning
- URL discovery (gau + katana)
- JavaScript analysis
- Parameter extraction
- Content discovery
- Vulnerability scanning integration
- Reporting system

---

## 📁 Project Structure

```

CoolRecon/

├── main.py
├── core/
│   ├── runner.py
│   ├── logger.py
│   ├── storage.py
│   └── merge.py
│
├── modules/
│   ├── subdomains.py
│   ├── http_probe.py
│   ├── dnsx.py
│   ├── passive/
│   │   └── subfinder.py
│   └── urls/
│       ├── gau.py
│       └── katana.py
│
├── output/
├── requirements.txt
└── README.md

```

---

## 🔄 How It Works

CoolRecon follows a modular pipeline:

```

Target Domain
│
▼
Subdomain Enumeration
│
▼
DNS Validation
│
▼
HTTP Probing
│
▼
URL Discovery (GAU + Katana)
│
▼
Result Merging
│
▼
Output Storage

```

---

## 🚀 Example Output Flow

```

example.com
│
├── subdomains/
│   └── merged.txt
│
├── dns/
│   └── resolved.txt
│
├── http/
│   └── alive.txt
│
└── urls/
├── gau.txt
├── katana.txt
└── merged.txt

````

---

## 📦 Installation

```bash
git clone <repository-url>
cd CoolRecon
pip install -r requirements.txt
````

Make sure required tools are installed:

* subfinder
* dnsx
* httpx
* gau
* katana

---

## ▶️ Usage

```bash
python3 main.py target.com
```

Example:

```
[+] CoolRecon started: target.com
[+] Subdomains found: 161
[+] Resolved: 41
[+] Live hosts found: 18
[+] Completed
```

---

## 🏗️ Architecture

CoolRecon separates responsibilities:

### Core

* Command execution
* Logging
* File storage
* Result merging

### Modules

Each recon technique is independent:

* subdomains
* dns
* http
* urls
* ports (planned)

---

## 🗺️ Development Roadmap

### v0.1

* Core framework
* Subdomain enumeration
* Output management

### v0.2

* DNS resolution
* HTTP probing
* Basic URL discovery

### v0.3

* JS analysis
* Parameter extraction
* Crawling improvements

### v1.0

* Full recon pipeline
* Reporting system
* Automation engine

---

## ⚠️ Disclaimer

CoolRecon is intended for:

* Security research
* Bug bounty programs
* Authorized penetration testing

Do not use it against systems without explicit permission.

---

## 📜 License

MIT License

```
```
