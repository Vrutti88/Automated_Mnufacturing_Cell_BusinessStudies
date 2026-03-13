import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Automated Manufacturing Intelligence",
    page_icon="🏭",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>

html, body {
    background-color: #0f1117;
}

.glass-card {
    background: rgba(255,255,255,0.03);
    padding:25px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.1);
}

.metric-label{
    color:#9aa4af;
    font-size:0.9rem;
}

.metric-value{
    font-size:2rem;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🏭 Automated Manufacturing Intelligence Lab")
st.markdown("### Simulation & Performance Analytics for Smart Production")

# ---------- SIDEBAR ----------
with st.sidebar:

    st.header("⚙️ Production Settings")

    machines = st.slider("Number of Machines",5,20,10)

    productivity = st.slider("Productivity Increase %",0,50,25)

    defect_reduction = st.slider("Defect Reduction %",0,50,30)

    downtime = st.slider("Average Downtime Hours",0,20,5)

    run = st.button("🚀 Run Simulation",use_container_width=True)

# ---------- LOGIC ----------
if run:

    base_cost = 8
    investment = 4

    savings = base_cost * (defect_reduction/100)

    net_benefit = savings - investment

    np.random.seed(0)

    data = pd.DataFrame({
        "Machine":[f"M{i}" for i in range(1,machines+1)],
        "Cycle Time":np.random.randint(40,80,machines),
        "Defect Rate":np.random.uniform(1,5,machines),
        "Production Volume":np.random.randint(800,1200,machines),
        "Downtime":np.random.randint(1,10,machines)
    })

    total_output = data["Production Volume"].sum()

    # ---------- TABS ----------
    tab1,tab2,tab3 = st.tabs(
        ["🏭 Production KPIs","📊 Performance Analysis","💡 Business Impact"]
    )

# ---------- TAB 1 ----------
    with tab1:

        c1,c2,c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="glass-card">
            <div class="metric-label">Total Production Output</div>
            <div class="metric-value">{total_output:,}</div>
            </div>
            """,unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="glass-card">
            <div class="metric-label">Estimated Savings</div>
            <div class="metric-value">₹{savings:.2f} Cr</div>
            </div>
            """,unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="glass-card">
            <div class="metric-label">Net Benefit</div>
            <div class="metric-value">₹{net_benefit:.2f} Cr</div>
            </div>
            """,unsafe_allow_html=True)

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=productivity,
            title={'text':"Productivity Gain %"},
            gauge={'axis':{'range':[0,100]}}
        ))

        st.plotly_chart(gauge,use_container_width=True)

# ---------- TAB 2 ----------
    with tab2:

        col1,col2 = st.columns(2)

        fig1 = px.bar(
            data,
            x="Machine",
            y="Production Volume",
            title="Machine Production Output"
        )

        fig2 = px.line(
            data,
            x="Machine",
            y="Defect Rate",
            markers=True,
            title="Defect Rate by Machine"
        )

        col1.plotly_chart(fig1,use_container_width=True)
        col2.plotly_chart(fig2,use_container_width=True)

        fig3 = px.bar(
            data,
            x="Machine",
            y="Downtime",
            title="Machine Downtime Analysis"
        )

        st.plotly_chart(fig3,use_container_width=True)

# ---------- TAB 3 ----------
    with tab3:

        st.subheader("Technical Components of Automated Manufacturing Cell")

        st.markdown("""
- CNC Machines for precision cutting and drilling  
- Robotic Arms for automated assembly and handling  
- Conveyor Systems for material transport  
- Sensors and Vision Systems for quality control  
- Central Control Unit for system coordination  
""")

        st.subheader("Business Impact")

        st.markdown(f"""
Automation is expected to reduce labor and rework costs by **{defect_reduction}%**.

Annual savings estimated: **₹{savings:.2f} Crores**

Investment required: **₹4 Crores**

Net Benefit (Year 1): **₹{net_benefit:.2f} Crores**
""")

        st.success("""
Recommendation: TechParts Manufacturing Ltd should invest in the Automated Manufacturing Cell.
The automation system will improve production efficiency, reduce defects,
increase productivity, and enhance competitiveness in the automobile industry.
""")

else:

    st.markdown("""
    <div style="text-align:center;padding:120px;opacity:0.5">
    <h1>Configure Production Settings in Sidebar 👈</h1>
    </div>
    """,unsafe_allow_html=True)