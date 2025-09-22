# Netflix Data Cleaning Task

## Project Overview
This project focuses on cleaning and preprocessing the **Netflix dataset** (`netflix_titles.csv`) using Python and Pandas. The main goal is to prepare the dataset for analysis by handling missing values, duplicates, inconsistent formatting, and extracting useful information from columns like duration and genres.

---

## Dataset
- **Source:** Netflix dataset containing movie and TV show information.
- **Columns include:**  
  - `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`.

---

## Key Cleaning Steps
1. **Remove Duplicates:** Ensures no repeated entries.  
2. **Handle Missing Values:**  
   - `country` → filled with `"Unknown"`  
   - `director` and `cast` → filled with `"Not Available"`  
3. **Standardize Categorical Columns:** Convert `type` and `listed_in` to lowercase and remove extra spaces.  
4. **Fix Date Formats:** Convert `date_added` to `dd-mm-yyyy` format.  
5. **Rename Columns:** Convert column names to snake_case for consistency.  
6. **Clean Duration Column:** Extract numeric values from the `duration` column.  

---

## Tools & Libraries
- Python 3.x  
- Pandas  

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/MukthaSP05/netflix_data_cleaning_task.git
2. Navigate to the project folder:
   cd netflix_data_cleaning_task
   
4. Install dependencies:
   pip install pandas

5. Run the cleaning script:
   python clean_data.py

The cleaned dataset will be saved as netflix_cleaned.csv.

Output:
Cleaned Dataset: netflix_cleaned.csv
New Columns:
duration_cleaned → numeric values extracted from duration

Future Improvements
- Split listed_in into a list of genres for better analysis.
- Handle NaT in date_added with imputation strategies.
- Include visualizations for cleaned data using Matplotlib or Seaborn.
