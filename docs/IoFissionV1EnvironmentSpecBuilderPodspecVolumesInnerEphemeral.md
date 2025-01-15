# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral

ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.  Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity    tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through    a PersistentVolumeClaim (see EphemeralVolumeSource for more    information on the connection between this volume type    and PersistentVolumeClaim).  Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.  Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.  A pod can use both types of ephemeral volumes and persistent volumes at the same time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_claim_template** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplate**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplate.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


