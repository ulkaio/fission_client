# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume

vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**storage_policy_id** | **str** | storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName. | [optional] 
**storage_policy_name** | **str** | storagePolicyName is the storage Policy Based Management (SPBM) profile name. | [optional] 
**volume_path** | **str** | volumePath is the path that identifies vSphere volume vmdk | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


