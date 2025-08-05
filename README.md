## 🛡️ Phishing URL Analyzer

A Python script that analyzes URLs to detect **phishing attempts**, **domain spoofing**, and **unsecure connections**. It compares input URLs to a list of trusted domains and checks for similar-looking or suspicious links using **Levenshtein similarity**.

---

### ✅ Features

* 🔍 **Breaks down** each URL into:

  * Protocol
  * Subdomain
  * Domain
  * TLD (Top-Level Domain)
* 🔁 Compares domain with trusted sites using **fuzzy string matching**
* ⚠️ Flags:

  * **Exact matches** as ✅ legit
  * **Close matches** as ⚠️ lookalike (possible phishing)
  * **Others** as ❌ suspicious or malicious
* 🚨 Warns when the URL uses **HTTP** instead of HTTPS

---

### 🧪 Example Analysis

```python
url_list = [
    'http://payp@l.com',
    'https://google.com',
    'http://faceb00k.com',
    'http://amazon.con',
    'http://etc.co',
]
```

Output:

```
🔎 Analyzing: http://payp@l.com
🔗 Protocol: HTTP | Main: payp@l | TLD: com | Sub: 
🚨 Caution: Using HTTP — data is not encrypted!
❌ Danger: Unknown or deceptive domain detected!

🔎 Analyzing: https://google.com
🔗 Protocol: HTTPS | Main: google | TLD: com | Sub: 
✅ Safe: Domain matches trusted list.

🔎 Analyzing: http://faceb00k.com
🔗 Protocol: HTTP | Main: faceb00k | TLD: com | Sub: 
🚨 Caution: Using HTTP — data is not encrypted!
⚠️ Alert: Domain closely resembles a trusted one — possible phishing.
```

---

### 🧠 How It Works

| Step | Action                                                                        |
| ---- | ----------------------------------------------------------------------------- |
| 1️⃣  | URL is parsed using `urlparse` and `tldextract`                               |
| 2️⃣  | The domain is reconstructed (e.g., `facebook.com`)                            |
| 3️⃣  | Each domain is compared with trusted domains using **Levenshtein similarity** |
| 4️⃣  | Categorized as: `legit`, `lookalike`, or `suspicious`                         |

---

### 🧰 Requirements

Install required Python libraries:

```bash
pip install tldextract python-Levenshtein
```

---

### 📌 Trusted Domains

You can define your own trusted domain list in the script:

```python
trusted_sites = [
    'paypal.com',
    'google.com',
    'facebook.com',
    'amazon.com',
    'etc.com'
]
```

🔄 **Extend or modify** this list based on your organizational or personal needs.

---

### 📜 License

This project is open-source and licensed under the MIT License.

---

### 🤝 Contribute

Contributions are welcome! Feel free to:

* Add features (e.g., GUI, file input, logging)
* Improve detection logic
* Add support for internationalized domain names (IDNs)

---
