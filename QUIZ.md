# 📝 Current Weekly Assessment — Edition #43

> **Subject / Focus Area**: Flask Framework
> **7-Day Cycle Period**: 2026-10-22 to 2026-10-29 UTC
> **Total Questions**: 16
> **Location**: `docs/Quiz/`

---

## 📋 Assessment Overview
This examination comprises the 7-day rotating test bank for **Flask Framework**.
Each question tests real-world systems architecture, cloud services, and production engineering practices.

---

## ❓ Questions & Verified Solutions

### Question 1: What is Werkzeug in relation to Flask?

- [x] **The underlying WSGI web application utility library upon which Flask is built** *(Correct Answer)*
- [ ] A database ORM engine
- [ ] A CSS styling grid framework
- [ ] A JavaScript testing tool

> **💡 Engineering Context & Rationale**:
> Flask relies on <strong>Werkzeug</strong> for WSGI request/response handling, routing lookup, and security utility functions.

---

### Question 2: What is the execution order of `@app.before_request` functions in Flask?

- [x] **Executed before every request is dispatched to its targeted route handler function** *(Correct Answer)*
- [ ] Executed only when database errors occur
- [ ] Executed after response body is sent
- [ ] Executed once at server boot time

> **💡 Engineering Context & Rationale**:
> Functions marked with <strong>@app.before_request</strong> run prior to view execution, ideal for connection handling or authentication checks.

---

### Question 3: What is the purpose of `url_for()` function in Flask templates and views?

- [x] **Generates a URL to a specific endpoint function based on its function name, avoiding hardcoded paths** *(Correct Answer)*
- [ ] Redirects the user to an external domain
- [ ] Fetches JSON data from remote URLs
- [ ] Validates URL syntax strings

> **💡 Engineering Context & Rationale**:
> <strong>url_for()</strong> dynamically builds paths relative to application endpoints, ensuring links automatically adapt if routes change.

---

### Question 4: What does Flask `jsonify()` helper function do?

- [x] **Converts Python dicts or lists into a JSON HTTP response object with content-type `application/json`** *(Correct Answer)*
- [ ] Parses incoming JSON text from requests
- [ ] Encrypts JSON strings using AES
- [ ] Validates JSON syntax schemas

> **💡 Engineering Context & Rationale**:
> <code>jsonify()</code> serializes payload data structures into proper JSON responses formatted with `200 OK` status.

---

### Question 5: How do you define custom CLI commands in Flask?

- [x] **Use `@app.cli.command()` decorator to register Click terminal commands** *(Correct Answer)*
- [ ] Write bash scripts in `/bin/`
- [ ] Modify system systemd services
- [ ] Override python built-in functions

> **💡 Engineering Context & Rationale**:
> Flask integrates with <strong>Click</strong>, allowing developers to create custom management commands registered via `@app.cli.command()`.

---

### Question 6: What is the purpose of `secure_filename()` from Werkzeug in Flask file upload handling?

- [x] **Sanitizes uploaded file names to prevent directory traversal security vulnerabilities** *(Correct Answer)*
- [ ] Encrypts uploaded file contents on disk
- [ ] Renames files to random UUIDs
- [ ] Compresses images before saving

> **💡 Engineering Context & Rationale**:
> <code>secure_filename()</code> removes unsafe path characters (e.g. `../`) from user-submitted file names to prevent arbitrary file overwrites.

---

### Question 7: How does Flask-Migrate handle database migrations?

- [x] **Wraps Alembic to provide command line database migration workflows (`flask db migrate`, `flask db upgrade`)** *(Correct Answer)*
- [ ] Recreates database tables from scratch every run
- [ ] Exports database tables to CSV format
- [ ] Translates SQL queries to MongoDB syntax

> **💡 Engineering Context & Rationale**:
> <strong>Flask-Migrate</strong> integrates Alembic migration tracking seamlessly with Flask-SQLAlchemy models.

---

### Question 8: Which templating engine is built into Flask by default?

- [x] **Jinja2** *(Correct Answer)*
- [ ] Django Templates
- [ ] Mustache
- [ ] Handlebars

