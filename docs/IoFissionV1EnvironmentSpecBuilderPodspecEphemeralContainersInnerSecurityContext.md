# IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext

Optional: SecurityContext defines the security options the ephemeral container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_privilege_escalation** | **bool** | AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows. | [optional] 
**app_armor_profile** | [**IoFissionV1EnvironmentSpecBuilderContainerSecurityContextAppArmorProfile**](IoFissionV1EnvironmentSpecBuilderContainerSecurityContextAppArmorProfile.md) |  | [optional] 
**capabilities** | [**IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities**](IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities.md) |  | [optional] 
**privileged** | **bool** | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**proc_mount** | **str** | procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**read_only_root_filesystem** | **bool** | Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**run_as_group** | **int** | The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**run_as_non_root** | **bool** | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 
**run_as_user** | **int** | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. | [optional] 
**se_linux_options** | [**IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeLinuxOptions**](IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeLinuxOptions.md) |  | [optional] 
**seccomp_profile** | [**IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile**](IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile.md) |  | [optional] 
**windows_options** | [**IoFissionV1EnvironmentSpecBuilderContainerSecurityContextWindowsOptions**](IoFissionV1EnvironmentSpecBuilderContainerSecurityContextWindowsOptions.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext from a JSON string
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context_instance = IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context_dict = io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext from a dict
io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context_form_dict = io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context.from_dict(io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


