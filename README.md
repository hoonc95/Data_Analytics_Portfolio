# HOON CHOI - Data Analytics Portfolio

Hello my name is HOON CHOI.
I have created this repository to serve as my hub to showcase expertise, recount certain challenges, and - overall - monitor progression.
Explore this repo for various insights, projects, and evolution on my Data Analytics and Data Science journey.

## OBJECTIVE
Data Analyst with expertise in data visualization and relational databases, using _Python_, _SQL_, and _Tableau_ - among other business intelligence tools.
Proven ability to drive business outcomes through insightful data, demonstrated by increased customer engagement and cost reduction. 
Skilled in creating impactful marketing strategies and content, contributing to business development. 
Certified in Data Analytics and Business Intelligence with a BBA in Business Administration, seeking to leverage analytical skills to support data-driven decision-making and growth in a dynamic organization.
## TABLE of CONTENTS
### Python Projects
  - [x] Blockchain.py
  - [x] Email_bot.py
  - [x] Desktop_Organizer.py
  - [x] Distance_Converter.py
### SQL Databases
  - [ ] Prospective_NBA_Expansion_Draft_Pool.sql
  - [ ] NBA_2023_Season_Analysis_Player_Stats.sql
### Tableau Dashboards
  - [ ] DASHBOARD-NBA_2023_Season
  - [ ] INFO_SHEET-How_I_Met_Your_Mother

### Certificates
### Contact
## PYTHON PROJECTS
### _Blockchain.py_
The code implements a simple blockchain for authentication.  
Previous blocks are encrypted with a SHA256 hash, used to authenticate the integrity of each new subsequent block.  
The chain starts with a genesis block and allows additional subsequent blocks.
#### Key functions:
```diff
• [calc_hash] to calculate the SHA-256 hash of the block data
• [add_transaction] add a new block to the chain and updates the balances of the transactional parties
• [print_blockchain_with_balances] prints blockchain with the balance of the transactional parties of each block
```
#### Key packages used:
```diff
• import 'hashlib' for secure hashing - SHA256
```
![Screenshot 2024-06-19 at 12 01 43 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/ce2d0930-6d0c-4097-990e-60e0663d6483)

<details>
<summary>Python Script</summary>
  
![blockchain py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/7cc9999d-c382-424c-ab1d-d683613b6f52)
</details>  

### _Email_bot.py_
This script automates sending emails from '_.rtf_' files.  
Locates the most recent '_.rtf_' file in specified directory, parses the file for email details (_FROM, TO, SUBJECT, BODY, and ATTACHMENTS_).  
After confirmation, email is sent and the processed '_.rtf_' file is renamed and catalogued.
#### Key functions:
```diff
• [dotenv] library is needed to load email server details (_username, password, server address, port_) from an configured '_.env_' file.
• [smtp_connection] connects to SMTP server using secure TLS encryption
• [send_email_via_smtp] to administer send emails with attachments
• [get_most_recent_rtf_file] reliant on email drafted from a '_.rtf_' file
• [confirm_send_email] final confirmation dialogue before email
• [rename_rtf_file] once sent, '_.rtf_' is renamed and catalogued as '_[date][time][to_email].rtf_'
```
#### Key packages used:
```diff
• import 'os' for file system operations
• import 'smtplib' for allows for connection to SMTP server
```
<details>
<summary>Python Script</summary>
  
![email_bot py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/76a652b8-9a29-4417-bd37-b9ac7284c9d0)
</details>

### _Desktop_Organizer.py_
Script, designed to automate File Organization on a specified directory ("_~/Desktop_" used in this example ).  
Scans selected directory for files -  based on supported file types (_e.g., audio, documents, images, videos_) - to categorize into selected directories.  
The GUI - built with tkinter - features a simple window with a title, input field, and file browse capabilities, to configure the file organization.  
Logs were configured to provide details about moved files and retreive relocated files.
#### Key functions:
```diff
• [make_unique] to handle duplicate filenames
• [move_file] to relocate files
• [process_file] to determine the appropriate destination for each file
```
#### Key packages used:
```diff
• import 'tkinter' for a simple GUI conformation
• import 'os' for file system operations
• import 'shutil' for high-level file handling
```

![Screenshot 2024-06-19 at 3 44 00 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/03b585c3-21bc-45e1-89f4-bf03d267aea7)
```diff
BEFORE (TOP) | AFTER (BOTTOM)
```
![Screenshot 2024-06-19 at 3 44 14 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/bc7eb833-ccd3-40d8-b1b7-3ba2bfd10666)
<details>
<summary>Python Script</summary>

![desktop_organizer py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/d9cae3e1-69b5-436f-a29b-1a318438607e)

</details>

### _Distance_Converter.py_
Desktop application ran to convert distance - "_mi to km_" / "_km to mi_", selected with a dropdown menu.  
Core function reads the input value and performs the conversion, based on the selected type.  
<Enter> key can be used to run conversion (for full-size keyboard users).
#### Key functions:
```diff
• [convert] to read and process input values
• [combobox] used to provide conversion unit selection
```
#### Key packages used:
```diff
• import 'tkinter' for a simple GUI conformation
• import 'ttk' for theme support
```
![Screenshot 2024-06-19 at 6 02 16 PM](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/c2ea3c59-239c-4800-b095-221d5df58ddc)
<details>
<summary>Python Script</summary>

