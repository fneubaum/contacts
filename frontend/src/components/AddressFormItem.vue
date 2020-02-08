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
      <div class="col">
        <q-input bg-color="grey7" dense filled square v-model="address.value" label="Address" />
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
      addressTypes: ["Home", "Work", "School", "Other"]
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
        value: "",
        type: ""
      });
    },
    removeAddress(addressId) {
      if (!this.blockRemoval) {
        this.addresses.splice(addressId, 1);
      } else {
        this.addresses.pop();
        this.addresses.push({
          value: "",
          type: ""
        });
      }
    }
  },
  created() {
    if (this.addresses.length == 0) {
      this.addAddress();
    }
  },
  beforeUpdate() {
    if (this.addresses.length == 0) {
      this.addAddress();
    }
  }
};
</script>