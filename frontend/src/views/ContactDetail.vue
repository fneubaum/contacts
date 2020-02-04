<template>
  <q-page class="q-pa-xl">
    <h5>Contact Name</h5>
    <div class="row">
      <div class="col-6">
        <q-input
          bg-color="grey7"
          filled
          square
          v-model="contact.first_name"
          label="First name"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Type the number without the code']"
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
          :rules="[ val => val && val.length > 0 || 'Type the number without the code']"
        />
      </div>
    </div>
    <h5>Phone</h5>
    <phone-form-item :phones="contact.phones"></phone-form-item>
    <h5>Email</h5>
    <email-form-item :emails="contact.emails"></email-form-item>
    <h5>Address</h5>
    <address-form-item :addresses="contact.addresses"></address-form-item>
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
  }
};
</script>
