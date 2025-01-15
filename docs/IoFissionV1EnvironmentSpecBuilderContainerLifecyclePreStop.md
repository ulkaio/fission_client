# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop

PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_exec** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec.md) |  | [optional] 
**http_get** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet.md) |  | [optional] 
**sleep** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep.md) |  | [optional] 
**tcp_socket** | [**IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop_dict = io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


