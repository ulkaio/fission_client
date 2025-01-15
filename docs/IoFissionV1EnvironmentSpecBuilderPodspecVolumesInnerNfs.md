# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs

nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | 
**read_only** | **bool** | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | [optional] 
**server** | **str** | server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


