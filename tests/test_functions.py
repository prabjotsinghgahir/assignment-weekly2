"""Testing file for moto mocking AWS"""
import boto3
from moto import mock_aws

from main import Delete
from upload_files import Upload

bucket_name = "my-bucket" # "cf-tag-bucket-psg"


def upload():
    s3_client = boto3.client('s3')
    folder_dir = "D:/assignments/Assignment2/Natural_Numbers"
    s3_client.create_bucket(Bucket=bucket_name)
    upload_obj = Upload(bucket_name, folder_dir,
                        "file", "text", "file",
                        "yaml", "table", "chair",
                        "copy", "pen")
    upload_obj.upload_object_tag()
    #rs = s3_client.list_objects(Bucket=bucket_name)

    #assert len(rs['Contents']) == 10 #Upload test case


@mock_aws()
def test_upload():
    upload()
    s3_client = boto3.client('s3')
    """Upload test case"""
    rs = s3_client.list_objects(Bucket=bucket_name)
    assert len(rs['Contents']) == 10  # Upload test case


@mock_aws()
def test_delete_tag_meta():
    upload()
    s3_client = boto3.client('s3')
    delete_obj = Delete("file", "text", "copy",
                           "pen", bucket_name)
    """Delete Tag test case"""
    delete_obj.delete_tag()
    rs = s3_client.list_objects(Bucket=bucket_name)
    assert len(rs['Contents']) == 8

    """Delete Metadata test case"""
    delete_obj.delete_meta()
    rs = s3_client.list_objects(Bucket=bucket_name)
    assert len(rs['Contents']) == 4
