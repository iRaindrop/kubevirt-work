from gettext import find
import json
import string
import xml.dom.minidom
import csv
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
from datetime import datetime, time
import calendar
import uuid
import shutil
import urllib.request 
import ssl
import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import copy
import requests
import os
from os import path
import glob
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import asyncio
import tracemalloc
from datetime import timedelta
from pathlib import Path


async def main():



    global navdata
    navdata = []

    global snippetData
    snippetData = []

    # ymlToSheet()
    # find_missing_h1_headings()

    add_missing_h1_headings()
    # remove_comments("/Users/Brucehamilton/GitHub/CNCF/configmap-kourier.yaml", "/Users/Brucehamilton/GitHub/CNCF/configmap-kourier2.yaml" )

    # for key, value in enumerate(soapnames.items()):
    #  print(0}: {1}").format(key,value)

    # find_Content()

    # get_titles_from_h1()

    # get_headings()

    # check_inclusive()

    # tidyJson()

def doWork():


    # findSnippets()

    # Construct and save the CSV file
    # fieldNames = ['Path', 'Filename', 'UsedByPath', 'UsedByName']

    # with open("snippets.csv", 'w') as csvfile: 
    #     writer = csv.DictWriter(csvfile, fieldnames = fieldNames) 
    #     writer.writeheader() 
    #     writer.writerows(snippetData)

    FileData = []

    Installation = []
    Configuration = []
    MonitorObserve = []
    Security = []
    UpdateMaintain = []

    with open("FileData.csv", 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file) # DictReader maps rows to dictionaries
        for row in csv_reader:
            FileData.append(row)

    with open("FileData.json", 'w', encoding='utf-8') as json_file:
        json.dump(FileData, json_file, indent=4)

    for item in FileData:
        if item["Category"] != "":
            curcat = item["Category"]
            record = {}
            fileName = item["Filename"]
            filePath = item["File Path"]
            record["Title"] = item["Title"]
            link = f"/{filePath}/{fileName}"
            record["Link"] = link
            record["Function"] = item["Function"]
            if curcat == "Configuration":
                Configuration.append(record)
            elif curcat == "Installation":
                Installation.append(record)
            elif curcat == "Monitoring and Observability":
                MonitorObserve.append(record)
            elif curcat == "Security":
                Security.append(record)
            elif curcat == "Updates and Maintenance":
                UpdateMaintain.append(record)


    # print(f"Configuration: {len(Configuration)}")
    # print(f"Installation: {len(Installation)}")
    # print(f"Monitoring & Observabilty: {len(MonitorObserve)}")
    # print(f"Security: {len(Security)}")
    # print(f"Updates & Maintenance: {len(UpdateMaintain)}")

    dashline = "-" * 30
    print("Configuration")
    print(dashline)
    for item in Configuration:
        print(f"{item["Function"]}\t[{item["Title"]}]({item["Link"]})")
    print()
    print("Installation")
    print(dashline)
    for item in Installation:
        print(f"{item["Function"]}\t[{item["Title"]}]({item["Link"]})")
    print()
    print("Monitoring & Observability")
    print(dashline)
    for item in MonitorObserve:
        print(f"{item["Function"]}\t[{item["Title"]}]({item["Link"]})")
    print()
    print("Security")
    print(dashline)
    for item in Security:
        print(f"{item["Function"]}\t[{item["Title"]}]({item["Link"]})")
    print()
    print("Updates & Maintenance")
    print(dashline)
    for item in UpdateMaintain:
        print(f"{item["Function"]}\t[{item["Title"]}]({item["Link"]})")
    print()



