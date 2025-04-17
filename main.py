"""This script deletes object from S3 based on specific tags and metadata"""
import boto3
import logging

s3_client = boto3.client('s3')

logging.getLogger().setLevel("INFO")


class Delete:
    def __init__(self, tag_key, tag_value, meta_key, meta_value, bucket):
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.meta_key = meta_key
        self.meta_value = meta_value
        self.bucket = bucket

    def delete_tag(self):
        paginator = s3_client.get_paginator('list_objects_v2')
        try:
            response_iterator = paginator.paginate(
                Bucket=self.bucket
            )
            for iterate in response_iterator:
                try:
                    for objects in iterate["Contents"]:
                        response = s3_client.get_object_tagging(
                            Bucket=self.bucket,
                            Key=objects["Key"]
                        )
                        if len(response["TagSet"]) == 0:
                            continue
                        for tags in response["TagSet"]:
                            if tags["Key"] == self.tag_key and tags["Value"] == self.tag_value:
                                s3_client.delete_object(
                                    Bucket=self.bucket,
                                    Key=objects["Key"]
                                )
                except KeyError as e:
                    logging.error("Bucket is empty")
                    raise Exception(e)
        except s3_client.exceptions.NoSuchBucket:
            logging.error(f"No such bucket present {self.bucket}")
            raise Exception("Bucket not present")

    def delete_meta(self):
        paginator = s3_client.get_paginator('list_objects_v2')
        try:
            response_iterator = paginator.paginate(
                Bucket=self.bucket
            )
            for iterate in response_iterator:
                try:
                    for objects in iterate["Contents"]:
                        response = s3_client.head_object(
                            Bucket=self.bucket,
                            Key=objects["Key"]
                        )
                        if len(response["Metadata"]) == 0:
                            continue
                        #  print(f"File name: {objects["Key"]}")
                        for key, value in response["Metadata"].items():
                            if key == self.meta_key and value == self.meta_value:
                                s3_client.delete_object(
                                    Bucket=self.bucket,
                                    Key=objects["Key"]
                                )
                except KeyError as e:
                    logging.error("Bucket is empty")
                    raise Exception(e)
        except s3_client.exceptions.NoSuchBucket:
            logging.error(f"No such bucket present {self.bucket}")
            raise Exception("Bucket not present")


if __name__ == "__main__":
    bucket_name = "cf-tag-bucket-psg"
    delete_object = Delete("file", "text", "copy",
                           "pen", bucket_name)
    logging.info("Staring deletion")
    delete_object.delete_tag()
    delete_object.delete_meta()
    logging.info("Deletion completed")
