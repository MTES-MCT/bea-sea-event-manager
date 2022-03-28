import { shallowMount } from "@vue/test-utils";
import SeaEventFormItem from "@/components/SeaEventFormItem.vue";
import SeaEventFormHeader from "@/components/SeaEventFormHeader.vue";
import SeaEventForm from "@/components/SeaEventForm.vue";
import SubmitButton from "@/components/SubmitButton.vue";
import CancelButton from "@/components/CancelButton.vue";
import {SeaEventFormLine} from "@/model/SeaEventFormLine";

const mockRouter = {
    push: jest.fn(),
};
const mockRoute = {
    params: {
        seaEventUUID: ""
    },
  };
jest.mock("vue-router", () => ({
    useRouter() {
        return {
            name: "mock_router",
            push: mockRouter.push
        }
    },
    useRoute() {
        return {
            name: "mock_route",
            params: mockRoute.params,
        };
    },
}));
const mockRegisterSeaEventForm = jest.fn();
const mockGetSeaEventFormData = jest.fn();
jest.mock("@/connectors/seaEventAccess", () => ({
    registerSeaEventForm (data: any) {
        return mockRegisterSeaEventForm(data);
    },
    getSeaEventFormData ( seaEventUUID: string ) {
        return mockGetSeaEventFormData(seaEventUUID);
    }
}));

const mountSeaEventForm = async (
    urlParamSea_event_uuid: string = "test_uuid"
  ) => {
    mockRouter.push.mockClear();
    mockRegisterSeaEventForm.mockClear();
    mockGetSeaEventFormData.mockClear();

    window.alert = jest.fn();
    mockRoute.params.seaEventUUID = urlParamSea_event_uuid;
    const seaEventFormComponent = shallowMount(SeaEventForm, {
      global: {
        mocks: {
          $router: mockRouter,
          $route: mockRoute,
        },
      },
    });
    await seaEventFormComponent.vm.$nextTick();
    return seaEventFormComponent;
  };

