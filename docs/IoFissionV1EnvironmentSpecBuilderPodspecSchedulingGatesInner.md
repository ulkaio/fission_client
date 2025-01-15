# IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner

PodSchedulingGate is associated to a Pod to guard its scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the scheduling gate. Each scheduling gate must have a unique name field. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner import IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner_dict = io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner from a dict
io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


