# IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef

Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** | Container name: required for volumes, optional for env vars | [optional] 
**divisor** | **object** | Specifies the output format of the exposed resources, defaults to \&quot;1\&quot; | [optional] 
**resource** | **str** | Required: resource to select | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef from a JSON string
io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef from a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref_form_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref.from_dict(io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


