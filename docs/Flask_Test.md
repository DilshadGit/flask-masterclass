# Flask Platform Testing Guide

A practical shell-based workflow for testing a Flask platform from development through production preparation.

---

## 1. Activate Your Virtual Environment

Go to your Flask project:

```bash
cd /path/to/your/flask-project
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

If your virtual environment has another name, for example `cloud_flask`:

```bash
source cloud_flask/bin/activate
```

Check Python and pip:

```bash
which python
python --version
pip --version
```

---

## 2. Check Python Syntax

Compile all Python files:

```bash
python -m compileall .
```

If there are no syntax errors, Python files should compile successfully.

Find Python files:

```bash
find . -name "*.py"
```

Test an individual file:

```bash
python -m py_compile app.py
```

If you see:

```text
SyntaxError: invalid syntax
```

check the filename and line number shown by Python.

---

## 3. Check Installed Packages

Run:

```bash
pip check
```

A healthy environment normally reports:

```text
No broken requirements found.
```

If your project has `requirements.txt`:

```bash
pip install -r requirements.txt
```

Then run:

```bash
pip check
```

Check Flask:

```bash
python -c "import flask; print(flask.__version__)"
```

---

## 4. Start Flask From the Shell

For an application called `app.py`:

```bash
flask --app app run
```

For development/debugging:

```bash
flask --app app run --debug
```

If your project uses an application factory:

```bash
flask --app "app:create_app()" run --debug
```

If the Flask package is called `cloud_app`:

```bash
flask --app cloud_app run --debug
```

Keep this terminal open. Flask errors and tracebacks will normally appear here.

---

## 5. Test the Server From Another Terminal

Keep Flask running in Terminal 1.

Open Terminal 2 and run:

```bash
curl http://127.0.0.1:5000/
```

Or inspect only the HTTP headers:

```bash
curl -I http://127.0.0.1:5000/
```

A successful response normally includes:

```text
HTTP/1.1 200 OK
```

Test important pages:

```bash
curl -I http://127.0.0.1:5000/
curl -I http://127.0.0.1:5000/about
curl -I http://127.0.0.1:5000/contact
curl -I http://127.0.0.1:5000/login
```

### Common results

`404 NOT FOUND`

Usually means the route does not exist or the URL is incorrect.

`500 INTERNAL SERVER ERROR`

Look at Terminal 1. The Flask traceback normally identifies the source of the error.

---

## 6. How to Read a Flask Error

Example:

```text
Traceback (most recent call last):
  File ".../views.py", line 45, in dashboard
    posts = Post.query.all()
NameError: name 'Post' is not defined
```

Read the traceback from the bottom upward.

The most important part is usually the final exception:

```text
NameError: name 'Post' is not defined
```

And the file/line:

```text
views.py, line 45
```

Open the file:

```bash
nano views.py
```

Or, if you use VS Code:

```bash
code views.py
```

Inspect the code around the reported line.

---

## 7. Display All Flask Routes

One of the most useful Flask checks is:

```bash
flask --app app routes
```

Example:

```text
Endpoint          Methods    Rule
----------------  ---------  ----------------
main.index        GET        /
main.about       GET        /about
main.contact     GET,POST   /contact
auth.login       GET,POST   /login
auth.logout      GET        /logout
```

This helps you identify missing or incorrectly registered routes.

Save the route list:

```bash
flask --app app routes > routes.txt
```

View it:

```bash
cat routes.txt
```

---

## 8. Test Templates

If Flask reports:

```text
jinja2.exceptions.TemplateNotFound
```

check your templates:

```bash
find . -type f | grep templates
```

A typical Flask structure is:

```text
project/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── contact.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

If your code contains:

```python
return render_template("contact.html")
```

you normally need:

```text
templates/contact.html
```

Check spelling and capitalization carefully.

---

## 9. Check the Database

If using SQLite:

```bash
find . -name "*.db"
```

Check database file size:

```bash
ls -lh *.db
```

Open a SQLite database:

```bash
sqlite3 your_database.db
```

Inside SQLite:

```sql
.tables
```

Check the schema:

```sql
.schema
```

Exit:

```sql
.quit
```

### Database environment variables

If your application uses `DATABASE_URL`, check that it exists:

