<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
        />

        <q-toolbar-title>Contacts</q-toolbar-title>

      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-2"
    >
      <q-list>
        <q-input
          dense
          standout="bg-grey-14 text-white"
          v-model="search"
          input-class="text-right"
          class="q-ma-md"
        >
          <template v-slot:append>
            <q-icon v-if="search === ''" name="search" />
            <q-icon
              v-else
              name="clear"
              class="cursor-pointer"
              @click="text = ''"
            />
          </template>
        </q-input>
        <q-item-label header>Contacts</q-item-label>
        <q-item clickable v-ripple to="/contact" exact>
          <q-item-section avatar>
            <q-icon name="people" />
          </q-item-section>
          <q-item-section>
            <q-item-label>All contacts</q-item-label>
            <q-item-label caption>To the contact list</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          v-for="contact in contacts"
          :key="contact.id"
          clickable
          v-ripple
          @click="openContactDetail(contact)"
        >
          <q-item-section avatar>
            <q-icon name="person" />
          </q-item-section>
          <q-item-section>
            <q-item-label
              >{{ contact.first_name }} {{ contact.last_name }}</q-item-label
            >
            <q-item-label caption>{{ contact.emails[0].address }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
// import ContactList from "./views/ContactList.vue";

export default {
  name: "LayoutDefault",

  components: {
    // ContactList
  },
  computed: {
    search: {
      get() {
        return this.$store.state.search;
      },
      set(value) {
        this.$store.commit("updateSearchInput", value);
      }
    },
    contacts() {
      return this.$store.getters.contacts;
    }
  },
  methods: {
    openContactDetail(contact) {
      this.$store.dispatch("makeActiveContact", contact);
      this.$router.push({ path: "/contact/" + contact.id });
    }
  },
  created: function() {
    this.$store.dispatch('getContacts');
  },
  data() {
    return {
      leftDrawerOpen: false,
      text: ""
    };
  }
};
</script>

<style></style>
