#Define keys and region
provider "aws" {
access_key = "SECRET-ACCESS-KEY"
secret_key = "SECRET-KEY"
region = "us-west-2"
}
#Define ec2 instance 
resource "aws_instance" "instance1" {
ami = "ami-089668cd321f3cf82"
instance_type = "t2.micro"
tags = {
Name = "ubuntu-20.04"
}
}
#Define s3 bucket
resource "aws_s3_bucket" "bucket1" {
bucket = "bucket-launched-using-terrafrom-20210106"
acl = "public-read" 
tags = {
Name = "Bucket"
Environment = "Production"
}
}