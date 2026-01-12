# since docker doesnt run notebooks we will use scripts
import pandas as pd


import sqlite3

def extract():
    """
    Extracts raw data from a CSV file and loads it into memory
    without applying any transformations.

    Parameters:
        source_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw dataset ready for transformation.
    """
    data = pd.read_csv("data/processed/cleaned.csv")

    return data


# the second step is to trasnform our data for the pipeline. in this case we will be getting the information for which major has the msot depression. 

def transform(data):
    df = data
    unique_majors = df["what_is_your_course?"].drop_duplicates()
    total_number_of_unique_majors = len(unique_majors)

    # this tells us the diffrent types of courses and their total amount

    # print("the total number of majors is ", total_number_of_unique_majors)
    # print("these are the unique majors", unique_majors)



                                     # depresion vs. majors 
    depression_and_majors = df.groupby(["what_is_your_course?", "do_you_have_depression?"]).size()

    yes_only = depression_and_majors.xs(
        "Yes", level="do_you_have_depression?"
    )
    top_depressed_courses = yes_only.sort_values(ascending=False).head(5)

    table = top_depressed_courses.reset_index()
    table.columns = ["course", "number of depressed individuals"]

    return table
    

    


    




# lets load our data final step

def load(table):

    conn = sqlite3.connect("data/db/mental_health.db")


    table.to_sql(
        "depression_by_course",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

if __name__ == "__main__":
    data = extract()
    table = transform(data)
    load(table)