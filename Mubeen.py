import requests,bs4,os,re,time

print("\033[1;37;40m\nThis Script Downloaded the Past Papers for Punjab boards 2ndyear")
print("\033[1;33;40mCreated By Mubeen Ahmad")
print("\033[1;31;40mIf any Problem in this Script than Inform me ")
print("\033[1;36;40mContact me on facebook https://m.facebook.com/SWEETERROR404")
print("\033[1;36;40mAlso Join my Group https://m.facebook.com/groups/sweeterror404/")
print("\033[1;36;40mMy Github link https://github.com/Sweeterror404\n")

board = None
subject = None
folder_name_board = None
folder_name_subject = None
Download_function = None

def searcher(url:str) -> str:
    user_agent = {"Accept-Language": "en-US,en;q=0.5",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    response = requests.get(url,headers=user_agent)
    data = bs4.BeautifulSoup(response.content, "html.parser")
    return data

def select_board() -> str:
    global board,folder_name_board
    lahore = "https://www.pastpapers.pk/12th-class-past-papers-lahore-board"
    gujranwala = "https://www.pastpapers.pk/12th-class-past-papers-gujranwala-board"
    bahawalpur = "https://www.pastpapers.pk/12th-class-past-papers-bahawalpur-board"
    dg_khan = "https://www.pastpapers.pk/12th-class-past-papers-dg-khan-board"
    faisalabad = "https://www.pastpapers.pk/12th-class-past-papers-faisalabad-board"
    multan = "https://www.pastpapers.pk/12th-class-past-papers-multan-board"
    rawalpindi = "https://www.pastpapers.pk/12th-class-past-papers-rawalpindi-board"
    sargodha = "https://www.pastpapers.pk/12th-class-past-papers-sargodha-board"
    sahiwal = "https://www.pastpapers.pk/12th-class-past-papers-sahiwal-board"

    while True:

        user_input = input("\033[1;32;40m    Please Select Board \n\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m1\033[1;31;40m for Lahore\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m2\033[1;31;40m for Gujranwala\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m3\033[1;31;40m for Bahawalpur\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m4\033[1;31;40m for Dg Khan\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m5\033[1;31;40m for Faisalabad\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m6\033[1;31;40m for Multan\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m7\033[1;31;40m for Rawalpindi\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m8\033[1;31;40m for Sargodha\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m9\033[1;31;40m for Sahiwal\t: \033[1;37;40m")

        try:
            if int(user_input) > 9 or int(user_input) < 1:
                print("\n\033[1;32;40m       Wronge Input !\n")
        except ValueError:
            print("\n\033[1;32;40m   Only Numbers are Allowed !\n")

        if user_input == "1":
            board = lahore
            folder_name_board = "Lahore"
            break
        elif user_input == "2":
            board = gujranwala
            folder_name_board = "Gujranwala"
            break
        elif user_input == "3":
            board = bahawalpur
            folder_name_board = "Bahawalpur"
            break
        elif user_input == "4":
            board = dg_khan
            folder_name_board = "Dg_khan"
            break
        elif user_input == "5":
            board = faisalabad
            folder_name_board = "Faisalabad"
            break
        elif user_input == "6":
            board = multan
            folder_name_board = "Multan"
            break
        elif user_input == "7":
            board = rawalpindi
            folder_name_board = "rawalpindi"
            break
        elif user_input == "8":
            board = sargodha
            folder_name_board = "Sargodha"
            break
        elif user_input == "9":
            board = sahiwal
            folder_name_board = "Sahiwal"
            break
    return board

def select_subject() -> str:
    global subject,folder_name_subject
    urdu = "-urdu"
    english="-english"
    computer = "-computer-science"
    math = "-mathematics"
    physic = "-physics"
    pak_study = "-pak-studies"
    chemistry = "-chemistry"
    biology = "-biology"

    while True:
        user_input = input("\n\033[1;32;40m    Please Select Subject\n\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m1\033[1;31;40m for Urdu\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m2\033[1;31;40m for English\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m3\033[1;31;40m for Computer\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m4\033[1;31;40m for Math\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m5\033[1;31;40m for Physic\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m6\033[1;31;40m for Pak Study\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m7\033[1;31;40m for Chemistry\n[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40m8\033[1;31;40m for Biology\t: \033[1;37;40m")
        try:
            if int(user_input) > 8 or int(user_input) < 1:
                print("\n\033[1;32;40m       Wronge Input !\n")
        except ValueError:
            print("\n\033[1;32;40m   Only Numbers are Allowed !\n")

        if user_input == "1":
            subject = urdu
            folder_name_subject = "Urdu"
            break
        elif user_input == "2":
            subject = english
            folder_name_subject = "English"
            break
        elif user_input == "3":
            subject = computer
            folder_name_subject = "Computer"
            break
        elif user_input == "4":
            subject = math
            folder_name_subject = "Math"
            break
        elif user_input == "5":
            subject = physic
            folder_name_subject = "Physic"
            break
        elif user_input == "6":
            subject = pak_study
            folder_name_subject = "Pak_Study"
            break
        elif user_input == "7":
            subject = chemistry
            folder_name_subject = "Chemistry"
            break
        elif user_input == "8":
            subject = biology
            folder_name_subject = "Biology"
            break

    subject = board.replace("-past-papers", subject) + "-past-paper"
    return subject

def remove_logs() -> str:
    for path, y, files in os.walk(f"{folder_name_board}/{folder_name_subject}"):
        for logs in files:
            if logs.find("logs.txt") != -1:
                os.remove(os.path.join(path,logs))

def Download() -> str :
    count = 1

    for path,y,z in sorted(os.walk(f"{folder_name_board}/{folder_name_subject}")):
        for link in z:
            if link.find("link.txt") != -1:
                with open(os.path.join(path,link)) as total_link:
                    length = int(total_link.read())
                    print(f"\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Total Links \033[1;37;40m{length}")

        for files in z:
            if files.find("logs.txt") != -1:
                logs_files = os.path.join(path,files)

                with open(logs_files) as read_text:
                    links = read_text.readlines()

                    for text in links:
                        link = text.replace("\n","")

                        try:
                            pic_link = requests.get(link)

                            if pic_link.status_code == 200:
                                with open(f"{path}/{count}.jpg", 'wb') as f:
                                    f.write(pic_link.content)
                                    print(f"\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Picture \033[1;37;40m{count} \033[1;31;40mDownload in \033[1;32;40m{path}/{count}.jpg \033[1;37;40m{int(length) - count} \033[1;32;40mare Left")
                                    count += 1

                        except requests.exceptions.MissingSchema:

                            print(f"\t\t\033[1;31;40m[\033[1;32;40mx\033[1;31;40m] Error Found Link = \033[1;37;40m{link} \033[1;31;40m[\033[1;32;40mx\033[1;31;40m]")
                            length -= 1

                        with open(f"{path}/Download.txt","a") as download:
                            download.write(text.replace("\n","")+"\n")

                        with open(f"{path}/logs.txt") as change:
                            new = change.read().replace(text.replace("\n",""),"NONE")

                        with open(f"{path}/logs.txt","w") as write_text:
                            write_text.write("")
                            write_text.write(new)

def Extract_Links() -> str:
    print("\n        \033[1;32;40mPlease Wait\n")
    try:
        os.makedirs(f"{folder_name_board}/{folder_name_subject}")
    except:
        pass

    count = 1
    for scrap_link in searcher(subject).find_all("a"):
        link = scrap_link.get("href")
        if str(scrap_link).find("menuBox") != -1:
            for pic_link in searcher("https://www.pastpapers.pk/" + link).find_all("a"):
                pic = pic_link.get("href")
                if str(pic_link).find("li") != -1:
                    for i in searcher("https://www.pastpapers.pk"+pic).find_all("img"):
                        i = str(i)
                        if i.find(".jpg") != -1 and i.find("alt") == -1:

                            final_link = i.replace('<img src="', '').replace('"/>', '')

                            try:
                                year = re.findall(r"[0-9]{4,7}", pic_link.text)[0]

                            except:
                                 pass

                            try:
                                os.mkdir(f"{folder_name_board}/{folder_name_subject}/{year}")
                            except:
                                pass

                            with open(f"{folder_name_board}/{folder_name_subject}/{year}/logs.txt","a") as logs:
                                logs.write(final_link+"\n")

                                print(f"\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Link \033[1;37;40m{count}\033[1;31;40m Save in \033[1;32;40m{folder_name_board}\033[1;36;40m/\033[1;32;40m{folder_name_subject}\033[1;36;40m/\033[1;32;40m{year}\033[1;36;40m/\033[1;32;40mlogs.txt")
                                count += 1

    print(f"\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Total Links \033[1;37;40m{count-1}")
    with open(f"{folder_name_board}/{folder_name_subject}/link.txt" ,"w") as w:
        w.write(str(count-1))
    Download()

def checker() -> str:

    command = 0
    for x,y,files in os.walk(f"{folder_name_board}/{folder_name_subject}"):
        for logs in files:
            if logs.find("logs.txt") != -1:
                command = 1

    if command == 1:
        while True:
            print("\n\033[1;32;40m    Logs files Found !")
            user_input = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40mR\033[1;31;40m for Remove logs files\n\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Press \033[1;37;40mD\033[1;31;40m for Download Picture from logs ").lower()
            if user_input == "r":
                 remove_logs()
                 break
            elif user_input == "d":
                global Download_function
                Download_function  = "call"
                break
            else:
                print("\n      \033[1;32;40mWronge input !")

select_board()
select_subject()
checker()

if Download_function == "call":
    Download()
else:
    Extract_Links()






