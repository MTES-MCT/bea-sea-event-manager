import { shallowMount } from "@vue/test-utils";
import SubmitButton from "@/components/SubmitButton.vue";

const mountSubmitButton = async (textButton: string = "Submit") => {
  const submitButton = shallowMount(SubmitButton, {
    props: {
        textButton: textButton
    }
  });

  return submitButton;
};

describe("SubmitButton.vue", () => {
    describe("when component is displayed", () => {
        it("should be a button", async () => {
            const submitButton = await mountSubmitButton();
    
            // no action
    
            expect(submitButton.element.tagName).toContain("BUTTON");
        });
        it.each(["Submit", "Confirm"])("should display expected text button ", async (expectedSubmitButton) => {
            const submitButton = await mountSubmitButton(expectedSubmitButton);
    
            // no action
    
            expect(submitButton.text()).toBe(expectedSubmitButton);
        });
    });
    describe("when component is clicked", () => {
        it("should emit a 'submit' event", async () => {
            const submitButton = await mountSubmitButton();
            const expectedEmittedEvent = "submit";
            const expectedNbSubmitEvent = 1;
    
            submitButton.trigger("click");
    
            expect(submitButton.emitted().click).toBeTruthy();
            expect(submitButton.emitted()[expectedEmittedEvent]).toBeTruthy();
            expect(submitButton.emitted()[expectedEmittedEvent].length).toBe(expectedNbSubmitEvent);
        });
    });
});
    
