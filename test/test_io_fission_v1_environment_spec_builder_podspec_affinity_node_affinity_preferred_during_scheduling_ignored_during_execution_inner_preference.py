# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference

class TestIoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference(
                match_expressions = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner.io_fission_v1_Environment_spec_builder_podspec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_preference_matchExpressions_inner(
                        key = '', 
                        operator = '', 
                        values = [
                            ''
                            ], )
                    ],
                match_fields = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner.io_fission_v1_Environment_spec_builder_podspec_affinity_nodeAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_preference_matchExpressions_inner(
                        key = '', 
                        operator = '', 
                        values = [
                            ''
                            ], )
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
