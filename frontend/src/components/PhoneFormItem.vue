<template>
  <div>
    <div v-for="(phone, index) in phones" v-bind:key="index">
      <div class="row">
        <div class="col-2">
          <q-select
            dense
            filled
            bg-color="grey7"
            square
            v-model="phone.type"
            label="Type"
            :options="phoneTypes"
          />
        </div>
        <div class="col-2">
          <q-select
            bg-color="grey7"
            dense
            filled
            square
            v-model="phone.country"
            label="Country"
            :options="countryCodes"
          />
        </div>
        <div class="col">
          <q-input
            bg-color="grey7"
            dense
            bordered
            filled
            square
            v-model="phone.number"
            label="Number"
            lazy-rules
            :rules="[
              val =>
                (val && val.length > 0) || 'Type the number without the code'
            ]"
          />
        </div>
        <div class="col-1">
          <q-btn-group>
            <q-btn
              size="md"
              color="red-14"
              @click="removePhone(index)"
              icon="remove"
              round
            />
            <q-btn
              size="md"
              color="primary"
              v-if="index + 1 === phones.length"
              @click="addPhone"
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
  name: "PhoneFormItem",
  props: {
    phones: {
      type: Array,
      default: function() {
        return [];
      }
    }
  },
  data() {
    return {
      blockRemoval: true,
      phoneTypes: [
        {
          label: "Home",
          value: "Home"
        },
        {
          label: "Work",
          value: "Work"
        },
        {
          label: "Mobile",
          value: "Mobile"
        },
        {
          label: "School",
          value: "School"
        }
      ],
      countryCodes: [
        {
          label: "+54",
          value: "+54"
        },
        {
          label: "+1",
          value: "+1"
        }
      ]
    };
  },
  watch: {
    phones() {
      this.blockRemoval = this.phones.length <= 1;
    }
  },
  methods: {
    addPhone() {
      let checkEmpty = this.phones.filter(phone => phone.number === null);
      if (checkEmpty.length > 0 && this.phones.length > 0) return;
      this.phones.push({
        country: null,
        number: null,
        type: null
      });
    },
    removePhone(phoneId) {
      if (!this.blockRemoval) this.phones.splice(phoneId, 1);
    }
  },
  mounted() {
    if (this.phones.length == 0) {
      this.addPhone();
    }
  }
};
</script>
