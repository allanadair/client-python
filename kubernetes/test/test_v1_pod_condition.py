# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_pod_condition import V1PodCondition


class TestV1PodCondition(unittest.TestCase):
    """ V1PodCondition unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1PodCondition(self):
        """
        Test V1PodCondition
        """
        model = kubernetes.client.models.v1_pod_condition.V1PodCondition()


if __name__ == '__main__':
    unittest.main()
