Add a CSV `Asset` into your `Data Source` by using the `add_csv_asset` function.

```python name="tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py get_spark_s3_asset"
```

Here we have added a `Asset` named `csv_taxi_s3_asset` using the `add_csv_asset` function. The `batching_regex` is a regular expression that 
indicates which files to treat as Batches in the Asset, and how to identify them. 

In our example, the pattern `r".*_(?P<year>\d{4})\.csv",` is intended to build a Batch for each file in the S3 bucket, which are:

```
    yellow_tripdata_sample_2020.csv
    yellow_tripdata_sample_2021.csv
    yellow_tripdata_sample_2022.csv
```

The `batching_regex` pattern will match the 4 digits of the year portion and assign it to the `year` domain.

