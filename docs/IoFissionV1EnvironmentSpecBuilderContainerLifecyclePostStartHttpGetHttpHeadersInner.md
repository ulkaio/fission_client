# IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner

HTTPHeader describes a custom header to be used in HTTP probes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. | 
**value** | **str** | The header field value | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner from a JSON string
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner from a dict
io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner_form_dict = io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner.from_dict(io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


