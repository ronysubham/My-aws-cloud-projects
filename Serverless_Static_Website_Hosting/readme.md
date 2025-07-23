🌐 Serverless Static Website Hosting on AWS with CloudFront, S3 & ACM
Deploy a blazing-fast, secure, and serverless static website using AWS CloudFront, S3, ACM, and a free custom subdomain — all at zero cost. This project is a perfect example of modern web hosting using CDNs and HTTPS with a focus on cost efficiency, resilience, and DNS troubleshooting.



📌 Project Objective
Build and deploy a fully static HTML/CSS website using AWS services like:

Amazon S3 (for static hosting),

AWS CloudFront (for global content delivery),

AWS Certificate Manager (for HTTPS),

and a free subdomain from InfinityFree with DNS integration.

The main goal: deliver secure, high-availability, and fast content with custom domain & SSL — without paying a penny.

⚙️ Tech Stack & Tools Used
Service / Tool	Purpose
🗂️ Amazon S3	Store and serve static website content
🌍 Amazon CloudFront	CDN to reduce latency and deliver globally
🔐 AWS ACM	Provision & manage SSL certificates (HTTPS)
🌐 InfinityFree	Free subdomain provider + DNS configuration
💻 HTML/CSS	Simple static website design (index & error)

🛠️ Step-by-Step Implementation
1️⃣ S3 Static Website Setup
Created an S3 bucket configured for static website hosting.

Uploaded index.html and error.html.

Enabled public access for CloudFront to fetch files.

2️⃣ SSL Certificate via AWS ACM
Requested a free SSL cert for cdn.ronusubham.rf.gd in us-east-1.

Verified domain by adding CNAME records in InfinityFree DNS.

Waited for DNS propagation and cert validation.

3️⃣ CloudFront Distribution
Set up CloudFront to:

Use S3 as the origin.

Set index.html as the default root object.

Add the ACM SSL cert for HTTPS.

Set CNAME as cdn.ronusubham.rf.gd.

4️⃣ DNS Configuration (Big Lesson!)
🛑 Challenge: InfinityFree restricts direct A/CNAME for ronusubham.rf.gd or www.

✅ Solution: Used a deeper subdomain — cdn.ronusubham.rf.gd.

Created a CNAME record pointing to CloudFront’s domain (e.g., d1xxx.cloudfront.net).

5️⃣ Testing & Troubleshooting
Tested site at https://cdn.ronusubham.rf.gd (not live right now )

Resolved DNS_PROBE_FINISHED_NXDOMAIN errors:

Verified DNS records.

Waited for propagation (~5–15 mins).

Used tools like whatsmydns.net and flushed DNS cache locally.

🎯 Key Learnings
✅ Hands-on with real-world DNS configuration and troubleshooting
✅ How to secure websites using ACM + CloudFront
✅ Leveraging free tools and services for production-grade deployment
✅ Understanding service limitations and adapting smartly

✨ Outcome
A fully working static website served globally via CloudFront CDN, secured by SSL, and mapped to a custom subdomain — all without touching a server or backend! ⚡️