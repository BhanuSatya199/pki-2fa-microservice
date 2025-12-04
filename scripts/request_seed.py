import requests
import json

api_url = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"
student_id = "23A91A05A0"
repo_url = "https://github.com/BhanuSatya199/pki-2fa-microservice"

with open("student_public.pem","r") as f:
    pub = f.read()

payload = {
    "student_id": student_id,
    "github_repo_url": repo_url,
    "public_key": pub
}
resp = requests.post(api_url, json=payload, timeout=30)
resp.raise_for_status()
data = resp.json()

with open("encrypted_seed.txt","w") as f:
    f.write(data["encrypted_seed"])

print("encrypted_seed saved to encrypted_seed.txt")
