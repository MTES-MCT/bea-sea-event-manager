<template>
  <button class="fr-btn fr-btn--tertiary" @click="ignoreEvent">
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
function ignoreEvent() {
  emit("ignore");
}
</script>
