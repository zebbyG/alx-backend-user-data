# Session Authentication

- 0-Et moi et moi et moi! : has a new endpoint GET /users/me to retrieve the authenticated User object. @app.before_request in api/v1/app.py is updated to assign the result of auth.current_user(request) to request.current_user.

- 1-Empty session: Contains a class SessionAuth in api/v1/auth/session_auth.py that inherits from Auth.
Contains an instance of SessionAuth and assigns it to the variable auth.

- 2-Create a session: Contains a class attribute user_id_by_session_id initialized by an empty dictionary, and an instance method def create_session(self, user_id: str = None) -> str.

- 3-User ID for Session ID: Contains an instance method def user_id_for_session_id(self, session_id: str = None) -> str that returns a User ID based on a Session ID.

- 4-Session cookie: Contains a method def session_cookie(self, request=None) that returns a cookie value from a request.

- 5-Before request: An update on the @app.before_request method in api/v1/app.py:
Add the URL path /api/v1/auth_session/login/ in the list of excluded paths of the method require_auth. If auth.authorization_header(request) and auth.session_cookie(request) return None, abort(401)

- 6-Use Session ID for identifying a User: Contains an instance method def current_user(self, request=None) (overload) that returns a User instance based on a cookie value

- 7-New view for Session Authentication: Contains a new Flask view that handles all routes for the Session authentication. In the file api/v1/views/session_auth.py, there is a route POST /auth_session/login (= POST /api/v1/auth_session/login)
Slash tolerant (/auth_session/login == /auth_session/login/) which uses request.form.get() to retrieve email and password parameters.

- 8-Logout: An update to the class SessionAuth by adding a new method def destroy_session(self, request=None) that deletes the user session / logout.

- 9-Expiration?: Contains a class SessionExpAuth that inherits from SessionAuth in the file api/v1/auth/session_exp_auth.py, Overload def __init__(self) method, which assigns an instance attribute session_duration to the environment variable SESSION_DURATION casts to an integer.

- 10-Sessions in database: Contains a new authentication system, based on Session ID stored in database.
