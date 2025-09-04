<template>
  <main>
    <nav style="display:flex; gap:1rem; padding:1rem; border-bottom:1px solid #eee;">
      <router-link to="/">Customers</router-link>
    </nav>
    <section style="padding:1rem;">
      <router-view />
    </section>
  </main>
</template>

<script setup lang="ts">
// no script needed; the router renders pages
</script>

<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial; }
a { text-decoration: none; }
a.router-link-active { font-weight: 600; }
table { border-collapse: collapse; }
th, td { padding: .5rem .75rem; border-bottom: 1px solid #eee; text-align: left; }
input { padding: .5rem .75rem; border: 1px solid #ddd; border-radius: 6px; }
</style>
