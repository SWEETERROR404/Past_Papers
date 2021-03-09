import requests,bs4,os,re,time

print("This Script Downloaded the Past Papers for Punjab boards 2ndyear")
print("Created By Mubeen Ahmad")
print("If any Problem in this Script than Inform me ")
print("Contect me on facebook https://m.facebook.com/SWEETERROR404")
print("Also Join my Group https://m.facebook.com/groups/sweeterror404/")
print("My Github link https://github.com/Sweeterror404\n")

def searcher(url:str) -> str:
    while True:
        try:
            user_agent = {"Accept-Language": "en-US,en;q=0.5",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
            response = requests.get(url,headers=user_agent)
            data = bs4.BeautifulSoup(response.content, "html.parser")
            return data
        except requests.exceptions.ConnectionError:
            print("Conection Problem\nTrying to Reconnecting")
            time.sleep(2)

board = None
subject = None
folder_name_board = None
folder_name_subject = None

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
        user_input = input("Please Select Board\n[1] Press 1 for Lahore\n[2] Press 2 for Gujranwala\n[3] Press 3 for Bahawalpur\n[4] Press 4 for Dg Khan\n[5] Press 5 for Faisalabad\n[6] Press 6 for Multan\n[7] Press 7 for Rawalpindi\n[8] Press 8 for Sargodha\n[9] Press 9 for Sahiwal \n")
        try:
            if int(user_input) > 9 or int(user_input) < 1:
                print("Wronge Input")
        except ValueError:
            print("Only Numbers are Allowed ")

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
    select_board()
    urdu = "-urdu"
    english="-english"
    computer = "-computer-science"
    math = "-mathematics"
    physic = "-physics"
    pak_study = "-pak-studies"
    chemistry = "-chemistry"
    biology = "-biology"

    while True:
        user_input = input("Please Select Subject\n[1] Press 1 for Urdu\n[2] Press 2 for English\n[3] Press 3 for Computer\n[4] Press 4 for Math\n[5] Press 5 for Physic\n[6] Press 6 for Pak Study\n[7] Press 7 for Chemistry\n[8] Press 8 for Biology ")
        try:
            if int(user_input) > 8 or int(user_input) < 1:
                print("Wronge Input")
        except ValueError:
            print("Only Numbers are Allowed ")

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

def Download():
    select_subject()
    try:
        os.makedirs(f"{folder_name_board}/{folder_name_subject}")
    except:
        pass
    os.chdir(f"{folder_name_board}/{folder_name_subject}")

    count = 1
    for i in searcher(subject).find_all("a"):
        i = str(i)
        if i.find("li") != -1 and i.find(".aspx")== -1:
            start = i.find('href="')+6
            end = i.find('"',start)
            link = 'https://www.pastpapers.pk'+i[start:end]
            year = re.findall(r"[0-9]{4,7}", link)
            try:
                year = year[0]
            except:
                pass

            for i in searcher(link).find_all("img"):
                i = str(i)
                if i.find("https") != -1:
                    x = i.replace("<img src=", "*")
                    if x.find("*") == False:
                        pic = x.replace('"/>', "").replace('*"', "")

                        try:
                            response = requests.get(pic)
                        except requests.exceptions.ConnectionError:
                            pass

                        try:
                            os.mkdir(year)
                        except:
                            pass

                        with open(f"{year}/{count}.jpg", 'wb') as f:
                            f.write(response.content)
                            print(f"{count}\n{pic}\nDownload Sucessfully in {folder_name_board}/{folder_name_subject}/{year}/{count}.jpg")
                        count += 1

Download()