![distance_converter py](https://github.com/hoonc95/Data_Analytics_Portfolio/assets/168390796/3d61725a-6e5e-4526-a627-0fafd99d7d15)
</details>

## SQL DATABASES
### _Prospective_NBA_Expansion_Draft_Pool.sql_
According to Adam Silver - NBA Commisioner - the NBA is exploring expansion [(ESPN)](https://www.espn.com/nba/story/_/id/40295974/nba-commissioner-silver-exploring-expansion-next-agenda) by adding 2 new teams to the league.  
Much speculation as to the teams, cities, and fanbase they will look to cultivate, but what is rather certain is there will be an expansion draft - most recent expansion draft in 2004 with the addition of the Charlotte Bobcats/Hornets.  

```diff
Currently favored potentials (no specific order):

• Seattle, WA                 [Climate Pledge Arena - 18,300 Capacity]  
  - former home of the Seattle Supersonics, now OKC Thunder
  - 15th highest Metropolitan Statistical Area (pop: 4,018,762) [2020 Census Data]

• Las Vegas, NV               [T-Mobile Arena - 18,000 Capacity]  
  - Pat McAfee show interview - Adam Silver states LV is a definite candidate
  - current home of the LV Aces (WNBA)  
  - annual host of the NBA Rookie Summer League  
  - LeBron James has shown interest in owning an NBA franchise
  - 29th highest Metropolitan Statistical Area (pop: 2,265,461) [2020 Census Data]

• Mexico City, MEXICO (CDMX)  [Mexico City Arena - 22,300 Capacity | Palacio de los Deportes - 20,000 Capacity]  
  - current home of the Capitanes de Ciudad de México (NBA G-League)
  - Adam Silver states discussions were opened about an NBA Academy in Ciudad De México
  - played host to the 1992 NBA Global Games
  - 3rd most populous city in the Western Hemisphere
  - Most populous city in North America (pop: 9,209,944) 

• Vancouver, CANADA          [Rogers Arena - 19,700 Capacity]  
  - former home of the Memphis Grizzlies
  - 3rd Largest Metropolitan city in Canada (pop: 2,642,825) [2021 StatCAN Data]

• San Diego, CA              [Pechanga Arena - 14,500 Capacity]  
  - former home of the Houston Rockets, GS Warriors, and LA Clippers
  - regular host of NBA team preseaon training camps and exhibition games
  - 17th highest Metropolitan Statistical Area (pop: 3,298,634) [2020 Census Data]
```
##### Sources 
> Mar 2024 [Metropolitan and Micropolitan Statistical Areas Population Totals: 2020-2023 | US Census Bureau](https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-metro-and-micro-statistical-areas.html#v2023)  
> June 2024 [Adam Silver Interview at the 2024 NBA Finals - Game 5 | NBC Sports](https://x.com/NBCSCeltics/status/1799940731907330263)  
> Feb 2024 [Adam Silver: Las Vegas 'definitely' an expansion candidate | ESPN](https://www.espn.com/nba/story/_/id/39525601/adam-silver-tells-espn-las-vegas-definitely-list-expansion-candidates)  
> June 2022 [Los Angeles Lakers star LeBron James says he wants to own NBA team in Las Vegas | ESPN](https://www.espn.com/nba/story/_/id/34065127/los-angeles-lakers-star-lebron-james-says-wants-own-nba-team-las-vegas)  
> June 2024 [List of cities in the Americas by population | Wikipedia](https://en.wikipedia.org/wiki/List_of_cities_in_the_Americas_by_population#cite_note-4)  
> Feb 2022 [Population and dwelling counts: Census metropolitan areas, census agglomerations and census subdivisions | StatCAN](https://doi.org/10.25318/9810000301-eng)  

#### Draft Rules
As per the previous 
<details>
<summary>SQL Query</summary>

</details>

### _NBA_2023_Season_Analysis_Player_Stats.sql_
<details>
<summary>SQL Query</summary>

</details>

## TABLEAU DASHBOARDS
### _DASHBOARD-NBA_2023_Season_
<details>

<summary>Source</summary>

[Kaggle - NBA Play-by-Play Data (1997-2023)](https://www.kaggle.com/datasets/szymonjwiak/nba-play-by-play-data-1997-2023?select=pbp2023.csv)
</details>

### _INFO_SHEET-How_I_Met_Your_Mother_
<details>

<summary>Source</summary>

[Kaggle - How I Met Your Mother Dataset](https://www.kaggle.com/datasets/vidheeshnacode/how-i-met-your-mother-himym-dataset))
</details>

## CERTIFICATES
• Feb 2024  [IBM Data Analyst](https://coursera.org/share/93fd896fbf75e92b6400e7be753f8ab0)  
• Feb 2024  [Google Data Analytics](https://coursera.org/share/3b9348c213103a5f10e22e412c460eee)  
• Jan 2024  [Google Digital Marketing & E-Commerce](https://coursera.org/share/fe6fd28a036b58c3edfdce1d6ee4142f)  
• Jul 2023  [Google Business Intelligence](https://coursera.org/share/33efd825b8d1ff48a48dac3e55ba31a1)
## CONTACT
#### [Email](mailto:ladders_bodkin0h@icloud.com)
#### [LinkedIn](https://www.linkedin.com/in/hoon-choi-49289615b)
