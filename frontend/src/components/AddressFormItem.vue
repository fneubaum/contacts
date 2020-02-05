<template>
  <div>
    <div class="row" v-for="(address, index) in addresses" v-bind:key="index">
      <div class="col-2">
        <q-select
          bg-color="grey7"
          dense
          filled
          square
          v-model="address.type"
          label="Type"
          :options="addressTypes"
        />
      </div>
      <div class="col-2">
        <q-select
          bg-color="grey7"
          dense
          filled
          square
          v-model="address.country"
          label="Country"
          :options="countries"
        />
      </div>
      <div class="col">
        <q-input
          bg-color="grey7"
          dense
          filled
          square
          v-model="address.value"
          label="Number"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Type an address']"
        />
      </div>
      <div class="col-1">
        <q-btn-group>
          <q-btn size="md" color="red-14" @click="removeAddress(index)" icon="remove" round />
          <q-btn
            size="md"
            color="secondary"
            v-if="index + 1 === addresses.length"
            @click="addAddress "
            icon="add"
            round
          />
        </q-btn-group>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddressFormItem",
  props: {
    addresses: {
      type: Array,
      default: function() {
        return [];
      }
    }
  },
  data() {
    return {
      blockRemoval: true,
      addressTypes: [
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
        },
        {
          label: "Other",
          value: "Other"
        }
      ],
      countries: [
        {
          label: "Argentina",
          value: "Argentina"
        },
        {
          label: "USA",
          value: "USA"
        }
      ]
    };
  },
  watch: {
    addresses() {
      this.blockRemoval = this.addresses.length <= 1;
    }
  },
  methods: {
    addAddress() {
      let checkEmpty = this.addresses.filter(address => address.value === null);
      if (checkEmpty.length > 0 && this.addresses.length > 0) return;
      this.addresses.push({
        country: null,
        value: null,
        type: null
      });
    },
    removeAddress(addressId) {
      if (!this.blockRemoval) this.addresses.splice(addressId, 1);
    }
  },
  mounted() {
    if (this.addresses.length == 0) {
      this.addAddress();
    }
  }
};
</script>