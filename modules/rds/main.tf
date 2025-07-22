resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "${var.name}-rds-subnet-group"
  subnet_ids = var.subnet_ids

  tags = {
    Name = "${var.name}-rds-subnet-group"
  }
}

data "aws_secretsmanager_secret_version" "db_credentials" {
  secret_id = "rds/dev/db_credentials"
}

locals {
  db_credentials = jsondecode(data.aws_secretsmanager_secret_version.db_credentials.secret_string)
}



resource "aws_db_instance" "main" {
  allocated_storage      = 20
  engine                 = "mysql"
  engine_version         = "8.0"
  instance_class         = "db.t3.micro"
  identifier             = "${var.name}-db"
  username               = local.db_credentials.username
  password               = local.db_credentials.password
  db_subnet_group_name   = aws_db_subnet_group.rds_subnet_group.id
  vpc_security_group_ids = var.security_group_ids
  multi_az               = false
  publicly_accessible    = false
  skip_final_snapshot    = true
}

# resource "aws_db_instance" "postgres" {
#   allocated_storage      = 20
#   engine                 = "postgres"
#   engine_version         = "15.5"
#   instance_class         = "db.t3.micro"
#   identifier             = "${var.name}-postgres-db"
#   username               = local.postgres_credentials.username
#   password               = local.postgres_credentials.password
#   db_subnet_group_name   = aws_db_subnet_group.rds_subnet_group.id
#   vpc_security_group_ids = var.security_group_ids
#   multi_az               = false
#   publicly_accessible    = false
#   skip_final_snapshot    = true

#   tags = {
#     Name = "${var.name}-postgres-db"
#   }
# }



