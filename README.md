# CoolRecon

<p align="center">
  Modular Python-based reconnaissance framework for automated attack surface discovery.
</p>

## About

CoolRecon is a modular reconnaissance framework designed to automate the process of discovering and organizing target assets.

The goal of CoolRecon is to provide a clean, extensible framework that combines different reconnaissance tools into structured workflows while keeping results separated and organized.

## Features

Current:

* Subdomain enumeration
* Modular architecture
* Tool execution engine
* Organized output storage
* Clean logging system

Planned:

* DNS reconnaissance
* Live host detection
* Port scanning
* URL discovery
* JavaScript analysis
* Parameter discovery
* Content discovery
* Vulnerability scanning integration
* Reporting system

## Project Structure

```text
CoolRecon/

├── main.py

├── core/
│   ├── runner.py
│   ├── logger.py
│   └── storage.py

├── modules/
│   └── subdomains.py

├── output/

├── requirements.txt

└── README.md
```

## How It Works

CoolRecon follows a modular pipeline:

```
Target Domain
      |
      v
Recon Module
      |
      v
Tool Execution
      |
      v
Result Processing
      |
      v
Output Storage
```

Example:

```
example.com

        |
        v

subfinder

        |
        v

output/example.com/subdomains.txt
```

## Installation

Clone the repository:

```bash
git clone <repository-url>

cd CoolRecon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure required reconnaissance tools are installed and available in your PATH.

Example:

```bash
subfinder -h
```

## Usage

Run:

```bash
python3 main.py target.com
```

Example output:

```
[+] CoolRecon started: target.com
[+] Subdomains found: 25
```

Results:

```
output/

└── target.com/

    └── subdomains.txt
```

## Architecture

CoolRecon separates responsibilities:

### Core

Handles framework functionality:

* Command execution
* Logging
* File storage

### Modules

Each reconnaissance technique is an independent module.

Example:

```
modules/

subdomains.py

http.py

ports.py

urls.py
```

This allows new capabilities to be added without modifying the core engine.

## Development Roadmap

### v0.1

* Core framework
* Subdomain enumeration
* Output management

### v0.2

* HTTP probing
* DNS intelligence
* Port scanning

### v0.3

* URL discovery
* JavaScript analysis
* Parameter extraction

### v1.0

* Complete reconnaissance workflow
* Reporting
* Advanced automation

## Disclaimer

CoolRecon is intended for authorized security testing, research, and learning purposes only.

Always ensure you have permission before performing reconnaissance against any target.

## License

MIT License

