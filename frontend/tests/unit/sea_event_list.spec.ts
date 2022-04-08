import IgnoreButton from "@/components/IgnoreButton.vue";
import { shallowMount } from "@vue/test-utils";
import SeaEventList from "@/components/SeaEventList.vue";
import SeaEventListItem from "@/components/SeaEventListItem.vue";
import { SeaEventSummary } from "@/model/SeaEventSummary";

const mountSeaEventListComponent = async (seaEventList: SeaEventSummary[]) => {
  const my_component = shallowMount(SeaEventList, {
    props: {
      seaEventList: seaEventList,
    },
  });
  return my_component;
};

describe("SeaEventItemsList.vue", () => {
  it("should display a title 'Liste des évènements de mer'", async () => {
    const expected_title_text = "Liste des évènements de mer";

    const my_component = await mountSeaEventListComponent([]);

    expect(my_component.findAll("h1")).toHaveLength(1);
    expect(my_component.find("h1").text()).toBe(expected_title_text);
  }),
    it.each([0, 1, 2])(
      "should display %s sea events called with appropriate props",
      async (nb_sea_events_to_display) => {
        const sea_events_to_display = <SeaEventSummary[]>[];
        for (let index = 0; index < nb_sea_events_to_display; index++) {
          sea_events_to_display.push(<SeaEventSummary>{
            uuid: `test_uuid_${index}`,
            label: `test_label_${index}`,
          });
        }
        const expected_item_component = SeaEventListItem;
        const sea_events_items_expected_props: any = [];
        sea_events_to_display.forEach((sea_event) => {
          sea_events_items_expected_props.push({
            seaEventItem: sea_event,
          });
        });
        const seaEventItemsList = await mountSeaEventListComponent(
          sea_events_to_display
        );

        const sea_event_items = seaEventItemsList.findAllComponents(
          expected_item_component
        );

        expect(sea_event_items).toHaveLength(nb_sea_events_to_display);
        sea_events_items_expected_props.forEach(
          (expected_props: any, index: number) => {
            expect(sea_event_items[index].props()).toEqual(expected_props);
          }
        );
      }
    );
  describe("when the seaEventListItem emits 'remove'", () => {
    it.each([0, 1])(
      "should remove the seaEventItem from the seaEventList",
      async (index) => {
        const seaEventsList: SeaEventSummary[] = [
          {
            uuid: "uuid1",
            label: "labelValue",
            date: "dateValue",
            time: "timeValue",
            CrossEntity: "crossEntityValue",
            sitrepNumber: "sitrepNumberValue",
            region: "regionValue",
            shipType: "shipTypeValue",
            imoNumber: "imoNumberValue",
            immatNumber: "immatNumberValue",
            lht: "lhtValue",
            casualtyNumber: "casualtyNumberValue",
            missingNumber: "missingNumberValue",
            injuredNumber: "injuredNumberValue",
            type: "typeValue",
          },
          {
            uuid: "uuid2",
            label: "labelValue",
            date: "dateValue",
            time: "timeValue",
            CrossEntity: "crossEntityValue",
            sitrepNumber: "sitrepNumberValue",
            region: "regionValue",
            shipType: "shipTypeValue",
            imoNumber: "imoNumberValue",
            immatNumber: "immatNumberValue",
            lht: "lhtValue",
            casualtyNumber: "casualtyNumberValue",
            missingNumber: "missingNumberValue",
            injuredNumber: "injuredNumberValue",
            type: "typeValue",
          },
        ];
        const seaEventsListComponent = await mountSeaEventListComponent(
          seaEventsList
        );
        const seaEventItemsComponent =
          seaEventsListComponent.findAllComponents(SeaEventListItem);
        const seaEventItemRemoved = seaEventItemsComponent[index];
        seaEventItemsComponent.forEach((element) => {});

        await seaEventItemRemoved.vm.$emit("remove");

        const newList =
          seaEventsListComponent.findAllComponents(SeaEventListItem);

        const expectedListLength = seaEventItemsComponent.length - 1;
        seaEventItemsComponent.forEach((element) => {});
        expect(seaEventsListComponent.exists()).toBeTruthy();
        expect(seaEventItemRemoved.props()).toStrictEqual({
          seaEventItem: seaEventsList[index],
        });
        expect(newList.length).toBe(expectedListLength);
        expect(newList).not.toEqual(
          expect.arrayContaining([
            expect.objectContaining({
              seaEvent: seaEventsList[index],
            }),
          ])
        );
      }
    );
  });
});
