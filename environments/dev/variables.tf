variable "db_username" {
  type        = string
  description = "DB master username"
  sensitive   = true
}

variable "db_password" {
  type        = string
  description = "DB master password"
  sensitive   = true
}
