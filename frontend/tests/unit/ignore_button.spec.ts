import { mount, shallowMount } from "@vue/test-utils";
import IgnoreButton from "@/components/IgnoreButton.vue";

const mountIgnoreButtonComponent = async (textButton: string = "ignorer") => {
  const ignoreButton = shallowMount(IgnoreButton, {
    props: {
      textButton: textButton,
    },
  });

  return ignoreButton;
};

describe("IgnoreButton", () => {
  describe("when component is displayed", () => {
    it("should be a button", async () => {
      const ignoreButton = await mountIgnoreButtonComponent();

      expect(ignoreButton.element.tagName).toBe("BUTTON");
    });
    it.each(["Ignorer", "Annuler"])(
      "should display expected text button",
      async (expectedTextButton) => {
        const ignoreButton = await mountIgnoreButtonComponent(
          expectedTextButton
        );

        expect(ignoreButton.text()).toBe(expectedTextButton);
      }
    );
    describe("When component is clicked", () => {
      it("should emit an ignore event", async () => {
        const ignoreButton = await mountIgnoreButtonComponent();
        const expectedEmittedEvent = "ignore";
        const expectedNbIgnoreEvent = 1;
        ignoreButton.trigger("click");

        expect(ignoreButton.emitted).toBeTruthy();
        expect(ignoreButton.emitted()[expectedEmittedEvent]).toBeTruthy();
        expect(ignoreButton.emitted()[expectedEmittedEvent].length).toBe(
          expectedNbIgnoreEvent
        );
      });
    });
  });
});
