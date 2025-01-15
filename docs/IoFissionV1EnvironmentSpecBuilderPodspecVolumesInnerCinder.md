# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder

cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | [optional] 
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinderSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinderSecretRef.md) |  | [optional] 
**volume_id** | **str** | volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