```bash
echo "$DATABASE_URL"
```

Do not expose passwords or complete production database URLs in shared logs or screenshots.

For production systems, test database migrations against a separate/staging database before touching the live database.

---

## 10. Run Automated Tests

If your project contains a `tests` directory:

```bash
pytest
```

More detail:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_auth.py -v
```

Stop at the first failure:

```bash
pytest -x
```

Very detailed output:

```bash
pytest -vv
```

Recommended development workflow:

```bash
pytest -x
```

Fix the first failure, then run the tests again.

---

## 11. Check for Development/Debug Code

Search for `print()` statements:

```bash
grep -R "print(" . --include="*.py"
```

Search for TODO/FIXME comments:

```bash
grep -R "TODO\|FIXME" . --include="*.py"
```

Search for hard-coded debug mode:

```bash
grep -R "debug=True" . --include="*.py"
```

Search for Flask's built-in development server:

```bash
grep -R "app.run" . --include="*.py"
```

For production, do not rely on:

```python
app.run(debug=True)
```

Use a production WSGI server such as Gunicorn instead.

---

# 12. Complete Basic Flask Testing Sequence

A useful first-pass testing sequence is:

```bash
cd /path/to/project

source venv/bin/activate

python --version

pip check

python -m compileall .

flask --app app routes

pytest -v

flask --app app run --debug
```

Then, from another terminal:

```bash
curl -I http://127.0.0.1:5000/
curl -I http://127.0.0.1:5000/login
curl -I http://127.0.0.1:5000/contact
```

---

# 13. Manual Functional Testing

After the technical checks, manually test the important user journeys.

Recommended flow:

```text
Home
  ↓
Registration
  ↓
Login
  ↓
Dashboard
  ↓
Create
  ↓
Read
  ↓
Update
  ↓
Delete
  ↓
Logout
  ↓
Login again
  ↓
Password reset
  ↓
Profile
  ↓
Comments
  ↓
Other important pages
```

For every feature, check:

- Page loads correctly
- Forms display correctly
- Validation works
- Successful submissions work
- Invalid submissions are handled
- Authentication works
- Authorization works
- Database records are correct
- Images/files work
- Redirects work
- Error pages work
- Logout works
- Mobile layout works
- Static CSS and JavaScript load correctly

---

# 14. Common Flask Errors and Where to Look

| Error | First thing to check |
|---|---|
| `SyntaxError` | Python file and reported line |
| `ModuleNotFoundError` | Virtual environment and installed packages |
| `ImportError` | Package version and import path |
| `TemplateNotFound` | `templates/` location and filename |
| `BuildError` | Flask route/endpoint name |
| `404` | URL and registered routes |
| `405` | HTTP method (`GET`/`POST`) |
| `500` | Flask traceback |
| `OperationalError` | Database connection/schema |
| `IntegrityError` | Database constraints |
| `UndefinedError` | Jinja variable/template |
| `PermissionError` | Linux file/directory permissions |
| `502 Bad Gateway` | Gunicorn, systemd, then Nginx |
| Missing CSS/JS | `static/` configuration/path |

---

# 15. Understanding 404 Errors

Check the available routes:

```bash
flask --app app routes
```

Then compare the requested URL with the route.

For example:

```python
@app.route("/contact")
def contact():
    ...
```

The correct URL is:

```text
/contact
```

Test it:

```bash
curl -I http://127.0.0.1:5000/contact
```

---

# 16. Understanding 405 Errors

A `405 Method Not Allowed` usually means the route exists, but the HTTP method is not allowed.

For example:

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    ...
```

The route accepts both:

```text
GET
POST
```

If a route only accepts:

```python
@app.route("/login", methods=["POST"])
```

a normal browser GET request can produce a 405 response.

---

# 17. Understanding 500 Errors

When you receive:

```text
500 INTERNAL SERVER ERROR
```

do not immediately change random files.

First:

1. Look at the Flask terminal.
2. Find the traceback.
3. Read the final exception.
4. Identify the file.
5. Identify the line.
6. Inspect the surrounding code.
7. Fix the underlying problem.
8. Restart Flask if necessary.
9. Run the same test again.
10. Run your automated tests.

Example:

```text
File ".../views.py", line 45
NameError: name 'Post' is not defined
```

