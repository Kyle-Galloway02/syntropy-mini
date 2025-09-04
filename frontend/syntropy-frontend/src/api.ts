import axios from "axios";
const api = axios.create({ baseURL: "http://localhost:8000" });

export async function login() {
  const { data } = await api.post("/auth/login", { username: "admin", password: "admin" });
  api.defaults.headers.common["Authorization"] = `Bearer ${data.access_token}`;
}

export type Customer = { id: number; name: string; email: string };
export type Txn = { id: number; amount: number; ts: string };

export async function listCustomers(q?: string, limit = 20, offset = 0): Promise<Customer[]> {
  const { data } = await api.get("/customers", { params: { q, limit, offset } });
  return data;
}

export async function listTransactions(customerId: number, limit = 20, offset = 0): Promise<Txn[]> {
  const { data } = await api.get(`/customers/${customerId}/transactions`, { params: { limit, offset } });
  return data;
}

export async function createTransaction(customerId: number, amount: number): Promise<Txn> {
  const { data } = await api.post(`/customers/${customerId}/transactions`, { amount });
  return data;
}

export default api;
