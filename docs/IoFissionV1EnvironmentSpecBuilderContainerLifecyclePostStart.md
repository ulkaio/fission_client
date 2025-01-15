# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart

PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_exec** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec.md) |  | [optional] 
**http_get** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet.md) |  | [optional] 
**sleep** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep.md) |  | [optional] 
**tcp_socket** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


