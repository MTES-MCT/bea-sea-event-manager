<template>
  <div class="button-wrapper" @click="emitEvent">
    <button
      class="arrow-button"
      title="Label bouton"
    ></button>
  </div>
</template>

<script lang="ts" setup>
import { defineEmits } from "vue";
const emit = defineEmits(["select"]);
function emitEvent() {
  emit("select");
}
</script>

<style scoped>
.button-wrapper {
  border-color: none;
  width: 3rem;
  cursor: pointer;
  font-weight: bold;
}

.button-wrapper > .arrow-button {
  width: 1rem;
  height: 1rem;
  border-right: 2px solid rgba(0, 0, 0, 0.3);
  border-bottom: 2px solid rgba(0, 0, 0, 0.3);
  position: relative;
  transform: rotate(-45deg);
  margin: 0 6px;
}

.button-wrapper > .arrow-button::before {
  display: block;
  width: 3px;
  height: 2px;
  position: absolute;
  content: "";
  right: 0;
}

.button-wrapper:hover {
  opacity: 0.3;
}
</style>
