# IoFissionV1FunctionList

FunctionList is a list of Function

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[IoFissionV1Function]**](IoFissionV1Function.md) | List of functions. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ListMeta**](IoK8sApimachineryPkgApisMetaV1ListMeta.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_list import IoFissionV1FunctionList

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionList from a JSON string
io_fission_v1_function_list_instance = IoFissionV1FunctionList.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionList.to_json()

# convert the object into a dict
io_fission_v1_function_list_dict = io_fission_v1_function_list_instance.to_dict()
# create an instance of IoFissionV1FunctionList from a dict
io_fission_v1_function_list_form_dict = io_fission_v1_function_list.from_dict(io_fission_v1_function_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


