# IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner

PodReadinessGate contains the reference to a pod condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | ConditionType refers to a condition in the pod&#39;s condition list with matching type. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner import IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner_dict = io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner from a dict
io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


