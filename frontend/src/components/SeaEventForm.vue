<template>
  <div class="sea-event-form">
    <sea-event-form-header />
    <div class="sea-event-form__rows">
      <sea-event-form-item
        v-for="seaEventFormLine in seaEventFormContent"
        :seaEventFormLine="seaEventFormLine"
        :key="seaEventFormLine.name"
        @update:name="
          (event) => updateContent(event, seaEventFormLine.name)
        "
      />
      <div class="buttons-area">
        <submit-button
          :textButton="'Confirmer'"
          @submit="confirm"
          class="button-form"
        />
        <cancel-button
          :textButton="'Annuler'"
          @cancel="cancel"
          class="button-form"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import SeaEventFormItem from "@/components/SeaEventFormItem.vue";
import { SeaEventFormLine } from "@/model/SeaEventFormLine";
import SubmitButton from "./SubmitButton.vue";
import CancelButton from "./CancelButton.vue";
import { useRoute, useRouter } from "vue-router";
import {
  registerSeaEventForm,
  getSeaEventFormData,
} from "@/connectors/seaEventAccess";
import SeaEventFormHeader from "./SeaEventFormHeader.vue";

const route = useRoute();
const router = useRouter();
const seaEventUUID = route.params.seaEventUUID as string;
const seaEventFormContent: SeaEventFormLine[] =
  getSeaEventFormData(seaEventUUID);

function updateContent(value: string, name: string) {
  seaEventFormContent.forEach((item) => {
    if (item.name === name) {
      item.defaultSelectedValue = value;
    }
  });
}

function textToDisplay(rawContent: SeaEventFormLine[]) {
  const textResultArray: string[] = [];
  rawContent.forEach((item) => {
    const textLine = `name => ${item.name}: ${item.defaultSelectedValue}`;
    textResultArray.push(textLine);
  })
  return textResultArray.join("\n");
}

function confirm() {
  alert(textToDisplay(seaEventFormContent))
  registerSeaEventForm(seaEventFormContent);
}

function cancel() {
  router.push({ name: "Main" });
}
</script>

<style>
.sea-event-form__row-container {
  display: grid;
  grid-gap: 2rem;
  grid-auto-rows: 3rem;
  margin-top: 1rem;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>

<style scoped>
.sea-event-form {
  display: grid;
  margin-bottom: 2rem;
}

.sea-event-form__rows {
  display: grid;
}

.buttons-area {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  column-gap: 1rem;
  padding-right: 2rem;
}

.button-form {
  align-items: center;
  justify-content: center;
  margin-top: 1rem;
  display: flex;
  grid-column-start: 5;
}
</style>
