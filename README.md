# Syntropy Mini

Full-stack demo app using **Vue 3 + TypeScript**, **FastAPI**, **Postgres**, **Docker Compose**, and a tiny **Terraform** stub.  
Built to practice end-to-end feature work for a banking/fintech-style dashboard.

## Stack
- Frontend: Vue 3 (Vite, TS)
- Backend: FastAPI (JWT auth)
- DB: Postgres
- Local: Docker Compose
- IaC: Terraform (stub)

## Run (local)
1) Start backend + DB:
   docker compose up --build

2) Start frontend:
   cd frontend/syntropy-frontend
   npm install
   npm run dev

## API quickstart
1. POST /auth/login  with {"username":"admin","password":"admin"} → copy token
2. Use header Authorization: Bearer <token> for:
   - GET /customers
   - GET /customers/{id}/transactions

## Notes
- Demo schemas: customers, transactions
- Pagination: limit & offset
- CORS: SPA origin http://localhost:5173
