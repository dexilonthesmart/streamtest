import streamlit as st



st.write("# Surprise 👋")

# Group by input anger level and calculate the mean fear for each level
grouped_df = df.groupby('input_fear_ordinal')['output_anger_ordinal'].mean().reset_index()

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(grouped_df['input_fear_ordinal'], grouped_df['output_anger_ordinal'], marker='o', linestyle='-')
plt.xlabel('Input Fear Level (Ordinal)')
plt.ylabel('Mean Output Anger Level (Ordinal)')
plt.title('Mean Output Anger Level by Input Fear Level')
plt.grid(True)
plt.show()
