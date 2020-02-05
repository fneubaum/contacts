<template>
  <div>
    <div v-for="(email, index) in emails" v-bind:key="index">
      <div class="row">
        <div class="col-2">
          <q-select
            bg-color="grey7"
            dense
            filled
            square
            v-model="email.type"
            label="Type"
            :options="emailTypes"
          />
        </div>
        <div class="col">
          <q-input
            bg-color="grey7"
            dense
            square
            filled
            v-model="email.address"
            label="Address"
            lazy-rules
            :rules="[
              val =>
                (val && val.length > 0) || 'Type the number without the code'
            ]"
          />
        </div>
        <div class="col-1">
          <q-btn-group>
            <q-btn size="md" color="red-14" @click="removeEmail(index)" icon="remove" round />
            <q-btn
              size="md"
              color="secondary"
              v-if="index + 1 === emails.length"
              @click="addEmail"
              icon="add"
              round
            />
          </q-btn-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmailFormItem",
  props: {
    emails: {
      type: Array,
      default: function() {
        return [];
      }
    }
  },
  data() {
    return {
      blockRemoval: true,
      emailTypes: [
        {
          label: "Home",
          value: "Home"
        },
        {
          label: "Work",
          value: "Work"
        },
        {
          label: "School",
          value: "School"
        }
      ]
    };
  },
  watch: {
    emails() {
      this.blockRemoval = this.emails.length <= 1;
    }
  },
  methods: {
    addEmail() {
      let checkEmpty = this.emails.filter(email => email.number === null);
      if (checkEmpty.length > 0 && this.emails.length > 0) return;
      this.emails.push({
        address: null,
        type: null
      });
    },
    removeEmail(emailId) {
      if (!this.blockRemoval) {
        this.emails.splice(emailId, 1);
      } else {
        this.emails.pop();
        this.emails.push({
          address: null,
          type: null
        });
      }
    }
  },
  mounted() {
    if (this.emails.length == 0) {
      this.addEmail();
    }
  }
};
</script>
