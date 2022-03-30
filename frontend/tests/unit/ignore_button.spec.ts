import { shallowMount } from "@vue/test-utils";
import IgnoreButton from "@/components/IgnoreButton.vue";

const mountIgnoreButtonComponent = async () => {
  const ignoreButton = shallowMount(IgnoreButton, {
    props: {},
  });

  return ignoreButton;
};

describe("IgnoreButton", () => {
  describe("When clicking on the button", () => {
    describe("When API call is successful", () => {
      it("should remove the item from the sea event list item", () => {
        // given the ignore button component
        // given a list of items
        // when clicking on the ignore button
        // when checking the response from API
        // expect item to be remove from the list of items
      });
    });
    describe("When API call fails", () => {
      it("should return an error message", () => {
        // given the ignore button component
        // given a list of items
        // when clicking on the ignore button
        // when checking the response from API
        // expect display of error message
      });
    });
  });
});
