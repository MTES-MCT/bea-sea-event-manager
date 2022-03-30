<template>
  <label
    >{{ seaEventItem.label }} / {{ seaEventItem.date }} /
    {{ seaEventItem.time }} / {{ seaEventItem.CrossEntity }} /
    {{ seaEventItem.sitrepNumber }} / {{ seaEventItem.region }} /
    {{ seaEventItem.shipType }} / {{ seaEventItem.imoNumber }} /
    {{ seaEventItem.immatNumber }} / {{ seaEventItem.lht }} /
    {{ seaEventItem.casualtyNumber }} / {{ seaEventItem.missingNumber }} /
    {{ seaEventItem.injuredNumber }} / {{ seaEventItem.type }}</label
  >

  <edit-form-button
    :buttonLabel="editFormButtonLabel"
    @editForm="redirect"
  ></edit-form-button>
  <ignore-button :textButton="'Ignorer'" @ignore="ignore()"></ignore-button>
</template>

<script lang="ts" setup>
import { SeaEventSummary } from "@/model/SeaEventSummary";
import { useRouter } from "vue-router";
import EditFormButton from "@/components/EditFormButton.vue";
import { defineProps, withDefaults, defineEmits } from "vue";
import IgnoreButton from "@/components/IgnoreButton.vue";
import { archiveSeaEvent } from "@/connectors/seaEventAccess";

interface Props {
  seaEventItem: SeaEventSummary;
}

const editFormButtonLabel = "Traiter";
const router = useRouter();
const props = withDefaults(defineProps<Props>(), {});
const emit = defineEmits(["remove"]);

function redirect() {
  router.push({
    name: "EmcipForm",
    params: { seaEventUUID: props.seaEventItem.uuid },
  });
}

function ignore() {
  archiveSeaEvent(props.seaEventItem.uuid);
  callForRemoval();
}

function callForRemoval(): void {
  emit("remove");
}
</script>