Start with `views.py` around line 45.

---

# 18. Testing Static Files

Check your static directory:

```bash
find static -type f
```

Typical structure:

```text
static/
├── css/
│   └── style.css
├── js/
│   └── app.js
└── images/
    └── logo.png
```

Test a CSS file:

```bash
curl -I http://127.0.0.1:5000/static/css/style.css
```

A successful response should normally return:

```text
HTTP/1.1 200 OK
```

If CSS or JavaScript is missing, inspect:

- Flask static configuration
- HTML `<link>`/`<script>` paths
- `url_for("static", ...)`
- Filename spelling
- File permissions

---

# 19. Test Forms

For each form, test both valid and invalid data.

Example registration tests:

```text
Valid email
Valid password
Missing email
Invalid email
Missing password
Short password
Existing email
Different password confirmation
```

Test login:

```text
Correct email + correct password
Correct email + wrong password
Unknown email + password
Missing email
Missing password
```

Do not only test the successful path.

---

# 20. Authentication and Authorization Testing

For protected pages, test:

```text
Anonymous user
    ↓
Protected URL
    ↓
Should be redirected or denied
```

Then:

```text
Logged-in normal user
    ↓
User dashboard
    ↓
Allowed
```

Then test administrator-only pages:

```text
Normal user
    ↓
Admin URL
    ↓
Should be denied
```

And:

```text
Administrator
    ↓
Admin URL
    ↓
Allowed
```

This is especially important for platforms containing users, staff, administrators, posts, records, or other sensitive data.

---

# 21. Database Safety Before Deployment

For a live Flask platform, do not test destructive operations directly against the production database.

Before deployment:

1. Create a verified live database backup.
2. Keep the backup outside the application directory.
3. Test the new version using a staging/test database.
4. Test migrations against the staging database.
5. Verify existing records remain intact.
6. Verify users remain intact.
7. Verify posts remain intact.
8. Verify images/files remain accessible.
9. Verify comments and other related records.
10. Verify database counts before and after migration.
11. Only then plan the production deployment.

Do not run destructive database commands against production unless you have deliberately verified the operation and have a tested backup.

---

# 22. Production Server Testing

For production, Flask's development server should not be used as the production application server.

A common architecture is:

```text
Internet
   ↓
Nginx
   ↓
Gunicorn
   ↓
Flask
   ↓
Database
```

Test each layer separately.

### Test Flask/Gunicorn locally

Example:

```bash
gunicorn -w 4 -b 127.0.0.1:8000 app:app
```

The exact module/application name depends on your project.

Test:

```bash
curl -I http://127.0.0.1:8000/
```

If this fails, investigate Gunicorn/Flask before investigating Nginx.

---

# 23. If You Receive a 502 Bad Gateway

A 502 from Nginx often means Nginx cannot successfully communicate with the upstream application server.

Check Gunicorn:

```bash
sudo systemctl status gunicorn
```

Check Gunicorn logs:

```bash
sudo journalctl -u gunicorn -n 100 --no-pager
```

Check Nginx:

```bash
sudo nginx -t
```

Then:

```bash
sudo systemctl status nginx
```

Check Nginx error logs:

```bash
sudo tail -n 100 /var/log/nginx/error.log
```

A useful order is:

```text
Flask
  ↓
Gunicorn
  ↓
Local curl
  ↓
Nginx
  ↓
External browser
```

Do not assume Nginx is the problem until Gunicorn has been checked.

---

# 24. Check Linux File Permissions

If you receive:

```text
PermissionError
```

check:

```bash
ls -la
```

For a particular directory:

```bash
ls -ld uploads
```

For files:

```bash
ls -l uploads/
```

Be careful with commands such as:

```bash
chmod -R 777 .
```

Do not use overly permissive permissions as a quick fix on a production server.

---

# 25. Recommended Testing Order

Use this order when debugging a Flask application:

```text
1. Python version
       ↓
2. Virtual environment
       ↓
3. Dependencies
       ↓
4. Python syntax
       ↓
5. Flask import/startup
       ↓
6. Flask routes
       ↓
7. Templates
       ↓
8. Static files
       ↓
9. Database
       ↓
10. Automated tests
       ↓
11. Manual functional tests
       ↓
12. Gunicorn
       ↓
13. Nginx
       ↓
14. External browser
```

