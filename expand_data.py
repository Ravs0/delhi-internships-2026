import os

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

corporate_firms = ["HSA Advocates", "SNG & Partners", "Dentons Link Legal", "Argus Partners", "Bhasin & Co.", "Dua Associates", "Majmudar & Partners", "Wadia Ghandy & Co.", "Juris Corp", "LexCounsel", "O.P. Khaitan & Co.", "Fox Mandal & Associates", "Titus & Co.", "Zeus Law", "Trust Legal", "SPICE Route Legal", "Ikigai Law", "Samvad Partners", "MVKini", "King Stubb & Kasiva", "KLaw (Krishnamurthy & Co)", "TMT Law Practice", "Hammurabi & Solomon", "Saraf and Partners", "Touchstone Partners", "Factum Law", "Athena Legal", "Alpha Partners", "Kesar Dass B. & Associates", "VSA Legal", "Acuity Law", "Aarna Law", "Chambers of Jain and Kumar", "PSL Advocates & Solicitors", "Clasis Law", "Sarthak Advocates & Solicitors", "Orbit Law Services", "P&A Law Offices", "A.K. Singh & Co.", "Mindspool Legal", "Aureus Law Partners", "Abhinav Law Chambers", "Aks Partners", "Archeus Law", "LexAequo", "Niti Nyaya Law Offices", "PXV Law Partners", "Prudentia Law", "S.K. Singhi & Partners"]

policy_orgs = ["PRS Legislative Research", "Centre for Policy Research (CPR)", "Observer Research Foundation (ORF)", "Institute of Peace and Conflict Studies (IPCS)", "National Commission for Women (NCW)", "National Commission for Protection of Child Rights (NCPCR)", "National Green Tribunal (NGT)", "Central Information Commission (CIC)", "Law Commission of India", "Human Rights Law Network (HRLN)", "Multiple Action Research Group (MARG)", "Centre for Civil Society (CCS)", "Internet Freedom Foundation (IFF)", "Software Freedom Law Center (sflc.in)", "Majlis Legal Centre", "Commonwealth Human Rights Initiative (CHRI)", "Association for Democratic Reforms (ADR)", "People's Union for Civil Liberties (PUCL)", "Amnesty India Legal Team", "Centre for Science and Environment (CSE)", "TERI Legal Division", "RTI India Research", "Vidhikrit Legal Policy", "Navtej Johar Foundation", "Naz Foundation Legal"]

ip_firms = ["K&S Partners", "Saikrishna & Associates", "Rahul Chaudhry & Partners", "Inttl Advocare", "Obhan & Associates", "Mason & Associates", "R.K. Dewan & Co.", "Chadha & Chadha", "RNA Technology and IP Attorneys", "D.P. Ahuja & Co.", "S. Majumdar & Co.", "Y.J. Trivedi & Co.", "Kan and Krishme", "Lex Mores", "Fidus Law Chambers", "Sujata Chaudhri IP Attorneys", "Seenergi IPR", "Aditya & Associates", "Agrawal & Associates", "Aswal Associates", "Groverlaw", "IP Gurus", "Khurana & Khurana", "L.S. Davar & Co.", "Lex Fons", "Parker & Parker", "Puthran & Associates", "R.R. Shah & Co.", "S.S. Datta & Associates", "Sagacious IP", "Scriboard", "Tridus", "Vidya Dinkel", "ZeusIP Advocates", "IPR International"]

chambers = ["Chamber of Kapil Sibal", "Chamber of Mukul Rohatgi", "Chamber of Abhishek Manu Singhvi", "Chamber of Tushar Mehta", "Chamber of Arvind Datar", "Chamber of Parag Tripathi", "Chamber of Vikas Singh", "Chamber of Neeraj Kishan Kaul", "Chamber of Aman Lekhi", "Chamber of Geeta Luthra", "Chamber of Rebecca John", "Chamber of Vrinda Grover", "Chamber of Karuna Nundy", "Chamber of Indira Jaising", "Chamber of Colin Gonsalves", "Chamber of Sidharth Luthra", "Chamber of Dayan Krishnan", "Chamber of Siddharth Agarwal", "Chamber of Maninder Singh", "Chamber of Pinaki Misra", "Chamber of KV Viswanathan", "Chamber of Nidhesh Gupta", "Chamber of Sanjay Jain", "Chamber of Jayant Bhushan", "Chamber of Shyam Divan"]

new_items = []

for idx, firm in enumerate(corporate_firms):
    new_items.append({"title": firm, "category": "firm", "focus": "Corporate & Commercial Law"})

for idx, org in enumerate(policy_orgs):
    new_items.append({"title": org, "category": "policy", "focus": "Policy, Research & Rights"})

for idx, ip in enumerate(ip_firms):
    new_items.append({"title": ip, "category": "firm", "focus": "Intellectual Property (IP)"})

for idx, ch in enumerate(chambers):
    new_items.append({"title": ch, "category": "litigation", "focus": "Appellate Litigation (SC/DHC)"})

# Build JS string
new_js = ""
start_id = 76
for i, item in enumerate(new_items):
    clean_title = item['title'].replace("'", "\\'")
    new_js += f"            {{ id: {start_id + i}, title: '{clean_title}', category: '{item['category']}', urgent: false, deadline: 'Check Website / Rolling', stipend: 'Varies', focus: '{item['focus']}', apply: 'https://www.google.com/search?q={clean_title.replace(' ', '+')}+Delhi+Internship' }},\n"

# Inject into content
new_content = content.replace("const internships = [", "const internships = [\n" + new_js)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully added {len(new_items)} new internships!")
