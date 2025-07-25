# 🚀 Advanced AWS Static Website Hosting with Multi-Site Setup Using S3, CloudFront & CloudWatch

## 📌 Project Overview

This project is a continuation of my AWS Cloud journey, where I previously hosted a static website on Amazon S3. In this advanced phase, I’ve implemented **multi-site static content hosting** with enhanced **CDN configurations**, **HTTPS security**, and **real-time monitoring** using CloudFront and CloudWatch.

---

## 🏗️ Architecture Summary

- **Primary Services Used:**  
  - Amazon S3  
  - Amazon CloudFront  
  - AWS Certificate Manager (ACM)  
  - Amazon CloudWatch

- **Domain Used:**  
  - `cdn.ronusubham.rf.gd` (Custom domain via ACM for HTTPS)

---

## 🌐 Multi-Site Hosting Strategy

- **Single S3 Bucket**:
  - Organized content as folders:  
    - `/` → Main Website  
    - `/portfolio/` → Portfolio Website  

- **Benefits**:
  - Cleaner folder structure
  - Easier content management
  - Efficient resource optimization  

---

## 🚀 CloudFront Configuration

- **Custom Distribution**:
  - Deployed a new CloudFront distribution for multi-site routing.

- **SSL/TLS Security**:
  - Integrated **ACM Certificate** for custom domain to ensure **HTTPS**.
  - Resolved “Not Secure” browser warnings.

- **Cache Behaviors**:
  - Defined path-based behavior rules:
    - `/portfolio/*` → Maps to `portfolio/` folder in S3.
    - `/` → Maps to main site.
  - Ensures seamless navigation and correct content delivery.

- **Custom Error Pages**:
  - Configured CloudFront to return `index.html` for `/portfolio/` path.
  - Solved `404 Not Found` errors when accessing sub-routes directly.

---

## 📊 CloudWatch Monitoring & Alarming

- **Metrics Tracked**:
  - `Requests`
  - `BytesDownloaded`
  - `CacheHitRate`
  - `4xxErrorRate`

- **Alerts**:
  - Configured CloudWatch Alarm to monitor high **4xx error rates**.
  - Sends notification when error threshold is breached.

---

## 🎯 Key Learnings & Takeaways

- Gained hands-on expertise in **multi-site hosting** using a single S3 bucket.
- Deep understanding of **CloudFront behavior patterns** and **custom error handling**.
- Secured site with **HTTPS** using ACM certificates.
- Implemented real-time **monitoring and alerting** with CloudWatch.
- Built scalable, secure, and observable web infrastructure following AWS best practices.

---


## 📚 Resources & References

- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/index.html)
- [Amazon CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [AWS Certificate Manager](https://docs.aws.amazon.com/acm/)
- [CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

---

## 🙌 Thank You

Always learning. Always building.  
If you found this project helpful, feel free to ⭐ the repo and connect!

