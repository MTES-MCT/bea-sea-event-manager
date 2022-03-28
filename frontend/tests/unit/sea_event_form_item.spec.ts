import { shallowMount } from "@vue/test-utils";
import SeaEventFormItem from "@/components/SeaEventFormItem.vue";
import CustomInput from "@/components/CustomInput.vue";
import { SeaEventFormLine } from "@/model/SeaEventFormLine";
import DataSelector from "@/components/DataSelector.vue";

const mountSeaEventFormItemComponent = async (
  seaEventFormLine: SeaEventFormLine
) => {
  const seaEventFormItemComp = shallowMount(SeaEventFormItem, {
    props: {
      seaEventFormLine: seaEventFormLine,
    },
  });
  return seaEventFormItemComp;
};

describe("SeaEventFormItem.vue", () => {
  describe("When mounting the component", () => {
    it.each(<SeaEventFormLine[]>[
      {
        name: "ship_name_1",
        initialReportValue: "moineau_1",
        referenceValue: "moineau_2",
        defaultSelectedValue: "",
      },
      {
        name: "ship_name_2",
        initialReportValue: "moineau_2",
        referenceValue: "moineau_3",
        defaultSelectedValue: "",
      },
    ])(
      "should display the attribute name with 2 data selector and 1 enabled custom input in this order",
      async (seaEventFormLine) => {
        const seaEventFormItem = await mountSeaEventFormItemComponent(
          seaEventFormLine
        );
        const seaEventFormItemNames = seaEventFormItem.findAll("label");
        const seaEventFormItemName = seaEventFormItemNames[0]
        const seaEventFormItemInputs =
          seaEventFormItem.findAllComponents(CustomInput);
        const seaEventFormItemInput = seaEventFormItemInputs[0];
        const seaEventFormDataSelectors =
          seaEventFormItem.findAllComponents(DataSelector);

        // no action

        expect(seaEventFormItemNames.length).toBe(1);
        expect(seaEventFormItemName.text()).toBe(seaEventFormLine.name);

        expect(seaEventFormDataSelectors.length).toBe(2);
        expect(seaEventFormDataSelectors[0].props()).toStrictEqual({
          displayValue: seaEventFormLine.initialReportValue,
        });
        expect(seaEventFormDataSelectors[1].props()).toStrictEqual({
          displayValue: seaEventFormLine.referenceValue,
        });

        expect(seaEventFormItemInputs.length).toBe(1);
        expect(seaEventFormItemInput.props()).toStrictEqual({
          modelValue: seaEventFormLine.defaultSelectedValue,
          isDisabled: false,
        });
      }
    );
  });
  describe("When receiving emit from custom input for selected value", () => {
    it.each(["test_update_value_1", "test_update_value_2"])(
      "Should emit the selected value",
      async (expectedUpdatedValue) => {
        const seaEventFormLine: SeaEventFormLine = {
          name: "test",
          initialReportValue: "",
          referenceValue: "",
          defaultSelectedValue: "initial_value",
        };
        const expectedEmittedEvent = "update:name";
        const seaEventFormItem = await mountSeaEventFormItemComponent(
          seaEventFormLine
        );
        const customInputs = seaEventFormItem.findAllComponents(CustomInput);
        const customInputWithSelectedValue = customInputs[0];
        expect(seaEventFormItem.emitted(expectedEmittedEvent)).toBeFalsy();

        customInputWithSelectedValue.vm.$emit(
          "update:modelValue",
          expectedUpdatedValue
        );

        await seaEventFormItem.vm.$nextTick();
        expect(seaEventFormItem.emitted(expectedEmittedEvent)).toBeTruthy();
        expect(
          seaEventFormItem.emitted(expectedEmittedEvent)?.values().next().value
        ).toEqual([expectedUpdatedValue]);
      }
    );
  });
  describe("When receiving emit 'select' from Data Selector", () => {
    it.each([[0], [1]])(
      "should update the value of the data selector number '%p' ",
      async (componentIndex) => {
        const seaEventFormLine: SeaEventFormLine = {
          name: "test",
          initialReportValue: "initialReportValue_test",
          referenceValue: "referenceValue_test",
          defaultSelectedValue: "initial_value_test",
        };
        const seaEventFormItem = await mountSeaEventFormItemComponent(
          seaEventFormLine
        );
        const customInput = seaEventFormItem.findComponent(CustomInput);
        const dataSelectors = seaEventFormItem.findAllComponents(DataSelector);
        const emittingDataSelector = dataSelectors[componentIndex];

        const DataSelectorEmittedEvent = "select";

        emittingDataSelector.vm.$emit(DataSelectorEmittedEvent);
        await seaEventFormItem.vm.$nextTick();

        expect(customInput.props()).toStrictEqual({
          modelValue: emittingDataSelector.props("displayValue"),
          isDisabled: false,
        });
      }
    );
  });
});
