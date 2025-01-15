# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume

flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | driver is the name of the driver to use for this volume. | 
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. The default filesystem depends on FlexVolume script. | [optional] 
**options** | **Dict[str, str]** | options is Optional: this field holds extra command options if any. | [optional] 
**read_only** | **bool** | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


