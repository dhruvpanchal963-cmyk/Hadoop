# ==========================================================
# HadoopVerse AI v2.0
# Interactive Hadoop Ecosystem Simulator
# Developed by Dhruv Panchal
# ==========================================================

from __future__ import annotations

from pathlib import Path
import random
import psutil

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="HadoopVerse AI",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

ASSET_DIR = BASE_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"

LOGO_IMAGE = IMAGE_DIR / "logo.png"
ARCHITECTURE_IMAGE = IMAGE_DIR / "hadoop_architecture.png"
DEVELOPER_IMAGE = ASSET_DIR / "developer.png"

VERSION = "2.0"


# ==========================================================
# HADOOP MODULES
# ==========================================================

MODULES = [
    "HDFS",
    "MapReduce",
    "YARN",
    "Hive",
    "Pig",
    "Spark",
    "HBase",
    "Kafka",
    "Flume",
    "Sqoop",
    "ZooKeeper",
    "Oozie",
    "Avro",
    "Parquet",
    "Mahout",
    "Ambari"
]


# ==========================================================
# MODULE INFORMATION
# ==========================================================

MODULE_INFO = {
    "HDFS": "Distributed File Storage System.",
    "MapReduce": "Parallel Data Processing Framework.",
    "YARN": "Cluster Resource Manager.",
    "Hive": "SQL-based Data Warehouse.",
    "Pig": "High-level Data Flow Language.",
    "Spark": "Fast In-Memory Processing Engine.",
    "HBase": "Distributed NoSQL Database.",
    "Kafka": "Real-Time Streaming Platform.",
    "Flume": "Log Collection System.",
    "Sqoop": "Transfers Data Between RDBMS & Hadoop.",
    "ZooKeeper": "Distributed Coordination Service.",
    "Oozie": "Workflow Scheduler.",
    "Avro": "Serialization Framework.",
    "Parquet": "Columnar Storage Format.",
    "Mahout": "Machine Learning Library.",
    "Ambari": "Cluster Management Tool."
}


# ==========================================================
# IMAGE LOADER
# ==========================================================

def load_image(path: Path):
    """Safely load image."""

    try:
        if path.exists():
            return Image.open(path)
    except Exception:
        return None

    return None


# ==========================================================
# SIMULATION FUNCTION
# ==========================================================

def run_python_script(module):

    simulations = {

        "HDFS": """
Initializing NameNode...

Connecting DataNodes...

Splitting file into 128 MB blocks...

Replicating data blocks...

Updating NameNode metadata...

File stored successfully in HDFS.
""",

        "MapReduce": """
Loading input dataset...

Map Phase Started...

Generating key-value pairs...

Shuffle & Sort Completed...

Reduce Phase Started...

Final output generated successfully.
""",

        "YARN": """
Starting Resource Manager...

Registering Node Managers...

Allocating cluster resources...

Launching containers...

Job execution completed successfully.
""",

        "Hive": """
Connecting to Hive Warehouse...

Executing SQL Query...

Reading distributed data...

Returning query results...

Query executed successfully.
""",

        "Pig": """
Loading Pig Latin Script...

Parsing commands...

Executing data flow...

Pig job completed successfully.
""",

        "Spark": """
Creating Spark Session...

Loading DataFrame...

Performing in-memory computation...

Caching results...

Spark job completed successfully.
""",

        "HBase": """
Connecting to HBase...

Creating table...

Inserting records...

Reading records...

Database operation successful.
""",

        "Kafka": """
Starting Kafka Broker...

Producer sending messages...

Consumer receiving messages...

Streaming completed successfully.
""",

        "Flume": """
Monitoring log source...

Collecting log events...

Sending logs to HDFS...

Flume completed successfully.
""",

        "Sqoop": """
Connecting to MySQL...

Reading database...

Importing records into HDFS...

Sqoop import completed successfully.
""",

        "ZooKeeper": """
Starting ZooKeeper...

Leader Election Completed...

Synchronizing distributed nodes...

Cluster coordination successful.
""",

        "Oozie": """
Loading workflow...

Scheduling Hadoop jobs...

Executing workflow...

Workflow completed successfully.
""",

        "Avro": """
Serializing dataset...

Writing Avro file...

Reading serialized data...

Serialization completed successfully.
""",

        "Parquet": """
Creating Parquet file...

Compressing columnar data...

Writing file to storage...

Parquet file created successfully.
""",

        "Mahout": """
Loading Machine Learning model...

Training algorithm...

Evaluating accuracy...

Model training completed successfully.
""",

        "Ambari": """
Connecting to Hadoop Cluster...

Monitoring services...

Collecting performance metrics...

Cluster status : Healthy.
"""
    }

    return {
        "status": "Simulation Completed Successfully",
        "output": simulations.get(module, "Simulation not available."),
        "time": round(random.uniform(0.5, 3.0), 2)
    }


