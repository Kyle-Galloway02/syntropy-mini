<template>
  <div>
    <router-link to="/">← Back</router-link>
    <h1>Customer {{ id }}</h1>

    <form @submit.prevent="submit" style="margin: 1rem 0; display:flex; gap:.5rem;">
      <input type="number" step="0.01" v-model.number="amount" placeholder="Amount" />
      <button type="submit">Add Transaction</button>
    </form>

    <div v-if="msg" style="color:#090">{{ msg }}</div>
    <div v-if="error" style="color:#c00; white-space:pre-wrap">{{ error }}</div>

    <div v-if="isLoading">Loading...</div>
    <table v-else>
      <thead><tr><th>ID</th><th>Amount</th><th>Timestamp</th></tr></thead>
      <tbody>
        <tr v-for="t in txns" :key="t.id">
          <td>{{ t.id }}</td>
          <td>{{ t.amount }}</td>
          <td>{{ t.ts }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { listTransactions, createTransaction, type Txn, login } from "../api";

const route = useRoute();
const id = Number(route.params.id);

const txns = ref<Txn[]>([]);
const isLoading = ref(false);
const error = ref<string | null>(null);
const msg = ref<string | null>(null);
const amount = ref<number | null>(null);

async function load() {
  isLoading.value = true;
  error.value = null;
  msg.value = null;
  try {
    txns.value = await listTransactions(id);
  } catch (e: any) {
    error.value = e?.message ?? "Error loading";
  } finally {
    isLoading.value = false;
  }
}

async function submit() {
  error.value = null;
  msg.value = null;

  if (amount.value == null || Number.isNaN(amount.value)) {
    error.value = "Please enter an amount.";
    return;
  }

  try {
    await createTransaction(id, amount.value);
    msg.value = "Transaction added.";
    amount.value = null;
    await load();
  } catch (e: any) {
    const server = (e?.response && JSON.stringify(e.response.data)) || "";
    error.value = `Create failed: ${e?.message ?? "Unknown"} ${server}`;
  }
}

onMounted(async () => {
  await login(); // sets Authorization header
  await load();
});
</script>
