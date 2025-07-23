# 🏗️ 3-Tier Architecture Project on AWS (Free Tier)

This project demonstrates a complete **3-tier architecture** built using **only AWS Console** and strictly within the **Free Tier limits**. It includes:

- Public Web Tier (EC2 + Load Balancer)
- Private Application Tier (EC2 + Internal Load Balancer)
- Private Database Tier (RDS)
- VPC with subnets, route tables, security groups, and NACLs
- Monitoring with CloudWatch
- Optional: Logging to S3 via Kinesis Firehose

---

## 📌 Architecture Diagram

![Architecture Diagram](./screenshots/aws-3tier-diagram.png)


## 🚀 Services Used

| Tier        | AWS Services                              |
|-------------|-------------------------------------------|
| Web Tier    | EC2 (Amazon Linux), ALB, Security Groups  |
| App Tier    | EC2 (Private Subnet), Internal ALB        |
| DB Tier     | Amazon RDS (MySQL), Subnet Group          |
| Networking  | VPC, Subnets, Route Tables, NACLs         |
| Monitoring  | CloudWatch Logs, Alarms                   |
| Logging     | (Optional) Kinesis Firehose, S3           |

---

## 📍 CIDR Blocks and Subnets

- **VPC CIDR**: `10.0.0.0/16`

| Tier       | Subnet AZ1         | Subnet AZ2         |
|------------|--------------------|--------------------|
| Web Tier   | 10.0.1.0/24        | 10.0.4.0/24        |
| App Tier   | 10.0.2.0/24        | 10.0.5.0/24        |
| DB Tier    | 10.0.3.0/24        | 10.0.6.0/24        |

---

## 🛡️ Network ACLs

| Tier        | Inbound Rules                          | Outbound Rules                         |
|-------------|----------------------------------------|----------------------------------------|
| Web Tier    | Allow HTTP(80), HTTPS(443), SSH(22)    | Allow All                              |
| App Tier    | Allow from Web Tier subnet only        | Allow to DB Tier only                  |
| DB Tier     | Allow MySQL(3306) from App Tier only   | Deny All (For security)                |

---

## 🔐 Security Groups

| Component        | Inbound Allowed From            |
|------------------|---------------------------------|
| Web EC2          | 0.0.0.0/0 (HTTP, HTTPS, SSH)    |
| App EC2          | Web SG                          |
| RDS              | App SG                          |
| ALB (Web)        | 0.0.0.0/0                       |
| ALB (Internal)   | Web SG                          |

---

## 🧱 Key Resources Created

- **VPC** with 6 subnets (3 tiers × 2 AZs)
- **2 ALBs**:
  - Public for web EC2s
  - Internal for app EC2s
- **Auto Scaling Groups** (optional)
- **RDS MySQL instance** in DB Tier
- **Security groups** per layer for strict traffic control
- **NACLs** to add an extra layer of protection between tiers
- **CloudWatch** for monitoring
- **Kinesis Firehose + S3** for logs (optional)

---

## 📊 Monitoring Setup

- Enabled detailed monitoring on EC2 instances
- CloudWatch Alarms for CPU > 70%
- Log group created: `/aws/ec2/web-tier`, `/aws/ec2/app-tier`
- Logs shipped via Kinesis Firehose to S3 bucket (`3tier-logs-bucket`)

---

## 🧪 Testing

✅ Web Tier: Access via public ALB  
✅ App Tier: Private access only via internal ALB  
✅ DB Tier: Access only from App EC2  
✅ Logs visible in CloudWatch and S3  
✅ CPU Alarm triggered when tested with `stress` tool

---

## 📌 Optional Enhancements

- Add Route 53 for domain-based routing
- Use CloudFormation or Terraform for IaC
- Configure Auto Scaling Group for both EC2 tiers
- Add WAF for ALB security
- Add SNS for Alarm notifications

---

## 📸 Screenshots

All screenshots related to each step are inside the `screenshots/` folder.

---

## 🧾 Author Notes

This project was created strictly using AWS Free Tier resources. No paid services were used. Please double-check region-based limits before trying in production environments.

---

