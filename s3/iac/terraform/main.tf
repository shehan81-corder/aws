terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.73.0"
    }
  }
}

provider "aws" {
  # Configuration options
  module "s3-bucket" {
    source  = "terraform-aws-modules/s3-bucket/aws"
    version = "5.17.1"
  } 
}