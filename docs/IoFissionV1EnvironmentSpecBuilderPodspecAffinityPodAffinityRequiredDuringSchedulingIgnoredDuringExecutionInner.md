# IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner

Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector.md) |  | [optional] 
**match_label_keys** | **List[str]** | MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with &#x60;labelSelector&#x60; as &#x60;key in (value)&#x60; to select the group of existing pods which pods will be taken into consideration for the incoming pod&#39;s pod (anti) affinity. Keys that don&#39;t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn&#39;t set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default). | [optional] 
**mismatch_label_keys** | **List[str]** | MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with &#x60;labelSelector&#x60; as &#x60;key notin (value)&#x60; to select the group of existing pods which pods will be taken into consideration for the incoming pod&#39;s pod (anti) affinity. Keys that don&#39;t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn&#39;t set. This is a beta field and requires enabling MatchLabelKeysInPodAffinity feature gate (enabled by default). | [optional] 
**namespace_selector** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector.md) |  | [optional] 
**namespaces** | **List[str]** | namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \&quot;this pod&#39;s namespace\&quot;. | [optional] 
**topology_key** | **str** | This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


