# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet

HTTPGet specifies the http request to perform.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. | [optional] 
**http_headers** | [**List[IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner]**](IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner.md) | Custom headers to set in the request. HTTP allows repeated headers. | [optional] 
**path** | **str** | Path to access on the HTTP server. | [optional] 
**port** | **object** | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 
**scheme** | **str** | Scheme to use for connecting to the host. Defaults to HTTP. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


