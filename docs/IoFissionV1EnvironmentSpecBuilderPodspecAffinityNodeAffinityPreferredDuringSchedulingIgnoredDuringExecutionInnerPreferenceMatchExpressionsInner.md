# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner

A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key that the selector applies to. | 
**operator** | **str** | Represents a key&#39;s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt. | 
**values** | **List[str]** | An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


