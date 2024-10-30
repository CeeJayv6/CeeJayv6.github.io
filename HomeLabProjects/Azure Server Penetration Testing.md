# Home Cybersecurity Lab: Azure Server Penetration Testing

## Project Overview
This project demonstrates my ability to configure and secure a virtual server on Microsoft Azure. Using **Nmap** and **Burp Suite**, I conducted penetration tests to identify potential vulnerabilities, simulating a real-world cybersecurity environment to assess the server’s security.

---

## Setup and Configuration
- **Azure Server Configuration**: Configured a Linux-based virtual server (e.g., Ubuntu) with initial hardening steps, including disabling unnecessary services and managing firewall rules.
- **Network Security**: Applied Network Security Groups (NSGs) to restrict access, allowing only essential ports and ensuring secure remote management.

---

## Tools Used

### Nmap (Network Mapper)
- **Purpose**: Nmap is an open-source tool used to scan networks and identify open ports, services, and OS details.
- **Application**:
  - **Open Ports**: Scanned for open and closed ports to validate that only required services were accessible.
  - **Service Enumeration**: Gathered service and version info to identify outdated software and potential risks.
  - **Operating System Detection**: Verified the OS and checked for misconfigurations that might lead to security breaches.

### Burp Suite
- **Purpose**: Burp Suite is a popular tool for web application security testing, ideal for finding vulnerabilities like XSS and SQL Injection.
- **Application**:
  - **Request Interception**: Captured HTTP requests to detect data exposure, such as credentials in plain text.
  - **Vulnerability Scanning**: Scanned the server for common web vulnerabilities and analyzed HTTP headers for secure configurations.
  - **Session Testing**: Examined session management, such as cookie settings, to check for secure handling.

---

## Findings and Analysis

### Open Ports and Service Exposure
- **Findings**: Nmap scans showed open ports beyond those necessary, including MySQL, which was accessible publicly.
- **Recommendation**: Restrict the MySQL port to internal IPs and close any non-essential ports.

### Outdated Software
- **Findings**: Detected outdated SSH and Apache versions, presenting known vulnerabilities.
- **Recommendation**: Implement a regular update schedule and automated patch management for essential services.

### Web Application Vulnerabilities
- **Findings**: Burp Suite found XSS vulnerabilities and insecure HTTP headers lacking Content Security Policy.
- **Recommendation**: Apply secure coding practices to validate input and configure security headers.

### Weak Session Management
- **Findings**: Session cookies lacked the “Secure” attribute, exposing sessions over non-HTTPS connections.
- **Recommendation**: Configure cookies with secure attributes to protect session data.

---

## Conclusion
This project highlights key skills in server setup and penetration testing using industry-standard tools, underscoring the importance of regular scanning, updates, and secure configurations for robust cybersecurity.


