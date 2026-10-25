# 🧪 Flask Enterprise Architecture Masterclass

[![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)](https://sqlalchemy.org)
[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

> Complete zero-to-hero curriculum in Flask application architecture, Application Factory design pattern, modular Blueprint structures, SQLAlchemy relational ORM, session authentication, CSRF defense, and automated Pytest test suites.

---

## 🏛️ The 10 Pillars of Flask Architecture

Every pillar is fully implemented with runnable code in the [`pillars/`](pillars/) folder:

1. **[`Pillar 01`](pillars/)**: Application Factory Pattern (`create_app`)
2. **[`Pillar 02`](pillars/)**: Modular Blueprints & Routing Architecture
3. **[`Pillar 03`](pillars/)**: SQLAlchemy Declarative Models & Database Relationships
4. **[`Pillar 04`](pillars/)**: User Authentication with Flask-Login & Password Hashing
5. **[`Pillar 05`](pillars/)**: Forms Validation & Automated CSRF Defense
6. **[`Pillar 06`](pillars/)**: RESTful API Design & JSON Serialization
7. **[`Pillar 07`](pillars/)**: Application Context & Request Context Lifecycles
8. **[`Pillar 08`](pillars/)**: Custom Error Handlers & Defensive HTTP Responses
9. **[`Pillar 09`](pillars/)**: Pytest Unit Testing & Test Client Fixtures
10. **[`Pillar 10`](pillars/)**: Production WSGI Deployment with Gunicorn & Docker

---

## 🛠️ Complete Runnable Flask Application Included

Located in [`teachcloud_flask/`](teachcloud_flask/):
- **Application Factory**: Configured with production and testing presets.
- **Blueprints**: Separated authentication, API, and core routing modules.
- **ORM**: User management models with secure password hashing.
- **Automated Pytest Suite**: Testing endpoints and database transactions.

### Quickstart:
```bash
cd teachcloud_flask
pip install -r ../requirements.txt
python run.py
```

---

## 🧪 Masterclass Examination

Complete your Flask mastery evaluation in [`QUIZ.md`](QUIZ.md), testing your knowledge of thread-local proxies (`current_app`, `g`), blueprint URL prefixes, session signing, and SQLAlchemy session rollback handling.
