module "vpc" {
  source = "../../modules/vpc"

  name                = "dev"
  vpc_cidr            = "10.0.0.0/16"
  public_subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnet_cidrs = ["10.0.101.0/24", "10.0.102.0/24"]
  availability_zones  = ["ap-southeast-1a", "ap-southeast-1b"]
}

module "eks" {
  source = "../../modules/eks"

  name       = "dev"
  subnet_ids = module.vpc.public_subnet_ids
  vpc_id     = module.vpc.vpc_id

  desired_capacity = 2
  min_size         = 1
  max_size         = 3
}