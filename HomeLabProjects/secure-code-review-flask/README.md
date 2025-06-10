# Secure Code Review - Flask App

This project demonstrates a simple example of identifying and fixing insecure coding issues in a web application, focusing on an Insecure Direct Object Reference (IDOR) vulnerability.

---

## Project Structure

- `insecure-app/app.py`: A Flask app with an IDOR vulnerability allowing users to access other users’ profiles without authorization.
- `secure-app/app.py`: The fixed Flask app enforcing proper session-based access control.

---

## What I Learned and What This Shows

- **IDOR vulnerability** happens when an application exposes internal references (like user IDs) without proper authorization checks, allowing attackers to access data they shouldn’t.
- The **insecure app** lets anyone access any user’s profile just by changing the `user_id` parameter in the URL.
- The **secure app** fixes this by enforcing session-based authentication, ensuring users can only access their own profile.
- This exercise showcases my ability to:
  - Identify common security flaws in web applications.
  - Understand the risks related to broken access control.
  - Implement secure coding practices to fix vulnerabilities.
  - Write clear, maintainable code with authentication and session management.

---

## How to Run

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo/secure-code-review-flask

