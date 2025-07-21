# 🏗️ Three-Tier Web Application Architecture on AWS (Hands-On Project)

This README outlines a **complete real-world AWS project** that demonstrates deploying a **secure, scalable, and highly available 3-tier web application** infrastructure, strictly using the **AWS Free Tier**. This project includes **both console and CLI commands**, and is crafted to match **industry standards**.

---

## 📌 Project Objectives

* 🛠️ Build an end-to-end 3-tier architecture (Web, App, DB)
* 🌐 Host frontend (nginx) and backend (Node.js + Express) using EC2
* 💾 Use MySQL RDS as backend database (Free Tier eligible)
* ☁️ Store uploaded files securely in S3
* ⚖️ Balance traffic using Application Load Balancer (External + Internal)
* 📈 Implement Auto Scaling for high availability
* 🔒 Configure IAM, NACL, SG for secure networking

---


### ✳️ Layers:

* **Web Tier**: Public EC2 instances with nginx
* **App Tier**: Private EC2 instances with Node.js backend
* **DB Tier**: Private RDS MySQL instance

### 🔧 AWS Services Used:

* **VPC**, **Subnets** (6 total)
* **EC2 Instances** (Amazon Linux 2)
* **Application Load Balancers** (External + Internal)
* **Auto Scaling Group** with Launch Template
* **Amazon RDS** (MySQL - Free Tier)
* **S3 Bucket** (for file uploads)
* **IAM Role** for S3 access
* **Security Groups** & **Network ACLs**

---

## 🏁 Step-by-Step Implementation

### 1. 🌐 VPC and Subnets Creation

* VPC CIDR: `10.0.0.0/16`
* AZs: `ap-south-1a`, `ap-south-1b`
* Subnets:

  * Web Tier: `10.0.1.0/24`, `10.0.4.0/24`
  * App Tier: `10.0.2.0/24`, `10.0.5.0/24`
  * DB Tier: `10.0.3.0/24`, `10.0.6.0/24`

### 2. 🚪 Internet Gateway + Route Tables

* Attach IGW to VPC
* Create public route table (route to IGW)
* Create private route table (with NAT Gateway)
* Associate route tables with corresponding subnets

### 3. 📦 S3 Bucket

```bash
aws s3 mb s3://my-app-bucket --region ap-south-1
```

* Enable Versioning
* Block All Public Access
* Add bucket policy to allow access from EC2 IAM role only

### 4. 🔐 IAM Role for EC2 (App Tier)

* Create role with `AmazonS3FullAccess`
* Attach to App EC2s

### 5. 🛡️ Security Groups

* Web SG: Allow HTTP/HTTPS from internet
* App SG: Allow traffic only from Web SG
* DB SG: Allow MySQL (port 3306) from App SG only

### 6. 📊 Network ACL Rules

* **Web Tier Subnets:**

  * Inbound: Allow 80, 443 from 0.0.0.0/0
  * Outbound: Allow all ephemeral ports
* **App Tier Subnets:**

  * Inbound: Allow 3000 from Web Tier subnets
  * Outbound: Allow port 3306 to DB Tier
* **DB Tier Subnets:**

  * Inbound: Allow 3306 from App Tier only
  * Outbound: Deny all except internal traffic

### 7. ⚙️ EC2 Instance Launch (Web & App Tier)

* Use **Amazon Linux 2 AMI (Free Tier eligible)**
* Install packages:

  ```bash
  sudo yum install git nginx nodejs npm -y
  ```
* Attach IAM Role to App EC2

### 8. 🚀 Node.js App Setup on App Tier

```bash
git clone https://github.com/your-node-app.git
cd your-node-app
npm install
npm install multer dotenv aws-sdk
```

* Run with PM2 (production ready):

```bash
npm install -g pm2
pm2 start app.js
```

### 9. 🌐 nginx Setup on Web Tier

* Configure reverse proxy:

```nginx
location /api/ {
  proxy_pass http://<Internal-ALB-DNS>;
}
```

* Restart nginx:

```bash
sudo systemctl restart nginx
```

### 10. 🧱 RDS MySQL Setup

* MySQL (Free Tier)
* Public Access: Disabled
* Subnet Group: Select DB Tier subnets
* DB SG: MySQL access only from App SG

### 11. ⚖️ Application Load Balancers

* **External ALB**:

  * Routes internet traffic to Web Tier EC2s
  * Listeners: HTTP (80)
* **Internal ALB**:

  * Routes internal traffic to App Tier EC2s
  * Listener: HTTP (3000 or app port)

### 12. 📈 Auto Scaling Group + Launch Template

* Create Launch Template for App EC2
* User-data script for app installation
* Create ASG linked to Internal ALB Target Group
* Define Scaling Policies based on CPU utilization

---

