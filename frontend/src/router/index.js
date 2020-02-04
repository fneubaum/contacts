import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: { name: "contacts" }
  },
  {
    path: "/contact",
    name: "contacts",
    component: () => import("../views/ContactList.vue")
  },
  {
    path: "/contact/:id",
    name: "contactDetail",
    component: () => import("../views/ContactDetail.vue")
  }
];

const router = new VueRouter({
  routes
});

export default router;
