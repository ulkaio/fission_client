# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket

Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Optional: Host name to connect to, defaults to the pod IP. | [optional] 
**port** | **object** | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


