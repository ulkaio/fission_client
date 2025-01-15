# IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile

appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localhost_profile** | **str** | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is \&quot;Localhost\&quot;. | [optional] 
**type** | **str** | type indicates which kind of AppArmor profile will be applied. Valid options are:   Localhost - a profile pre-loaded on the node.   RuntimeDefault - the container runtime&#39;s default profile.   Unconfined - no AppArmor enforcement. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile from a JSON string
io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile_instance = IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile_dict = io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile from a dict
io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile_form_dict = io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile.from_dict(io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


