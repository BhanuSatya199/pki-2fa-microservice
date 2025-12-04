#!/usr/bin/env python3
from app.totp_utils import generate_totp_code
from datetime import datetime, timezone
import os

DATA_PATH = "/data/seed.txt"

def main():
    try:
        if not os.path.exists(DATA_PATH):
            print("Seed not found", flush=True)
            return
        with open(DATA_PATH) as f:
            seed = f.read().strip()

        code = generate_totp_code(seed)
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        print(f"{ts} - 2FA Code: {code}", flush=True)

    except Exception as e:
        import sys
        print(str(e), file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
