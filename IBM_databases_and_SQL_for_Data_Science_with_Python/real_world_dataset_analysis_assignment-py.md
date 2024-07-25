<h1 align=center><font size = 5>Assignment: Notebook for Graded Assessment</font></h1>


Using this Python notebook you will:

1.  Understand three Chicago datasets
2.  Load the three datasets into three tables in a SQLIte database
3.  Execute SQL queries to answer assignment questions


To complete the assignment problems in this notebook you will be using three datasets that are available on the city of Chicago's Data Portal:

### 1. Socioeconomic Indicators in Chicago

This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

### 2. Chicago Public Schools

This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year. This dataset is provided by the city of Chicago's Data Portal.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

### 3. Chicago Crime Data

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)


### Download the datasets

This assignment requires you to have these three tables populated with a subset of the whole datasets.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. 

Use the links below to read the data files using the Pandas library. 

* Chicago Census Data

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01

* Chicago Public Schools

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01

* Chicago Crime Data

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01

**NOTE:** Ensure you use the datasets available on the links above instead of directly from the Chicago Data Portal. The versions linked here are subsets of the original datasets and have some of the column names modified to be more database friendly which will make it easier to complete this assignment.


### Store the datasets in database tables

To analyze the data using SQL, it first needs to be loaded into SQLite DB.
We will create three tables in as under:

1.  **CENSUS_DATA**
2.  **CHICAGO_PUBLIC_SCHOOLS**
3.  **CHICAGO_CRIME_DATA**


Load the `pandas` and `sqlite3` libraries and establish a connection to `FinalDB.db`



```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('FinalDB.db')
```

Load the SQL magic module



```python
%load_ext sql
%sql sqlite:///FinalDB.db
```

    The sql extension is already loaded. To reload it, use:
      %reload_ext sql





    'Connected: @FinalDB.db'



Use `Pandas` to load the data available in the links above to dataframes. Use these dataframes to load data on to the database `FinalDB.db` as required tables.



```python
# Define URLs for datasets
census_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01"
schools_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01"
crime_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01"

# Load datasets into pandas DataFrames
census_data = pd.read_csv(census_data_url)
schools_data = pd.read_csv(schools_data_url)
crime_data = pd.read_csv(crime_data_url)

# Create tables in the SQLite database and load data into these tables
census_data.to_sql('CENSUS_DATA', conn, if_exists='replace', index=False)
schools_data.to_sql('CHICAGO_PUBLIC_SCHOOLS', conn, if_exists='replace', index=False)
crime_data.to_sql('CHICAGO_CRIME_DATA', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
```

Establish a connection between SQL magic module and the database `FinalDB.db`



```python
%sql sqlite:///FinalDB.db
```




    'Connected: @FinalDB.db'



## Problems

Now write and execute SQL queries to solve assignment problems

### Problem 1

##### Find the total number of crimes recorded in the CRIME table.



```python
conn = sqlite3.connect('FinalDB.db')

query = "SELECT COUNT(*) AS total_crimes FROM CHICAGO_CRIME_DATA"
df = pd.read_sql_query(query, conn)
total_crimes = df['total_crimes'].iloc[0]
print(f"Total number of crimes recorded: {total_crimes}")
```

    Total number of crimes recorded: 533


### Problem 2

##### List community area names and numbers with per capita income less than 11000.



```python
query = """
SELECT community_area_number, community_area_name 
FROM CENSUS_DATA 
WHERE per_capita_income < 11000
"""
df = pd.read_sql_query(query, conn)
print(df)
```

       COMMUNITY_AREA_NUMBER COMMUNITY_AREA_NAME
    0                   26.0  West Garfield Park
    1                   30.0      South Lawndale
    2                   37.0         Fuller Park
    3                   54.0           Riverdale


### Problem 3

##### List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis) 



```python
query = """
SELECT case_number 
FROM CHICAGO_CRIME_DATA 
WHERE description LIKE '%MINOR%' OR primary_type LIKE '%MINOR%'
"""
df = pd.read_sql_query(query, conn)
print(df)
```

      CASE_NUMBER
    0    HL266884
    1    HK238408


### Problem 4

##### List all kidnapping crimes involving a child?



