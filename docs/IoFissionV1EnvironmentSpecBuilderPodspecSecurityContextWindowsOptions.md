# IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions

The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gmsa_credential_spec** | **str** | GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. | [optional] 
**gmsa_credential_spec_name** | **str** | GMSACredentialSpecName is the name of the GMSA credential spec to use. | [optional] 
**host_process** | **bool** | HostProcess determines if a container should be run as a &#39;Host Process&#39; container. All of a Pod&#39;s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true. | [optional] 
**run_as_user_name** | **str** | The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_windows_options import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions from a JSON string
io_fission_v1_environment_spec_builder_podspec_security_context_windows_options_instance = IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_security_context_windows_options_dict = io_fission_v1_environment_spec_builder_podspec_security_context_windows_options_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions from a dict
io_fission_v1_environment_spec_builder_podspec_security_context_windows_options_form_dict = io_fission_v1_environment_spec_builder_podspec_security_context_windows_options.from_dict(io_fission_v1_environment_spec_builder_podspec_security_context_windows_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


