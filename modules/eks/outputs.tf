output "cluster_name" {
  description = "Name of the EKS cluster"
  value       = aws_eks_cluster.eks.name
  
}

output "cluster_endpoint" {
  description = "Endpoint of the EKS cluster"
  value       = aws_eks_cluster.eks.endpoint
  
}

output "cluster_arn" {
  description = "EKS cluster ARN"
  value       = aws_eks_cluster.eks.arn
}

output "node_security_group_id" {
  description = "Security Group ID of the EKS worker nodes"
  value       = aws_eks_node_group.eks_node_group.resources[0].autoscaling_groups[0].security_group
}