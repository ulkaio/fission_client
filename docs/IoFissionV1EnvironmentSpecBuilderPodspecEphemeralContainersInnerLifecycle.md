# IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle

Lifecycle is not allowed for ephemeral containers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_start** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart.md) |  | [optional] 
**pre_stop** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle from a JSON string
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle_instance = IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle_dict = io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle from a dict
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle_form_dict = io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle.from_dict(io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


