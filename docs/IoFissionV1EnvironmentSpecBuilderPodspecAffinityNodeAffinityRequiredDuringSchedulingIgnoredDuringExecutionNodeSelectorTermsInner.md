# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner

A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.md) | A list of node selector requirements by node&#39;s labels. | [optional] 
**match_fields** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.md) | A list of node selector requirements by node&#39;s fields. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


