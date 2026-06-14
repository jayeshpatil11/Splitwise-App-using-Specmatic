# Splitwise-like Expense Sharing Application using Specmatic

A contract-first Expense Sharing Application inspired by Splitwise, built using FastAPI, OpenAPI 3.0, and Specmatic.

This project demonstrates how executable API contracts can eliminate integration uncertainty by serving as a single source of truth for developers, testers, and AI coding agents.

---

## Objective

In traditional software development, frontend and backend teams often make assumptions about API behavior, leading to integration issues discovered late in the development cycle.

This project uses Specmatic to:

- Define APIs as executable contracts
- Generate mock servers directly from OpenAPI specifications
- Validate backend implementations through contract testing
- Reduce integration uncertainty
- Enable AI coding agents to build against a precise specification

---

## Tech Stack

- FastAPI
- Python
- OpenAPI 3.0
- Specmatic
- Docker

---

## API Operations

### Groups

| Method | Endpoint |
|----------|----------|
| POST | /groups |
| GET | /groups/{groupId} |

### Expenses

| Method | Endpoint |
|----------|----------|
| POST | /expenses |
| GET | /expenses |

### Balances

| Method | Endpoint |
|----------|----------|
| GET | /balances/{userId} |

### Settlements

| Method | Endpoint |
|----------|----------|
| POST | /settlements |

---

## Project Structure

```text
splitwise-specmatic-demo
│
├── openapi
│   └── expense-sharing-api.yaml
│
├── backend
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── requirements.txt
│
├── specmatic.yaml
│
├── screenshots
│
└── README.md
```

---

## Contract-First Workflow

```text
OpenAPI Contract
        ↓
Specmatic Mock Server
        ↓
FastAPI Implementation
        ↓
Specmatic Contract Testing
        ↓
Verified Integration
```

The OpenAPI specification acts as the single source of truth throughout the development lifecycle.

---

## Running the Backend

Navigate to the backend directory:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## Running Specmatic Mock Server

Generate a mock server directly from the OpenAPI contract:

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
-v /c/splitwise-specmatic-demo:/work \
-w /work \
specmatic/specmatic mock openapi/expense-sharing-api.yaml
```

Specmatic automatically creates mock endpoints based on the contract.

---

## Running Contract Tests

Start the FastAPI server and execute:

```bash
MSYS_NO_PATHCONV=1 docker run --rm \
-v /c/splitwise-specmatic-demo:/work \
-w /work \
--add-host=host.docker.internal:host-gateway \
specmatic/specmatic test \
--testBaseURL=http://host.docker.internal:8000 \
openapi/expense-sharing-api.yaml
```

Specmatic validates:

- Response status codes
- Response schema
- Required fields
- Data types

---

## Example API

### Create Group

Request:

```json
{
  "name": "Goa Trip"
}
```

Response:

```json
{
  "groupId": 1,
  "name": "Goa Trip"
}
```

---

## Why Specmatic?

Specmatic transforms OpenAPI specifications into executable contracts.

Benefits include:

- Early integration testing
- Automated contract validation
- Mock generation
- Faster feedback cycles
- Reduced integration failures
- Improved AI-assisted development

---

## How This Helps AI Coding Agents

AI coding agents often generate code based on assumptions.

By providing an executable OpenAPI contract, AI agents receive:

- Precise endpoint definitions
- Request schemas
- Response schemas
- Validation rules

This significantly reduces ambiguity and improves generated code quality.

---

## Key Learnings

Through this project I learned:

- Contract-first API development
- OpenAPI specification design
- Mock generation using Specmatic
- Contract testing
- Integration validation
- Executable contracts for AI-assisted development

---

## Future Enhancements

- User Management
- Group Members
- Expense Splitting Logic
- Authentication and Authorization
- Database Integration
- Microservices Architecture
- CI/CD Contract Validation


