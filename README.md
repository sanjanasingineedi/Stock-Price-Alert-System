# 📈 Real-Time Stock Price Alert System

A cloud-native serverless application that automatically monitors stock prices and sends real-time alerts via **SMS** and **email** using **AWS services**. This project helps investors and traders stay updated and make quick decisions when market conditions change.

---

## 📝 Description

This system allows users to:
- Track specific stock prices in real time
- Define upper and lower price thresholds
- Receive instant alerts via SMS or email when those thresholds are crossed

It's built entirely on **AWS serverless architecture** using **Lambda**, **SNS**, **CloudWatch Events (EventBridge)**, and **IAM**, and developed within **AWS Cloud9**. It offers flexibility, scalability, and reduced operational overhead, making it a modern approach to financial alert systems.

---

## ✅ Features

- ⏱ **Real-Time Price Monitoring**
- 📤 **SNS Notifications (SMS/Email)**
- ☁️ **Fully Serverless Architecture**
- 💡 **Custom Threshold Triggers**
- 🔄 **Scheduled Lambda Execution**
- 🔐 **Secure IAM Role Configuration**
- 📈 **Scalable Cloud Solution**

---

## 🧠 What I Learned

- Designing **event-driven** architectures with AWS
- Creating **modular and secure Lambda functions**
- Managing environment variables and dependencies in **Cloud9**
- Handling **API rate limits** and errors gracefully
- Setting up **CloudWatch Event rules** to automate function triggers
- Applying **IAM principles** for least-privilege access

---

## 🧰 Technologies Used

| Service | Purpose |
|--------|---------|
| **AWS Lambda** | Executes stock checking logic |
| **Amazon SNS** | Sends alert messages to users |
| **Amazon CloudWatch + EventBridge** | Triggers Lambda on schedule |
| **AWS Cloud9** | Cloud-based IDE for coding and deployment |
| **IAM** | Manages permissions securely |
| **Alpha Vantage API** | Retrieves stock prices |

---

## 🛠 How to Use

### 📦 Prerequisites
- AWS Account (with IAM access to Lambda, SNS, CloudWatch)
- Alpha Vantage API Key
- AWS CLI or Management Console access

### 🔧 Setup Steps

1. **Create an SNS Topic**
   - Subscribe via Email or SMS

2. **Set Up Cloud9 Environment**
   - Create project directory  
   - Install `requests` library using:  
     `pip install requests -t .`

3. **Write and Zip Lambda Code**
   - Include `lambda_function.py` and dependencies  
   - Use `zip -r lambda_function.zip .` to create package

4. **Create Lambda Function**
   - Upload zip file in AWS Lambda Console  
   - Set environment variables:
     - `STOCK_API_KEY`, `STOCK_SYMBOL`, `SNS_TOPIC_ARN`, `UPPER_THRESHOLD`, `LOWER_THRESHOLD`

5. **Add SNS Publish Permissions via IAM Role**

6. **Schedule Execution with CloudWatch**
   - Use EventBridge to run the Lambda every 15 minutes using a `rate(15 minutes)` expression

7. **Test the System**
   - Use a manual test event in Lambda Console  
   - Monitor logs via CloudWatch

---

## 🧪 Use Cases

- 📈 Investment Monitoring  
- 🛡 Risk Alerts for Portfolio Management  
- 💼 Day Trading Automation  
- 📬 Watchlist Notifications  
- 🎓 Educational Tool for Real-Time Stock Analysis

---

## ⚠️ Challenges Faced

| Challenge | Solution |
|----------|----------|
| **API Rate Limiting** | Cached calls, used efficient schedule |
| **Lambda Packaging** | Used Cloud9 and zipped requests correctly |
| **IAM Permissions** | Created custom policies with least privilege |
| **Latency in Alerts** | Monitored Lambda and SNS logs |
| **Scheduling Errors** | Tested with CloudWatch Events |
| **Threshold Logic** | Calibrated to prevent unnecessary alerts |

---

## 👥 Credits

### Developed By:
**Sanjana Singineedi**  
[GitHub](https://github.com/sanjanasingineedi)  
📧 sanjanasingineedi0508@gmail.com  
**K.S.V.S.Sahithi,**
**E.Divya**

### Mentorship & Support:
**T-Hub, Aditya Educational Institutions**  
🌐 [https://technicalhub.io](https://technicalhub.io)  

---