```python
query = """
SELECT case_number, description, primary_type
FROM CHICAGO_CRIME_DATA
WHERE primary_type = 'KIDNAPPING' AND description LIKE '%CHILD%'
"""
df = pd.read_sql_query(query, conn)
print(df)
```

      CASE_NUMBER               DESCRIPTION PRIMARY_TYPE
    0    HN144152  CHILD ABDUCTION/STRANGER   KIDNAPPING


### Problem 5

##### List the kind of crimes that were recorded at schools. (No repetitions)



```python
query = """
SELECT DISTINCT primary_type
FROM CHICAGO_CRIME_DATA
WHERE location_description LIKE '%SCHOOL%'
"""
df = pd.read_sql_query(query, conn)
print(df)
```

                 PRIMARY_TYPE
    0                 BATTERY
    1         CRIMINAL DAMAGE
    2               NARCOTICS
    3                 ASSAULT
    4       CRIMINAL TRESPASS
    5  PUBLIC PEACE VIOLATION


### Problem 6

##### List 5 community areas with highest % of households below poverty line



```python
schema_query = "PRAGMA table_info(CENSUS_DATA);"
columns_df = pd.read_sql_query(schema_query, conn)
print(columns_df)
```

       cid                                          name     type  notnull  \
    0    0                         COMMUNITY_AREA_NUMBER     REAL        0   
    1    1                           COMMUNITY_AREA_NAME     TEXT        0   
    2    2                    PERCENT_OF_HOUSING_CROWDED     REAL        0   
    3    3              PERCENT_HOUSEHOLDS_BELOW_POVERTY     REAL        0   
    4    4                   PERCENT_AGED_16__UNEMPLOYED     REAL        0   
    5    5  PERCENT_AGED_25__WITHOUT_HIGH_SCHOOL_DIPLOMA     REAL        0   
    6    6              PERCENT_AGED_UNDER_18_OR_OVER_64     REAL        0   
    7    7                             PER_CAPITA_INCOME  INTEGER        0   
    8    8                                HARDSHIP_INDEX     REAL        0   
    
      dflt_value  pk  
    0       None   0  
    1       None   0  
    2       None   0  
    3       None   0  
    4       None   0  
    5       None   0  
    6       None   0  
    7       None   0  
    8       None   0  


### Problem 7

##### Which community area is most crime prone? Display the coumminty area number only.



```python
schema_query = "PRAGMA table_info(CHICAGO_CRIME_DATA);"
columns_df = pd.read_sql_query(schema_query, conn)
print(columns_df)
```

        cid                   name     type  notnull dflt_value  pk
    0     0                  index   BIGINT        0       None   0
    1     1                     ID   BIGINT        0       None   0
    2     2            CASE_NUMBER     TEXT        0       None   0
    3     3                   DATE     TEXT        0       None   0
    4     4                  BLOCK     TEXT        0       None   0
    5     5                   IUCR     TEXT        0       None   0
    6     6           PRIMARY_TYPE     TEXT        0       None   0
    7     7            DESCRIPTION     TEXT        0       None   0
    8     8   LOCATION_DESCRIPTION     TEXT        0       None   0
    9     9                 ARREST  BOOLEAN        0       None   0
    10   10               DOMESTIC  BOOLEAN        0       None   0
    11   11                   BEAT   BIGINT        0       None   0
    12   12               DISTRICT   BIGINT        0       None   0
    13   13                   WARD    FLOAT        0       None   0
    14   14  COMMUNITY_AREA_NUMBER    FLOAT        0       None   0
    15   15                FBICODE     TEXT        0       None   0
    16   16           X_COORDINATE    FLOAT        0       None   0
    17   17           Y_COORDINATE    FLOAT        0       None   0
    18   18                   YEAR   BIGINT        0       None   0
    19   19              UPDATEDON     TEXT        0       None   0
    20   20               LATITUDE    FLOAT        0       None   0
    21   21              LONGITUDE    FLOAT        0       None   0
    22   22               LOCATION     TEXT        0       None   0


### Problem 8

##### Use a sub-query to find the name of the community area with highest hardship index



```python
query = """
SELECT community_area_name
FROM CENSUS_DATA
WHERE hardship_index = (
    SELECT MAX(hardship_index)
    FROM CENSUS_DATA
);
"""
df = pd.read_sql_query(query, conn)
print(df)
```

      COMMUNITY_AREA_NAME
    0           Riverdale

