import { shallowMount } from '@vue/test-utils';
import SeaEventFormHeader from '@/components/SeaEventFormHeader.vue';

describe("SeaEventFormHeader.vue", () => {
    describe("When component is mounted", () => {
        it("should display the component", async () => {
            const seaEventFormHeaderComponent = shallowMount(SeaEventFormHeader);
            expect(seaEventFormHeaderComponent.exists()).toBeTruthy();
        });
        it("should display an empty header and 3 text headers", async () => {
            const seaEventFormHeaderComponent = shallowMount(SeaEventFormHeader);
            const expectedHeaders = [
                "SITREP",
                "GINA/NAVPRO",
                "Vers EMCIP",
            ];
            const headers = seaEventFormHeaderComponent.findAll("span");
            expect(headers.length).toBe(expectedHeaders.length);
            expectedHeaders.forEach((expectedHeader, index) => {
                expect(headers[index].text()).toBe(expectedHeader);
            });
        });
    });
});
