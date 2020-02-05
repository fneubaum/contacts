<template>
  <q-page>
    <h3>{{ contacts.name }}</h3>
    <q-list bordered separator>
      <transition-group
        appear
        enter-active-class="animated fadeIn"
        leave-active-class="animated fadeOut"
      >
        <q-item
          v-for="contact in contacts"
          :key="contact.id"
          class="q-py-lg"
          clickable
          v-ripple
          @click="openContactDetail(contact)"
        >
          <q-item-section avatar>
            <q-avatar color="primary" text-color="white">
              {{ contact.first_name[0] }}
            </q-avatar>
          </q-item-section>

          <q-item-section>
            <q-item-label
              >{{ contact.first_name }} {{ contact.last_name }}</q-item-label
            >
            <q-item-label caption lines="1">
              {{ contact.emails[0]["address"] }}
            </q-item-label>
          </q-item-section>

          <q-item-section side>
            <q-icon name="dots-vertical" color="grey" />
          </q-item-section>
        </q-item>
      </transition-group>
    </q-list>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-fab color="primary" icon="keyboard_arrow_up" direction="up">
        <q-fab-action color="secondary" icon="add" @click="addNewContact" />
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "ContactList",
  components: {
    // HelloWorld
  },
  computed: {
    contacts() {
      return this.$store.getters.contacts;
    }
  },
  methods: {
    addNewContact() {
      this.$store.dispatch("emptyActiveContact");
      this.$router.push({ path: "/contact/new" });
    },
    openContactDetail(contact) {
      this.$store.dispatch("makeActiveContact", contact);
      this.$router.push({ path: "/contact/" + contact.id });
    }
  }
};
</script>
