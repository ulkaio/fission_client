# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy

ExecutionStrategy specifies low-level parameters for function execution, such as the number of instances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executor_type** | **str** | ExecutorType is the executor type of function used. Defaults to \&quot;poolmgr\&quot;.  Available value:  - poolmgr  - newdeploy  - container | [optional] 
**max_scale** | **int** | This is only for newdeploy to set up maximum replicas of deployment. | [optional] 
**min_scale** | **int** | This is only for newdeploy to set up minimum replicas of deployment. | [optional] 
**specialization_timeout** | **int** | This is the timeout setting for executor to wait for pod specialization. | [optional] 
**target_cpu_percent** | **int** | Deprecated: use hpaMetrics instead. This is only for executor type newdeploy and container to set up target CPU utilization of HPA. Applicable for executor type newdeploy and container. | [optional] 
**hpa_behavior** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior.md) |  | [optional] 
**hpa_metrics** | [**List[IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner]**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner.md) | hpaMetrics is the list of metrics used to determine the desired replica count of the Deployment created for the function. Applicable for executor type newdeploy and container. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


