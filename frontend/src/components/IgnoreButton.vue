<template>
  <button class="fr-btn fr-btn--tertiary" @click="emitEvent">
    {{ textButton }}
  </button>
</template>

<script lang="ts" setup>
import { withDefaults, defineProps, defineEmits } from "vue";
interface Props {
  textButton: string;
}

withDefaults(defineProps<Props>(), { textButton: "" });

const emit = defineEmits(["ignore"]);
function emitEvent() {
  emit("ignore");
}
</script>
