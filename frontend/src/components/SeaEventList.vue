<template>
  <div class="list-wrapper">
    <h1>Liste des évènements de mer</h1>
    <li
      class="list-group-item d-flex justify-content-between"
      v-for="seaEvent in displayedSeaEvents"
      v-bind:key="seaEvent.uuid"
    >
      <sea-event-list-item-vue
        :seaEventItem="seaEvent"
        @remove="removeFromList(seaEvent)"
      >
      </sea-event-list-item-vue>
    </li>
  </div>
</template>

<script lang="ts" setup>
import { SeaEventSummary } from "@/model/SeaEventSummary";
import { defineProps, ref } from "vue";
import SeaEventListItemVue from "@/components/SeaEventListItem.vue";

const props = defineProps<{
  seaEventList: SeaEventSummary[];
}>();

const displayedSeaEvents = ref([...props.seaEventList]);

function removeFromList(seaEventItem: SeaEventSummary): void {
  const index = displayedSeaEvents.value.indexOf(seaEventItem);
  displayedSeaEvents.value.splice(index, 1);
}
</script>

<style>
.list-wrapper {
  margin-top: 2rem;
  margin-bottom: 2rem;
}
</style>
