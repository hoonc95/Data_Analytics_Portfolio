# HOON CHOI - Data Analytics Portfolio

Hello my name is HOON CHOI.
I have created this repository to serve as my hub to showcase expertise, recount certain challenges, and - overall - monitor progression.
Explore this repo for various insights, projects, and evolution on my Data Analytics and Data Science journey.

## OBJECTIVE
Data Analyst with expertise in data visualization and relational databases, using _Python_, _SQL_, and _Tableau_ - among other business intelligence tools.
Proven ability to drive business outcomes through insightful data, demonstrated by increased customer engagement and cost reduction. 
Skilled in creating impactful marketing strategies and content, contributing to business development. 
Certified in Data Analytics and Business Intelligence with a BBA in Business Administration, seeking to leverage analytical skills to support data-driven decision-making and growth in a dynamic organization.
## RESUME
## TABLE OF CONTENTS
### Projects
#### Python
  - [x] Distance Converter
  - [x] Desktop_Cleaner.py
  - [x] Email_bot.py
#### SQL
  - [ ] NBA 2023 Season Analysis
  - [ ] How I Met Your Mother Ratings
#### Tableau
  - [ ] NBA 2023 Season Dashboard
  - [ ] Spotify Song Popularity
### Certificates
### Contact
## PROJECTS
### _Python_
#### Desktop_Organizer.py
Script, designed to automate File Organization on a specified directory ("_~/Desktop_") used in this example.  
Scans desktop for files -  based on supported file types (_e.g., images, videos, audio, documents_) - to categorize into predefined directories.  
The GUI, built with tkinter, features a simple window with a title and a button, that begins the file organization process.  
Logs were configured to provide details about moved files and retreive relocated files.

##### Key functions:
- [_make_unique_] to handle duplicate filenames
- [_move_file_] to relocate files
- [_process_file_] to determine the appropriate destination for each file

##### Key packages used:
- 'tkinter' for a simple GUI conformation
- 'os' for file system operations
- 'shutil' for high-level file handling
<details>
<summary>Script</summary>
  
![desktop_organizer](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/23196a1f-26c8-4e3c-9f6f-ec84c3ace539)
</details>

#### Distance_Converter.py
Desktop application ran to convert distance - "_mi to km_" / "_km to mi_", selected with a dropdown menu.  
Core function reads the input value and performs the conversion, based on the selected type.  
<Enter> key can be used to run conversion (for full-size keyboard users).

##### Key functions:
- [_convert_] to read and process input values
- [_combobox_] used to provide conversion unit selection

##### Key packages used:
- 'tkinter' for a simple GUI conformation
- 'ttk' for theme support
<details>
<summary>Script</summary>

![distance_converter py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/53261b73-1a9f-4898-89ab-f0e3cd5fd668)
</details>

#### Email_bot.py
This script automates sending emails from '_.rtf_' files.  
Locates the most recent '_.rtf_' file in specified directory, parses the file for email details (_FROM, TO, SUBJECT, BODY, and ATTACHMENTS_).  
After confirmation, email is sent and the processed '_.rtf_' file is renamed and catalogued.

##### Key functions:
- [_dotenv_] library is needed to load email server details (_username, password, server address, port_) from an configured '_.env_' file.
- [_smtp_connection_] connects to SMTP server using secure TLS encryption
- [_send_email_via_smtp_] to administer send emails with attachments
- [_get_most_recent_rtf_file_] reliant on email drafted from a '_.rtf_' file
- [_confirm_send_email_] final confirmation dialogue before email
- [_rename_rtf_file_] once sent, '_.rtf_' is renamed and catalogued as '_[date][time][to_email].rtf_'

##### Key packages used:
- 'os' for file system operations
- 'smtplib' for theme support
<details>
<summary>Script</summary>
  
![email_bot py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/76a652b8-9a29-4417-bd37-b9ac7284c9d0)
</details>

### _SQL_
#### NBA_2023_Season_Player_Stats.sql
#### Sri_Lanka_Auto_Accident_Insights.sql
### _Tableau_
#### NBA_2023_Season_Dashboard
<details>

<summary>Details</summary>

Source: 
[Kaggle - NBA Play-by-Play Data (1997-2023)](https://www.kaggle.com/datasets/szymonjwiak/nba-play-by-play-data-1997-2023?select=pbp2023.csv)
</details>

#### Popular_Spotify_Songs
<details>

<summary>Details</summary>

Source:
[Kaggle - Spotify Songs Album)](https://www.kaggle.com/datasets/zeesolver/spotfy/data)
</details>

## CERTIFICATES
- Feb 2024 [IBM Data Analyst](https://coursera.org/share/93fd896fbf75e92b6400e7be753f8ab0)
- Feb 2024 [Google Data Analytics](https://coursera.org/share/3b9348c213103a5f10e22e412c460eee)
- Jan 2024 [Google Digital Marketing & E-Commerce](https://coursera.org/share/fe6fd28a036b58c3edfdce1d6ee4142f)
- Jul 2023 [Google Business Intelligence](https://coursera.org/share/33efd825b8d1ff48a48dac3e55ba31a1)
## CONTACT
#### [Email](mailto:ladders_bodkin0h@icloud.com)
#### [LinkedIn](https://www.linkedin.com/in/hoon-choi-49289615b)
