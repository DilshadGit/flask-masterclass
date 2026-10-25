# 🎓 Flask Masterclass Quiz (24 Questions & Complete Answer Key)

1. **What is the Application Factory pattern in Flask?**
   - Answer: A function (e.g. `create_app()`) that configures and returns Flask app instances, enabling flexible testing and multiple environments.
2. **What is a Flask Blueprint?**
   - Answer: A way to organize related routes, templates, and static files into modular components.
3. **How do you access JSON payloads in a POST request?**
   - Answer: `request.get_json()`
4. **Which ORM extension is standard for Flask?**
   - Answer: `Flask-SQLAlchemy`
5. **How do you store flash messages across redirects?**
   - Answer: `flash('Message text')` and `get_flashed_messages()` in templates.
6. **What is 'g' in Flask?**
   - Answer: An application context global object used to store data during a single request lifecycle.
7. **How do you generate URLs dynamically?**
   - Answer: `url_for('blueprint.endpoint_name', param=value)`
8. **What does 'render_template()' do?**
   - Answer: Renders a Jinja2 template file with passed keyword arguments.
9. **How do you define URL route parameters?**
   - Answer: `<converter:variable_name>` (e.g. `/user/<int:user_id>`).
10. **How do you handle 404 errors with a custom template?**
    - Answer: `@app.errorhandler(404)`
11. **Which command commits database changes in SQLAlchemy?**
    - Answer: `db.session.commit()`
12. **How do you rollback a transaction on database error?**
    - Answer: `db.session.rollback()`
13. **What is the difference between app context and request context?**
    - Answer: App context holds application-level state (e.g., config, db); request context holds HTTP request data (request, session).
14. **How do you write unit tests in Flask?**
    - Answer: `client = app.test_client()` and `client.get('/')`.
15. **What is WTForms used for in Flask?**
    - Answer: Form generation, CSRF protection, and server-side input validation.
16. **How to protect routes from unauthenticated users?**
    - Answer: Custom decorator or `flask_login.login_required`.
17. **Which setting must NEVER be True in production?**
    - Answer: `app.config['DEBUG'] = True`
18. **What WSGI server is recommended for deploying Flask?**
    - Answer: Gunicorn or uWSGI.
19. **How to return custom status codes from a Flask route?**
    - Answer: `return jsonify(data), 201`
20. **What is 'current_app' proxy?**
    - Answer: A thread-safe proxy pointing to the application handling the current request.
21. **How do you hash passwords securely in Flask?**
    - Answer: `werkzeug.security.generate_password_hash()`.
22. **What does 'before_request' hook do?**
    - Answer: Executes a function before each incoming HTTP request.
23. **How do you stream file downloads in Flask?**
    - Answer: `send_file()` or `send_from_directory()`.
24. **How do you manage database schema migrations in Flask?**
    - Answer: `Flask-Migrate` (backed by Alembic).
