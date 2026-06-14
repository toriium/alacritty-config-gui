import tomli_w

data = {
    "value": 42,
    "database": {
        "host": "localhost",
    },
    "l1": [1, 2, 3],
    "I1": {
        "IV1": "IV1",
        "I2": {
            "I3": {
            }
        }
    }
}

with open("config.toml", "wb") as f:
    tomli_w.dump(data, f)
