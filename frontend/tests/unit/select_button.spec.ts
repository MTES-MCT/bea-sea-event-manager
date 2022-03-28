import { shallowMount } from "@vue/test-utils";
import SelectButton from "@/components/SelectButton.vue";

const mountSelectButtonComponent = async (
  buttonLabel: string = "defaultTextButton"
) => {
  const selectButton = shallowMount(SelectButton, {
    props: {
      buttonLabel: buttonLabel,
    },
  });

  return selectButton;
};

describe("SelectButton.vue", () => {
  describe("When clicking on the button", () => {
    it("should emit a select event once'", async () => {
      const selectButton = await mountSelectButtonComponent();
      const expectedEvents = ["click", "select"];
      const expectedNbEmittedSelectEvents = 1;

      await selectButton?.trigger("click");

      const emittedEvents = Object.keys(selectButton.emitted());
      expect(emittedEvents.length).toBe(expectedEvents.length);
      expectedEvents.forEach((expectedEvent) =>
        expect(selectButton.emitted(expectedEvent)).toBeTruthy()
      );
      expect(selectButton.emitted().select.length).toBe(
        expectedNbEmittedSelectEvents
      );
    });
  });
});
