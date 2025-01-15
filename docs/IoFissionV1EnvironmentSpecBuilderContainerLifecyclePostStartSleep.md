# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep

Sleep represents the duration that the container should sleep before being terminated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Seconds is the number of seconds to sleep. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


