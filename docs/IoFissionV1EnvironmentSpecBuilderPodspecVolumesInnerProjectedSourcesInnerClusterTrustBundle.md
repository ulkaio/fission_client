# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle

ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.  Alpha, gated by the ClusterTrustBundleProjection feature gate.  ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.  Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector.md) |  | [optional] 
**name** | **str** | Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector. | [optional] 
**optional** | **bool** | If true, don&#39;t block pod startup if the referenced ClusterTrustBundle(s) aren&#39;t available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. | [optional] 
**path** | **str** | Relative path from the volume root to write the bundle. | 
**signer_name** | **str** | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


