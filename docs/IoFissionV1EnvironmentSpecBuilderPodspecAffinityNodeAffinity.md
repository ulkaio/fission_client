# IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity

Describes node affinity scheduling rules for the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred_during_scheduling_ignored_during_execution** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.md) | The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \&quot;weight\&quot; to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. | [optional] 
**required_during_scheduling_ignored_during_execution** | [**IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


