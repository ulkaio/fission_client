# IoFissionV1MessageQueueTrigger

MessageQueueTrigger invokes functions when messages arrive to certain topic that trigger subscribes to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) |  | 
**spec** | [**IoFissionV1MessageQueueTriggerSpec**](IoFissionV1MessageQueueTriggerSpec.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_message_queue_trigger import IoFissionV1MessageQueueTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1MessageQueueTrigger from a JSON string
io_fission_v1_message_queue_trigger_instance = IoFissionV1MessageQueueTrigger.from_json(json)
# print the JSON string representation of the object
print IoFissionV1MessageQueueTrigger.to_json()

# convert the object into a dict
io_fission_v1_message_queue_trigger_dict = io_fission_v1_message_queue_trigger_instance.to_dict()
# create an instance of IoFissionV1MessageQueueTrigger from a dict
io_fission_v1_message_queue_trigger_form_dict = io_fission_v1_message_queue_trigger.from_dict(io_fission_v1_message_queue_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


