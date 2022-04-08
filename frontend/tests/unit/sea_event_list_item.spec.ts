import IgnoreButton from "@/components/IgnoreButton.vue";
import { shallowMount } from "@vue/test-utils";
import SeaEventItem from "@/components/SeaEventListItem.vue";
import EditFormButton from "@/components/EditFormButton.vue";
import { SeaEventSummary } from "@/model/SeaEventSummary";

const DEFAULT_SEA_EVENT_SUMMARY = {
  uuid: "default_test1_uuid",
  label: "default_test_label",
  type: "default_test_type",
  date: "default_test_date",
  time: "default_test_time",
  CrossEntity: "default_test_CrossEntity",
  sitrepNumber: "default_test_sitrepNumber",
  region: "default_test_region",
  shipType: "default_test_shipType",
  imoNumber: "default_test_imoNumber",
  immatNumber: "default_test_immatNumber",
  lht: "default_test_lht",
  casualtyNumber: "default_test_casualtyNumber",
  missingNumber: "default_test_missingNumber",
  injuredNumber: "default_test_injuredNumber",
};

const mockRouter = {
  push: jest.fn(),
};
const mockRoute = {
  params: {
    seaEventUUID: DEFAULT_SEA_EVENT_SUMMARY.uuid,
  },
};
jest.mock("vue-router", () => ({
  useRouter() {
    return {
      name: "mock_router",
      push: mockRouter.push,
    };
  },
  useRoute() {
    return {
      name: "mock_route",
      params: mockRoute.params,
    };
  },
}));

const mountSeaEventListItemComponent = async (
  seaEventSummary: SeaEventSummary = DEFAULT_SEA_EVENT_SUMMARY
) => {
  mockRouter.push.mockClear();
  mockRoute.params.seaEventUUID = seaEventSummary.uuid;
  const my_component = shallowMount(SeaEventItem, {
    global: {
      mocks: {
        $router: mockRouter,
        $route: mockRoute,
      },
    },
    props: {
      seaEventItem: seaEventSummary,
    },
  });
  return my_component;
};

describe("SeaEventItem.vue", () => {
  describe("when the edit form button emits 'editForm'", () => {
    it("should redirect to the expected route", async () => {
      const editFormRouteName = "EmcipForm";
      const seaEventSummary = {
        uuid: "test_uuid",
        label: DEFAULT_SEA_EVENT_SUMMARY.label,
        type: "test_type",
        date: "test_date",
        time: "test_time",
        CrossEntity: "test_CrossEntity",
        sitrepNumber: "test_sitrepNumber",
        region: "test_region",
        shipType: "test_shipType",
        imoNumber: "test_imoNumber",
        immatNumber: "test_immatNumber",
        lht: "test_lht",
        casualtyNumber: "test_casualtyNumber",
        missingNumber: "test_missingNumber",
        injuredNumber: "test_injuredNumber",
      };

      const seaEventItem = await mountSeaEventListItemComponent(
        seaEventSummary
      );
      const redirectionContent = {
        name: editFormRouteName,
        params: { seaEventUUID: seaEventSummary.uuid },
      };
      expect(seaEventItem.vm.$router.push).toHaveBeenCalledTimes(0);

      await seaEventItem.findComponent(EditFormButton).vm.$emit("editForm");

      expect(seaEventItem.vm.$router.push).toHaveBeenCalledWith(
        redirectionContent
      );
    });
  });
  it.each([
    [
      "test_label_1",
      "test_date_1",
      "test_time_1",
      "test_CrossEntity_1",
      "test_sitrepNumber_1",
      "test_region_1",
      "test_shipType_1",
      "test_imoNumber_1",
      "test_immatNumber_1",
      "test_lht_1",
      "test_casualty_1",
      "test_missing_1",
      "test_injured_1",
      "test_type_1",
    ],
    [
      "test_label_2",
      "test_date_2",
      "test_time_2",
      "test_CrossEntity_2",
      "test_sitrepNumber_2",
      "test_region_2",
      "test_shipType_2",
      "test_imoNumber_2",
      "test_immatNumber_2",
      "test_lht_2",
      "test_casualty_2",
      "test_missing_2",
      "test_injured_2",
      "test_type_2",
    ],
  ])(
    "should display the summary of the sea event label",
    async (
      labelValue,
      dateValue,
      timeValue,
      crossEntityValue,
      sitrepNumberValue,
      regionValue,
      shipTypeValue,
      imoNumberValue,
      immatNumberValue,
      lhtValue,
      casualtyNumberValue,
      missingNumberValue,
      injuredNumberValue,
      typeValue
    ) => {
      const seaEventSummary: SeaEventSummary = {
        uuid: DEFAULT_SEA_EVENT_SUMMARY.uuid,
        label: labelValue,
        date: dateValue,
        time: timeValue,
        CrossEntity: crossEntityValue,
        sitrepNumber: sitrepNumberValue,
        region: regionValue,
        shipType: shipTypeValue,
        imoNumber: imoNumberValue,
        immatNumber: immatNumberValue,
        lht: lhtValue,
        casualtyNumber: casualtyNumberValue,
        missingNumber: missingNumberValue,
        injuredNumber: injuredNumberValue,
        type: typeValue,
      };
      const seaEventItem = await mountSeaEventListItemComponent(
        seaEventSummary
      );
      const seaEventItemLabel = seaEventItem.find("label");

      // no action

      expect(seaEventItemLabel?.element.tagName).toBe("LABEL");
      expect(seaEventItemLabel.text()).toBe(
        labelValue +
          " / " +
          dateValue +
          " / " +
          timeValue +
          " / " +
          crossEntityValue +
          " / " +
          sitrepNumberValue +
          " / " +
          regionValue +
          " / " +
          shipTypeValue +
          " / " +
          imoNumberValue +
          " / " +
          immatNumberValue +
          " / " +
          lhtValue +
          " / " +
          casualtyNumberValue +
          " / " +
          missingNumberValue +
          " / " +
          injuredNumberValue +
          " / " +
          typeValue
      );
    }
  );
  it("should display an edit form button labelled 'Traiter'", async () => {
    const seaEventItem = await mountSeaEventListItemComponent();

    expect(seaEventItem.findComponent(EditFormButton).exists()).toBeTruthy();
    expect(seaEventItem.findComponent(EditFormButton).html()).toContain(
      "Traiter"
    );
  });
  it("should display an ignore button labelled 'Ignorer'", async () => {
    const seaEventItem = await mountSeaEventListItemComponent();

    expect(seaEventItem.findComponent(IgnoreButton).exists()).toBeTruthy();
    expect(seaEventItem.findComponent(IgnoreButton).html()).toContain(
      "Ignorer"
    );
  });
  describe("when the ignore button emits 'ignore'", () => {
    it("should emit a remove event", async () => {
      const seaEventItem = await mountSeaEventListItemComponent();
      const expectedEmittedEvent = "remove";
      const expectedNRemoveEvent = 1;

      await seaEventItem.findComponent(IgnoreButton).vm.$emit("ignore");

      expect(seaEventItem.emitted).toBeTruthy();
      expect(seaEventItem.emitted()[expectedEmittedEvent]).toBeTruthy();
      expect(seaEventItem.emitted()[expectedEmittedEvent].length).toBe(
        expectedNRemoveEvent
      );
    });
  });
});