# ==========================================================
# CUSTOM CSS
# ==========================================================

def inject_css():

    st.markdown(
        """
<style>

.main{
    padding-top:1rem;
}

/* Background */

.stApp{
background:linear-gradient(
135deg,
#061423,
#0b1d34,
#122b45
);
color:white;
}

/* Hero */

.hero{

background:linear-gradient(
135deg,
#0d47a1,
#1565c0,
#1e88e5
);

padding:35px;

border-radius:20px;

box-shadow:0px 10px 25px rgba(0,0,0,0.3);

text-align:center;

margin-bottom:25px;

}

/* Cards */

.card{

background:rgba(255,255,255,0.08);

padding:20px;

border-radius:15px;

border:1px solid rgba(255,255,255,0.10);

backdrop-filter:blur(10px);

margin-bottom:15px;

}

/* Footer */

.footer{

text-align:center;

padding:20px;

font-size:14px;

opacity:0.8;

}

</style>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar():

    with st.sidebar:

        logo = load_image(LOGO_IMAGE)

        if logo:
            st.image(logo, width=140)

        st.title("🧩 HadoopVerse AI")

        st.caption("Interactive Hadoop Ecosystem Simulator")

        page = st.radio(

            "Navigation",

            [

                "🏠 Home",

                "📘 Introduction",

                "🏗 Architecture",

                *MODULES,

                "📊 Dashboard",

                "📝 Quiz",

                "📖 Glossary",

                "👨‍💻 About Developer"

            ]

        )

        st.divider()

        st.info(f"Version {VERSION}")

        return page
        # ==========================================================
# HOME PAGE
# ==========================================================

def home_page():

    st.markdown(
        """
        <div class="hero">
            <h1>🚀 HadoopVerse AI</h1>
            <h3>Interactive Hadoop Ecosystem Simulator</h3>
            <p>Learn • Explore • Visualize • Simulate • Analyze</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Modules", len(MODULES))
    c2.metric("Version", VERSION)
    c3.metric("Status", "Ready")
    c4.metric("Language", "Python")

    st.divider()

    st.header("📌 About HadoopVerse AI")

    st.write("""
HadoopVerse AI is a modern interactive learning platform developed using
**Python** and **Streamlit**.

It allows students to understand every component of the Hadoop ecosystem
through visual explanations, simulations, dashboards and interactive content.

Instead of installing a complete Hadoop Cluster, this application demonstrates
how every Hadoop technology works using Python equivalents.
""")

    st.divider()

    st.header("🎯 Project Objectives")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
✔ Learn Hadoop Architecture

✔ Explore Hadoop Components

✔ Understand Big Data Workflow

✔ Interactive Simulations
""")

    with col2:

        st.info("""
✔ Beginner Friendly

✔ Modern User Interface

✔ Python Based

✔ Educational Simulator
""")

    st.divider()

    st.header("🛠 Technology Stack")

    t1, t2, t3, t4 = st.columns(4)

    t1.info("🐍 Python")
    t2.info("🌐 Streamlit")
    t3.info("📊 Plotly")
    t4.info("💾 Pandas")

    st.divider()

    st.header("🏗 Hadoop Ecosystem Architecture")

    image = load_image(ARCHITECTURE_IMAGE)

    if image:

        st.image(
            image,
            use_container_width=True
        )

    else:

        st.warning(
            "Architecture image not found.\n\nPlace the image inside:\nassets/images/"
        )

    st.divider()

    st.markdown(
        """
<div class="footer">
© 2026 HadoopVerse AI • Interactive Hadoop Ecosystem Simulator
</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# INTRODUCTION PAGE
# ==========================================================

def introduction_page():

    st.title("📘 Introduction to Hadoop")

    st.write("""

Apache Hadoop is an open-source framework that enables distributed storage
and processing of massive datasets across clusters of computers.

It is designed to scale from a single machine to thousands of servers,
providing high availability and fault tolerance.

The Hadoop ecosystem consists of multiple tools that work together for
storage, processing, querying, streaming, scheduling and resource management.
""")

    st.subheader("⭐ Key Features")

    features = [

        "Distributed Storage (HDFS)",

        "Parallel Processing (MapReduce)",

        "Resource Management (YARN)",

        "Fault Tolerance",

        "Horizontal Scalability",

        "Open Source",

        "High Availability"

    ]

    for feature in features:

        st.markdown(f"✅ {feature}")


# ==========================================================
# ARCHITECTURE PAGE
# ==========================================================

def architecture_page():

    st.title("🏗 Hadoop Ecosystem Architecture")

    image = load_image(ARCHITECTURE_IMAGE)

    if image:

        st.image(
            image,
            use_container_width=True
        )

    st.write("""

The Hadoop ecosystem consists of multiple integrated components.

• HDFS stores distributed data.

• YARN manages cluster resources.

• MapReduce processes large datasets.

• Hive provides SQL queries.

• Pig simplifies data processing.

• Spark performs in-memory computation.

• Kafka streams real-time data.

• HBase stores NoSQL data.

• Oozie schedules workflows.

• ZooKeeper coordinates distributed services.

Together these tools provide a complete Big Data platform capable of
handling petabytes of structured and unstructured data.
""")

    st.success("Interactive simulations for each component are available from the sidebar.")
    # ==========================================================
# HADOOP COMPONENT PAGE
# ==========================================================

def simple_component_page(module):

    st.title(f"🧩 {module}")

    st.markdown(f"""
### {module}

{MODULE_INFO[module]}
""")

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📖 Overview",
            "⚙ Workflow",
            "✅ Advantages",
            "💻 Python Simulation"
        ]
    )

    # ------------------------------------------------------

    with tab1:

        st.subheader("Overview")

        st.write(f"""
**{module}** is one of the major Hadoop ecosystem components.

It works together with other Hadoop services to provide
distributed storage, resource management, data processing,
streaming or workflow management depending upon its role.
""")

        st.info(MODULE_INFO[module])

    # ------------------------------------------------------

    with tab2:

        st.subheader("Workflow")

        workflow = {

            "HDFS":"Stores distributed files.",

            "MapReduce":"Processes data in parallel.",

            "YARN":"Allocates cluster resources.",

            "Hive":"Executes SQL queries.",

            "Pig":"Processes data using Pig Latin.",

            "Spark":"Performs in-memory computation.",

            "HBase":"Stores NoSQL records.",

            "Kafka":"Streams real-time messages.",

            "Flume":"Collects log data.",

            "Sqoop":"Transfers database records.",

            "ZooKeeper":"Coordinates distributed nodes.",

            "Oozie":"Schedules Hadoop workflows.",

            "Avro":"Serializes data.",

            "Parquet":"Stores columnar datasets.",

            "Mahout":"Performs Machine Learning.",

            "Ambari":"Monitors Hadoop Cluster."
        }

        st.success(workflow[module])

    # ------------------------------------------------------

    with tab3:

        st.subheader("Advantages")

        advantages = [

            "✔ Scalable",

            "✔ Fault Tolerant",

            "✔ Distributed",

            "✔ Open Source",

            "✔ High Performance"

        ]

        for item in advantages:

            st.write(item)

    # ------------------------------------------------------

    with tab4:

        st.subheader("Simulation")

        st.code(
f"""
# {module} Simulation

print("Running {module}...")

print("Simulation Successful")
""",
language="python"
        )

        if st.button(
            f"▶ Run {module} Simulation",
            use_container_width=True
        ):

            result = run_python_script(module)

            st.success(result["status"])

            st.code(result["output"])

            st.metric(
                "Execution Time",
                f'{result["time"]} sec'
            )
            # ==========================================================
