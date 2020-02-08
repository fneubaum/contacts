import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    search: "",
    contacts: {
      id: 1,
      name: "",
      list: []
    },
    activeContact: {
      first_name: "",
      last_name: "",
      emails: [{ type: "", address: "" }],
      phones: [{ type: "", country: "", number: "" }],
      addresses: [{ type: "", value: "" }]
    }
  },
  getters: {
    contacts: state => {
      return state.contacts.list.filter(contact =>
        contact.first_name
          .toLowerCase()
          .concat(" ", contact.last_name.toLowerCase())
          .includes(state.search.toLowerCase())
      );
    },
    activeContact: state => {
      return state.activeContact;
    }
  },
  mutations: {
    setContacts(state, contacts) {
      state.contacts = contacts;
    },
    setActiveContact(state, contact) {
      state.activeContact = {
        first_name: contact.first_name,
        last_name: contact.last_name,
        id: contact.id,
        emails: [...contact.emails],
        phones: [...contact.phones],
        addresses: [...contact.addresses]
      };
    },
    insertIntoContacts(state, contact) {
      let newContact = {
        first_name: contact.first_name,
        last_name: contact.last_name,
        id: contact.id,
        emails: [...contact.emails],
        phones: [...contact.phones],
        addresses: [...contact.addresses]
      };
      state.contacts.list.push(newContact);
    },
    deleteFromContacts(state, contact) {
      state.contacts.list = state.contacts.list.filter(function(c) {
        return c.id != contact.id;
      });
    },
    updateSearchInput(state, search) {
      state.search = search;
    }
  },
  actions: {
    getContacts(context) {
      return axios
        .get(process.env.VUE_APP_API_URL + "/contact")
        .then(response => {
          context.commit("setContacts", response.data);
          return response.data;
        });
    },
    emtpyContacts(context) {
      context.commit("setContacts", {
        name: "",
        list: []
      });
    },
    emptyActiveContact(context) {
      context.commit("setActiveContact", {
        first_name: "",
        last_name: "",
        emails: [{ type: "", address: "" }],
        phones: [{ type: "", country: "", number: "" }],
        addresses: [{ type: "", value: "" }]
      });
    },
    makeActiveContact(context, contact) {
      context.commit("setActiveContact", contact);
    },
    createContact(context, contact) {
      return axios
        .post(process.env.VUE_APP_API_URL + "/contact", contact)
        .then(response => {
          context.commit("insertIntoContacts", response.data);
          context.commit("setActiveContact", response.data);
          return response.data;
        });
    },
    removeContact(context, contact) {
      return axios
        .delete(process.env.VUE_APP_API_URL + "/contact/" + contact.id)
        .then(response => {
          context.commit("deleteFromContacts", response.data);
          context.dispatch("emptyActiveContact");
          return response.data;
        });
    },
    updateContact(context, contact) {
      return axios
        .put(process.env.VUE_APP_API_URL + "/contact/" + contact.id, contact)
        .then(response => {
          context.commit("deleteFromContacts", contact);
          context.commit("insertIntoContacts", contact);
          context.dispatch("emptyActiveContact");
          return response.data;
        });
    }
  },
  modules: {}
});
