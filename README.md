
# 📝 QuickNotes

A lightweight Flask-based note-taking app, containerized with Docker and ideal for practicing modern DevOps and container deployment workflows.

---

## 🚀 Project Overview

**QuickNotes** is a minimal Python web app designed for learners, cloud engineers, and DevOps professionals who want to:

- Build and containerize Flask apps
- Use Docker Compose with secure environment management
- Align with real-world DevOps scenarios
- Build muscle memory for cloud deployment, version control, and container registries

This project reflects hands-on work from concept to container, with a focus on security, efficiency, and repeatable deployments.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Flask** (Lightweight Python web framework)
- **Docker** + **Docker Compose**
- **dotenv** for environment variable management

---

## 📁 File Structure

```text
quicknotes/
├── .env
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── webapp.py
├── templates/
│   └── index.html
└── static/
    └── style.css
---

## ⚙️ Local Setup (Docker Compose)

### 1. Clone the Repository


git clone https://github.com/YOUR_USERNAME/quicknotes.git
cd quicknotes


### 2. Configure Environment Variables


cp .env.example .env

> Update `.env` as needed. Default Flask port is `5000`.

### 3. Run Locally


docker compose up --build

Visit [http://localhost:5000](http://localhost:5000)

---

## 🔐 Security Practices

* Secrets are externalized via `.env` and not hardcoded.
* Docker image is lean, exposing only the necessary port (5000 or 5001).
* Follows container isolation best practices.
* Local dev setup isolates dependencies and avoids system conflicts.

---

## 📚 Learning Outcomes

By completing this project, you'll gain experience with:

* Dockerizing Python web apps
* Using Docker Compose in local dev environments
* Managing secrets and ports securely
* Preparing apps for GitHub and public collaboration
* Practicing hands-on fundamentals for Azure certification

---

## 🤝 Fork, Contribute, or Clone

Use this repo to:

* Practice Python containerization
* Run test environments locally
* Share or fork for training labs or small business internal use

---