# HADOOP COMPONENT PAGE
# ==========================================================

def simple_component_page(module):

    st.title(f"🧩 {module}")

    st.markdown(f"""
### {module}

{MODULE_INFO[module]}
""")

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📖 Overview",
            "⚙ Workflow",
            "✅ Advantages",
            "💻 Python Simulation"
        ]
    )

    # ------------------------------------------------------

    with tab1:

        st.subheader("Overview")

        st.write(f"""
**{module}** is one of the major Hadoop ecosystem components.

It works together with other Hadoop services to provide
distributed storage, resource management, data processing,
streaming or workflow management depending upon its role.
""")

        st.info(MODULE_INFO[module])

    # ------------------------------------------------------

    with tab2:

        st.subheader("Workflow")

        workflow = {

            "HDFS":"Stores distributed files.",

            "MapReduce":"Processes data in parallel.",

            "YARN":"Allocates cluster resources.",

            "Hive":"Executes SQL queries.",

            "Pig":"Processes data using Pig Latin.",

            "Spark":"Performs in-memory computation.",

            "HBase":"Stores NoSQL records.",

            "Kafka":"Streams real-time messages.",

            "Flume":"Collects log data.",

            "Sqoop":"Transfers database records.",

            "ZooKeeper":"Coordinates distributed nodes.",

            "Oozie":"Schedules Hadoop workflows.",

            "Avro":"Serializes data.",

            "Parquet":"Stores columnar datasets.",

            "Mahout":"Performs Machine Learning.",

            "Ambari":"Monitors Hadoop Cluster."
        }

        st.success(workflow[module])

    # ------------------------------------------------------

    with tab3:

        st.subheader("Advantages")

        advantages = [

            "✔ Scalable",

            "✔ Fault Tolerant",

            "✔ Distributed",

            "✔ Open Source",

            "✔ High Performance"

        ]

        for item in advantages:

            st.write(item)

    # ------------------------------------------------------

    with tab4:

        st.subheader("Simulation")

        st.code(
f"""
# {module} Simulation

print("Running {module}...")

print("Simulation Successful")
""",
language="python"
        )

        if st.button(
            f"▶ Run {module} Simulation",
            use_container_width=True
        ):

            result = run_python_script(module)

            st.success(result["status"])

            st.code(result["output"])

            st.metric(
                "Execution Time",
                f'{result["time"]} sec'
            )
            # ==========================================================
