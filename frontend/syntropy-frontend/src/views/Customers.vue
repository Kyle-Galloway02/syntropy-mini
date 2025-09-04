<template>
  <div>
    <h1>Customers</h1>

    <div>
      <input v-model="q" placeholder="Search..." @keyup.enter="refresh" />
      <button @click="refresh">Load</button>
    </div>

    <div v-if="isLoading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>

   <ul v-else>
  <li v-for="c in customers" :key="c.id">
    <router-link :to="`/customers/${c.id}`">{{ c.name }} - {{ c.email }}</router-link>
  </li>
</ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { login, listCustomers, type Customer } from "../api";

const router = useRouter();

const customers = ref<Customer[]>([]);
const isLoading = ref(false);
const error = ref<string | null>(null);
const q = ref("");

async function refresh() {
  try {
    isLoading.value = true;
    error.value = null;
    customers.value = await listCustomers(q.value || undefined);
  } catch (e: any) {
    error.value = e?.message ?? "Error loading customers";
  } finally {
    isLoading.value = false;
  }
}

function go(id: number) {
  router.push(/customers/);
}

onMounted(async () => {
  await login();
  await refresh();
});
</script>
