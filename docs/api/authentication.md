# Authentication API

**Base path:** `/api/v1/auth`

## 1. Responsibilities

Authentication establishes identity. Authorization is handled separately by resource services.

## 2. Endpoints

### `POST /register`

Create an account.

**Request**

```json
{
  "email": "learner@example.com",
  "password": "...",
  "displayName": "Learner"
}
```

**Response**

```json
{
  "user": {
    "id": "usr_123",
    "email": "learner@example.com",
    "displayName": "Learner"
  }
}
```

### `POST /login`

Authenticate an existing user and establish the application's session/token.

### `POST /logout`

Invalidate the current session/token as supported by the chosen auth strategy.

### `GET /me`

Return the authenticated user's profile.

### `POST /refresh`

Refresh short-lived access credentials when the chosen auth design uses refresh tokens.

## 3. Authorization model

Roles should remain minimal initially:

- `learner`
- `instructor`
- `admin`

Public lessons require no authentication. User-owned circuits, progress, conversations, and private projects require authorization checks.

## 4. Security

- Hash passwords using a proven password hashing implementation.
- Never log credentials or session tokens.
- Rate-limit login attempts.
- Validate email and password policies server-side.
- Use secure, HTTP-only cookies if using cookie sessions.
- Rotate secrets through deployment configuration.
