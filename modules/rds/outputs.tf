output "rds_endpoint" {
  description = "RDS endpoint to connect to the database"
  value       = aws_db_instance.default.endpoint
}

output "rds_instance_id" {
  description = "RDS instance ID"
  value       = aws_db_instance.default.id
}

output "rds_arn" {
  description = "RDS instance ARN"
  value       = aws_db_instance.default.arn
}


output "db_identifier" {
  description = "RDS Identifier"
  value       = aws_db_instance.main.id
}