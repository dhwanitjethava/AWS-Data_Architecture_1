
# AWS Data Architecture

Use of S3, Lambda, RDS, MySQL Workbench, CloudWatch and IAM role


<img width="1342" alt="Screen Shot 2022-03-28 at 2 45 38 pm" src="https://user-images.githubusercontent.com/96478746/160584241-d578e3c1-48fe-4998-9c1b-5cd3c9c76d7a.png">


**1. Create S3 Bucket**

- Name - **aws-learning-scaletech**  
- Bucket & Objects - **private access**  
- AWS Region - **ap-south-1**  

**2. Create S3 Bucket**  
- Create a folder - **JSON_files/(object of S3)**  
- S3 URI - **s3://aws-learning-scaletech/JSON_files/**  

**3. Properties of S3 bucket** (Event Notifications)
- Name - **09f29903-9ce3-4728-bad8-47fa925311ba**  <img width="1342" alt="image" src="https://user-images.githubusercontent.com/96478746/160584304-3e6e23f0-0ef9-4ca2-b545-f891dc67dbe3.png">

- Event type - **PUT**  
- Filters - Prefix: **JSON_files/** | Suffix: **.json**  
- Destination type - **Lambda function**  
- Destination - **ReadDataFromS3-JSON**

**4. Create IAM role**  
- Name - **aws-learning-lambda-role-s3-cw**  
- Description - **Allows Lambda functions to call AWSs on your behalf.**   
- Policies :  
    - **CloudWatchFullAccess** 
    - **AmazonS3FullAccess**

**5. Create Lambda function**  
- Name - **ReadDataFromS3-JSON**  
- Runtime - **Python 3.8**  
- Role - **Use existing role** **(aws-learning-lambda-role-s3-cw)**

**6. Add Lambda Trigger** (Trigger Configuration)
- Select **S3 trigger**  
- Select S3 Bucket **aws-learning-scaletech**  
- Event type - **PUT**  
- Prefix: **JSON_files/**  
- Suffix: **.json**  

**7. Verify the event coming in when Lambda trigger**  
- **Note** - You have to write a code for testing lambda when we upload file in S3 bucket. Please refer GitHub.  

**8. For verification of Lambda trigger**  
- Upload file in S3 bucket.
- Open a CloudWatch and there should be **Log Groups** entry for **Lambda function trigger**. (Fix errors)
- There is event in log file and you can that view in Online json viewer.
- Please check hierarchy of function and location of file that uploaded in S3.  
- Write Lambda function code in **Python** for read data from json file.  

**9. Create RDS Schema**
- Creation Method - **Easy create**
- Configuration - **MySQL** (Free tier)
- DB instance - **employee-db**
- Master Username - **admin**
- Password - **admin1234**
- Access - **Public accessibility** 

**10. Make changes in Security Group configuration**  
- Make sure, it is **Public Accessible**
- Check the security group configuration for **Inbound** and **Outbound**
- You have to add rule on **Inbound**

**11. Connect to MySQL Workbench**
- Open **MySQL Workbench** and Create a **connection**
- Connection Name - **AWS_RDS**
- Connection Method - **Standard (TCP/IP)**
- Hostname - **Endpoint**
- Port - **3306**
- Username - **admin**
- Password - **admin1234**

#### *Java need to install on your machine to work with MySQL workbench*

**12. Open existing role in IAM role**  
- Existing role - **aws-learning-lambda-role-s3-cw**
- Attach **AmazonRDSFullAccess** policy to existing **IAM role**

**13. Connect to RDS instance in Lambda function**
- Configuration as required below:
- db_host = **AWS RDS Endpoint**
- db_username = **admin**
- db_password = **admin1234**
- db_name = **employee_db**

#### *Further, please refer lambda_function.py*
