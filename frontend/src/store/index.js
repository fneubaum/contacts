import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    search: "",
    contacts: {
      id: 1,
      name: "My Contacts",
      list: [
        {
          id: 1,
          first_name: "Juan",
          last_name: "Perez",
          emails: [{ type: "Home", address: "juan@perez.com" }],
          phones: [{ type: "Home", number: "8754433" }],
          addresses: [{ type: "Home", number: "Main street 123" }]
        },
        {
          id: 2,
          first_name: "Jose",
          last_name: "Lopez",
          emails: [{ type: "Home", address: "jose@lopez.com" }],
          phones: [{ type: "Home", number: "jose@lopez.com" }],
          addresses: [{ type: "Home", number: "Main street 123" }]
        }
      ]
    },
    activeContact: {
      id: 1,
      first_name: "Juan",
      last_name: "Perez",
      emails: [{ type: "Home", address: "juan@perez.com" }],
      phones: [{ type: "Home", country: "+1", number: "8889900" }],
      addresses: [{ kind: "Home", number: "Main street 123" }]
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
    emtpyContacts(context) {
      context.commit("setContacts", {
        id: null,
        name: "",
        list: []
      });
    },
    emptyActiveContact(context) {
      context.commit("setActiveContact", {
        id: null,
        first_name: "",
        last_name: "",
        emails: [{ type: "", address: "" }],
        phones: [{ type: "", country: "", number: "" }],
        addresses: [{ kind: "", number: "" }]
      });
    },
    makeActiveContact(context, contact) {
      context.commit("setActiveContact", contact);
    },
    createContact(context, contact) {
      context.commit("insertIntoContacts", contact);
    },
    removeContact(context, contact) {
      context.commit("deleteFromContacts", contact);
    },
    updateContact(context, contact) {
      context.commit("deleteFromContacts", contact);
      context.commit("insertIntoContacts", contact);
    }
  },
  modules: {}
});
