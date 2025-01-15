# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner

Volume represents a named volume in a pod that may be accessed by any container in the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_elastic_block_store** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore.md) |  | [optional] 
**azure_disk** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureDisk**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureDisk.md) |  | [optional] 
**azure_file** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile.md) |  | [optional] 
**cephfs** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs.md) |  | [optional] 
**cinder** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder.md) |  | [optional] 
**config_map** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap.md) |  | [optional] 
**csi** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi.md) |  | [optional] 
**downward_api** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI.md) |  | [optional] 
**empty_dir** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir.md) |  | [optional] 
**ephemeral** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral.md) |  | [optional] 
**fc** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc.md) |  | [optional] 
**flex_volume** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume.md) |  | [optional] 
**flocker** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker.md) |  | [optional] 
**gce_persistent_disk** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk.md) |  | [optional] 
**git_repo** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo.md) |  | [optional] 
**glusterfs** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs.md) |  | [optional] 
**host_path** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath.md) |  | [optional] 
**image** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage.md) |  | [optional] 
**iscsi** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi.md) |  | [optional] 
**name** | **str** | name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**nfs** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs.md) |  | [optional] 
**persistent_volume_claim** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim.md) |  | [optional] 
**photon_persistent_disk** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk.md) |  | [optional] 
**portworx_volume** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume.md) |  | [optional] 
**projected** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected.md) |  | [optional] 
**quobyte** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte.md) |  | [optional] 
**rbd** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerRbd**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerRbd.md) |  | [optional] 
**scale_io** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO.md) |  | [optional] 
**secret** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret.md) |  | [optional] 
**storageos** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerStorageos**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerStorageos.md) |  | [optional] 
**vsphere_volume** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


