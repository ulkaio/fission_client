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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector(BaseModel):
    """
    A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means \"this pod's namespace\". An empty selector ({}) matches all namespaces.
    """ # noqa: E501
    match_expressions: Optional[List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner]] = Field(default=None, description="matchExpressions is a list of label selector requirements. The requirements are ANDed.", alias="matchExpressions")
    match_labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", alias="matchLabels")
    __properties: ClassVar[List[str]] = ["matchExpressions", "matchLabels"]

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
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in match_expressions (list)
        _items = []
        if self.match_expressions:
            for _item in self.match_expressions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchExpressions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "matchExpressions": [IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.from_dict(_item) for _item in obj.get("matchExpressions")] if obj.get("matchExpressions") is not None else None,
            "matchLabels": obj.get("matchLabels")
        })
        return _obj


