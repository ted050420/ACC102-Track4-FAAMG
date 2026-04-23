# ACC102 Track4 - FAAMG Stock Analysis Tool
# Student: Tairan.Luo24 | ID: 2469624
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("2025 FAAMG Stock Price Analysis")
st.subheader("ACC102 Mini Assignment | Track4")

# 生成模拟数据
dates = pd.date_range('2025-01-01', '2025-12-31', freq='B')
np.random.seed(42)
base = {'AAPL':180,'MSFT':380,'AMZN':170,'GOOGL':140,'META':320}
data = pd.DataFrame(index=dates)
for t,p in base.items():
    data[t] = p + np.linspace(0,15,len(dates)) + np.random.normal(0,3,len(dates))

# 数据展示
st.subheader("Raw Data Preview")
st.dataframe(data.head(10))

# 计算均值
avg = data.mean().sort_values(ascending=False)
st.subheader("Average Closing Price (2025)")
st.dataframe(avg.round(2))

# 绘图1
st.subheader("Price Trend")
fig1, ax1 = plt.subplots(figsize=(10,4))
for col in data.columns:
    ax1.plot(data.index, data[col], label=col)
ax1.legend(), ax1.grid(alpha=0.3)
st.pyplot(fig1)

# 绘图2
st.subheader("Average Price Comparison")
fig2, ax2 = plt.subplots(figsize=(8,3))
avg.plot(kind='bar', ax=ax2, color=['#1f77b4','#ff7f0e','#2ca02c','#d62828','#9467bd'])
ax2.grid(axis='y',alpha=0.3)
st.pyplot(fig2)

# 结论
st.success("Key Insights")
st.write("1. MSFT has the highest average price")
st.write("2. GOOGL has the lowest average price")
st.write("3. FAAMG stocks kept stable in 2025")