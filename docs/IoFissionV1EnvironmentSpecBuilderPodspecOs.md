# IoFissionV1EnvironmentSpecBuilderPodspecOs

Specifies the OS of the containers in the pod. Some pod and container fields are restricted if this is set.  If the OS field is set to linux, the following fields must be unset: -securityContext.windowsOptions  If the OS field is set to windows, following fields must be unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile - spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile - spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy - spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser - spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups - spec.securityContext.supplementalGroupsPolicy - spec.containers[*].securityContext.appArmorProfile - spec.containers[*].securityContext.seLinuxOptions - spec.containers[*].securityContext.seccompProfile - spec.containers[*].securityContext.capabilities - spec.containers[*].securityContext.readOnlyRootFilesystem - spec.containers[*].securityContext.privileged - spec.containers[*].securityContext.allowPrivilegeEscalation - spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser - spec.containers[*].securityContext.runAsGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_os import IoFissionV1EnvironmentSpecBuilderPodspecOs

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecOs from a JSON string
io_fission_v1_environment_spec_builder_podspec_os_instance = IoFissionV1EnvironmentSpecBuilderPodspecOs.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecOs.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_os_dict = io_fission_v1_environment_spec_builder_podspec_os_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecOs from a dict
io_fission_v1_environment_spec_builder_podspec_os_form_dict = io_fission_v1_environment_spec_builder_podspec_os.from_dict(io_fission_v1_environment_spec_builder_podspec_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


