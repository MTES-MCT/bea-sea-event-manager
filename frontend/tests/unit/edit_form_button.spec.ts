import { shallowMount } from "@vue/test-utils";
import EditFormButton from "@/components/EditFormButton.vue";

const mountEditFormButtonComponent = async (
  buttonLabel: string = "defaultTextButton"
) => {
  const editFormButton = shallowMount(EditFormButton, {
    props: {
      buttonLabel: buttonLabel,
    },
  });

  return editFormButton;
};

describe("RedirectButton.vue", () => {
  describe("When displayed", () => {
    it("should be a button", async () => {
      const editFormButton = await mountEditFormButtonComponent();

      // no action

      expect(editFormButton.element.tagName).toBe("BUTTON");
    });
    it.each(["buttonLabel1", "buttonLabel2"])(
      "should display expected text button '%s'",
      async (expectedButtonLabel) => {
        const editFormButton = await mountEditFormButtonComponent(
          expectedButtonLabel
        );

        // no action

        expect(editFormButton.text()).toBe(expectedButtonLabel);
      }
    );
  });
  describe("When clicking on the button", () => {
    it("should emit expected events", async () => {
      const editFormButton = await mountEditFormButtonComponent();
      const expectedEvents = ["click", "editForm"];
      const expectedNbEmittededitFormEvents = 1;

      await editFormButton?.trigger("click");

      const emitted_events = Object.keys(editFormButton.emitted());
      expect(emitted_events.length).toBe(expectedEvents.length);
      expectedEvents.forEach((expectedEvent) =>
        expect(editFormButton.emitted(expectedEvent)).toBeTruthy()
      );
      expect(editFormButton.emitted().editForm.length).toBe(
        expectedNbEmittededitFormEvents
      );
    });
  });
});
