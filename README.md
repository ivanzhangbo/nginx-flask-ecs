# AWS ECS deploy Nginx+Flask(Use Service Discovery)

1.CFn运行ecs-template.yml,创建基本的VPC，Subnent，安全组和Cloud9

1.创建ECR并将镜像上传

2.分别创建Nginx Task和Flask Task

3.创建Flask Service的时候选择Use Service Discovery