# IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner

ContainerResizePolicy represents resource resize policy for the container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. | 
**restart_policy** | **str** | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_resize_policy_inner import IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner from a JSON string
io_fission_v1_environment_spec_builder_container_resize_policy_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_resize_policy_inner_dict = io_fission_v1_environment_spec_builder_container_resize_policy_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner from a dict
io_fission_v1_environment_spec_builder_container_resize_policy_inner_form_dict = io_fission_v1_environment_spec_builder_container_resize_policy_inner.from_dict(io_fission_v1_environment_spec_builder_container_resize_policy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