describe("SeaEventForm.vue", () => {
    describe("When mounting the component", () => {
        it("should display form item headers", async () => {
            const seaEventFormComponent = await mountSeaEventForm();
            const headersComponent = seaEventFormComponent.findComponent(SeaEventFormHeader);

            expect(headersComponent.exists()).toBeTruthy();
        });
        it("should retrieve sea event data based on sea event uuid", async () => {
            const seaEventUUID = "test_uuid";
            mockRoute.params.seaEventUUID = seaEventUUID;

            await mountSeaEventForm();

            expect(mockGetSeaEventFormData).toHaveBeenCalledWith(seaEventUUID)
        });
        it("should display a submit button", async () => {
            const expectedComponent = SubmitButton
            const seaEventFormComponent = await mountSeaEventForm();
            const submitButton = seaEventFormComponent.findComponent(expectedComponent);

            //no action

            expect(submitButton.exists()).toBeTruthy();
            expect(seaEventFormComponent.findAllComponents(expectedComponent).length).toBe(1);
            expect(submitButton.props("textButton")).toBe("Confirmer");
        });
        it("should display a cancel button", async () => {
            const expectedComponent = CancelButton
            const seaEventFormComponent = await mountSeaEventForm();
            const cancelButton = seaEventFormComponent.findComponent(expectedComponent);

            //no action

            expect(cancelButton.exists()).toBeTruthy();
            expect(seaEventFormComponent.findAllComponents(expectedComponent).length).toBe(1);
            expect(cancelButton.props("textButton")).toBe("Annuler");
        });
        it("should display expected lines", async () => {
            const initialSeaEventFormData = <SeaEventFormLine[]>[
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
            ]
            mockGetSeaEventFormData.mockReturnValue(initialSeaEventFormData);
            const seaEventFormComponent = await mountSeaEventForm();
            const seaEventFormItem = seaEventFormComponent.findAllComponents(
                SeaEventFormItem
            );
    
            // no action
    
            expect(seaEventFormItem.length).toBe(initialSeaEventFormData.length);
            seaEventFormItem.forEach((seaEventFormItemComponent, index) => {
                expect(seaEventFormItemComponent.props().seaEventFormLine).toStrictEqual(initialSeaEventFormData[index]);
            });
        });
    });
    describe("When 'cancel' event is received", () => {
        it("should redirect to the Main page WITHOUT registering sea event form", async () => {
            const redirectionRouteName = "Main";
            
            const seaEventFormComponent = await mountSeaEventForm();
            const cancelButton = seaEventFormComponent.findComponent(CancelButton);
            const redirectionContent = { name: redirectionRouteName };
            expect(seaEventFormComponent.vm.$router.push).toHaveBeenCalledTimes(0);
    
            cancelButton.vm.$emit("cancel");
    
            expect(seaEventFormComponent.vm.$router.push).toHaveBeenCalledWith(redirectionContent);
        });
        it("should not register the sea event form", async () => {
            const seaEventFormComponent = await mountSeaEventForm();
            const cancelButton = seaEventFormComponent.findComponent(CancelButton);
            expect(mockRegisterSeaEventForm).toHaveBeenCalledTimes(0);

            cancelButton.vm.$emit("cancel");
    
            expect(mockRegisterSeaEventForm).toHaveBeenCalledTimes(0);
        });
    });
    describe("When 'submit' event is received", () => {
        describe("When 'update:name' event is received beforehand", () => {
            it("should call the registerSeaEventForm with updated data", async () => {
                const initialData: SeaEventFormLine[] = [
                    {
                        name: "ship_name_1",
                        initialReportValue: "moineau_1",
                        referenceValue: "moineau_2",
                        defaultSelectedValue: "",
                    },
                    {
                        name: "ship_name_2",
                        initialReportValue: "moineau_12",
                        referenceValue: "moineau_23",
                        defaultSelectedValue: "",
                    },
                ];
                mockGetSeaEventFormData.mockReturnValue(initialData);
                const newSelectedValue1 = "test_updated_value1";
                const newSelectedValue2 = "test_updated_value2";
                const expectedSubmittedData: SeaEventFormLine[] = [{
                    name: "ship_name_1",
                    initialReportValue: "moineau_1",
                    referenceValue: "moineau_2",
                    defaultSelectedValue: newSelectedValue1,
                },
                {
                    name: "ship_name_2",
                    initialReportValue: "moineau_12",
                    referenceValue: "moineau_23",
                    defaultSelectedValue: newSelectedValue2,
                }];
                const seaEventFormComponent = await mountSeaEventForm();

                const seaEventFormItems = seaEventFormComponent.findAllComponents(SeaEventFormItem)
                seaEventFormItems[0].vm.$emit('update:name', newSelectedValue1);
                seaEventFormItems[1].vm.$emit('update:name', newSelectedValue2);

                seaEventFormComponent.findComponent(SubmitButton).vm.$emit('submit');

                expect(mockRegisterSeaEventForm).toHaveBeenCalledWith(expectedSubmittedData);
            });
            it("should display an alert with the confirmed content", async () => {
                const initialData: SeaEventFormLine[] = [
                    {
                        name: "ship_name_1",
                        initialReportValue: "moineau_1",
                        referenceValue: "moineau_2",
                        defaultSelectedValue: "test_selected_value1",
                    },
                    {
                        name: "ship_name_2",
                        initialReportValue: "moineau_12",
                        referenceValue: "moineau_23",
                        defaultSelectedValue: "test_selected_value2",
                    },
                ];
                mockGetSeaEventFormData.mockReturnValue(initialData);
                const seaEventFormComponent = await mountSeaEventForm();
                const expectedDisplayedContentArray = <string[]>[]
                initialData.forEach((item) => {
                    const textLine = `name => ${item.name}: ${item.defaultSelectedValue}`
                    expectedDisplayedContentArray.push(textLine)
                })
                const expectedDisplayedContent = expectedDisplayedContentArray.join("\n")

                seaEventFormComponent.findComponent(SubmitButton).vm.$emit('submit');
                expect(window.alert).toHaveBeenCalledWith(expectedDisplayedContent)
            });
        });
        describe("When no 'update:name' event is received beforehand", () => {
            it("should call the registerSeaEventForm", async () => {
                const initialSeaEventFormData: SeaEventFormLine[] = [
                    {
                        name: "ship_name_1",
                        initialReportValue: "moineau_1",
                        referenceValue: "moineau_2",
                        defaultSelectedValue: "",
                    },
                ];
                mockGetSeaEventFormData.mockReturnValue(initialSeaEventFormData);
                const seaEventFormComponent = await mountSeaEventForm();
                const receivedEvent = 'submit';
                seaEventFormComponent.findComponent(SubmitButton).vm.$emit(receivedEvent);

                expect(mockRegisterSeaEventForm).toHaveBeenCalledWith(initialSeaEventFormData);
            });
        });
    });
});
