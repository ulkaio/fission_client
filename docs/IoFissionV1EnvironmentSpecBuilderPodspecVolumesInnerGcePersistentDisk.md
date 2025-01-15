# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk

gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | [optional] 
**partition** | **int** | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \&quot;1\&quot;. Similarly, the volume partition for /dev/sda is \&quot;0\&quot; (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | [optional] 
**pd_name** | **str** | pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | 
**read_only** | **bool** | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