def csv_to_table():

    csvfile = "table.tsv"

    tabledata = []
    tablerows = []

    with open(csvfile, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tabledata.append(row)

    # Get the header row from the fieldnames
    header = [col.strip() for col in csv_reader.fieldnames]
    tablerows.append("| " + " | ".join(header) + " |")
    tablerows.append("|" + "---|" * len(header)) # Add separator line

    # Add the data rows
    for row in tabledata:
        row_data = [str(row[col]).strip() for col in header]
        tablerows.append("| " + " | ".join(row_data) + " |")

    md_data = "\n".join(tablerows)

    # | Access control | Serving | Authoring requests to Knative services | serving/istio-authorization.md |

    # # Post proceess 

    # # new_data = []

    # # x = 0
    # for line in tablerows:
    #     # if x > 2:
    #     parts = line.split("\t")
    #     # last = len(parts) - 1
    #     # link = parts[last].rstrip(" |")
    #     # print(link)
    #     # nextlast = last - 1
    #     # title = parts[nextlast]
    #     # print(parts[nextlast])
    #     # col1 = parts[0].lstrip("| ")
    #     col1 = parts[0]
    #     col2 = parts[1]
    #     newline = f"| {col1} | {col2} |"
    #     print(newline)
    #     # print(line)
    #     # x+= 1

    print(md_data)

def csv_to_table_defined():

    csvfile = "tasks.csv"

    tabledata = []
    mdrows = []

    with open(csvfile, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tabledata.append(row)

    for item in tabledata:
        record = {}
        record["Area"] = item["Area"]
        record["Component"] = item["Component"]
        title = item["Task"]
        link = item["File"]
        record["Task"] = f"[{title}]({link})"
        record["Description"] = item["Description"]
        mdrows.append(record)

    for item in mdrows:
        print(f"| {item["Area"]} | {item["Component"]} | {item["Task"]} | {item["Description"]} |")

   

def sniff_yaml():
    filename = "eventing-crds.yaml"

    # FileInfo = {}
    with open(filename, 'r') as mdFile:
        text = mdFile.read()
        pattern = re.compile(r'(?m)^metadata:\n\s*name:\s*(.*)')

        matches = pattern.findall(text)
        for m in matches:
            print(m)

def long_line():

        with open("/Users/BruceHamilton/GitHub/CNCF/Techdocs/Analyses/2026/Flatcar/Analysis.md", 'r') as mdFile:
            lnum = 1
            for line in mdFile:
                if len(line) > 80:
                    print(f"Long line {lnum}")
                lnum += 1

def sniff_file(filename):


    FileInfo = {}

    with open(filename, 'r') as mdFile:

        lnum = 0
        inum = 0
        gnum = 0
        tnum = 0
        audience = ""
        funcTion = ""
        snippet = "No"
        for line in mdFile:
            if line.startswith("audience: "):
                parts = line.split(": ")
                audience = parts[1]
                audience = audience[:-1]
            elif line.startswith("function: "):
                parts = line.split(": ")
                funcTion = parts[1]
                funcTion = funcTion[:-1]
            elif line.startswith("<!-- Snippet"):
                print(line)
                exit()
                snippet = "Yes"
            elif line.startswith("--8"):
                inum += 1
            elif line.startswith("==="):
                tnum += 1
            elif line.startswith("!["):
                gnum += 1

            lnum += 1

    FileInfo["inum"] = str(inum)
    FileInfo["gnum"] = str(gnum)
    FileInfo["tnum"] = str(tnum)
    FileInfo["lnum"] = str(lnum)
    FileInfo["funcTion"] = funcTion
    FileInfo["audience"] = audience
    FileInfo["snippet"] = snippet
    return(FileInfo)
            
        

def ymlToSheet():


    with open('nav.yml', 'r') as file:

        navorder = 0
        navpath = ""
        level = ""
        linkcurrent = ""
        linkprerel = ""
        fpath = ""
        fname = ""
        L1 = ""
        L2 = ""
        L3 = ""
        L4 = ""
        L5 = ""
        L6 = ""
        L7 = ""
        L8 = ""
        L9 = ""
        data_rows = []


        inum = ""
        gnum = ""
        tnum = ""
        lnum = ""
        audience = ""
        funcTion = ""
        snippet = ""
        for line in file:
            if "#" not in line.strip():
                if "- " in line:
                    data_record = []
                    title = ""
                    filepath = ""
                    if ".md" in line:
                        # navrecord = {}
                        # linkitem = {}
                        parts = line.split(":")
                        spacetitle = parts[0]
                        dash_index = spacetitle.find('- ')
                        title = spacetitle[dash_index + 2:]
                        filepath = parts[1].strip()
                        # linkitem[title] = filepath
                        # navrecord[navpath] = linkitem
                        # navdata.append(navrecord)
                        fpath, fname = os.path.split(filepath)
                        fileInfo = sniff_file(f"/Users/Brucehamilton/GitHub/CNCF/Knative/Docs/Docs/Versioned/{fpath}/{fname}")
                        inum = fileInfo["inum"]
                        gnum = fileInfo["gnum"]
                        tnum = fileInfo["tnum"]
                        lnum = fileInfo["lnum"]
                        audience = fileInfo["audience"]
                        funcTion = fileInfo["funcTion"]
                        snippet = fileInfo["snippet"]

                        # Construct the Web links
                        linkcurrent = f"=HYPERLINK(\"https://knative.dev/docs/{fpath}/{fname[:-3]}\", \"Link\")"
                        linkprerel = f"=HYPERLINK(\"https://knative.dev/development/{fpath}/{fname[:-3]}\", \"Link\")"
                    else:
                        dash_index = line.find('-')
                        # Count leading spaces before the dash
                        # indent_level = len(line[:dash_index]) - len(line[:dash_index].lstrip())
                        indent = len(line[:dash_index])
                        head = line[dash_index +2:-2]
                        if indent == 4:
                            L1 = head
                            navpath = L1
                            level = "1"
                        elif indent == 6:
                            L2 = head
                            navpath = f"{L1}/{L2}"
                            level = "2"
                        elif indent == 8:
                            L3 = head
                            navpath = f"{L1}/{L2}/{L3}"
                            level = "3"
                        elif indent == 10:
                            L4 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}"
                            level = "4"
                        elif indent == 12:
                            L5 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}/{L5}"
                            level = "5"
                        elif indent == 14:
                            L6 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}/{L5}/{L6}"
                            level = "6"
                        elif indent == 16:
                            L7 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}/{L5}/{L6}/{L7}"
                            level = "7"
                        elif indent == 18:
                            L8 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}/{L5}/{L6}/{L7}/{L8}"
                            level = "8"
                        elif indent == 20:
                            L9 = head
                            navpath = f"{L1}/{L2}/{L3}/{L4}/{L5}/{L6}/{L7}/{L8}/{L9}"
                            level = "9"
                        elif indent > 20:
                            print("Need more levels!")

                        if level == "":
                            print(f"No level - {indent} - {line}")


                    if navpath != "" and title != "" and linkcurrent != "" and linkprerel != "" and level != "" and fpath != "" and fname != "" and lnum != "" and inum != "" and gnum != "" and tnum != "" and audience != "" and funcTion != "" and snippet != "":
                        navorder += 1
                        nav_order = str(navorder)
                        data_record = [nav_order,navpath,title,linkcurrent, linkprerel,level,fpath,fname,audience,funcTion,str(inum),str(gnum),str(tnum),snippet,str(lnum)]
                        data_rows.append(data_record) 
                    
    print(len(data_rows))

    with open(f"knaive.csv", 'w') as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow(['Nav Order','Nav Path', 'Title', 'Current', 'Prerel', 'Level', 'File Path', 'Filename','Audience','Function','Includes','Graphics','Tabs','Snippet','Lines']) 
        writer.writerows(data_rows)