This prevents you from trying to fix Nginx when the actual problem is inside Flask.

---

# 26. Quick Diagnostic Commands

### Python

```bash
python --version
which python
```

### Pip

```bash
pip --version
pip check
pip list
```

### Syntax

```bash
python -m compileall .
```

### Routes

```bash
flask --app app routes
```

### Tests

```bash
pytest -v
```

### Server

```bash
flask --app app run --debug
```

### HTTP

```bash
curl -I http://127.0.0.1:5000/
```

### Files

```bash
find . -name "*.py"
find . -type f | grep templates
find static -type f
```

### Search for debug code

```bash
grep -R "debug=True" . --include="*.py"
grep -R "app.run" . --include="*.py"
```

### Production

```bash
sudo nginx -t
sudo systemctl status nginx
sudo systemctl status gunicorn
sudo journalctl -u gunicorn -n 100 --no-pager
```

---

# 27. Final Pre-Deployment Checklist

Before deploying a Flask platform:

## Application

- [ ] Python version confirmed
- [ ] Virtual environment confirmed
- [ ] Dependencies installed
- [ ] `pip check` passes
- [ ] Python syntax checked
- [ ] Flask starts without errors
- [ ] All routes checked
- [ ] Templates checked
- [ ] Static files checked
- [ ] Environment variables checked
- [ ] Secrets are not hard-coded
- [ ] Debug mode disabled for production

## Database

- [ ] Production database backed up
- [ ] Backup verified
- [ ] Migration tested separately
- [ ] Existing records verified
- [ ] Users verified
- [ ] Posts/content verified
- [ ] Images/files verified
- [ ] Database permissions checked
- [ ] No destructive migration is planned without review

## Testing

- [ ] `pytest` passes
- [ ] Registration tested
- [ ] Login tested
- [ ] Logout tested
- [ ] Password reset tested
- [ ] Profile tested
- [ ] Authorization tested
- [ ] CRUD operations tested
- [ ] Forms tested with invalid data
- [ ] Error pages tested
- [ ] Mobile/browser testing completed

## Production

- [ ] Gunicorn tested
- [ ] Nginx configuration tested
- [ ] `nginx -t` passes
- [ ] Gunicorn service running
- [ ] Nginx service running
- [ ] Local upstream tested
- [ ] HTTPS tested
- [ ] External domain tested
- [ ] 404 tested
- [ ] 500 tested
- [ ] 502 troubleshooting path confirmed
- [ ] Logs checked

---

# 28. The Most Important Rule

When something fails, do not change many things at once.

Use this process:

```text
ERROR
  ↓
Read the exact error
  ↓
Find the file
  ↓
Find the line
  ↓
Understand the cause
  ↓
Make one controlled change
  ↓
Run the same test again
  ↓
Run the complete test suite
```

This makes Flask debugging much safer and makes it easier to know which change actually fixed the problem.

---

# 29. Simple Daily Flask Testing Routine

For normal development, this is a useful routine:

```bash
cd /path/to/project

source venv/bin/activate

python --version

pip check

python -m compileall .

flask --app app routes

pytest -v

flask --app app run --debug
```

Then in another terminal:

```bash
curl -I http://127.0.0.1:5000/
curl -I http://127.0.0.1:5000/login
curl -I http://127.0.0.1:5000/contact
```

Finally, manually test the important user journeys in your browser.

---

# 30. Important Production Reminder

Development testing and production deployment are different.

Use a separate test/staging environment whenever possible.

For a live platform containing real records:

```text
LIVE DATABASE
     ↓
VERIFIED BACKUP
     ↓
STAGING/TEST DATABASE
     ↓
TEST NEW FLASK VERSION
     ↓
RUN AUTOMATED TESTS
     ↓
TEST MANUALLY
     ↓
CHECK MIGRATIONS
     ↓
CHECK BACKUP AGAIN
     ↓
DEPLOY CAREFULLY
     ↓
VERIFY LIVE SYSTEM
```

Never assume that because Flask works on your local machine, the production deployment will automatically work.

Check the application, database, Gunicorn, Nginx, environment variables, file permissions, static files, domain, HTTPS, logs, and backups separately.
