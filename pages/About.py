import streamlit as st
st.markdown("<h1 style='text-align: center; color: white;'>ABOUT  PROJECT</h1>", unsafe_allow_html=True)
st.markdown("<p color: white;'>This is an Energy Consumption Analysis Web App. This app is created using Streamlit and Python. In this Web App we have analysed the Energy Consumption dataset from kaggle.</p>", unsafe_allow_html=True)

st.markdown("<p color: white;>For Analysis Purpose we have used the following charts: </p>",unsafe_allow_html=True)
st.markdown("1. Bar Chart")
st.markdown("2. Histogram Chart")
st.markdown("3. Line Chart")
st.markdown("4. Pie Chart")
st.markdown("5. Time Series Chart")

st.markdown("### 🌟 Introduction\n\nThe Energy Consumption Analysis app presents visualizations of energy generation and consumption patterns. Users can explore insights from the data, including the generation trends for fossil gas, fossil oil, and nuclear energy, as well as the proportion of forecasted load vs. actual load and the distribution of fossil fuel generation over time. Interactive pie charts showcase the proportions of various renewable energy sources, while histograms and area charts depict the generation trends for fossil hard coal, solar, and nuclear energy.")

# Bar chart to show Fossil Gas Generation Over Time
st.subheader('Fossil Gas Generation Over Time')
st.markdown("📊 This bar chart displays the generation of fossil gas over different years. The x-axis represents the years, while the y-axis shows the generation in megawatts (MW). The tallest bar corresponds to the year with the maximum fossil gas generation, while the shortest bar represents the year with the minimum fossil gas generation.")

# Bar chart to show Fossil Oil Generation Over Time
st.subheader('Fossil Oil Generation Over Time')
st.markdown("📊 Similar to the previous chart, this bar chart illustrates the generation of fossil oil over different years. The x-axis represents the years, and the y-axis shows the fossil oil generation in MW. The tallest bar corresponds to the year with the highest fossil oil generation, while the shortest bar represents the year with the lowest fossil oil generation.")

# Bar chart to show Nuclear Energy Generation Over Time
st.subheader('Nuclear Energy Generation Over Time')
st.markdown("📊 This bar chart visualizes the generation of nuclear energy over different years. The x-axis represents the years, and the y-axis shows the nuclear energy generation in MW. The tallest bar corresponds to the year with the maximum nuclear energy generation, while the shortest bar represents the year with the minimum nuclear energy generation.")

# Proportion of Forecasted Load vs. Actual Load
st.subheader('Proportion of Forecasted Load vs. Actual Load')
st.markdown("📊 This bar chart compares the proportion of forecasted load and actual load. The chart displays the percentage of total load in megawatts (MW) represented by the forecasted load and the actual load. The larger segment of the pie corresponds to the higher value between forecasted and actual loads.")

# Line chart to show Fossil Hard Coal Generation Over Time
st.subheader('Fossil Hard Coal Generation Over Time')
st.markdown("📈 This line chart shows the generation of fossil hard coal over different years. The x-axis represents the years, and the y-axis shows the generation in MW. The highest point on the line corresponds to the year with the maximum fossil hard coal generation, while the lowest point represents the year with the minimum fossil hard coal generation.")

# Line chart to show Fossil Oil Generation Over Time
st.subheader('Fossil Oil Generation Over Time')
st.markdown("📈 Similar to the previous line chart, this visualization depicts the generation of fossil oil over different years. The x-axis represents the years, and the y-axis shows the fossil oil generation in MW. The highest point on the line corresponds to the year with the maximum fossil oil generation, while the lowest point represents the year with the minimum fossil oil generation.")

# Line chart to show Nuclear Energy Generation Over Time
st.subheader('Nuclear Energy Generation Over Time')
st.markdown("📈 This line chart illustrates the generation of nuclear energy over different years. The x-axis represents the years, and the y-axis shows the nuclear energy generation in MW. The highest point on the line corresponds to the year with the maximum nuclear energy generation, while the lowest point represents the year with the minimum nuclear energy generation.")

# Proportion of Fossil Fuel Generation
st.subheader('Proportion of Fossil Fuel Generation')
st.markdown("📊 This pie chart presents the proportion of fossil fuel generation compared to other energy sources. It shows the percentage of total generation that comes from fossil fuels, including brown coal/lignite, hard coal, and gas. The largest segment of the pie represents the highest percentage of fossil fuel generation, while the other segments show the respective percentages of the other energy sources.")

# Interactive Pie Charts - Energy Generation Proportions
st.subheader('Interactive Pie Charts - Energy Generation Proportions')
st.markdown("📊 These interactive pie charts show the proportion of generation from various renewable energy sources. Users can explore the percentages for geothermal, hydro, marine, solar, wind, and other renewable energy sources. The largest segment of each pie chart represents the highest percentage of generation for that specific renewable source.")

# Histogram for Fossil Gas Generation
st.subheader('Fossil Gas Generation')
st.markdown("📊 This histogram displays the frequency distribution of fossil gas generation in MW. The x-axis represents the generation levels, while the y-axis shows the frequency (number of occurrences) of each generation level. The highest bar in the histogram corresponds to the maximum fossil gas generation, while the lowest bar represents the minimum fossil gas generation.")

# Histogram for Fossil Hard Coal Generation
st.subheader('Fossil Hard Coal Generation')
st.markdown("📊 This histogram visualizes the frequency distribution of fossil hard coal generation in MW. The x-axis represents the generation levels, while the y-axis shows the frequency of each generation level. The highest bar in the histogram corresponds to the maximum fossil hard coal generation, while the lowest bar represents the minimum fossil hard coal generation.")

# Total Fossil Fuel Generation Over Time
st.subheader('Total Fossil Fuel Generation Over Time')
st.markdown("📊 This histogram displays the frequency distribution of the total fossil fuel generation (sum of hard coal, oil, shale, and peat) over different time points. The x-axis represents the total generation levels, and the y-axis shows the frequency of each total generation level. The highest bar in the histogram corresponds to the maximum total fossil fuel generation, while the lowest bar represents the minimum total fossil fuel generation.")

#st.subheader('Nuclear Generation Over Time')
st.subheader("Nuclear Generation Over Time")
st.markdown("📈 This stack area chart illustrates the generation of nuclear energy over time. The x-axis represents time, and the y-axis shows the nuclear energy generation in MW. The highest point on the area chart corresponds to the maximum nuclear energy generation, while the lowest point represents the minimum nuclear energy generation.")

# Solar Generation Over Time (Line Area Chart)
st.subheader('Solar Generation Over Time')
st.markdown("📈 This line area chart displays the generation of solar energy over time. The x-axis represents time, and the y-axis shows the solar energy generation in MW. The highest point on the line area chart corresponds to the maximum solar energy generation, while the lowest point represents the minimum solar energy generation.")

# Line chart with dual y-axes - Nuclear Generation vs. Fossil Gas Generation Over Time
st.subheader('Nuclear Generation vs. Fossil Gas Generation Over Time')
st.markdown("📈 This line chart with dual y-axes compares the generation of nuclear energy and fossil gas over time. The x-axis represents time, while the left y-axis shows nuclear energy generation in purple, and the right y-axis shows fossil gas generation in blue. The highest point on the purple line corresponds to the maximum nuclear energy generation, while the highest point on the blue line represents the maximum fossil gas generation.")

