import streamlit as st
import pandas as pd

final_cluster_data = pd.read_csv("final_cluster_data.csv")
sensitivity_results_df = pd.read_csv("sensitivity_results.csv")
transition_percentages = pd.read_csv("transition_percentages.csv", index_col=0)


# MENSTRUAL CYCLE PATTERN DASHBOARD


st.set_page_config(
    page_title="Menstrual Cycle Pattern Dashboard",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 Menstrual Cycle Pattern Dashboard")

st.markdown(
    """
    This dashboard presents the results of an exploratory,
    data-driven analysis of menstrual cycle patterns using
    longitudinal cycle-level data.
    """
)

# SIDEBAR NAVIGATION


st.sidebar.title("Dashboard Sections")

section = st.sidebar.radio(
    "Go to:",
    [
        "Overview",
        "Cycle Patterns",
        "Clustering Evaluation",
        "Longitudinal Patterns"
    ]

# OVERVIEW    

)
if section == "Overview":

    st.header("1) Overview")

    st.markdown(
        """
        This dashboard presents the results of an exploratory,
        data-driven analysis of menstrual cycle patterns using
        longitudinal cycle-level data.
        """
    )

    st.subheader("a) Study Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Original Cycles", "1,665")

    with col2:
        st.metric("Final Clustering Sample", "1,661")

    with col3:
        st.metric("Exploratory Clusters", "3")

    with col4:
        st.metric("Valid Transitions", "1,483")

    st.subheader("b) Analytical Workflow")

    st.markdown(
        """
        **Data Quality Assessment → Exploratory Data Analysis → 
        Correlation Analysis → Feature Selection → K-Means Clustering 
        → Cluster Stability Assessment → Longitudinal Transition Analysis**
        """
    )   

    st.info(
            """
            The patterns presented in this dashboard are exploratory,
            data-derived groupings and should not be interpreted as
            clinically defined menstrual-cycle categories.
            """
        ) 
    


    
# CYCLE PATTERNS


if section == "Cycle Patterns":

    st.header("2) Cycle Patterns")

    st.markdown(
        """
        The final clustering solution identified three exploratory
        menstrual-cycle patterns based on cycle length and length of menses.
        """
    )

    st.subheader("a) Final Cluster Profiles")

    st.markdown(
        """
        The table below summarises the mean cycle length and mean
        menstrual duration for each exploratory cluster.
        """
    )

    st.dataframe(
        {
            "Cluster": [
                "Cluster 0 — Longer-Menses Profile",
                "Cluster 1 — Shorter-Cycle and Shorter-Menses Profile",
                "Cluster 2 — Longer-Cycle Profile"
            ],
            "Mean Cycle Length (days)": [
                28.66,
                27.56,
                35.50
            ],
            "Mean Menses Length (days)": [
                6.57,
                4.43,
                5.24
            ]
        },
        use_container_width=True,
        hide_index=True
    )


    st.subheader("b) Distribution of Cycle Patterns")

    st.markdown(
        """
        Each point represents a cycle-level observation. The position of
        each point reflects cycle length and length of menses, while the
        marker colour indicates the assigned exploratory cluster.
        """
    )

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 6))

    for cluster in [0, 1, 2]:

        cluster_data = final_cluster_data[
            final_cluster_data["FinalCluster"] == cluster
        ]

        ax.scatter(
            cluster_data["LengthofCycle"],
            cluster_data["LengthofMenses"],
            label=f"Cluster {cluster}",
            alpha=0.6
        )

    ax.set_xlabel("Length of Cycle (days)")
    ax.set_ylabel("Length of Menses (days)")
    ax.set_title("Exploratory Menstrual Cycle Patterns")
    ax.legend(title="Final Cluster")

    st.pyplot(fig)

    st.caption(
        "The cluster labels are descriptive and refer to the dominant "
        "cycle characteristics observed within the selected feature space."
    )

   
  
# CLUSTERING EVALUATION


if section == "Clustering Evaluation":

    st.header("3) Clustering Evaluation")

    st.markdown(
        """
        The final exploratory clustering solution was evaluated using
        cluster separation and stability measures. Feature-set sensitivity
        was also examined to assess how the clustering structure changed
        with different feature representations.
        """
    )

    st.subheader("a) Final Clustering Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Number of Clusters", "3")

    with col2:
        st.metric("Silhouette Score", "0.4118")

    with col3:
        st.metric("Mean Stability ARI", "0.9832")

    st.subheader("b) Final Feature Representation")

    st.markdown(
        """
        **Feature Set C**

        - Length of Cycle
        - Length of Menses

        **Observations retained:** 1,661 of 1,665
        """
    )


    st.subheader("c) Clustering Sensitivity Across Feature Sets")

    st.markdown(
        """
        Silhouette scores are shown for different numbers of clusters
        across the three candidate feature sets. The comparison illustrates
        how the clustering structure changed with feature representation.
        """
    )

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 6))

    for feature_set in sensitivity_results_df["Feature Set"].unique():

        subset = sensitivity_results_df[
            sensitivity_results_df["Feature Set"] == feature_set
        ]

        ax.plot(
            subset["K"],
            subset["Silhouette Score"],
            marker="o",
            label=feature_set
        )

    ax.set_xlabel("Number of Clusters (K)")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Silhouette Score Across Feature Sets")
    ax.set_xticks([2, 3, 4, 5, 6])
    ax.legend(title="Feature Set")

    st.pyplot(fig)

    
# LONGITUDINAL PATTERNS


if section == "Longitudinal Patterns":

    st.header("4) Longitudinal Patterns")

    st.markdown(
        """
        The longitudinal analysis examines how observations assigned
        to the three exploratory cycle-pattern clusters changed between
        genuinely consecutive cycles.
        """
    )

    st.subheader("a) Cycle-to-Cycle Transitions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Valid Transitions", "1,483")

    with col2:
        st.metric("Same Cluster", "66.69%")

    with col3:
        st.metric("Changed Cluster", "33.31%")

    st.subheader("b) Transition Probabilities Between Consecutive Cycles")

    st.markdown(
        """
        The heatmap shows the percentage of transitions from each
        previous cluster to each cluster in the subsequent cycle.
        """
    )

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 6))

    image = ax.imshow(
        transition_percentages.values,
        aspect="auto"
    )

    for i in range(transition_percentages.shape[0]):
        for j in range(transition_percentages.shape[1]):
            ax.text(
                j,
                i,
                f"{transition_percentages.iloc[i, j]:.2f}%",
                ha="center",
                va="center"
            )

    ax.set_xticks(
        range(len(transition_percentages.columns))
    )

    ax.set_xticklabels(
        transition_percentages.columns.astype(int)
    )

    ax.set_yticks(
        range(len(transition_percentages.index))
    )

    ax.set_yticklabels(
        transition_percentages.index.astype(int)
    )

    ax.set_xlabel("Next Cluster")
    ax.set_ylabel("Previous Cluster")
    ax.set_title("Transition Probabilities Between Consecutive Cycles")

    fig.colorbar(
        image,
        ax=ax,
        label="Transition Percentage"
    )

    st.pyplot(fig)    