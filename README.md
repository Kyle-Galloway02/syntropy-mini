# Syntropy Mini

Full-stack demo built to practice end-to-end feature work for a fintech-style dashboard:

- **Frontend:** Vue 3 + TypeScript (Vite)
- **Backend:** FastAPI (Python) with JWT auth
- **Database:** PostgreSQL
- **Local Dev:** Docker Compose
- **IaC:** Terraform stub (generates `.env` consumed by Compose)

> Goal: show ability to design, build, and ship a small feature across the whole stack (list customers, view transactions, create new transactions).

---

## Architecture (high level)
+-----------------------+ +---------------------------+ +------------------+
| Vue 3 + TS (Vite) | Axios | FastAPI (Uvicorn) | ORM | PostgreSQL |
| - Customers view +--------->+ - Auth (JWT) +------->+ customers, |
| - Customer detail | | - /customers | | transactions |
| - Add transaction | | - /customers/{id}/txns | +------------------+
+-----------------------+ +---------------------------+
^ |
| | seeds demo data on startup
+---------------------------------+

---

## What’s included

- **JWT auth** (`/auth/login`) with static admin creds for local demo (`admin/admin`)
- **CRUD slice**:
  - `GET /customers` with simple search/pagination params
  - `GET /customers/{id}/transactions`
  - `POST /customers/{id}/transactions` (create)
- **Automatic DB seeding** on app startup if DB is empty (Ava, Ben + example transactions)
- **CORS** configured for the Vite dev server (`http://localhost:5173`)
- **Terraform** writes a `.env` file Compose reads (no hardcoding secrets in YAML)

---

## Prerequisites

- Docker Desktop
- Node 18+
- (Local dev only) Python is **not** required on host; the API runs in Docker.

---

## Quickstart (Windows / PowerShell)

## 0) Clone
powershell
git clone https://github.com/Kyle-Galloway02/syntropy-mini.git
cd syntropy-mini

## 1) Generate .env via Terraform
cd .\infra\terraform
terraform init
terraform apply -auto-approve
cd ..\..

## 2) Start backend + DB
docker compose up --build

## 3) Start Frontend
cd .\frontend\syntropy-frontend
npm install
npm run dev

### API (quick reference)
## Auth
POST /auth/login
Body: {"username":"admin","password":"admin"}
→ { "access_token": "<jwt>", "token_type": "bearer" }

## Customers
POST /auth/login
Body: {"username":"admin","password":"admin"}
→ { "access_token": "<jwt>", "token_type": "bearer" }

## Transactions
GET /customers/{id}/transactions
→ 200 [{id, amount, ts}, ...]

## POST /customers/{id}/transactions
Body: { "amount": 12.34 }
→ 200 {id, amount, ts}



## Development workflow highlights

Infrastructure as Code: Terraform writes .env; Compose pulls variables via ${VAR}.

Repeatable startup: FastAPI startup hook seeds data if the customers table is empty.

Local-friendly: Everything runs on localhost; CORS set to Vite origin.

Auth first: Frontend performs POST /auth/login on mount, then sets Authorization on Axios.


## Verification Script (powershell)
"== Health =="; (Invoke-WebRequest http://localhost:8000/health).Content
"== Login =="; $body=@{username="admin";password="admin"}|ConvertTo-Json; $login=Invoke-RestMethod -Method Post -Uri http://localhost:8000/auth/login -Body $body -ContentType "application/json"; $token=$login.access_token; $headers=@{Authorization="Bearer $token"}
"== Customers =="; $customers=Invoke-RestMethod -Method Get -Uri http://localhost:8000/customers -Headers $headers; $customers|Format-Table id,name,email -AutoSize
if($customers){ $cid=$customers[0].id; "== Txns for customer $cid =="; Invoke-RestMethod -Method Get -Uri ("http://localhost:8000/customers/{0}/transactions" -f $cid) -Headers $headers | Format-Table id,amount,ts -AutoSize }

## Screenshots

### Customer list loaded
![Customers List](./screenshots/Screenshot%202025-09-04%20094937.png)

### Search filter applied
![Search Filter](./screenshots/Screenshot%202025-09-04%20094946.png)

### Customer detail view
![Customer Detail](./screenshots/Screenshot%202025-09-04%20094953.png)

### Adding a transaction
![Add Transaction](./screenshots/Screenshot%202025-09-04%20095004.png)

### Updated transaction list
![Updated Transactions](./screenshots/Screenshot%202025-09-04%20095011.png)


