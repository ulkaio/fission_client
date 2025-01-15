# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected

projected items for all in one resources secrets, configmaps, and downward API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**sources** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner]**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner.md) | sources is the list of volume projections. Each entry in this list handles one source. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


