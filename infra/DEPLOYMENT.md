# AWS deployment blueprint (not executed)

Prerequisites: authorized AWS account, budget alert, CLI, Docker, IAM execution role and approved VPC networking.

1. Create an ECR repository and CloudWatch log group `/ecs/opsstatus`. Build, tag and push the image to your ECR URI.
2. Replace placeholders in task-definition.json and register it using `aws ecs register-task-definition --cli-input-json file://task-definition.json`.
3. Create an ECS Fargate service with approved networking and health checks on /health. Prefer private subnets with ECR/log connectivity and an HTTPS load balancer. Do not expose this unauthenticated demo directly to the public internet.
4. Verify service events, health and logs with fictional input. Production requires authentication, rate limits, monitoring and security review.
5. Tear down only your demo resources to avoid ongoing charges.

Do not commit credentials. This is a runbook, not deployed infrastructure.
