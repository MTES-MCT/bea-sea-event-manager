<template>
  <div class="sea-event-form__row-container">
    <div class="sea_event_form_header__header empty_header"></div>
    <div
      v-for="header in headers"
      :key="header"
      class="sea_event_form_header__header"
    >
      <span>
        {{ header }}
      </span>
    </div>
  </div>
</template>

<script lang="ts" setup>
const headers = ["SITREP", "GINA/NAVPRO", "Vers EMCIP"];
</script>

<style scoped>
.sea_event_form_header__header {
  font-size: 1.5rem;
  text-align: center;
  color: white;
  background-color: #000091;
  display: flex;
  justify-content: center;
  align-items: center;
}

.empty_header {
  background-color: transparent;
}
</style>
