# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi

iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chap_auth_discovery** | **bool** | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication | [optional] 
**chap_auth_session** | **bool** | chapAuthSession defines whether support iSCSI Session CHAP authentication | [optional] 
**fs_type** | **str** | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi | [optional] 
**initiator_name** | **str** | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface &lt;target portal&gt;:&lt;volume name&gt; will be created for the connection. | [optional] 
**iqn** | **str** | iqn is the target iSCSI Qualified Name. | 
**iscsi_interface** | **str** | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to &#39;default&#39; (tcp). | [optional] 
**lun** | **int** | lun represents iSCSI Target Lun number. | 
**portals** | **List[str]** | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | [optional] 
**read_only** | **bool** | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef.md) |  | [optional] 
**target_portal** | **str** | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


