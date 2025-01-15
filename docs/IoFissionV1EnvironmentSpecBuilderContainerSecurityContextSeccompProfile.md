# IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile

The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localhost_profile** | **str** | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet&#39;s configured seccomp profile location. Must be set if type is \&quot;Localhost\&quot;. Must NOT be set for any other type. | [optional] 
**type** | **str** | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile from a JSON string
io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile_instance = IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile_dict = io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile from a dict
io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile_form_dict = io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile.from_dict(io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


