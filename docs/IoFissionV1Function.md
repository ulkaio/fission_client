# IoFissionV1Function

Function is function runs within environment runtime with given package and secrets/configmaps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ObjectMeta**](IoK8sApimachineryPkgApisMetaV1ObjectMeta.md) |  | 
**spec** | [**IoFissionV1FunctionSpec**](IoFissionV1FunctionSpec.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function import IoFissionV1Function

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1Function from a JSON string
io_fission_v1_function_instance = IoFissionV1Function.from_json(json)
# print the JSON string representation of the object
print IoFissionV1Function.to_json()

# convert the object into a dict
io_fission_v1_function_dict = io_fission_v1_function_instance.to_dict()
# create an instance of IoFissionV1Function from a dict
io_fission_v1_function_form_dict = io_fission_v1_function.from_dict(io_fission_v1_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


