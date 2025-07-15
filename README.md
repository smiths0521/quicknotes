# 📝 QuickNotes

A lightweight Flask-based note-taking app, containerized with Docker and perfect for practicing modern web app deployment.

---

## 🚀 Project Overview

**QuickNotes** is a beginner-friendly Python web app designed for learners and DevOps professionals who want to:

- Understand how Flask apps are structured and deployed
- Practice using `docker-compose` with environment variables
- Learn how to manage `.env` files and keep credentials secure
- Lay a foundation for future Azure container deployments

It serves as an ideal hands-on lab for those studying for the **Azure Administrator Associate** certification or exploring real-world DevOps and container security concepts.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Flask** (Lightweight web framework)
- **Docker + Docker Compose**
- **dotenv** (Environment variable management)

---

## 🗂️ File Structure


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

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/YOUR_USERNAME/quicknotes.git
cd quicknotes


### 2. Create Your `.env` File


cp .env.example .env

> Edit `.env` as needed (default port is 5000).

### 3. Start the App with Docker Compose


docker compose up --build

Then open your browser to: [http://localhost:5000](http://localhost:5000)

---

## 🔐 Security Notes

* All secrets are stored via `.env` files.
* This project avoids hardcoded credentials in the Dockerfile or source code.
* Follows container best practices with volume mounting and isolated ports.

---

## 📚 Learning Goals

This project reinforces:

* How to build and containerize Python web apps
* Managing config with `.env` files
* Using Docker Compose to orchestrate services
* Preparing apps for cloud-native platforms (Azure Container Apps, ACI)

---

## ✅ Potential Enhancements

* Save notes to a persistent volume (or simple file)
* Add SQLite/PostgreSQL for full CRUD persistence
* Azure Container Registry + Azure Container App deployment
* CI/CD pipeline integration with GitHub Actions

---


## 🤝 Contributing / Forking

Feel free to fork this repo to:

* Build your own note app
* Practice Azure deployments
* Test persistent data strategies in Docker

---

**Built to be simple. Scaled to teach. Ready for the cloud.**


---
