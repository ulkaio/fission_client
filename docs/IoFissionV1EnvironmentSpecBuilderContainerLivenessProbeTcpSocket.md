# IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket

TCPSocket specifies an action involving a TCP port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Optional: Host name to connect to, defaults to the pod IP. | [optional] 
**port** | **object** | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket import IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket from a JSON string
io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket_instance = IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket_dict = io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket from a dict
io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket_form_dict = io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket.from_dict(io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


