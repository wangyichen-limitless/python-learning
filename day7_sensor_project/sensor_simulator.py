import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 模拟 10 秒的传感器数据
time = np.linspace(0, 10, 100)
temperature = 25 + 5 * np.sin(time) + np.random.normal(0, 0.5, 100)
vibration = np.abs(np.sin(time * 2)) + np.random.normal(0, 0.1, 100)

# 把数据存成表格
df = pd.DataFrame({
    "Time(s)": time,
    "Temperature(C)": temperature,
    "Vibration(mm/s)": vibration
})

# 保存为 CSV 文件
df.to_csv("sensor_data.csv", index=False)
print("数据已保存为 sensor_data.csv")

# 画图
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(df["Time(s)"], df["Temperature(C)"], label="Temperature")
plt.xlabel("Time (s)")
plt.ylabel("Temp (C)")
plt.title("Temperature Over Time")

plt.subplot(1, 2, 2)
plt.plot(df["Time(s)"], df["Vibration(mm/s)"], label="Vibration", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Vibration (mm/s)")
plt.title("Vibration Over Time")

plt.tight_layout()
plt.show()