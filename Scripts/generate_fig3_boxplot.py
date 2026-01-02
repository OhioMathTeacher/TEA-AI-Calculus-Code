#!/usr/bin/env python3
"""
Generate Figure 3: Box plots of student-talk percentages by course section.
Data extracted from Appendix C of the manuscript.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data extracted from appendix.tex - Student Talk Percentages by Section
# Format: section -> list of student talk percentages

data_by_section = {
    'Section 3': [72.7, 58.1],  # P33-G16-S3, P42-G11-S3
    'Section 4': [
        5.4, 5.2, 7.4, 8.1, 27.6, 55.7, 31.2, 47.2, 5.8, 44.8, 42.4, 42.9, 51.3, 14.9,
        30.0, 41.1, 58.9, 14.0, 3.5, 85.3, 48.7, 0.0, 52.6, 36.3, 69.1, 100.0, 74.7,
        64.1, 46.9, 57.5, 22.1, 18.4, 17.6, 100.0, 85.8, 46.5, 13.3, 5.4, 0.0, 48.6, 33.8
    ],
    'Section 5': [
        66.8, 18.3, 64.4, 48.9, 8.8, 80.3, 45.5, 61.9, 78.8, 100.0, 76.9, 42.0, 81.9,
        46.4, 64.1, 39.9, 82.0, 0.0, 61.2, 44.7, 26.9, 87.6, 24.4, 61.8, 51.6, 53.6,
        49.7, 35.2, 73.9, 100.0, 74.6, 0.0, 38.0, 51.7, 88.4, 78.8, 47.3, 8.3, 24.1,
        53.1, 39.6, 53.9, 3.7, 18.6
    ],
    'Section 6': [
        86.9, 41.9, 0.0, 77.1, 72.1, 19.3, 83.2, 75.1, 62.6, 55.7, 38.6, 15.3, 68.6,
        60.9, 51.4, 44.9, 94.7, 46.2, 16.9, 24.4, 50.7, 100.0, 35.9, 47.5, 90.8, 0.0,
        66.7, 69.1, 76.1, 34.8, 100.0, 63.7, 82.7, 38.9, 19.9, 100.0
    ]
}

# Calculate medians for reference
for section, values in data_by_section.items():
    median = np.median(values)
    print(f"{section}: n={len(values)}, median={median:.1f}%")

# Create the boxplot
fig, ax = plt.subplots(figsize=(10, 6))

# Prepare data for boxplot
sections = list(data_by_section.keys())
data = [data_by_section[s] for s in sections]

# Create boxplot with red median line
bp = ax.boxplot(data, labels=sections, patch_artist=True,
                medianprops=dict(color='red', linewidth=2),
                boxprops=dict(facecolor='lightblue', color='black'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', markerfacecolor='gray', markersize=6))

# Add individual data points (jittered)
for i, (section, values) in enumerate(data_by_section.items(), 1):
    # Add jitter to x position
    x = np.random.normal(i, 0.04, size=len(values))
    ax.scatter(x, values, alpha=0.5, color='darkblue', s=20, zorder=3)

# Formatting
ax.set_ylabel('Student Talk Percentage (%)', fontsize=12)
ax.set_xlabel('Course Section', fontsize=12)
ax.set_ylim(-5, 105)
ax.set_title('Distribution of Student Talk Percentages by Course Section', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add sample size annotations
for i, (section, values) in enumerate(data_by_section.items(), 1):
    ax.annotate(f'n={len(values)}', xy=(i, -3), ha='center', fontsize=10, color='gray')

plt.tight_layout()

# Save the figure
output_path = '/home/todd/TEA-repos/TEA-Taylor-Series-Paper/Manuscript/figures/fig3.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"\nFigure saved to: {output_path}")

plt.show()