> **💡 Engineering Context & Rationale**:
> Flask uses <strong>Jinja2</strong> as its default templating engine, supporting template inheritance, macros, and expression evaluation.

---

### Question 9: What is a Flask Blueprint?

- [x] **A way to organize and structure related views, routes, and static assets into reusable application modules** *(Correct Answer)*
- [ ] A database schema diagram builder
- [ ] A CSS styling grid framework
- [ ] A deployment playbook for Ansible

> **💡 Engineering Context & Rationale**:
> <strong>Blueprints</strong> allow developers to break large Flask applications into isolated sub-modules registered on the main app instance.

---

### Question 10: What is the role of Flask-Login extension?

- [x] **Manages user session state, handles login/logout procedures, and restricts routes via `@login_required`** *(Correct Answer)*
- [ ] Enforces password complexity rules
- [ ] Sends account activation emails
- [ ] Generates HTML login forms

> **💡 Engineering Context & Rationale**:
> <strong>Flask-Login</strong> handles user session persistence, storing user IDs in secure session cookies and providing `current_user` helpers.

---

### Question 11: What is WSGI (Web Server Gateway Interface) in Flask application deployment?

- [x] **The standard specification defining how web servers (like Nginx/Gunicorn) communicate with Python web applications** *(Correct Answer)*
- [ ] A database query language
- [ ] A client-side JavaScript engine
- [ ] A CSS preprocessor

> **💡 Engineering Context & Rationale**:
> <strong>WSGI</strong> acts as a standardized bridge between production web servers and Python application frameworks.

---

### Question 12: How does Flask-WTF enhance security in HTML web forms?

- [x] **Provides automatic CSRF token generation and validation for web form submissions** *(Correct Answer)*
- [ ] Encrypts form inputs in transit
- [ ] Disables JavaScript on client browsers
- [ ] Stores passwords in plain text

> **💡 Engineering Context & Rationale**:
> <strong>Flask-WTF</strong> integrates WTForms with Flask, automatically validating hidden CSRF protection tokens on submitted forms.

---

### Question 13: What is the Flask Application Context vs Request Context?

- [x] **Application Context manages application-level data (`current_app`, `g`); Request Context manages request-level data (`request`, `session`)** *(Correct Answer)*
- [ ] Application Context runs on client side; Request Context runs on server side
- [ ] Request Context is permanent
- [ ] They are exact aliases

> **💡 Engineering Context & Rationale**:
> Flask splits context into <strong>Application Context</strong> (bound to app configuration) and <strong>Request Context</strong> (bound to active HTTP request thread).

---

### Question 14: Why must `app.config['SECRET_KEY']` be set in a Flask application?

- [x] **Required to cryptographically sign session cookies and protect against session tampering** *(Correct Answer)*
- [ ] Required to enable debug mode
- [ ] Required to bind to localhost IP
- [ ] Required to parse JSON request bodies

> **💡 Engineering Context & Rationale**:
> Without a secure <strong>SECRET_KEY</strong>, Flask cannot sign session cookies or validate WTForms CSRF tokens securely.

---

### Question 15: What is Flask-SQLAlchemy?

- [x] **An extension that adds SQLAlchemy support to Flask applications, simplifying ORM database session management** *(Correct Answer)*
- [ ] A raw SQL query parsing library
- [ ] A NoSQL driver for MongoDB
- [ ] A template engine replacement for Jinja

> **💡 Engineering Context & Rationale**:
> <strong>Flask-SQLAlchemy</strong> binds SQLAlchemy's ORM seamlessly to Flask's application context and lifecycle.

---

### Question 16: How do you set a response cookie in Flask?

- [x] **Create a response object using `make_response()` and call `response.set_cookie('name', 'value')`** *(Correct Answer)*
- [ ] Modify `request.headers` directly
- [ ] Use `session['cookie'] = value`
- [ ] Write directly to `/tmp/cookies.txt`

> **💡 Engineering Context & Rationale**:
> Cookies are set on the outbound HTTP response object using <strong>response.set_cookie()</strong>.

---

## 🏆 End of Assessment
*TeachCloud Automated Quiz Engine — Edition #43 (Active Week).*
