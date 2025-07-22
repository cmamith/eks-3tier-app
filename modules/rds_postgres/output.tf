output "db_identifier" {
  description = "PostgreSQL RDS Identifier"
  value       = aws_db_instance.main.id
}

output "rds_endpoint" {
  description = "PostgreSQL RDS Endpoint"
  value       = aws_db_instance.main.endpoint
}

output "rds_instance_id" {
  description = "PostgreSQL RDS Instance ID"
  value       = aws_db_instance.main.id
}

output "rds_arn" {
  description = "PostgreSQL RDS ARN"
  value       = aws_db_instance.main.arn
}
