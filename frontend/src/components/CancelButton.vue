<template>
  <button class="fr-btn fr-btn--secondary" @click="emitEvent">
    {{ textButton }}
  </button>
</template>

<script lang="ts" setup>
import { withDefaults, defineProps, defineEmits } from "vue";
interface Props {
  textButton: string;
}

withDefaults(defineProps<Props>(), { textButton: "" });

const emit = defineEmits(["cancel"]);
function emitEvent() {
  emit("cancel");
}
</script>
