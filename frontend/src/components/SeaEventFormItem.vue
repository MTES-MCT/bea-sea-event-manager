<template>
  <div class="sea-event-form__row-container">
    <label
      class="fr-label emcip-form__data-container-label"
      for="text-input-text"
      >{{ seaEventFormLine.name }}</label
    >
    <data-selector
      :displayValue="seaEventFormLine.initialReportValue"
      @select="updateValue(seaEventFormLine.initialReportValue)"
    ></data-selector>
    <data-selector
      :displayValue="seaEventFormLine.referenceValue"
      @select="updateValue(seaEventFormLine.referenceValue)"
    ></data-selector>
    <custom-input
      class="fr-input"
      type="text"
      id="text-input-text"
      name="text-input-text"
      :is-disabled="false"
      v-model="currentSelectedValue"
    ></custom-input>
  </div>
</template>

<script lang="ts" setup>
import CustomInput from "./CustomInput.vue";
import DataSelector from "./DataSelector.vue";
import { SeaEventFormLine } from "@/model/SeaEventFormLine";
import { defineProps, withDefaults, defineEmits, ref, watch } from "vue";

interface Props {
  seaEventFormLine: SeaEventFormLine;
}

const emit = defineEmits(["update:name"]);
const props = withDefaults(defineProps<Props>(), {});
const currentSelectedValue = ref(props.seaEventFormLine.defaultSelectedValue);

watch(currentSelectedValue, (newValue: string) => {
  emit("update:name", newValue);
});

function updateValue(newValue: string) {
  currentSelectedValue.value = newValue;
}
</script>

<style scoped>
.emcip-form__data-container-label {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

@media (max-width: 980px) {
  .emcip-form__data-container {
    grid-template-columns: 1fr;
  }
}
</style>
