<template>
  <q-page>
    <h3>{{ contacts.name }}</h3>
    <q-list bordered separator>
      <q-item
        v-for="contact in contacts"
        :key="contact.id"
        class="q-py-lg"
        clickable
        v-ripple
        :to="contact.id.toString()"
        append
      >
        <q-item-section avatar>
          <q-avatar color="primary" text-color="white">{{
            contact.first_name[0]
          }}</q-avatar>
        </q-item-section>

        <q-item-section>
          <q-item-label
            >{{ contact.first_name }} {{ contact.last_name }}</q-item-label
          >
          <q-item-label caption lines="1">{{
            contact.emails[0]["address"]
          }}</q-item-label>
        </q-item-section>

        <q-item-section side>
          <q-icon name="dots-vertical" color="grey" />
        </q-item-section>
      </q-item>
    </q-list>
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
  methods: {}
};
</script>
