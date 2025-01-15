# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_up import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior(BaseModel):
    """
    hpaBehavior is the behavior of HPA when scaling in up/down direction. Applicable for executor type newdeploy and container.
    """ # noqa: E501
    scale_down: Optional[IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown] = Field(default=None, alias="scaleDown")
    scale_up: Optional[IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp] = Field(default=None, alias="scaleUp")
    __properties: ClassVar[List[str]] = ["scaleDown", "scaleUp"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of scale_down
        if self.scale_down:
            _dict['scaleDown'] = self.scale_down.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scale_up
        if self.scale_up:
            _dict['scaleUp'] = self.scale_up.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scaleDown": IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown.from_dict(obj.get("scaleDown")) if obj.get("scaleDown") is not None else None,
            "scaleUp": IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp.from_dict(obj.get("scaleUp")) if obj.get("scaleUp") is not None else None
        })
        return _obj


