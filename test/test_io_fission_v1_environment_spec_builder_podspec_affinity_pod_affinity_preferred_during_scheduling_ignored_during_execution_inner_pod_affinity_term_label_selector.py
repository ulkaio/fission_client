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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector

class TestIoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector(
                match_expressions = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner.io_fission_v1_Environment_spec_builder_podspec_affinity_podAffinity_preferredDuringSchedulingIgnoredDuringExecution_inner_podAffinityTerm_labelSelector_matchExpressions_inner(
                        key = '', 
                        operator = '', 
                        values = [
                            ''
                            ], )
                    ],
                match_labels = {
                    'key' : ''
                    }
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
