# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs

glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | **str** | endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**path** | **str** | path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**read_only** | **bool** | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


