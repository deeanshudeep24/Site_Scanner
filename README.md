

```markdown
# Site Scanner

Welcome to the **Site Scanner**, a Python-based web security analysis tool designed to help identify common vulnerabilities in websites. This tool automates various penetration testing tasks to enhance the security assessment process.

## Features

- **Directory Enumeration**: Scans for hidden directories and files using customizable wordlists.
- **Subdomain Enumeration**: Identifies potential subdomains to assess the attack surface.
- **Cookie Tampering**: Tests for vulnerabilities related to cookie handling and security.
- **Report Generation**: Compiles findings into a structured report for easy review.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `requests`
  - `dnspython`

You can install the required libraries using pip:

```bash
pip install requests dnspython
```

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/deeanshudeep24/site-scanner.git
   cd Site-Scanner
   ```

2. Run the tool:

   ```bash
   python main.py
   ```

3. Follow the prompts to input the target website URL and wordlist options.

### Custom Wordlists

You can use custom wordlists for directory and subdomain enumeration. If you choose not to, the tool will use default wordlists.

### Reporting

The tool will generate a `pentest_report.txt` file containing the results of the scans.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.



## Author

**Deepanshu Deep** - [Your LinkedIn Profile](https://www.linkedin.com/in/deepanshu-deep24/)
```


