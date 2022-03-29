
# AWS Data Architecture

Use of S3, Lambda, RDS, MySQL Workbench, CloudWatch and IAM role

**1. Create S3 Bucket**

Name - **aws-learning-scaletech**  
Bucket & Objects - **private access**  
AWS Region - **ap-south-1**  

**2. Create S3 Bucket**  
Create a folder - **JSON_files/(object of S3)**  
S3 URI - **s3://aws-learning-scaletech/JSON_files/**  

**3. Properties of S3 bucket**  
**Event Notifications:**  
Name - **09f29903-9ce3-4728-bad8-47fa925311ba**  
Event type - **PUT**  
Filters - Prefix: **JSON_files/** | Suffix: **.json**  
Destination type - **Lambda function**  
Destination - **ReadDataFromS3-JSON**

