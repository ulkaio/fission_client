# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk

photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**pd_id** | **str** | pdID is the ID that identifies Photon Controller persistent disk | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


