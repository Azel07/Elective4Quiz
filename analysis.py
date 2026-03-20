import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

# --- STEP 1: FIX THE PATH ---
# This ensures Python looks in the folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Current working directory: {os.getcwd()}")

# --- STEP 2: FIND THE CSV ---
csv_files = glob.glob("*.csv")

if not csv_files:
    print("Error: No CSV file found in this folder!")
    exit(1)

file_path = csv_files[0]
print(f"Found dataset: {file_path}")

try:
    # Load the data
    df = pd.read_csv(file_path, low_memory=False)
    
    # Identify numeric and categorical columns automatically
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    if len(numeric_cols) < 2:
        print("Error: Dataset needs at least 2 numeric columns for analysis.")
        exit(1)

    # Clean data: Remove rows with empty values in the columns we'll use
    plot_data = df.dropna(subset=[numeric_cols[0], numeric_cols[1]])

    print(f"Analyzing: {numeric_cols[0]} and {numeric_cols[1]}")

    # --- GRAPH 1: Distribution (Histogram) ---
    plt.figure(figsize=(10, 5))
    sns.histplot(plot_data[numeric_cols[0]], kde=True, color='blue')
    plt.title(f'Distribution of {numeric_cols[0]}')
    plt.savefig('graph_1_distribution.png')
    plt.close()
    print("Saved: graph_1_distribution.png")

    # --- GRAPH 2: Relationship (Scatter Plot) ---
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=plot_data[numeric_cols[0]], y=plot_data[numeric_cols[1]])
    plt.title(f'{numeric_cols[0]} vs {numeric_cols[1]}')
    plt.savefig('graph_2_scatter.png')
    plt.close()
    print("Saved: graph_2_scatter.png")

    # --- GRAPH 3: Comparison (Bar Chart for Top 10) ---
    plt.figure(figsize=(10, 5))
    if categorical_cols:
        # Sort and take the top 10 values for a cleaner bar chart
        top_10 = plot_data.nlargest(10, numeric_cols[0])
        sns.barplot(x=numeric_cols[0], y=categorical_cols[0], data=top_10)
        plt.title(f'Top 10 {categorical_cols[0]} by {numeric_cols[0]}')
    else:
        sns.boxplot(x=plot_data[numeric_cols[0]])
        plt.title(f'Boxplot of {numeric_cols[0]}')
    
    plt.savefig('graph_3_comparison.png')
    plt.close()
    print("Saved: graph_3_comparison.png")
    
    print("\n--- TEST SUCCESSFUL ---")
    print("Check your folder for the 3 .png files.")

except Exception as e:
    print(f"Failed to process CSV: {e}")