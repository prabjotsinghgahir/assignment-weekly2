"""Upload files to S3 Bucket"""
import boto3
import os
import logging

s3_client = boto3.client('s3')

logging.getLogger().setLevel("INFO")

class Upload:
    def __init__(self, bucket_name, cwd, key_tag1, value_tag1,
                 key_tag2, value_tag2, metadata_key1, metadata_value1,
                 metadata_key2, metadata_value2):
        self.bucket_name = bucket_name
        self.directory = cwd
        self.tag_key_value_pair1 = f"{key_tag1}={value_tag1}"
        self.tag_key_value_pair2 = f"{key_tag2}={value_tag2}"
        self.metadata_key_value_pair1 = f"{metadata_key1}:{metadata_value1}"
        self.metadata_key_value_pair2 = f"{metadata_key2}:{metadata_value2}"

    def upload_object_tag(self):
        count = 1
        try:
            for files in os.listdir(self.directory):
                if count <= 2:
                    print(f"Files in the directory: {files}")
                    s3_client.put_object(
                        Body = os.path.join(self.directory, files),
                        Bucket = self.bucket_name,
                        Key = files,
                        Tagging = f'{self.tag_key_value_pair1}'
                    )
                elif 2 < count <= 4:
                    s3_client.put_object(
                        Body=os.path.join(self.directory, files),
                        Bucket=self.bucket_name,
                        Key=files,
                        Tagging=f'{self.tag_key_value_pair2}'
                    )
                count = count + 1
        except FileNotFoundError:
            logging.error("File does not exists run folder.py script")
        except s3_client.exceptions.NoSuchBucket:
            logging.error("Bucket does not exists")


if __name__ == "__main__":
    bucket = "cf-tag-bucket-psg"
    folder_name = "Natural_Numbers"
    curr_dir = os.path.join(os.getcwd(), folder_name)
    tag_key1 = "file"
    tag_value1 = "text"
    tag_key2 = "file"
    tag_value2 = "yaml"
    key_metadata1 = "table"
    value_metadata1 = "chair"
    key_metadata2 = "copy"
    value_metadata2 = "pen"
    upload_object = Upload(bucket, curr_dir, tag_key1, tag_value1,
                           tag_key2, tag_value2, key_metadata1, value_metadata1,
                           key_metadata2, value_metadata2)

    upload_object.upload_object_tag()

