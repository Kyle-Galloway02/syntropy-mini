import { createRouter, createWebHistory } from "vue-router";
import Customers from "./views/Customers.vue";
import CustomerDetail from "./views/CustomerDetail.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Customers },
    { path: "/customers/:id", component: CustomerDetail, props: true },
  ],
});
