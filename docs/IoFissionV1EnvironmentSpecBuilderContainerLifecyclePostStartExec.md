# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec

Exec specifies the action to take.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **List[str]** | Command is the command line to execute inside the container, the working directory for the command  is root (&#39;/&#39;) in the container&#39;s filesystem. The command is simply exec&#39;d, it is not run inside a shell, so traditional shell instructions (&#39;|&#39;, etc) won&#39;t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


