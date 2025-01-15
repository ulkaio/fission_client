# IoFissionV1EnvironmentSpecBuilderContainerLifecycle

Actions that the management system should take in response to container lifecycle events. Cannot be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_start** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart.md) |  | [optional] 
**pre_stop** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle import IoFissionV1EnvironmentSpecBuilderContainerLifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecycle from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecycle.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecycle.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_dict = io_fission_v1_environment_spec_builder_container_lifecycle_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecycle from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


