# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume

portworxVolume represents a portworx volume attached and mounted on kubelets host machine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**volume_id** | **str** | volumeID uniquely identifies a Portworx volume | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


