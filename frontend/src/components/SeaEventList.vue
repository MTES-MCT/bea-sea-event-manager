<template>
  <div class="list-wrapper">
    <h1>Liste des évènements de mer</h1>
    <li
      class="list-group-item d-flex justify-content-between"
      v-for="seaEvent in seaEventList"
      v-bind:key="seaEvent.uuid"
    >
      <sea-event-list-item-vue :seaEventItem="seaEvent">
      </sea-event-list-item-vue>
    </li>
  </div>
</template>

<script lang="ts" setup>
import { SeaEventSummary } from "@/model/SeaEventSummary";
import { defineProps } from "vue";
import SeaEventListItemVue from "@/components/SeaEventListItem.vue";

defineProps<{
  seaEventList: SeaEventSummary[];
}>();
</script>

<style>
.list-wrapper {
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>
