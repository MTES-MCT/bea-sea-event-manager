import { createRouter, createWebHistory } from "vue-router";
import SeaEventList from "./components/SeaEventList.vue";
import SeaEventForm from "./components/SeaEventForm.vue";
import { createApp, h } from "vue";
import App from "./App.vue";
import "bootstrap/dist/css/bootstrap.css";

import { SeaEventSummary } from "@/model/SeaEventSummary";
import { SeaEventFormLine } from "@/model/SeaEventFormLine";

const seaEventFormData: SeaEventFormLine[] = [];
const seaEventList: SeaEventSummary[] = [
  {
    uuid: "123141-12312-12312-123131",
    label: "IBIS (FRANCE)",
    type: "Collision avec un Iceberg",
    date: " 9 mars 22 ",
    time: "18:12",
    CrossEntity: "CROSS Jobourg",
    sitrepNumber: "0283 ",
    region: "eaux territoriales",
    shipType: "navire à passagers",
    imoNumber: "1234567",
    immatNumber: "987654",
    lht: "154 m ",
    casualtyNumber: "1234",
    missingNumber: "54",
    injuredNumber: "8",
  },

  {
    uuid: "123141-12312-12312-123134",
    label: "MOINEAU (FRANCE)",
    type: "collision",
    date: " 1 décembre 21 ",
    time: "12:06",
    CrossEntity: "CROSS Brest",
    sitrepNumber: "0245",
    region: "eaux territoriales",
    shipType: "navire à passagers",
    imoNumber: "8910111",
    immatNumber: "987689",
    lht: "134 m ",
    casualtyNumber: "0",
    missingNumber: "0",
    injuredNumber: "0",
  },

  {
    uuid: "123141-12312-12312-123133",
    label: "MOUETTE (FRANCE)",
    type: "incendie",
    date: " 24 septembre 21 ",
    time: "07:34",
    CrossEntity: "CROSS Etel",
    sitrepNumber: "0256",
    region: "eaux territoriales",
    shipType: "navire à passagers",
    imoNumber: "9910234",
    immatNumber: "995683",
    lht: "111 m ",
    casualtyNumber: "0",
    missingNumber: "0",
    injuredNumber: "1",
  },
  {
    uuid: "123141-12372-12312-123133",
    label: "KIWI (FRANCE)",
    type: "Loss of propulsion power",
    date: " 12 septembre 21 ",
    time: "05:32",
    CrossEntity: "CROSS Corse",
    sitrepNumber: "0256",
    region: "eaux territoriales",
    shipType: "navire à passagers",
    imoNumber: "9910234",
    immatNumber: "995683",
    lht: "54 m ",
    casualtyNumber: "0",
    missingNumber: "0",
    injuredNumber: "0",
  },
  {
    uuid: "123131-12312-12312-123133",
    label: "COUCOU (FRANCE)",
    type: "Loss of propulsion power",
    date: " 07 mars 21 ",
    time: "02:13",
    CrossEntity: "CROSS La Garde",
    sitrepNumber: "0256",
    region: "eaux territoriales",
    shipType: "navire à passagers",
    imoNumber: "9910234",
    immatNumber: "995683",
    lht: "54 m ",
    casualtyNumber: "0",
    missingNumber: "0",
    injuredNumber: "0",
  },
];

const routes = [
  {
    path: "/",
    name: "Main",
    component: SeaEventList,
    props: {
      seaEventList: seaEventList,
    },
  },
  {
    path: "/seaEventForm/:seaEventUUID",
    name: "EmcipForm",
    component: SeaEventForm,
    props: {
      seaEventFormContent: seaEventFormData,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});
const app = createApp({
  render: () => h(App),
});

app.use(router).mount("#app");
