# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2alpha1ObjectMetricSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, metric_name=None, target=None, target_value=None):
        """
        V2alpha1ObjectMetricSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metric_name': 'str',
            'target': 'V2alpha1CrossVersionObjectReference',
            'target_value': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'target': 'target',
            'target_value': 'targetValue'
        }

        self._metric_name = metric_name
        self._target = target
        self._target_value = target_value

    @property
    def metric_name(self):
        """
        Gets the metric_name of this V2alpha1ObjectMetricSource.
        metricName is the name of the metric in question.

        :return: The metric_name of this V2alpha1ObjectMetricSource.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this V2alpha1ObjectMetricSource.
        metricName is the name of the metric in question.

        :param metric_name: The metric_name of this V2alpha1ObjectMetricSource.
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")

        self._metric_name = metric_name

    @property
    def target(self):
        """
        Gets the target of this V2alpha1ObjectMetricSource.
        target is the described Kubernetes object.

        :return: The target of this V2alpha1ObjectMetricSource.
        :rtype: V2alpha1CrossVersionObjectReference
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this V2alpha1ObjectMetricSource.
        target is the described Kubernetes object.

        :param target: The target of this V2alpha1ObjectMetricSource.
        :type: V2alpha1CrossVersionObjectReference
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    @property
    def target_value(self):
        """
        Gets the target_value of this V2alpha1ObjectMetricSource.
        targetValue is the target value of the metric (as a quantity).

        :return: The target_value of this V2alpha1ObjectMetricSource.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """
        Sets the target_value of this V2alpha1ObjectMetricSource.
        targetValue is the target value of the metric (as a quantity).

        :param target_value: The target_value of this V2alpha1ObjectMetricSource.
        :type: str
        """
        if target_value is None:
            raise ValueError("Invalid value for `target_value`, must not be `None`")

        self._target_value = target_value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V2alpha1ObjectMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
