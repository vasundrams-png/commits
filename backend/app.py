from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Frontend-ல இருந்து Backend-க்கு data thadama varathuku ithu mukkiyam

# Simulated CVE & Trust-Chain Data Database (Mock Data)
VULNERABILITY_DB = {
    "lodash": {
        "version": "4.17.11",
        "risk_score": 9.6,
        "risk_level": "Critical",
        "issue": "CVE-2021-23337 (Prototype Pollution)",
        "recommendation": "Update to >=4.17.21",
        "type": "Library",
        "dependencies": ["Your Application"]
    },
    "jsonwebtoken": {
        "version": "8.5.1",
        "risk_score": 7.8,
        "risk_level": "High",
        "issue": "CVE-2022-23540 (Signature Verification Bypass)",
        "recommendation": "Update to >=9.0.2",
        "type": "Library",
        "dependencies": ["Your Application", "lodash"]  # Transitive dependency mapping
    },
    "axios": {
        "version": "1.2.0",
        "risk_score": 5.4,
        "risk_level": "Medium",
        "issue": "CVE-2023-45857 (Server-Side Request Forgery)",
        "recommendation": "Update to >=1.6.0",
        "type": "Library",
        "dependencies": ["Your Application"]
    },
    "firebase": {
        "version": "9.6.0",
        "risk_score": 3.2,
        "risk_level": "Low",
        "issue": "No known critical CVEs",
        "recommendation": "Keep up to date",
        "type": "SaaS / API",
        "dependencies": ["Your Application"]
    }
}

@app.route('/api/analyze', methods=['POST'])
def analyze_dependencies():
    data = request.json
    # Frontend input-la irunthu tech stack keywords-ah edukkurom
    user_input = data.get("tech_stack", "")
    
    # Text input-ah split panni individual packages-ah mathuroom
    requested_packages = [pkg.strip().lower() for pkg in user_input.replace(",", " ").split()]
    
    results = []
    total_score = 0
    count = 0
    
    # Matching data found in our simulated DB
    for pkg in requested_packages:
        if pkg in VULNERABILITY_DB:
            pkg_info = VULNERABILITY_DB[pkg].copy()
            pkg_info["name"] = pkg
            results.append(pkg_info)
            total_score += pkg_info["risk_score"]
            count += 1
            
    # Calculate Overall Risk Score
    overall_score = round(total_score / count, 1) if count > 0 else 0.0
    risk_status = "SAFE"
    if overall_score >= 7.0: risk_status = "HIGH RISK"
    elif overall_score >= 4.0: risk_status = "MEDIUM RISK"
    elif overall_score > 0: risk_status = "LOW RISK"

    return jsonify({
        "packages": results,
        "overall_score": overall_score,
        "risk_status": risk_status
    })


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)
