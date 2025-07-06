variable "name" {
    description = "Name prefix of resources"
    type        = string
}

variable "vpc_cidr" {
    description = "CIDR block for the VPC"
    type        = string        
  
}

variable "public_subnet_cidrs" {
    description = "List of CIDR blocks for public subnets"
    type        = list(string)
    # default     = []
  
}

variable "private_subnet_cidrs" {
    description = "List of CIDR blocks for private subnets"
    type        = list(string)
    # default     = []
  
}

variable "availability_zones" {
    description = "List of availability zones for the subnets"
    type        = list(string)
    # default     = []
  
}