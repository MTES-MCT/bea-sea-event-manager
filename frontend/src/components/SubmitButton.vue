<template>
  <button type="submit" class="fr-btn" @click="emitSubmitEvent">
    {{ textButton }}
  </button>
</template>

<script lang="ts" setup>
import { defineEmits, defineProps } from "vue";

const emit = defineEmits(["submit"]);
defineProps({
  textButton: String,
});

function emitSubmitEvent() {
  emit("submit");
}
</script>
