import Vue from "vue";

import "./styles/quasar.sass";
import "@quasar/extras/roboto-font/roboto-font.css";
import "@quasar/extras/material-icons/material-icons.css";
import { Quasar } from "quasar";

Vue.use(Quasar, {
  plugins: ["Notify"],
  config: {
    notify: {
      /* Notify defaults */
    }
  },
  components: {
    /* not needed if importStrategy is not 'manual' */
  },
  directives: {
    /* not needed if importStrategy is not 'manual' */
  },
  animations: ["fadeIn", "fadeOut"]
});