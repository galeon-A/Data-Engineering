import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate(n=5000):
    base_time = datetime.now()

    data = []
    for i in range(n):
        data.append({
            "txn_id": i,
            "customer_id": random.randint(1, 200),
            "merchant_id": random.randint(1, 80),
            "amount": round(np.random.exponential(scale=500), 2),
            "country": random.choice(["IN", "US", "UK", "SG"]),
            "timestamp": (base_time - timedelta(minutes=random.randint(0, 10000))).isoformat()
        })

    df = pd.DataFrame(data)
    df.to_csv("data/raw/transactions.csv", index=False)

if __name__ == "__main__":
    generate()
