import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("VERYFI_CLIENT_ID")
USERNAME  = os.getenv("VERYFI_USERNAME")
API_KEY   = os.getenv("VERYFI_API_KEY")

def call_veryfi(file_bytes, file_name):

    url = "https://api.veryfi.com/api/v8/partner/documents/"

    headers = {
        "CLIENT-ID":     CLIENT_ID,
        "AUTHORIZATION": f"apikey {USERNAME}:{API_KEY}"
    }

    files = {
        "file": (file_name, file_bytes)
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            files=files
        )

        data = response.json()

        print("VERYFI RESPONSE:", data)

        confidence = data.get("confidence", 50)
        fraud_info = data.get("fraud", {})
        triggers   = fraud_info.get("triggers", [])
        signal     = fraud_info.get("signal", "unknown")

        return {
            "confidence": confidence,
            "triggers":   triggers,
            "signal":     signal,
            "vendor":     data.get("vendor", {}).get("name", "Unknown"),
            "total":      data.get("total", 0),
            "date":       data.get("date", "Unknown"),
            "connected":  True
        }

    except Exception as e:
        print("VERYFI ERROR:", str(e))
        return {
            "confidence": 50,
            "triggers":   [],
            "signal":     "unknown",
            "vendor":     "Unknown",
            "total":      0,
            "date":       "Unknown",
            "connected":  False,
            "error":      str(e)
        }