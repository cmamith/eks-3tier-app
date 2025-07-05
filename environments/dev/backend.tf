terraform {
  backend "s3" {
    bucket         = "interview-project-s3-20021988"
    key            = "eks/dev/terraform.tfstate"
    region         = "ap-southeast-1"
    dynamodb_table = "interiew-project-locktable"
    encrypt        = true
  }
}