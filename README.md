# Analytics and Data Quality Portfolio

Welcome to my analytics portfolio! This repository showcases my expertise in data quality analysis, SQL querying, and Python scripting to ensure accurate and consistent data reporting.

## Overview

This project involves in-depth analysis and validation of various datasets, focusing on data integrity, consistency, and the identification of discrepancies. The analyses cover multiple areas, including cost validation, conversion stability, backend data verification, attribution model consistency, and channel performance.

## Key Analyses

1. **Cost Validation:**
   - Verified that costs in the `api_adwords_costs` table align with those in the `session_sources` table.
   - Identified discrepancies across campaigns, highlighting areas of over-reporting, under-reporting, and timing issues.

2. **Conversion Stability:**
   - Assessed the stability of conversions over time, identifying patterns and potential causes for fluctuations.

3. **Backend Data Verification:**
   - Cross-checked `conversions` data with the `conversions_backend` table to identify discrepancies in revenue, dates, and other key metrics.
   - Developed a Python script to automate the identification and reporting of discrepancies.

4. **Attribution Model Consistency:**
   - Evaluated the consistency of `ihc` values in conversion data, accounting for floating-point precision errors and identifying potential data collection or model issues.

5. **Channel Performance Analysis:**
   - Analyzed session trends across various marketing channels, identifying stable and unstable trends, with a focus on potential issues such as data entry inconsistencies and declining channel performance.

## Tools and Technologies

- **SQL:** Used for querying and validating data across different tables.
- **Python:** Developed scripts to automate the detection of data discrepancies and generate summary reports.
- **Power BI:** Leveraged for visualizing data trends and patterns.
