import { shallowMount } from "@vue/test-utils";
import CustomInput from "@/components/CustomInput.vue";

const mountCustomInputComponent = async (
  input_message: string = "defaultMessage",
  is_disabled: boolean = true
) => {
  const my_component = shallowMount(CustomInput, {
    props: {
      modelValue: input_message,
      isDisabled: is_disabled,
    },
  });

  return my_component;
};
describe("when Input.vue is displayed", () => {
  it("should display an input", async () => {
    const input = await mountCustomInputComponent();

    // no action

    expect(input.element.tagName).toBe("INPUT");
  });
  it.each(["testDefaultValue1", "testDefaultValue2"])(
    "should contain a default text value '%s'",
    async (input_message) => {
      const input = await mountCustomInputComponent(input_message);

      //no action

      expect(input.find("input").element.value).toBe(input_message);
    }
  );
  it("should be a disabled text input", async () => {
    const defaultInputMsg = "defaultMessage";
    const isDisabled = true;
    const input = await mountCustomInputComponent(defaultInputMsg, isDisabled);
    const inputElement = input.find("input");

    expect(inputElement.element.disabled).toBe(true);
  });
  it.each([
    [true, ""],
    [false, undefined],
  ])(
    "should not update the value",
    async (isDisabled, isDisabledHtmlTruthy) => {
      const defaultValue = "defaultValue";
      const input = await mountCustomInputComponent(defaultValue, isDisabled);
      const inputElement = input.find("input");

      expect(inputElement.attributes("disabled")).toBe(isDisabledHtmlTruthy);
    }
  );
  describe("When input value is updated", () => {
    it("should inform the parent of the update", async () => {
      const defaultInputMsg = "defaultMessage";
      const inputComponent = await mountCustomInputComponent(defaultInputMsg, false);
      const expectedUpdateValue = "testUpdateValue";
      const expectedEmittedEvent = "update:modelValue";
      expect(inputComponent.emitted()[expectedEmittedEvent]).toBeFalsy();

      await inputComponent.find("input").setValue(expectedUpdateValue);

      expect(inputComponent.emitted()[expectedEmittedEvent]).toBeTruthy();
      expect(inputComponent.emitted()[expectedEmittedEvent][0]).toStrictEqual([expectedUpdateValue]);
    });
  });
});
