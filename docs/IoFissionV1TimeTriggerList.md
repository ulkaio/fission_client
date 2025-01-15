# IoFissionV1TimeTriggerList

TimeTriggerList is a list of TimeTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[IoFissionV1TimeTrigger]**](IoFissionV1TimeTrigger.md) | List of timetriggers. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ListMeta**](IoK8sApimachineryPkgApisMetaV1ListMeta.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_time_trigger_list import IoFissionV1TimeTriggerList

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1TimeTriggerList from a JSON string
io_fission_v1_time_trigger_list_instance = IoFissionV1TimeTriggerList.from_json(json)
# print the JSON string representation of the object
print IoFissionV1TimeTriggerList.to_json()

# convert the object into a dict
io_fission_v1_time_trigger_list_dict = io_fission_v1_time_trigger_list_instance.to_dict()
# create an instance of IoFissionV1TimeTriggerList from a dict
io_fission_v1_time_trigger_list_form_dict = io_fission_v1_time_trigger_list.from_dict(io_fission_v1_time_trigger_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


