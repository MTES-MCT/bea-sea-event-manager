<template>
  <div class="data-selector-wrapper">
    <custom-input
      type="text"
      :is-disabled="true"
      v-model="displayedValue"
    ></custom-input>
    <select-button @select="select"></select-button>
  </div>
</template>

<script lang="ts" setup>
import SelectButton from "./SelectButton.vue";
import CustomInput from "./CustomInput.vue";
import { withDefaults, defineProps, defineEmits, ref } from "vue";

interface Props {
  displayValue: string;
}

const props = withDefaults(defineProps<Props>(), { displayValue: "" });
const displayedValue = ref(props.displayValue);

const emit = defineEmits(["select"]);

function select() {
  emit("select");
}
</script>

<style>
.data-selector-wrapper {
  display: flex;
  max-height: 2.5rem;
}
</style>
