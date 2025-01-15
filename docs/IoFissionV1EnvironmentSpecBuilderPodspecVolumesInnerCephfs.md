# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs

cephFS represents a Ceph FS mount on the host that shares a pod's lifetime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | **List[str]** | monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | 
**path** | **str** | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_file** | **str** | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfsSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfsSecretRef.md) |  | [optional] 
**user** | **str** | user is optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


