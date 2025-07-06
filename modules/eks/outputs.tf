output "cluster_name" {
  description = "Name of the EKS cluster"
  value       = aws_eks_cluster.main.name
  
}

output "cluster_endpoint" {
  description = "Endpoint of the EKS cluster"
  value       = aws_eks_cluster.main.endpoint
  
}

output "cluster_arn" {
  description = "EKS cluster ARN"
  value       = aws_eks_cluster.eks.arn
}