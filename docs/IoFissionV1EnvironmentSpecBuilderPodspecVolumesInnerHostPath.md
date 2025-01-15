# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath

hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | 
**type** | **str** | type for HostPath Volume Defaults to \&quot;\&quot; More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


