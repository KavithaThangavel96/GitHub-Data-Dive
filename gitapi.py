
# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit dashboard setting
slt.title("GitHub Data Dive Insights")
slt.subheader("SELECT THE QUESTIONS TO GET INSIGHTS")

options=slt.selectbox("Select options",("1.What are the names of all the repository and their corresponding owners?",
                          "2.Which repository have the most number of stars and their name?",
                          "3.What are the top 25 forks and their repository?",
                          "4.List of open issue and their repository?",
                          "5.Count of programming languages",
                          "6.What are the names of all the repository and their url and like counts top 10?",
                          "7.What are the names of all the repository and their descriptions and forks counts top 10?",
                          "8.What are the names of all the repository that have created in the year 2016?",
                          "9.Count of license type",
                          "10.Which repository name and owner used python?"))
# Query to excute 1st Question
if options=="1.What are the names of all the repository and their corresponding owners?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute(''' select Repository_Name,Owner from Git
                        order by Repository_Name''')
        out=my_cursor.fetchall()
        que_1=pd.DataFrame(out,columns=["Repository_Name","Owner"])
        slt.success("ANSWER")
        slt.write(que_1)

# Query to excute 3rd Question
if options=="2.Which repository have the most number of stars and their name?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute(''' select Repository_Name,Number_of_Stars as counts from Git
                        order by Number_of_Stars desc limit 25''')
        out=my_cursor.fetchall()
        col1,col2 = slt.columns([2,2],gap="small")
        with col1:
            que_2=pd.DataFrame(out,columns=["Repository_Name","Number_of_Stars"])
            slt.success("ANSWER")
            slt.write(que_2)
        with col2:
            # Create a bar chart
            slt.bar_chart(que_2.set_index("Repository_Name"))

# Query to excute 3rd Question
if options=="3.What are the top 25 forks and their repository?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute(''' select Repository_Name,Number_of_Forks from Git
                        order by Number_of_Forks desc limit 25''')
        out=my_cursor.fetchall()
        col1,col2 = slt.columns([2,2],gap="small")
        with col1:
            que_3=pd.DataFrame(out,columns=["Repository_Name","Number_of_Forks"])
            slt.success("ANSWER")
            slt.write(que_3)
        with col2:
            # Create a bar chart
            slt.bar_chart(que_3.set_index("Repository_Name"))

# Query to excute 4th Question
if options=="4.List of open issue and their repository?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute(''' select Repository_Name,Number_of_Open_Issues from Git
                        order by Number_of_Open_Issues desc limit 10''')
        out=my_cursor.fetchall()
        col1,col2 = slt.columns([2,2],gap="small")
        with col1:
            que_4=pd.DataFrame(out,columns=["Repository_Name","Number_of_Open_Issues"])
            slt.success("ANSWER")
            slt.write(que_4)
        with col2:
            # Create a bar chart
            slt.bar_chart(que_4.set_index("Repository_Name"))


# Query to excute 5th Question
if options=="5.Count of programming languages":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select Programming_Language , count(Programming_Language) as counts from Git
                        group by Programming_Language order by counts desc limit 25 offset 1''')
        out=my_cursor.fetchall()
        que_5=pd.DataFrame(out,columns=["Programming_Language","counts"])
        slt.success("ANSWER")
        slt.write(que_5)

        # Create a horizontal bar chart using seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=que_5,
            y="Programming_Language",
            x="counts",
            palette="viridis"  # You can change the palette to others like "coolwarm", "magma", etc.
        )

        # Add labels and title
        plt.xlabel("Counts")
        plt.ylabel("Programming Language")
        plt.title("Counts of Programming Languages")

        # Display the plot in Streamlit
        slt.pyplot(plt)

# Query to excute 6th Question
if options=="6.What are the names of all the repository and their url and like counts top 10?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select Repository_Name , URL  from Git
                        limit 10''')
        out=my_cursor.fetchall()
        que_6=pd.DataFrame(out,columns=["Repository_Name","URL"])
        slt.success("ANSWER")
        slt.write(que_6)

# Query to excute 7th Question
if options=="7.What are the names of all the repository and their descriptions and forks counts top 10?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select Repository_Name , Description from Git
                        limit 10''')
        out=my_cursor.fetchall()
        que_7=pd.DataFrame(out,columns=["Repository_Name","Description"])
        slt.success("ANSWER")
        slt.write(que_7)

# Query to excute 8th Question
if options=="8.What are the names of all the repository that have created in the year 2016?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select Repository_Name , Owner, Programming_Language,Creation_Date from Git
                        where year(Git.Creation_Date)=2016''')
        out=my_cursor.fetchall()
        que_8=pd.DataFrame(out,columns=["Repository_Name","Owner","Programming_Language","Creation_Date"])
        slt.success("ANSWER")
        slt.write(que_8)

# Query to excute 9th Question
if options=="9.Count of license type":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select License_Type , count(License_Type) as counts from Git
                        group by License_Type order by counts desc limit 25 ''')
        out=my_cursor.fetchall()
        que_9=pd.DataFrame(out,columns=["License_Type","counts"])
        slt.success("ANSWER")
        slt.write(que_9)
                # Create a horizontal bar chart using seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=que_9,
            y="License_Type",
            x="counts",
            palette="viridis"  # You can change the palette to others like "coolwarm", "magma", etc.
        )

        # Add labels and title
        plt.xlabel("Counts")
        plt.ylabel("License_Type")
        plt.title("Counts of License_Type")

        # Display the plot in Streamlit
        slt.pyplot(plt)

# Query to excute 10th Question
if options=="10.Which repository name and owner used python?":
    if slt.button("SUBMIT"):
        conn = mysql.connector.connect(host="localhost", user="root", password="kavi",database="Githubapi")
        my_cursor = conn.cursor()
        my_cursor.execute('''select Repository_Name , Owner, Programming_Language from Git
                        where Programming_Language="Python"''')
        out=my_cursor.fetchall()
        que_10=pd.DataFrame(out,columns=["Repository_Name","Owner","Programming_Language"])
        slt.success("ANSWER")
        slt.write(que_10)