# IoFissionV1MessageQueueTriggerSpec

MessageQueueTriggerSpec defines a binding from a topic in a message queue to a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Content type of payload | [optional] 
**cooldown_period** | **int** | The period to wait after the last trigger reported active before scaling the deployment back to 0 | [optional] 
**error_topic** | **str** | Topic to collect error response sent from function | [optional] 
**functionref** | [**IoFissionV1MessageQueueTriggerSpecFunctionref**](IoFissionV1MessageQueueTriggerSpecFunctionref.md) |  | [optional] 
**max_replica_count** | **int** | Maximum number of replicas KEDA will scale the deployment up to | [optional] 
**max_retries** | **int** | Maximum times for message queue trigger to retry | [optional] 
**message_queue_type** | **str** | Type of message queue (NATS, Kafka, AzureQueue) | [optional] 
**metadata** | **Dict[str, str]** | ScalerTrigger fields | [optional] 
**min_replica_count** | **int** | Minimum number of replicas KEDA will scale the deployment down to | [optional] 
**mqtkind** | **str** | Kind of Message Queue Trigger to be created, by default its fission | [optional] 
**podspec** | [**IoFissionV1MessageQueueTriggerSpecPodspec**](IoFissionV1MessageQueueTriggerSpecPodspec.md) |  | [optional] 
**polling_interval** | **int** | The period to check each trigger source on every ScaledObject, and scale the deployment up or down accordingly | [optional] 
**resp_topic** | **str** | Topic for message queue trigger to sent response from function. | [optional] 
**secret** | **str** | Secret name | [optional] 
**topic** | **str** | Subscribed topic | 

## Example

```python
from fission_client.models.io_fission_v1_message_queue_trigger_spec import IoFissionV1MessageQueueTriggerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1MessageQueueTriggerSpec from a JSON string
io_fission_v1_message_queue_trigger_spec_instance = IoFissionV1MessageQueueTriggerSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1MessageQueueTriggerSpec.to_json()

# convert the object into a dict
io_fission_v1_message_queue_trigger_spec_dict = io_fission_v1_message_queue_trigger_spec_instance.to_dict()
# create an instance of IoFissionV1MessageQueueTriggerSpec from a dict
io_fission_v1_message_queue_trigger_spec_form_dict = io_fission_v1_message_queue_trigger_spec.from_dict(io_fission_v1_message_queue_trigger_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


