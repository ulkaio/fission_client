# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore

awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore | [optional] 
**partition** | **int** | partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \&quot;1\&quot;. Similarly, the volume partition for /dev/sda is \&quot;0\&quot; (or you can leave the property empty). | [optional] 
**read_only** | **bool** | readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore | [optional] 
**volume_id** | **str** | volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


