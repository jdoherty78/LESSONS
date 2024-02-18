###  add key and key value of either legacy or current
[data_curr[i].update({"type": "current"}) for i in range(len(data_curr))]
[data_legacy[i].update({"type": "legacy"}) for i in range(len(data_legacy))]

combined_data = data_curr + data_legacy
print(len(combined_data))
combined_data
