🏭 Automated Manufacturing Intelligence Lab

A Streamlit-powered interactive simulation dashboard designed to analyze the impact of automation in a manufacturing environment.

This project models how TechParts Manufacturing Ltd. can improve production efficiency, reduce defects, and increase productivity by implementing an Automated Manufacturing Cell.

The system simulates machine performance data and provides real-time business insights, financial analysis, and production analytics through an interactive dashboard.

📌 Project Overview

TechParts Manufacturing Ltd. currently operates using manual workstations for cutting, drilling, and assembly.

This leads to:

Higher production cycle time

Human operational errors

Material handling delays

Increased defect rates

Machine downtime

The company plans to invest ₹4 Crores in an Automated Manufacturing Cell integrating CNC machines, robotic systems, and conveyor automation.

This project simulates production data and analyzes the business impact of automation using Python and Streamlit.

✨ Features
⚙️ Interactive Production Simulation

Users can configure manufacturing parameters through a sidebar including:

Number of machines

Productivity increase percentage

Defect reduction percentage

Average downtime hours

The system then runs a production simulation model.

📊 Real-Time Production KPIs

The dashboard calculates key performance indicators such as:

Total Production Output

Estimated Annual Savings

Net Financial Benefit

Productivity Gain

📈 Machine Performance Analytics

The application visualizes simulated production data using interactive Plotly charts, including:

Machine production output

Defect rate analysis

Machine downtime analysis

💰 Business Impact Evaluation

The dashboard calculates:

Annual operational savings

Net benefit after automation investment

Productivity improvement impact

The system also provides an automation investment recommendation based on simulation results.

🛠️ Technology Stack
Category	Technology
Programming Language	Python
Dashboard Framework	Streamlit
Data Processing	Pandas
Numerical Simulation	NumPy
Data Visualization	Plotly
Charts	Plotly Express

Required libraries:

streamlit
pandas
numpy
matplotlib
plotly
📊 Simulation Model

The system generates synthetic production data for machines using NumPy random distributions.

Example parameters generated in the simulation include:

Machine ID

Cycle Time

Defect Rate

Production Volume

Downtime Hours

The simulation dynamically adjusts output depending on the selected parameters such as productivity increase and defect reduction.

🏭 Automated Manufacturing Cell Components

The proposed automated manufacturing system includes:

CNC Machines

Used for precision cutting, drilling, and machining operations.

Robotic Arms

Handle automated assembly and part movement between stations.

Conveyor Systems

Transport materials between production processes.

Sensors and Vision Systems

Monitor product quality and detect defects.

Central Control Unit

Coordinates all machines and monitors system performance.

💰 Financial Analysis
Current Annual Cost

The company currently spends:

₹8 Crores per year

Costs include:

Labor

Machine idle time

Defect rework

Expected Cost Reduction

Automation reduces labor and rework costs by:

30%

Estimated annual savings:

Savings = 8 × 0.30
Savings = ₹2.4 Crores
Net Benefit Formula
Net Benefit = Total Savings – Investment

Where:

Investment required:

₹4 Crores

Net Benefit = 2.4 – 4
Net Benefit = – ₹1.6 Crores (Year 1)

Although the first year has a negative return due to investment cost, the automation system will produce positive financial returns in subsequent years.

📈 Dashboard Sections

The application interface includes three major analysis tabs.

🏭 Production KPIs

Displays key production metrics:

Total production output

Estimated annual savings

Net benefit

Productivity gauge indicator

📊 Performance Analysis

Provides machine-level analytics through interactive charts:

Machine production volume

Defect rate per machine

Machine downtime analysis

💡 Business Impact

Explains:

Automation system components

Expected cost reduction

Financial impact

Final business recommendation

🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/automated-manufacturing-intelligence.git
cd automated-manufacturing-intelligence
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit Application
streamlit run app.py

The dashboard will open in your browser at:

http://localhost:8501
📂 Project Structure
automated-manufacturing-intelligence/
│
├── app.py            # Streamlit interactive dashboard
├── main.ipynb        # Data simulation & analysis notebook
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
📊 Business Insights

Based on the simulation:

Automation reduces operational costs significantly

Production output increases with higher productivity

Defect rates decrease with improved automation

Machine downtime insights help optimize maintenance strategies

Overall, automation improves manufacturing efficiency, scalability, and competitiveness.

✅ Final Recommendation

TechParts Manufacturing Ltd. should invest in the Automated Manufacturing Cell.

The system will:

Reduce operational costs

Improve production efficiency

Lower defect rates

Increase manufacturing capacity

This investment will help the company remain competitive in the automobile manufacturing industry.

📜 License

This project is developed for educational and academic purposes.