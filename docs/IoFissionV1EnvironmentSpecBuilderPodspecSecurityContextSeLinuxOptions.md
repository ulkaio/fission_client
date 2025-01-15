# IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions

The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Level is SELinux level label that applies to the container. | [optional] 
**role** | **str** | Role is a SELinux role label that applies to the container. | [optional] 
**type** | **str** | Type is a SELinux type label that applies to the container. | [optional] 
**user** | **str** | User is a SELinux user label that applies to the container. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions from a JSON string
io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options_instance = IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options_dict = io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions from a dict
io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options_form_dict = io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options.from_dict(io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


