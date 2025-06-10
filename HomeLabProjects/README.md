# 🐐 WebGoat Vulnerability Lab – OWASP Top 10 Practice

Welcome to my WebGoat security walkthrough! This repo showcases what I learned while completing **all WebGoat modules**, a hands-on platform built by OWASP to help developers and security professionals understand how common web vulnerabilities work — and how to defend against them.

---

## 🔐 Project Summary

**WebGoat** is an intentionally vulnerable web application designed to teach secure coding practices through real-world attack simulations.

I used this tool to gain hands-on experience identifying, exploiting, and fixing vulnerabilities like SQL injection, XSS, broken authentication, CSRF, IDOR, and more.

---

## 📚 What I Learned

Here’s a breakdown of key vulnerabilities and what I took away from each module:

### 🧱 SQL Injection (SQLi)
- 🧠 **Learned:** How attackers manipulate backend queries with malicious input.
- 🔧 **Skill Gained:** Writing safe, parameterized queries to prevent SQLi in real applications.

### ⚠️ Cross-Site Scripting (XSS)
- 🧠 **Learned:** The impact of reflected, stored, and DOM-based XSS.
- 🔧 **Skill Gained:** Output encoding, input validation, and avoiding risky client-side logic.

### 🔓 Insecure Direct Object References (IDOR)
- 🧠 **Learned:** How attackers bypass access control by modifying parameters.
- 🔧 **Skill Gained:** Enforcing strict server-side authorization checks.

### 🔐 Broken Authentication & Session Management
- 🧠 **Learned:** Risks of weak sessions, password leaks, and flawed login flows.
- 🔧 **Skill Gained:** Implementing secure sessions, MFA, and hashed credentials.

### 🌐 Cross-Site Request Forgery (CSRF)
- 🧠 **Learned:** How attackers trick users into unwanted authenticated actions.
- 🔧 **Skill Gained:** Defending with CSRF tokens and SameSite cookie attributes.

### 🧨 Command Injection & Path Traversal
- 🧠 **Learned:** Dangers of unsanitized user input hitting system commands or file paths.
- 🔧 **Skill Gained:** Validating input, avoiding shell calls, and hardening file access logic.

### 🧱 Security Misconfigurations
- 🧠 **Learned:** How default settings and verbose error messages can expose systems.
- 🔧 **Skill Gained:** Performing secure deployments and hiding sensitive metadata.

### 🔐 Insecure Deserialization & JWT Attacks
- 🧠 **Learned:** How tampering with serialized data or weak JWTs can grant escalated access.
- 🔧 **Skill Gained:** Using strong cryptographic libraries and verifying token integrity.

---

## 💡 Key Takeaways

- ✅ I now have hands-on experience with the **OWASP Top 10** vulnerabilities.
- ✅ I’ve strengthened my skills in both **offensive and defensive security**.
- ✅ I understand how to **write secure code**, test for flaws, and think like an attacker.
- ✅ I’m comfortable using tools like **Burp Suite**, browser DevTools, and logging/debugging utilities to investigate security flaws.

---

## 📁 Repo Contents

> 🚨 _No exploit scripts or payloads are included to follow responsible disclosure practices._

- `NOTES.md` – Vulnerability explanations, walkthroughs, and screenshots
- `BestPractices.md` – Secure coding patterns and remediation strategies
- Screenshots from completed challenges (optional)
- Final reflections and security checklists

---

## 📎 Related Links

- 🔗 [OWASP WebGoat Project](https://owasp.org/www-project-webgoat/)
- 🔐 [OWASP Top 10 Overview](https://owasp.org/www-project-top-ten/)

---

## 🧠 Bonus: What This Taught Me About Security

Through WebGoat, I didn’t just learn how to break things — I learned **why things break**, and how to prevent it.

This experience pushed me to:
- Think critically about **code architecture**
- Question how user input flows through an app
- Stay up-to-date on modern **secure development practices**

---

Thanks for checking out my WebGoat portfolio. Feel free to fork, star ⭐, or connect!

