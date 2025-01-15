# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir

emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **str** | medium represents what type of storage medium should back this directory. The default is \&quot;\&quot; which means to use the node&#39;s default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 
**size_limit** | **object** | sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


