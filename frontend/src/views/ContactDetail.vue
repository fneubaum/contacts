<template>
  <q-page class="q-pa-xl">
    <transition-group
      appear
      enter-active-class="animated fadeIn"
      leave-active-class="animated fadeOut"
    >
      <h5 key="title">Contact Name</h5>
      <div key="form" class="row">
        <div class="col-6">
          <q-input
            bg-color="grey7"
            filled
            square
            v-model="contact.first_name"
            label="First name"
            lazy-rules
            :rules="[
              val =>
                (val && val.length > 0) || 'Type the number without the code'
            ]"
          />
        </div>
        <div class="col-6">
          <q-input
            bg-color="grey7"
            filled
            square
            v-model="contact.last_name"
            label="Last name"
            lazy-rules
            :rules="[
              val =>
                (val && val.length > 0) || 'Type the number without the code'
            ]"
          />
        </div>
      </div>
      <h5 key="phones-title">Phone</h5>
      <phone-form-item key="phones" :phones="contact.phones"></phone-form-item>
      <h5 key="emails-title">Email</h5>
      <email-form-item key="emails" :emails="contact.emails"></email-form-item>
      <h5 key="addresses-title">Address</h5>
      <address-form-item
        key="addresses"
        :addresses="contact.addresses"
      ></address-form-item>
    </transition-group>
    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-fab color="primary" icon="keyboard_arrow_up" direction="up">
        <q-fab-action color="primary" icon="add" @click="createContact()" />
        <q-fab-action color="secondary" icon="edit" @click="updateContact()" />
        <q-fab-action color="red-14" icon="remove" @click="removeContact()" />
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>

<script>
// @ is an alias to /src
import PhoneFormItem from "@/components/PhoneFormItem.vue";
import EmailFormItem from "@/components/EmailFormItem.vue";
import AddressFormItem from "@/components/AddressFormItem.vue";

export default {
  name: "home",
  components: {
    AddressFormItem,
    EmailFormItem,
    PhoneFormItem
  },
  computed: {
    contact() {
      return this.$store.getters.activeContact;
    }
  },
  methods: {
    removeContact() {
      this.$store.dispatch("removeContact", this.$store.getters.activeContact);
      this.$router.push({ path: "/contact" });
    },
    createContact() {
      this.$store.dispatch("createContact", this.$store.getters.activeContact);
      this.$router.push({ path: "/contact" });
    },
    updateContact() {
      this.$store.dispatch("updateContact", this.$store.getters.activeContact);
      this.$router.push({ path: "/contact" });
    }
  },
  beforeDestroy: function() {
    this.$store.dispatch("emptyActiveContact");
  }
};
</script>
