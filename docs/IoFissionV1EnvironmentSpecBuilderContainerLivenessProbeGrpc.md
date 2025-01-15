# IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc

GRPC specifies an action involving a GRPC port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port number of the gRPC service. Number must be in the range 1 to 65535. | 
**service** | **str** | Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_liveness_probe_grpc import IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc from a JSON string
io_fission_v1_environment_spec_builder_container_liveness_probe_grpc_instance = IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_liveness_probe_grpc_dict = io_fission_v1_environment_spec_builder_container_liveness_probe_grpc_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc from a dict
io_fission_v1_environment_spec_builder_container_liveness_probe_grpc_form_dict = io_fission_v1_environment_spec_builder_container_liveness_probe_grpc.from_dict(io_fission_v1_environment_spec_builder_container_liveness_probe_grpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