# DASHBOARD
# ==========================================================

def dashboard_page():

    st.title("📊 Hadoop Dashboard")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Modules", len(MODULES))
    c2.metric("CPU", f"{cpu}%")
    c3.metric("Memory", f"{memory}%")
    c4.metric("Disk", f"{disk}%")

    st.divider()

    performance = pd.DataFrame({
        "Module": MODULES,
        "Performance": [random.randint(80,100) for _ in MODULES]
    })

    fig = px.bar(
        performance,
        x="Module",
        y="Performance",
        color="Performance",
        title="Module Performance"
    )

    st.plotly_chart(fig, use_container_width=True)

    pie = px.pie(
        names=["Completed","Pending"],
        values=[100,0],
        hole=.65,
        title="Project Status"
    )

    st.plotly_chart(pie, use_container_width=True)


# ==========================================================
# QUIZ
# ==========================================================

def quiz_page():

    st.title("📝 Hadoop Quiz")

    question = st.radio(

        "Which Hadoop component manages cluster resources?",

        ["Hive","Pig","YARN","Spark"]

    )

    if st.button("Submit"):

        if question == "YARN":

            st.success("Correct Answer ✅")

        else:

            st.error("Wrong Answer ❌")

            st.info("Correct Answer : YARN")


# ==========================================================
# GLOSSARY
# ==========================================================

def glossary_page():

    st.title("📖 Hadoop Glossary")

    glossary = pd.DataFrame({

        "Term":[

            "HDFS",
            "YARN",
            "Hive",
            "Pig",
            "Spark",
            "Kafka",
            "HBase",
            "Sqoop",
            "ZooKeeper"

        ],

        "Meaning":[

            "Distributed File System",
            "Resource Manager",
            "SQL Warehouse",
            "Data Flow Language",
            "Fast Processing Engine",
            "Streaming Platform",
            "NoSQL Database",
            "Database Transfer Tool",
            "Distributed Coordination"

        ]

    })

    st.dataframe(
        glossary,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# ABOUT
# ==========================================================

def about_page():

    st.title("👨‍💻 About Developer")

    image = load_image(DEVELOPER_IMAGE)

    if image:

        st.image(image,width=220)

    st.subheader("Dhruv Panchal")

    st.write("""
BSc Data Science Student

Python Developer

Machine Learning Enthusiast

Big Data Learner

Streamlit Developer
""")

    st.success("HadoopVerse AI Version 2.0")


# ==========================================================
# MAIN
# ==========================================================

def main():

    inject_css()

    page = sidebar()

    if page == "🏠 Home":

        home_page()

    elif page == "📘 Introduction":

        introduction_page()

    elif page == "🏗 Architecture":

        architecture_page()

    elif page in MODULES:

        simple_component_page(page)

    elif page == "📊 Dashboard":

        dashboard_page()

    elif page == "📝 Quiz":

        quiz_page()

    elif page == "📖 Glossary":

        glossary_page()

    elif page == "👨‍💻 About Developer":

        about_page()


if __name__ == "__main__":

    main()