def findSnippets():



    for dirpath, dirnames, filenames in os.walk("/Users/Brucehamilton/GitHub/CNCF/Knative/docs"):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r') as f:
                        lines = f.readlines()
                        if lines and lines[0].startswith("<!-- Snippet"):
                            usedByPath = ""
                            usedByName = ""
                            snippet_record = {}
                            # <!-- Snippet used in the following topics:
                            # - docs/serving/revisions/revision-admin-config-options.md
                            # - docs/serving/revisions/revision-developer-config-options.md
                            # -->
                            for line in lines:
                                if line != "-->" and line != lines[0]:
                                    if line.startswith("- "):
                                        pathtofile = line[2:]
                                        usedByPath = os.path.dirname(pathtofile)
                                        usedByName = os.path.basename(pathtofile)
                                elif line == "-->":
                                    break
                            snippet_record["Path"] = dirpath.strip()
                            snippet_record["Filename"] = filename.strip()
                            snippet_record["UsedByPath"] = usedByPath.strip()
                            snippet_record["UsedByName"] = usedByName.strip()

                            snippetData.append(snippet_record)

                except Exception as e:
                        print(f"Error reading file {filepath}: {e}")
                        exit()
    
    # print(snippetData)


def remove_comments(input_path, output_path):
    """
    Reads lines from input_path, skips lines that are comments (starting with '#'
    after stripping leading whitespace), and writes the remaining lines to output_path.
    
    Preserves original line endings and any trailing whitespace/newlines.
    """
    with open(input_path, 'r') as infile:
        with open(output_path, 'w') as outfile:
            for line in infile:
                # Strip leading whitespace to check for comment
                if line.lstrip() and not line.lstrip().startswith('#'):
                    outfile.write(line)


