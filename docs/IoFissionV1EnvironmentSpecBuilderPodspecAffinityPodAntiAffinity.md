# IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity

Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred_during_scheduling_ignored_during_execution** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.md) | The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \&quot;weight\&quot; to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. | [optional] 
**required_during_scheduling_ignored_during_execution** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner.md) | If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity from a JSON string
io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity_instance = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity from a dict
io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity_form_dict = io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity.from_dict(io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


