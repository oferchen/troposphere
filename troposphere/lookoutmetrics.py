# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer


class LambdaConfiguration(AWSProperty):
    """
    `LambdaConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html>`__
    """

    props: PropsDictType = {
        "LambdaArn": (str, True),
        "RoleArn": (str, True),
    }


class SNSConfiguration(AWSProperty):
    """
    `SNSConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
        "SnsTopicArn": (str, True),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html>`__
    """

    props: PropsDictType = {
        "LambdaConfiguration": (LambdaConfiguration, False),
        "SNSConfiguration": (SNSConfiguration, False),
    }


class Alert(AWSObject):
    """
    `Alert <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html>`__
    """

    resource_type = "AWS::LookoutMetrics::Alert"

    props: PropsDictType = {
        "Action": (Action, True),
        "AlertDescription": (str, False),
        "AlertName": (str, False),
        "AlertSensitivityThreshold": (integer, True),
        "AnomalyDetectorArn": (str, True),
    }


class AnomalyDetectorConfig(AWSProperty):
    """
    `AnomalyDetectorConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html>`__
    """

    props: PropsDictType = {
        "AnomalyDetectorFrequency": (str, True),
    }


class Metric(AWSProperty):
    """
    `Metric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html>`__
    """

    props: PropsDictType = {
        "AggregationFunction": (str, True),
        "MetricName": (str, True),
        "Namespace": (str, False),
    }


class AppFlowConfig(AWSProperty):
    """
    `AppFlowConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html>`__
    """

    props: PropsDictType = {
        "FlowName": (str, True),
        "RoleArn": (str, True),
    }


class CloudwatchConfig(AWSProperty):
    """
    `CloudwatchConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html>`__
    """

    props: PropsDictType = {
        "RoleArn": (str, True),
    }


class VpcConfiguration(AWSProperty):
    """
    `VpcConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIdList": ([str], True),
        "SubnetIdList": ([str], True),
    }


class RDSSourceConfig(AWSProperty):
    """
    `RDSSourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html>`__
    """

    props: PropsDictType = {
        "DBInstanceIdentifier": (str, True),
        "DatabaseHost": (str, True),
        "DatabaseName": (str, True),
        "DatabasePort": (integer, True),
        "RoleArn": (str, True),
        "SecretManagerArn": (str, True),
        "TableName": (str, True),
        "VpcConfiguration": (VpcConfiguration, True),
    }


class RedshiftSourceConfig(AWSProperty):
    """
    `RedshiftSourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html>`__
    """

    props: PropsDictType = {
        "ClusterIdentifier": (str, True),
        "DatabaseHost": (str, True),
        "DatabaseName": (str, True),
        "DatabasePort": (integer, True),
        "RoleArn": (str, True),
        "SecretManagerArn": (str, True),
        "TableName": (str, True),
        "VpcConfiguration": (VpcConfiguration, True),
    }


class CsvFormatDescriptor(AWSProperty):
    """
    `CsvFormatDescriptor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html>`__
    """

    props: PropsDictType = {
        "Charset": (str, False),
        "ContainsHeader": (boolean, False),
        "Delimiter": (str, False),
        "FileCompression": (str, False),
        "HeaderList": ([str], False),
        "QuoteSymbol": (str, False),
    }


class JsonFormatDescriptor(AWSProperty):
    """
    `JsonFormatDescriptor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html>`__
    """

    props: PropsDictType = {
        "Charset": (str, False),
        "FileCompression": (str, False),
    }


class FileFormatDescriptor(AWSProperty):
    """
    `FileFormatDescriptor <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html>`__
    """

    props: PropsDictType = {
        "CsvFormatDescriptor": (CsvFormatDescriptor, False),
        "JsonFormatDescriptor": (JsonFormatDescriptor, False),
    }


class S3SourceConfig(AWSProperty):
    """
    `S3SourceConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html>`__
    """

    props: PropsDictType = {
        "FileFormatDescriptor": (FileFormatDescriptor, True),
        "HistoricalDataPathList": ([str], False),
        "RoleArn": (str, True),
        "TemplatedPathList": ([str], False),
    }


class MetricSource(AWSProperty):
    """
    `MetricSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html>`__
    """

    props: PropsDictType = {
        "AppFlowConfig": (AppFlowConfig, False),
        "CloudwatchConfig": (CloudwatchConfig, False),
        "RDSSourceConfig": (RDSSourceConfig, False),
        "RedshiftSourceConfig": (RedshiftSourceConfig, False),
        "S3SourceConfig": (S3SourceConfig, False),
    }


class TimestampColumn(AWSProperty):
    """
    `TimestampColumn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html>`__
    """

    props: PropsDictType = {
        "ColumnFormat": (str, False),
        "ColumnName": (str, False),
    }


class MetricSet(AWSProperty):
    """
    `MetricSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html>`__
    """

    props: PropsDictType = {
        "DimensionList": ([str], False),
        "MetricList": ([Metric], True),
        "MetricSetDescription": (str, False),
        "MetricSetFrequency": (str, False),
        "MetricSetName": (str, True),
        "MetricSource": (MetricSource, True),
        "Offset": (integer, False),
        "TimestampColumn": (TimestampColumn, False),
        "Timezone": (str, False),
    }


class AnomalyDetector(AWSObject):
    """
    `AnomalyDetector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html>`__
    """

    resource_type = "AWS::LookoutMetrics::AnomalyDetector"

    props: PropsDictType = {
        "AnomalyDetectorConfig": (AnomalyDetectorConfig, True),
        "AnomalyDetectorDescription": (str, False),
        "AnomalyDetectorName": (str, False),
        "KmsKeyArn": (str, False),
        "MetricSetList": ([MetricSet], True),
    }
