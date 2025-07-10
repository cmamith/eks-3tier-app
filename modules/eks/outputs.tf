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
  description = "Security Group ID of the EKS node group"
  value       = aws_security_group.eks_node_group_sg.id
}
