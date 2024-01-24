"""
Purpose: To ensure that all named snippets are referenced in the docs.

Python code snippets refers to the Python module, containing the test, as follows:

```python name="tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context"
```

whereby "tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context", which
is the Python module, containing the integration test in the present example, would contain the following tagged code:

# Python
# <snippet name="tests/integration/docusaurus/general_directory/specific_directory/how_to_do_my_operation.py get_context">
import great_expectations as gx

context = gx.get_context()
# </snippet>

Find all named snippets and ensure that they are referenced in the docs using the above syntax.
"""

import pathlib
import shutil
import subprocess
import sys
from typing import List

# TODO: address ignored snippets by deleting snippet or test file, or adding documentation that references them
IGNORED_VIOLATIONS = [
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_python_example.py add datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_python_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_python_example.py test datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/pandas/inferred_and_runtime_yaml_example.py validator_creation",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_python_example.py add datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_python_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_python_example.py test datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py add datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py batch request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py get validator",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/azure/spark/inferred_and_runtime_yaml_example.py test datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py rumtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/pandas/inferred_and_runtime_yaml_example.py validator_creation",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_python_example.py add datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_python_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_python_example.py test datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py runtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py validator_creation",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/gcs/spark/inferred_and_runtime_yaml_example.py validator_creation_2",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_python_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_python_example.py test datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_yaml_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_yaml_example.py test datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/database/bigquery_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/bigquery_python_example.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/database/bigquery_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/bigquery_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/mysql_python_example.py add datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/database/mysql_python_example.py datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/database/mysql_python_example.py test datasource config",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py batch_request with query",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py batch_request with table",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/database/postgres_yaml_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/snowflake_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/snowflake_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/snowflake_python_example.py python batch_request name table",
    "tests/integration/docusaurus/connecting_to_your_data/database/snowflake_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py batch request table name",
    "tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/sqlite_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/trino_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/database/trino_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/database/trino_python_example.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/database/trino_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/pandas_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/pandas_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/pandas_python_example.py yaml",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py batch_request directory",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py batch_request directory validator",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py batch_request validator",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py python",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py runtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py runtime_batch_request validator",
    "tests/integration/docusaurus/connecting_to_your_data/filesystem/spark_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/fluent_datasources/get_existing_data_asset_from_existing_datasource_pandas_filesystem_example.py my_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_choose_which_dataconnector_to_use.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_choose_which_dataconnector_to_use.py datasource_config_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_choose_which_dataconnector_to_use.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_choose_which_dataconnector_to_use.py datasource_yaml_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py batch_request 1",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py batch_request example 2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py datasource_config yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py get_validator 1",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py get_validator example 2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py import pandas",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py path",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py python datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py python imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_runtimedataconnector.py yaml imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py batch_request 2019-02",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config add an InferredAssetDataConnector to a Datasource configuration",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config basic configuration with more than one Data Asset",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config each file own data asset",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config nested directory structure with the data_asset_name on the inside",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_config nested directory structure with the data_asset_name on the outside",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml add an InferredAssetDataConnector to a Datasource configuration",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml basic configuration with more than one Data Asset",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml each file own data asset",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml nested directory structure with the data_asset_name on the inside",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml nested directory structure with the data_asset_name on the outside",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py datasource_yaml redundant information in the naming convention",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py get_validator",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py imports python",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py imports yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py python datasource_config redundant information in the naming convention",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py create_expectation_suite",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py get_expectation_suite",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py get_validator_args",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py get_validator_runtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py path_to_file",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py read_csv",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py runtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py runtime_batch_request_with_path",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_pandas_dataframe.py validator head",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py create_expectation_suite",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py get_expectation_suite",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py get_validator",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py get_validator_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py path_to_file",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py pyspark_df",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py runtime_batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py runtime_batch_request_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_create_a_batch_of_data_from_an_in_memory_spark_dataframe.py validator_head",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py all batches",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py data_connector_query",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py first 5 batches from 2020",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py get_batch_list",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py get_validator",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py index data_connector_query",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py print(validator.batches)",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py print(validator.head())",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_get_one_or_more_batches_of_data_from_a_configured_datasource.py twelve batches from 2020",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py batch_filter_parameters",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py sample_using_random 10 pct",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py sampling batch size",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py split_on_column_value passenger_count",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_complete.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py add configureed asset data connector to datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py another_buggy_data_connector_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py buggy_data_connector_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py configured_data_connector_yaml add granular group_names",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py configured_data_connector_yaml only by filename and type",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py get_available_data_asset_names",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/files/yaml_example_gradual.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py assertions",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py batch_request",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_complete.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py add_datasource_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py buggy_datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py datasource_yaml",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py datasource_yaml_introspection",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py datasource_yaml_tables",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py datasource_yaml_tables_partitioners",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py get_available_data_asset_names",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py get_context",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py imports",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py test_yaml_config_2",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py test_yaml_config_3",
    "tests/integration/docusaurus/connecting_to_your_data/how_to_introspect_and_partition_your_data/sql_database/yaml_example_gradual.py test_yaml_config_4",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/pandas_python_example.py add_datasource",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/pandas_python_example.py datasource_config",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/pandas_python_example.py test_yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/spark_python_example.py add datasource",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/spark_python_example.py batch request",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/spark_python_example.py config",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/spark_python_example.py test yaml_config",
    "tests/integration/docusaurus/connecting_to_your_data/in_memory/spark_python_example.py validator",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_pandas.py get_batch_list",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_pandas.py get_batch_request",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py add_data_docs_store",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py add_expectations",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py build_docs",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py create_checkpoint",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py existing_expectations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py existing_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py get_batch_list",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py get_batch_request",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py get_validator",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py imports",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py new_expectations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py new_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py run checkpoint",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py save_expectations",
    "tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py set_new_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py add_data_docs_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py create_checkpoint",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py existing_expectations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py existing_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py imports",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py new_expectations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py new_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py run checkpoint",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py save_expectations",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py set_new_validations_store",
    "tests/integration/docusaurus/deployment_patterns/aws_redshift_deployment_patterns.py validator_calls",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py add datasource config",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py add expectations",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py create batch request",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py datasource config",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py get validator",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py imports",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py root directory",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py run checkpoint",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py save suite",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py set up context",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_yaml_configs.py test datasource config",
    "tests/integration/docusaurus/deployment_patterns/gcp_deployment_patterns_file_bigquery.py existing_expectations_store",
    "tests/integration/docusaurus/deployment_patterns/gcp_deployment_patterns_file_bigquery.py get_context",
    "tests/integration/docusaurus/deployment_patterns/gcp_deployment_patterns_file_gcs.py batch_request",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler build_suite",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler create_asset",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler create_profiler",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler create_validator",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler e2e",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler get_asset",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler name_suite",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler optional_params",
    "tests/integration/docusaurus/expectations/how_to_create_and_edit_expectations_with_a_profiler semantic",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py assert_suite",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py checkpoint_example",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py keys_passed_at_runtime",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py nesting_with_defaults",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py no_nesting",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py run_checkpoint_5",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py using_simple_checkpoint",
    "tests/integration/docusaurus/reference/core_concepts/checkpoints_and_actions.py using_template",
    "tests/integration/docusaurus/reference/glossary/checkpoints.py create_and_run",
    "tests/integration/docusaurus/reference/glossary/checkpoints.py save",
    "tests/integration/docusaurus/reference/glossary/checkpoints.py setup",
    "tests/integration/docusaurus/reference/glossary/data_docs.py data_docs",
    "tests/integration/docusaurus/reference/glossary/data_docs.py data_docs_site",
    "tests/integration/docusaurus/setup/configuring_data_contexts/how_to_configure_credentials.py add_credential_from_yml",
    "tests/integration/docusaurus/setup/configuring_data_contexts/how_to_configure_credentials.py add_credentials_as_connection_string",
    "tests/integration/docusaurus/setup/configuring_data_contexts/how_to_configure_credentials.py export_env_vars",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py build data docs command",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py build data docs output",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py create bucket command",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py create bucket output",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py gcloud app deploy",
    "tests/integration/docusaurus/setup/configuring_data_docs/how_to_host_and_share_data_docs_on_gcs.py gcloud login and set project",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_a_validation_result_store_in_gcs.py copy_validation_command",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_a_validation_result_store_in_gcs.py copy_validation_output",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_a_validation_result_store_in_gcs.py list_validation_stores_command",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_a_validation_result_store_in_gcs.py list_validation_stores_output",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_an_expectation_store_in_gcs.py copy_expectation_command",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_an_expectation_store_in_gcs.py copy_expectation_output",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_an_expectation_store_in_gcs.py list_expectation_stores_command",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_an_expectation_store_in_gcs.py list_expectation_stores_output",
    "tests/integration/docusaurus/setup/configuring_metadata_stores/how_to_configure_an_expectation_store_in_gcs.py list_expectation_suites_command",
    "tests/integration/docusaurus/tutorials/getting-started/getting_started.py checkpoint_yaml_config",
    "tests/integration/docusaurus/tutorials/getting-started/getting_started.py datasource_yaml",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py build_batch_request",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py get_context",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py get_validator_and_inspect_data",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py imports",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py inspect_data_no_jupyter",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py interactive_validation",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py interactive_validation_no_jupyter",
    "tests/integration/docusaurus/validation/validator/how_to_create_and_edit_expectations_with_instant_feedback_block_config.py save_expectation_suite",
    "tests/integration/fixtures/gcp_deployment/great_expectations/great_expectations.yml expectations_GCS_store",
    "tests/integration/fixtures/gcp_deployment/great_expectations/great_expectations.yml expectations_store_name",
    "tests/integration/fixtures/gcp_deployment/great_expectations/great_expectations.yml gs_site",
    "tests/integration/fixtures/gcp_deployment/great_expectations/great_expectations.yml validations_GCS_store",
    "tests/integration/fixtures/gcp_deployment/great_expectations/great_expectations.yml validations_store_name",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_python_configs.py choose context_root_dir",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_python_configs.py imports",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_python_configs.py run checkpoint",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_dataframe_python_configs.py set up context",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_file_python_configs.py add expectations",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_file_python_configs.py get validator",
    "tests/integration/docusaurus/deployment_patterns/databricks_deployment_patterns_file_python_configs.py save suite",
    "tests/integration/docusaurus/deployment_patterns/postgres_deployment_patterns.py pg_batch_request",
    "tests/integration/docusaurus/setup/setup_overview.py setup",
    "tests/integration/docusaurus/template/script_example.py full",
]


