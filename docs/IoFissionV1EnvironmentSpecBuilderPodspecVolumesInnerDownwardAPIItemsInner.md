# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner

DownwardAPIVolumeFile represents information to create the file containing the pod field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef.md) |  | [optional] 
**mode** | **int** | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**path** | **str** | Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the &#39;..&#39; path. Must be utf-8 encoded. The first item of the relative path must not start with &#39;..&#39; | 
**resource_field_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