def tidyJson():
    data = []
    with open('wordlist.json', 'r') as file:
        data = json.load(file)
    with open("inclusive-word-hits.json", "w") as file:
        json.dump(data, file, indent=4)


def check_inclusive(output_csv=True):
    # Load the JSON file
    with open('inclusive-word-hits.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # The list of words is inside the "data" key
    words = data.get("data", [])
    
    local_path = "/Users/Brucehamilton/GitHub/CNCF/flatcar-website/content/docs"
    
    # Prepare results list for CSV
    results = []
    
    print("Starting scan for inclusive language terms...\n")
    
    for dirpath, dirnames, filenames in os.walk(local_path):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
                
            filepath = os.path.join(dirpath, filename)

            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                for line_num, line in enumerate(lines, 1):
                    linelow = line.lower().strip()
                    if not linelow:  # Skip empty lines
                        continue
                        
                    for word in words:
                        term = word.get("term", "").strip()
                        if not term:
                            continue
                            
                        if term.lower() in linelow:
                            results.append({
                                "term": term,
                                "file": filepath,
                                "line_number": line_num,
                                "line_content": line.strip()
                            })
                            print(f"Found: '{term}' → {filepath}:{line_num}")
    
    # Write results to CSV
    if output_csv and results:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"inclusive_hits_{timestamp}.csv"
        
        fieldnames = ["term", "file", "line_number", "line_content"]
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print(f"\n✅ Scan completed!")
        print(f"Found {len(results)} matches.")
        print(f"Results saved to: {csv_filename}")
    elif not results:
        print("\n✅ Scan completed! No matching terms found.")
    else:
        print(f"\n✅ Scan completed! Found {len(results)} matches.")



def get_headings():
    
        mdFile = open("analysis.md","r")
        for line in mdFile.readlines():
            if line.startswith("#"):
                print(line)

def add_missing_h1_headings():

    local_path = "/home/brucehamilton/github/flatcar-refactor/content/docs/latest"

    updated_files = 0
    skipped_files = 0

    with open("add-h1-headings.csv", 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            filepath = os.path.join(local_path, row["path"])
            meta_title = (row.get("meta-title") or "").strip()
            new_h1 = (row.get("new-h1") or "").strip()

            if not os.path.exists(filepath):
                print(f"File not found: {filepath}. Skipping.")
                skipped_files += 1
                continue

            if not new_h1:
                print(f"No new-h1 found for {filepath}. Skipping.")
                skipped_files += 1
                continue

            with open(filepath, 'r+', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines(keepends=True)

                if not lines or lines[0].strip() != "---":
                    print(f"No front matter delimiter found at top of {filepath}. Skipping.")
                    skipped_files += 1
                    continue

                closing_idx = None
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        closing_idx = i
                        break

                if closing_idx is None:
                    print(f"No closing front matter delimiter found in {filepath}. Skipping.")
                    skipped_files += 1
                    continue

                changed = False

                # Update front matter title when it differs from row["meta-title"].
                if meta_title:
                    title_idx = None
                    for i in range(1, closing_idx):
                        if re.match(r"^\s*title\s*:\s*", lines[i], flags=re.IGNORECASE):
                            title_idx = i

                    if title_idx is not None:
                        current_title = lines[title_idx].split(":", 1)[1].strip().strip('"').strip("'")
                        if current_title != meta_title:
                            lines[title_idx] = f"title: {meta_title}\n"
                            changed = True

                body_start = closing_idx + 1
                body_lines = lines[body_start:]

                # Avoid adding a duplicate H1 if one already exists in the content body.
                first_nonblank_idx = None
                for i, line in enumerate(body_lines):
                    if line.strip():
                        first_nonblank_idx = i
                        break

                has_existing_h1 = (
                    first_nonblank_idx is not None
                    and re.match(r"^#\s+\S", body_lines[first_nonblank_idx].strip()) is not None
                )

                if not has_existing_h1:
                    # Enforce exactly: blank line, H1, blank line, then existing content.
                    while body_lines and body_lines[0].strip() == "":
                        body_lines.pop(0)

                    heading_line = f"# {new_h1}\n"
                    lines = lines[:body_start] + ["\n", heading_line, "\n"] + body_lines
                    changed = True

                if changed:
                    f.seek(0)
                    f.write(''.join(lines))
                    f.truncate()
                    updated_files += 1
                    print(f"Updated: {filepath}")
                else:
                    skipped_files += 1
                    print(f"No changes needed: {filepath}")

    print(f"Completed. Updated: {updated_files}, Skipped: {skipped_files}")
                    

def find_missing_h1_headings():

    local_path = "/home/brucehamilton/github/flatcar-refactor/content/docs/latest/"
    FixData = []
    

    # Construct a data dictionary to add to the list of data
    record = {
        "path": "",
        "filename": "",
        "meta-title": "",
    }

    missing_h1_files = 0

    for dirpath, dirnames, filenames in os.walk(local_path):
        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        found_h1 = False
                        title = ""
                        last_line_num = 0
                        in_code_fence = False

                        for linenum, line in enumerate(lines, 1):
                            last_line_num = linenum
                            stripped = line.strip()

                            if stripped.startswith("```") or stripped.startswith("~~~"):
                                in_code_fence = not in_code_fence
                                continue

                            if in_code_fence:
                                continue

                            if stripped.startswith("title:"):
                                title = line.split(":", 1)[1].strip()
                            # Match Markdown H1 only ("# Heading"), not H2+.
                            elif re.match(r"^#\s+\S", stripped):
                                found_h1 = True
                                break

                        if not found_h1:
                            record["path"] = filepath[64:]  # Adjust this slicing based on your directory structure
                            record["filename"] = filename
                            record["meta-title"] = title
                            FixData.append(record.copy())
                            missing_h1_files += 1
                except Exception as e:
                        print(f"Error reading file {filepath}: {e}")

    
    print(f"Total files missing H1 headings: {missing_h1_files}")
    fieldnames = ["path", "filename", "meta-title"]
    csv_filename = "missing_h1_headings.csv"    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(FixData)

def get_titles_from_h1():
    dirpath = "/home/brucehamilton/github/flatcar-refactor"
    md_files = [
        "debug_virt_stack/debug.md",
        "debug_virt_stack/logging.md",
        "debug_virt_stack/privileged-node-debugging.md",
        "debug_virt_stack/virsh-commands.md",
        "debug_virt_stack/launch-qemu-strace.md",
        "debug_virt_stack/launch-qemu-gdb.md",
    ]

    for filename in md_files:
        filepath = os.path.join(dirpath, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith("# "):
                        title = line[2:].strip()
                        print(f"{title}")
                        break  # usually only want the first H1
        except FileNotFoundError:
            print(f"⚠️  File not found: {filename}")
        except Exception as e:
            print(f"❌ Error reading {filename}: {e}")


def find_Content():
    # List to collect data
    repodata = []

    # Local path to docs
    # local_path = "/Users/Brucehamilton/GitHub/CNCF/flatcar-website/content/docs"
    # local_path = "/Users/BruceHamilton/GitHub/CNCF/KubeVirt/kubevirt.github.io/pages"
    # local_path = "/home/brucehamilton/github/cncf/kubevirt/user-guide/docs"
    local_path = "/home/brucehamilton/github/flatcar-refactor/content/docs"

    
    # Sequence of the enumeration, not needed for spreadsheet
    place = 0
    for dirpath, dirnames, filenames in os.walk(local_path):
        for filename in filenames:
            if not filename.endswith(".md"):
                # only process Markdown files
                continue

            filepath = os.path.join(dirpath, filename)


            # Gets the last portion of the path that reflects the repo

            repopath = os.path.relpath(filepath, local_path)


            pth = Path(repopath)
            lnkparent = pth.parent

            # get the topic (page)
            lnkstem = pth.stem.lower()

            # Construct the link to the topic
            # KubeVirt:
            hyperlink = f"=HYPERLINK(\"https://kubevirt.io/user-guide/{lnkparent}/{lnkstem}\", \"link\")"
            topic_URL = f"https://kubevirt.io/user-guide/{lnkparent}/{lnkstem}"
            
            # Validate the URL
            check_url(topic_URL)                
            place += 1

            # Construct a data dictionary to add to the list of data
            record = {
                "repo": "user-guide",
                "place": str(place),
                "link": hyperlink,
                "path": repopath,
                "title": "",
                "linktitle": "",
                "description": "",
                "weight": "0",
                "snippets": "",
                "lines": "0"
            }

            
            try:
                # Tally the lines of code in the file and collect languages
                codeblocks = []
                with open(filepath, 'r', encoding='utf-8') as f:
                    lnum = 0
                    for line in f:
                        if line.strip().startswith("weight:"):
                            weight = line.split(":", 1)[1].strip()
                            record["weight"] = weight
                        elif line.strip().startswith("linktitle:"):
                            lnktitle = line.split(":", 1)[1].strip()
                            record["linktitle"] = lnktitle
                        elif line.strip().startswith("description:"):
                            descr = line.split(":", 1)[1].strip()
                            if len(descr) > 1:
                             record["description"] = descr
                        elif line.strip().startswith("# "):
                            record["title"] = line[2:].strip()
                            # print(record["title"])
                            # exit()
                        elif line.strip().startswith("```"):
                            fence = line.strip()
                            if (len(fence)) > 3:
                                codename = fence[3:]
                                if codename not in codeblocks:
                                    codeblocks.append(codename)
                        
                        lnum += 1

                    codelist = ""
                    for cb in codeblocks:
                        codelist = codelist + f"{cb} "

                    record["snippets"] = codelist
                    record["lines"] = str(lnum)
                

            except Exception as e:
                print(f"Error reading {filepath}: {e}")
                # don't exit() – just skip
                continue
                
            # Add the record to the list
            repodata.append(record)
            # print(record)   # ← uncomment only when debugging

    print(f"Found {len(repodata)} topics")

    # Write out as an csv
    with open("kubevirt.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['repo', 'place', 'link', 'path', 'title', 'linktitle', 'description', 'weight', 'snippets','lines']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repodata)

def find_configmaps():

    config_maps = []

    for dirpath, dirnames, filenames in os.walk("/Users/Brucehamilton/GitHub/CNCF"):
        for filename in filenames:
            if filename.endswith(".yaml"):
                filepath = os.path.join(dirpath, filename)
                name = ""
                namespace = ""
                record = {}
                with open(filepath, 'r') as yamlFile:
                    # alltext = yamlFile.read()
                    # if "kind: ConfigMap" in alltext:
                    # print("found configMap")
                    for line in yamlFile:
                        if "name: " in line:
                            name_parts = line.split(": ")
                            name = name_parts[1].strip()
                        elif "namespace: " in line:
                            ns_parts = line.split(": ")
                            namespace = ns_parts[1].strip()
                        elif name != "" and namespace != "":
                            record["namespace"] = namespace
                            record["name"] = name
                            # print(f"{record["namespace"]}\t{record["name"]}")
                            config_maps.append(record)

                            break
    for item in config_maps:
        print(f"{item["namespace"]}\t{item["name"]}")
    # with open(f"configmaps.csv", 'w') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(['Namesapce','Name']) 
    #     writer.writerows(config_maps) 

def check_url(url):
    try:
        r = requests.head(url, timeout=8, allow_redirects=True)
        if r.status_code >= 400:
            print(f"Failed: {url} → {r.status_code}")
    except Exception as e:
        print(f"Failed: {url} - {str(e)}")

if __name__ == "__main__":
#     asyncio.run(main())
    tracemalloc.start()  # Optional: Enables memory tracking

    try:
        asyncio.run(main())  # ✅ Works reliably in VS Code
    except RuntimeError as e:
        print(f"RuntimeError detected: {e}")
        print("Attempting to get the running loop...")
        
        loop = asyncio.get_event_loop()
        loop.create_task(main())  # ✅ Safely schedules without stopping existing loops

