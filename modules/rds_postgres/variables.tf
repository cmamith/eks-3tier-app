variable "name" {
  description = "Prefix name for RDS resources"
  type        = string
}

variable "subnet_ids" {
  description = "List of private subnet IDs for RDS"
  type        = list(string)
}


variable "security_group_id" {
  description = "Security group for RDS access"
  type        = string
  }

variable "security_group_ids" {
  description = "List of security group IDs to associate with the RDS instance"
  type        = list(string)
}