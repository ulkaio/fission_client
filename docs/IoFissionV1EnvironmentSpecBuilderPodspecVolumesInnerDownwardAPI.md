# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI

downwardAPI represents downward API about the pod that should populate this volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**items** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner.md) | Items is a list of downward API volume file | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


