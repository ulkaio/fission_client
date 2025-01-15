# IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner

A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is the label key that the selector applies to. | 
**operator** | **str** | operator represents a key&#39;s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. | 
**values** | **List[str]** | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


