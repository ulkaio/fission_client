# IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector

A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means \"this pod's namespace\". An empty selector ({}) matches all namespaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **Dict[str, str]** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


