<template>
  <button class="fr-btn" @click="emitEvent">
    {{ buttonLabel }}
  </button>
</template>

<script lang="ts" setup>
import { withDefaults, defineProps, defineEmits } from "vue";
interface Props {
  buttonLabel: string;
}
withDefaults(defineProps<Props>(), { buttonLabel: "" });
const emit = defineEmits(["editForm"]);
function emitEvent() {
  emit("editForm");
}
</script>
