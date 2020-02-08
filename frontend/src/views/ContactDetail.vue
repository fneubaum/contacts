/* eslint-disable no-unused-vars */
<template>
  <q-page class="q-pa-xl">
    <q-form ref="contactForm">
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
                (val && val.length > 0) || 'Type your first name'
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
                (val && val.length > 0) || 'Type your last name'
            ]"
          />
        </div>
      </div>
      <h5 key="phones-title">Phone</h5>
      <phone-form-item key="phones" :phones="contact.phones"></phone-form-item>
      <h5 key="emails-title">Email</h5>
      <email-form-item key="emails" :emails="contact.emails"></email-form-item>
      <h5 key="addresses-title">Address</h5>
      <address-form-item key="addresses" :addresses="contact.addresses"></address-form-item>
    </q-form>

    <q-page-sticky position="bottom-right" :offset="[18, 18]">
      <q-fab color="primary" icon="keyboard_arrow_up" direction="up">
        <q-fab-action
          v-show="contact.id === undefined"
          color="secondary"
          icon="save"
          @click="add = !add"
        />
        <q-fab-action
          v-show="contact.id >= 1"
          color="red-14"
          icon="delete"
          @click="remove = !remove"
        />
        <q-fab-action v-show="contact.id >= 1" color="secondary" icon="save" @click="edit = !edit" />
      </q-fab>
    </q-page-sticky>

    <q-dialog v-model="remove" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="red-14" text-color="white" />
          <span class="q-ml-sm">Are you sure you want to delete this contact? This cannot be undone!</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn flat label="Remove" color="primary" v-close-popup @click="removeContact()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="edit" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="save" color="secondary" text-color="white" />
          <span class="q-ml-sm">Ready to save the changes made to this contact?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn flat label="Save" color="primary" v-close-popup @click="updateContact()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="add" persistent>
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="save" color="secondary" text-color="white" />
          <span class="q-ml-sm">Ready to save this contact?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn flat label="Save" color="primary" v-close-popup @click="createContact()" />
        </q-card-actions>
      </q-card>
    </q-dialog>
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
  data() {
    return {
      add: false,
      remove: false,
      edit: false
    };
  },
  computed: {
    contact() {
      return this.$store.getters.activeContact;
    }
  },
  methods: {
    cleanContact(contactToClean) {
      let contact = {
        first_name: contactToClean.first_name,
        last_name: contactToClean.last_name,
        id: contactToClean.id,
        emails: [...contactToClean.emails],
        phones: [...contactToClean.phones],
        addresses: [...contactToClean.addresses]
      };
      contact.emails = contact.emails.filter(function(e) {
        return (
          !(e.type === null && e.address === null) ||
          !(e.type === "" && e.address === "")
        );
      });
      contact.phones = contact.phones.filter(function(p) {
        return !(p.type === null || p.number === null || p.country === null);
      });
      contact.addresses = contact.addresses.filter(function(a) {
        return !(a.value === "" || a.type === null);
      });
      return contact;
    },
    removeContact() {
      let cleanedContact = this.cleanContact(this.$store.getters.activeContact);
      // eslint-disable-next-line no-unused-vars
      this.$store.dispatch("removeContact", cleanedContact).then(data => {});
      this.$router.push({ path: "/contact" });
    },
    createContact() {
      let cleanedContact = this.cleanContact(this.$store.getters.activeContact);
      this.$refs.contactForm.validate().then(success => {
        if (success) {
          this.$store.dispatch("createContact", cleanedContact);
          this.$router.push({ path: "/contact" });
        } else {
          this.$q.notify("Danger, Will Robinson! Danger!");
        }
      });
      // eslint-disable-next-line no-unused-vars
    },
    updateContact() {
      let cleanedContact = this.cleanContact(this.$store.getters.activeContact);
      this.$refs.contactForm.validate().then(success => {
        if (success) {
          this.$store.dispatch("updateContact", cleanedContact);
          this.$router.push({ path: "/contact" });
        } else {
          this.$q.notify({
            message: "There are errors in the form.",
            color: "red-14"
          });
        }
      });
      // eslint-disable-next-line no-unused-vars
    }
  },
  beforeDestroy: function() {
    this.$store.dispatch("emptyActiveContact");
  }
};
</script>
