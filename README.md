# Phonepe Pulse Data Visualization and Exploration
## The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.
### The solution must include the following steps:
#### 1. Extract data from the Phonepe pulse Github repository through scripting and clone it..
#### 2. Transform the data into a suitable format and perform any necessary cleaning and pre-processing steps.
#### 3. Insert the transformed data into a MySQL database for efficient storage and retrieval.
#### 4. Create a live geo visualization dashboard using Streamlit and Plotly in Python to display the data in an interactive and visually appealing manner.
#### 5. Fetch the data from the MySQL database to display in the dashboard.
## Approach:
#### 1. Data extraction: Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.
#### 2. Data transformation: Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This may include cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
#### 3. Database insertion: Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
#### 4. Dashboard creation: Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.
#### 5. Data retrieval: Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.
#### 6. Deployment: Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.

Download Git Software : https://git-scm.com/download/win
clone github data for data extraction 
```
import git
url='https://github.com/PhonePe/pulse.git'
destination=r'C:\Users\user\OneDrive\Desktop\praveen\phonepe'
git.Repo.clone_from(url,destination)
```
Data Extraction : 
```
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/main/phonepe.ipynb
```
Import required libraries
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L1-L8

Creating option menu page
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L17-L26

![Screenshot 2024-05-05 110653](https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/assets/161042655/36bc4fa5-ee22-44e6-8578-02bc5e8520ca)

About page: 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L29-L49

Home page:
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L52-L88

![Screenshot 2024-05-05 111105](https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/assets/161042655/f2324516-f153-477a-a61c-3268386a782c)

Top chart page: 
####option creating 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L92-L110
![Screenshot 2024-05-05 111449](https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/assets/161042655/b15f3902-054a-407f-a94e-10fe7570a8d5)

#### Option Transaction: 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L112-L275

#### Option Users: 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L277-L530

Explore data page:
#### option creating 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L533-L550

![Screenshot 2024-05-05 111945](https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/assets/161042655/a2b71b86-ee3b-4849-85d2-af804eaf6e3f)
#### Option Transaction : 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L552-L763

#### Option Users: 
https://github.com/PraveenkuamrA/Phonepe-Pulse-Data-Visualization-and-Exploration-/blob/4495a6b6ac13e6f024e21b618bd8195926dcc7b4/phonepe.py#L765-L1069





