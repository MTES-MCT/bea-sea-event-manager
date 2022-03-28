import { shallowMount } from "@vue/test-utils";
import DataSelector from "@/components/DataSelector.vue";
import SelectButton from "@/components/SelectButton.vue";
import CustomInput from "@/components/CustomInput.vue";

const dataDisplayComponent = CustomInput;
const selector = SelectButton;

const mountDataSelectorComponent = async (
  displayValue: string = "default_value"
) => {
  const dataSelector = shallowMount(DataSelector, {
    props: {
      displayValue: displayValue,
    },
  });
  return dataSelector;
};

describe("DataSelector.vue", () => {
  describe("when component is displayed", () => {
    it.each(["testValue1", "testValue2"])(
      "should display a display for the data with '%s' value",
      async (displayValue) => {
        const dataSelector = await mountDataSelectorComponent(displayValue);

        // no action

        expect(
          dataSelector.findComponent(dataDisplayComponent).exists()
        ).toBeTruthy();

        const dataDisplay = dataSelector.findComponent(dataDisplayComponent);
        expect(dataDisplay.props()).toStrictEqual({
          modelValue: displayValue,
          isDisabled: true,
        });
      }
    );
    it("should display a selection component", async () => {
      const DataSelector = await mountDataSelectorComponent();

      //no action

      expect(DataSelector.findComponent(selector).exists()).toBeTruthy();
    });
    describe("When receiving emit 'select' from the selection component", () => {
      it("should emit an event 'select'", async () => {
        const dataSelector = await mountDataSelectorComponent();
        const selectButton = dataSelector.findComponent(selector);

        selectButton.vm.$emit("select");

        expect(dataSelector.emitted("select")).toBeTruthy();
      });
    });
  });
});
