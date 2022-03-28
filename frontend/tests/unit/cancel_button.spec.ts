import { shallowMount } from "@vue/test-utils";
import CancelButton from "@/components/CancelButton.vue";

const mountCancelButtonComponent = async (
  textButton: string = "defaultTextButton"
) => {
  const cancelButton = shallowMount(CancelButton, {
    props: {
      textButton: textButton,
    },
  });

  return cancelButton;
};

describe("CancelButton.vue", () => {
  describe("When displayed", () => {
    it("should be a button", async () => {
      const cancelButton = await mountCancelButtonComponent();

      // no action

      expect(cancelButton.element.tagName).toBe("BUTTON");
    });
    it.each(["test", "test2"])(
      "should display expected text button '%s'",
      async (textButton) => {
        const cancelButton = await mountCancelButtonComponent(
          textButton
        );

        // no action

        expect(cancelButton.text()).toBe(textButton);
      }
    );
  });
  describe("When clicking on the button", () => {
    it("should emit the cancel event once", async () => {
      const cancelButton = await mountCancelButtonComponent();
      const expectedEvents = ["click", "cancel"];
      const expectedNbEmittedCancelEvents = 1;

      await cancelButton?.trigger("click");

      const emittedEvents = Object.keys(cancelButton.emitted());
      expect(emittedEvents.length).toBe(expectedEvents.length);
      expectedEvents.forEach((expectedEvents) =>
        expect(cancelButton.emitted(expectedEvents)).toBeTruthy()
      );
      expect(cancelButton.emitted().cancel.length).toBe(
        expectedNbEmittedCancelEvents
      );
    });
  });
});
