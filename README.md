#Assignment2

This has been made for weekly assignment2.

Below is a short description of different files:
1. .github/workflows/workflow.yaml => This is a github workflow file. This file runs when a push is happened on dev branch or pull request on main branch.
2. deploy_scripts/stack_deploy.py => This file creates a cloudformation stack using templates/copy-object-stack.yaml file. If the stack is already present then it will update the stack(if any updates are there to perform).
3. templates/assignment-stack.yaml => Cloudformation Template file.
4. main.py => This file will fetch all the files from S3 and will delete the one with specific tags and metadata.
5. folder.py => This file make a new folder Natural_Numbers in same directory. Then creates 10 files and write the name of the file as contents in the file, then adds these 10 text files in that folder Natural_Numbers.
6. upload_files.py => This file uploads all the text files from Natural_Numbers folder to S3 bucket with tags and metadata.
7. tests/test_functions.py => This is a test file which uses moto and pytest library to test the functions that are present in above files.

Flow:
1. Run stack.py file or GitHub workflows to deploy infrastructure.
2. Run folder.py to make folder and create files in it.
3. Then run upload_files.py to upload files in S3 bucket with specific tags and metadata.
4. Then run main.py to fetch all the files from S3 and deletes the one with specific tags and metadata.