# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector

Select all ClusterTrustBundles that match this label selector.  Only has effect if signerName is set.  Mutually-exclusive with name.  If unset, interpreted as \"match nothing\".  If set but empty, interpreted as \"match everything\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **Dict[str, str]** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


