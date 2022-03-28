<template>
  <input
    class="fr-input"
    :disabled="isDisabled"
    type="text"
    :value="modelValue"
    @input="updateModelValue"
  />
</template>

<script lang="ts" setup>
import { withDefaults, defineProps, defineEmits } from "vue";
interface Props {
  modelValue: string;
  isDisabled: boolean;
}

const emit = defineEmits(["update:modelValue"]);
withDefaults(defineProps<Props>(), { modelValue: "" });

function updateModelValue(event: any) {
  emit("update:modelValue", event.target.value);
}
</script>
