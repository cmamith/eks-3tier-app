output "db_identifier" {
  description = "RDS Identifier"
  value       = aws_db_instance.main.id
}

output "rds_endpoint" {
  description = "RDS Endpoint"
  value       = aws_db_instance.main.endpoint
}

output "rds_instance_id" {
  description = "RDS Instance ID"
  value       = aws_db_instance.main.id
}

output "rds_arn" {
  description = "RDS ARN"
  value       = aws_db_instance.main.arn
}

# output "postgres_endpoint" {
#   value = aws_db_instance.postgres.endpoint
# }

# output "postgres_instance_id" {
#   value = aws_db_instance.postgres.id
# }