def check_dependencies(*deps: str) -> None:
    for dep in deps:
        if not shutil.which(dep):
            raise Exception(f"Must have `{dep}` installed in PATH to run {__file__}")


def get_snippet_definitions(target_dir: pathlib.Path) -> List[str]:
    try:
        res_snippets = subprocess.run(  # noqa: PLW1510
            [
                "grep",
                "--recursive",
                "--binary-files=without-match",
                "--no-filename",
                "--ignore-case",
                "--word-regexp",
                "--regexp",
                r"^# <snippet .*name=.*>",
                str(target_dir),
            ],
            text=True,
            capture_output=True,
        )
        res_snippet_names = subprocess.run(  # noqa: PLW1510
            ["sed", 's/.*name="//; s/">//; s/version-[0-9\\.]* //'],
            text=True,
            input=res_snippets.stdout,
            capture_output=True,
        )
        return res_snippet_names.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Command {e.cmd} returned with error (code {e.returncode}): {e.output}"
        ) from e


def get_snippets_used(target_dir: pathlib.Path) -> List[str]:
    try:
        res_snippet_usages = subprocess.run(  # noqa: PLW1510
            [
                "grep",
                "--recursive",
                "--binary-files=without-match",
                "--no-filename",
                "--exclude-dir=versioned_code",
                "--exclude-dir=versioned_docs",
                "--ignore-case",
                "-E",
                "--regexp",
                r"```(python|yaml).*name=",
                str(target_dir),
            ],
            text=True,
            capture_output=True,
        )
        res_snippet_used_names = subprocess.run(  # noqa: PLW1510
            ["sed", 's/.*="//; s/".*//; s/version-[0-9\\.]* //'],
            text=True,
            input=res_snippet_usages.stdout,
            capture_output=True,
        )
        return res_snippet_used_names.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Command {e.cmd} returned with error (code {e.returncode}): {e.output}"
        ) from e


def main() -> None:
    check_dependencies("grep", "sed")
    project_root = pathlib.Path(__file__).parent.parent.parent
    docs_dir = project_root / "docs"
    assert docs_dir.exists()
    tests_dir = project_root / "tests"
    assert tests_dir.exists()
    new_violations = sorted(
        set(get_snippet_definitions(tests_dir))
        .difference(set(get_snippets_used(docs_dir)))
        .difference(set(IGNORED_VIOLATIONS))
    )
    if new_violations:
        print(
            f"[ERROR] Found {len(new_violations)} snippets which are not used within a doc file."
        )
        for line in new_violations:
            print(line)
        sys.exit(1)


if __name__ == "__main__":
    main()
