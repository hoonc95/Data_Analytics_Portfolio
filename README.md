# HOON CHOI - Data Analytics Portfolio

Hello my name is HOON CHOI.
I have created this repository to serve as my hub to showcase expertise, recount certain challenges, and - overall - monitor progression.
Explore this repo for various insights, projects, and evolution on my Data Analytics and Data Science journey.

## OBJECTIVE
Data Analyst with expertise in data visualization and relational databases, using _Python_, _SQL_, and _Tableau_ - among other business intelligence tools.
Proven ability to drive business outcomes through insightful data, demonstrated by increased customer engagement and cost reduction. 
Skilled in creating impactful marketing strategies and content, contributing to business development. 
Certified in Data Analytics and Business Intelligence with a BBA in Business Administration, seeking to leverage analytical skills to support data-driven decision-making and growth in a dynamic organization.
## TABLE OF CONTENTS
### Projects
#### Python
  - [x] Blockchain.py
  - [x] Email_bot.py
  - [x] Desktop_Cleaner.py
  - [x] Distance_Converter.py
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
#### Blockchain.py
The code implements a simple blockchain for authentication.  
Previous blocks are encrypted with a SHA256 hash, used to authenticate the integrity of each new subsequent block.  
The chain starts with a genesis block and allows additional subsequent blocks.
##### Key functions:
```diff
* [calc_hash] to calculate the SHA-256 hash of the block data
* [add_transaction] add a new block to the chain and updates the balances of the transactional parties
* [print_blockchain_with_balances] prints blockchain with the balance of the transactional parties of each block
```
##### Key packages used:
```diff
* import 'hashlib' for secure hashing - SHA256
```
![Screenshot 2024-06-19 at 12 01 43 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/ce2d0930-6d0c-4097-990e-60e0663d6483)

<details>
<summary>Script</summary>

![blockchain_w__balance](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/49c4f97f-88a6-4c02-bf6a-329031bd4fe2)
</details>

#### Email_bot.py
This script automates sending emails from '_.rtf_' files.  
Locates the most recent '_.rtf_' file in specified directory, parses the file for email details (_FROM, TO, SUBJECT, BODY, and ATTACHMENTS_).  
After confirmation, email is sent and the processed '_.rtf_' file is renamed and catalogued.
##### Key functions:
```diff
* [dotenv] library is needed to load email server details (_username, password, server address, port_) from an configured '_.env_' file.
* [smtp_connection] connects to SMTP server using secure TLS encryption
* [send_email_via_smtp] to administer send emails with attachments
* [get_most_recent_rtf_file] reliant on email drafted from a '_.rtf_' file
* [confirm_send_email] final confirmation dialogue before email
* [rename_rtf_file] once sent, '_.rtf_' is renamed and catalogued as '_[date][time][to_email].rtf_'
```
##### Key packages used:
```diff
* import 'os' for file system operations
* import 'smtplib' for allows for connection to SMTP server
```
<details>
<summary>Script</summary>
  
![email_bot py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/76a652b8-9a29-4417-bd37-b9ac7284c9d0)
</details>

#### Desktop_Organizer.py
Script, designed to automate File Organization on a specified directory ("_~/Desktop_" used in this example ).  
Scans selected directory for files -  based on supported file types (_e.g., audio, documents, images, videos_) - to categorize into selected directories.  
The GUI - built with tkinter - features a simple window with a title, input field, and file browse capabilities, to configure the file organization.  
Logs were configured to provide details about moved files and retreive relocated files.
##### Key functions:
```diff
* [make_unique] to handle duplicate filenames
* [move_file] to relocate files
* [process_file] to determine the appropriate destination for each file
```
##### Key packages used:
```diff
* import 'tkinter' for a simple GUI conformation
* import 'os' for file system operations
* import 'shutil' for high-level file handling
```

![Screenshot 2024-06-19 at 3 44 14 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/bc7eb833-ccd3-40d8-b1b7-3ba2bfd10666)
```diff
BEFORE (TOP) | AFTER (BOTTOM)
```
![Screenshot 2024-06-19 at 3 44 00 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/03b585c3-21bc-45e1-89f4-bf03d267aea7)
<details>
<summary>Script</summary>

![desktop_organizer py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/d9cae3e1-69b5-436f-a29b-1a318438607e)

</details>

#### Distance_Converter.py
Desktop application ran to convert distance - "_mi to km_" / "_km to mi_", selected with a dropdown menu.  
Core function reads the input value and performs the conversion, based on the selected type.  
<Enter> key can be used to run conversion (for full-size keyboard users).
##### Key functions:
```diff
* [convert] to read and process input values
* [combobox] used to provide conversion unit selection
```
##### Key packages used:
```diff
* import 'tkinter' for a simple GUI conformation
* import 'ttk' for theme support
```
<details>
<summary>Script</summary>

![distance_converter py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/3d61725a-6e5e-4526-a627-0fafd99d7d15)
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
