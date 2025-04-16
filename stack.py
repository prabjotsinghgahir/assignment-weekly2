import os
from deploy_scripts import stack_deploy

template_name = 'templates/assignment-stack.yaml'
stack_name = 'assignment2'
source_bucket_name = "cf-tag-bucket-psg"
region = 'ap-south-1'


parameter = [
        {
            'ParameterKey': 'SourceBucketName',
            'ParameterValue': source_bucket_name
        }
]

opening_temp = open(template_name)
reading = opening_temp.read()

call_create_stack = stack_deploy.StackCreation(stack_name, reading, parameter)

call_create_stack.create_stack()
call_create_stack.stack_status()
