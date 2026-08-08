# 🤖 AI Software Engineer Assistant

An intelligent backend application built with **Python**, **FastAPI**, and **PostgreSQL** that automatically analyzes GitHub repositories and generates a structured software engineering report.

Instead of manually exploring hundreds of project files, the application scans a repository, detects its technology stack, identifies its architecture, evaluates repository quality, and provides actionable engineering insights.

The long-term vision of this project is to build an **AI-powered Software Engineering Assistant** capable of helping developers quickly understand unfamiliar codebases.

---

# 🎥 Demo

> Watch the AI Software Engineer Assistant in action.

https://github.com/user-attachments/assets/2f225a74-821e-4ef2-814a-ef801ea7be33

---

# 🛠️ Technology Stack

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### API Documentation
- Swagger UI

### Version Control
- Git
- GitHub

---

# 🚀 Why This Project?

Understanding an existing software project is one of the most time-consuming tasks for software developers.

Before contributing to a repository, developers often need to answer questions such as:

- Which programming language is used?
- Which backend framework powers the application?
- What architecture pattern does it follow?
- Which authentication mechanism is implemented?
- Which database is configured?
- Is Docker available?
- Is CI/CD configured?
- Which testing framework is used?
- Is the project properly documented?

Finding these answers manually may require reading hundreds of project files.

This project automates that process by generating a structured engineering report in seconds.

---

# 🎯 Objective

The goal of this project is to reduce the time required to understand an unfamiliar software repository.

Instead of manually inspecting project files, developers receive:

- Repository Metadata
- Technology Stack Detection
- Architecture Detection
- Confidence Scores
- Repository Health Score
- Repository Summary
- Improvement Suggestions

---

# ✨ Current Capabilities

## 📂 Repository Cloning

- Clone any public GitHub repository using its URL.
- Prepare the repository for automated analysis.

---

## 📊 Repository Metadata Analysis

Automatically extracts repository information including:

- Total Files
- Total Folders
- Primary Programming Language
- Project Framework
- Package Manager
- README Availability

---

## 🏗️ Architecture Detection

Detects common software architecture patterns including:

- MVC
- Layered Architecture
- Clean Architecture
- Monolithic Architecture
- Microservices

Each result includes a confidence score.

Example:

```json
{
    "name": "Monolithic",
    "confidence": 100
}
```

---

## ⚙️ API Framework Detection

Automatically detects frameworks such as:

- FastAPI
- Flask
- Django
- Express.js
- Spring Boot
- ASP.NET Core

Each detection includes a confidence percentage.

---

## 🔐 Authentication Detection

Detects authentication mechanisms including:

- JWT
- OAuth
- Session Authentication
- API Key Authentication

---

## 🗄️ Database Detection

Supports detection of:

- PostgreSQL
- MySQL
- SQLite
- MongoDB
- Redis

---

## 🧪 Testing Framework Detection

Detects testing technologies including:

- pytest
- unittest
- JUnit
- TestNG
- Jest
- Mocha
- NUnit
- xUnit

---

## 🐳 Docker Detection

Determines whether Docker support is configured within the repository.

---

## 🔄 CI/CD Detection

Currently supports detection of:

- GitHub Actions

The detection engine is designed to support additional CI/CD platforms in future releases.

---

## 📜 License Detection

Detects common open-source licenses including:

- MIT
- Apache 2.0
- GPL
- BSD
- MPL
- ISC
- Unlicense

---

# 🧠 Repository Intelligence

Beyond technology detection, the application generates engineering insights.

## 🎯 Confidence Score Engine

Every detected technology includes a confidence percentage, allowing users to understand how reliable each detection is.

Example:

```json
{
    "framework": {
        "name": "Flask",
        "confidence": 90
    }
}
```

---

## 📝 Repository Summary

Automatically generates a human-readable project summary.

Example:

> This repository is a Python project built using Flask. It follows a Monolithic architecture, uses Session Authentication, implements testing with pytest, includes GitHub Actions for CI/CD, and is licensed under BSD 3-Clause.

---

## 📈 Repository Health Score

Evaluates repository quality using engineering metrics including:

- Documentation
- Architecture
- API Framework
- Authentication
- Database
- Testing
- Docker
- CI/CD
- License

Example:

```json
{
    "score": 90,
    "grade": "A"
}
```

---

## 💡 Improvement Suggestions

Provides practical recommendations to improve repository quality.

Example:

```json
[
    "Configure a database for the project.",
    "Add Docker support."
]
```

---

# 📊 Sample API Response

```json
{
    "metadata": {
        "primary_language": "Python",
        "framework": "Flask"
    },
    "architecture": {
        "name": "Monolithic",
        "confidence": 100
    },
    "api_framework": {
        "name": "Flask",
        "confidence": 90
    },
    "repository_score": {
        "score": 90,
        "grade": "A"
    },
    "suggestions": [
        "Configure a database for the project.",
        "Add Docker support."
    ]
}
```

---

# 📁 Project Structure

```text
backend/
│
├── api/
├── schemas/
├── services/
│   ├── api_service.py
│   ├── architecture_service.py
│   ├── authentication_service.py
│   ├── cicd_service.py
│   ├── database_service.py
│   ├── docker_service.py
│   ├── github_service.py
│   ├── license_service.py
│   ├── metadata_service.py
│   ├── repository_score_service.py
│   ├── suggestion_service.py
│   ├── summary_service.py
│   └── testing_service.py
│
├── utils/
│   ├── confidence_detector.py
│   ├── repository_constants.py
│   ├── repository_scanner.py
│   └── score_detector.py
│
└── main.py
```

---

# 🚀 Development Progress

| Sprint | Description | Status |
|--------|-------------|--------|
| Sprint 1 | Project Planning & Setup | ✅ |
| Sprint 2 | FastAPI Backend | ✅ |
| Sprint 3 | GitHub Repository Integration | ✅ |
| Sprint 4 | Metadata Extraction | ✅ |
| Sprint 5 | Technology Detection Engine | ✅ |
| Sprint 6 | Detection Services & Refactoring | ✅ |
| Sprint 7 | Repository Intelligence | ✅ |
| Sprint 8 | AI Repository Understanding | 🚧 |
| Sprint 9 | Semantic Code Search | ⏳ |
| Sprint 10 | RAG Knowledge Base | ⏳ |
| Sprint 11 | AI Chat Assistant | ⏳ |
| Sprint 12 | Deployment & Optimization | ⏳ |

---

# 🔮 Future Enhancements

- Large Language Model (LLM) Integration
- Semantic Code Search
- Retrieval-Augmented Generation (RAG)
- AI Repository Chat
- Automatic Documentation Generation
- Code Quality Analysis
- Security Analysis
- Multi-Repository Comparison
- Cloud Deployment

---

# 👨‍💻 Author

## Pragadeeswaran

**Backend Developer | Python | FastAPI | PostgreSQL**

Passionate about building intelligent developer tools, scalable backend systems, and AI-powered software engineering solutions.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
