# IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities

The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** | Added capabilities | [optional] 
**drop** | **List[str]** | Removed capabilities | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_capabilities import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities from a JSON string
io_fission_v1_environment_spec_builder_container_security_context_capabilities_instance = IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_security_context_capabilities_dict = io_fission_v1_environment_spec_builder_container_security_context_capabilities_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities from a dict
io_fission_v1_environment_spec_builder_container_security_context_capabilities_form_dict = io_fission_v1_environment_spec_builder_container_security_context_capabilities.from_dict(io_fission_v1_environment_spec_builder_container_security_context_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


