import PyPDF2
import argparse
import os
import pandas as pd
Name=["Benzene","Toluene","Ethylbenzene",
      "Phenylethyne","Styrene","Naphthalene",
      "Benzaldehyde","Phenol","p-Xylene","Cyclohexane",
      "Methyl Isobutyl Ketone"]
Mass=[78,92,106,
      102,104,128,
      106,94,106,84,
      100
      ]
Name_CH=["苯","甲苯","乙苯","苯乙炔","苯乙烯","萘",
         "苯甲醛","苯酚","二甲基苯","苯","4-甲基-2-戊酮"]

def collect_liquid(pdf_file,pdf_name):
    Area=[0,0,0,0,0,0,0,0,0,0,0]
    name.append(pdf_name)
    pages=len(pdf_file.pages)
    for pg in range(pages):
        text=pdf_file.pages[pg].extract_text()
        for i in range(len(text)):
            if text[i:i+len("Compound Name")]=="Compound Name":
                i+=81
                if text[i]>="0"and text[i]<="9":
                    i=i+1
                Proba=0
                for cp in range(len(Name)):
                    if(text[i:i+len(Name[cp])]==Name[cp]) and text[i+len(Name[cp])]==" ":
                        # print(Name[cp])
                        # print(pg)
                        i+=len(Name[cp])
                        flag=0
                        temp=0
                        while i<len(text):
                            if text[i]==" "and text[i+1]!=" ":
                                flag+=1
                                if flag==2:
                                    i=i+1
                                    if text[i+2]==" ":
                                        mass=float(text[i:i+2])
                                    else:
                                        mass=float(text[i:i+3])
                                    # print(mass)
                                    if mass!=Mass[cp]:
                                        break
                                if flag==3:
                                    i=i+1
                                    if text[i+4]==" ":
                                        #print(text[i:i+4])
                                        temp=float(text[i:i+4])
                                    else:
                                        #print(text[i:i+5])
                                        temp=float(text[i:i+5])
                                if flag==4:
                                    i=i+1
                                    #print(text[i:i+5])
                                    Proba=float(text[i:i+5])
                                    break
                            i=i+1
                        if Proba>=39 and Area[cp]!=temp:
                            Area[cp]+=temp
                        break
    Area[0]+=Area[-2]
    for j in range(9):
        Class[j].append(Area[j])
    _CP10.append(Area[10])
    #print(Area)
def parse_args():
    parser = argparse.ArgumentParser(description='Process PDF files')
    parser.add_argument('directory',help='Path to directory containing PDF files')
    return parser.parse_args()

def process_pdf_file(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        i=-1
        for i in range(-11,-24,-1):
            if pdf_file_path[i]=="/":
                break
        if pdf_file_path[i+1]=="L":
            i+=1
        pdf_name=pdf_file_path[i+1:-11]
        collect_liquid(pdf_reader,pdf_name)

def process_directory(directory_path):
    sucess=int(0)
    fail=int(0)
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(directory_path, filename)
            try:
                process_pdf_file(pdf_file_path)
                sucess+=1
            except:
                print(pdf_file_path)
                fail+=1
    print("成功",sucess,"个文件\n","失败",fail,"个文件")
        
    



if __name__ == '__main__':
    name=[]
    _CP0=[]
    _CP1=[]
    _CP2=[]
    _CP3=[]
    _CP4=[]
    _CP5=[]
    _CP6=[]
    _CP7=[]
    _CP8=[]
    _CP10=[]
    Class=[_CP0,_CP1,_CP2,_CP3,_CP4,_CP5,_CP6,_CP7,_CP8,_CP10]
    args = parse_args()
    process_directory(args.directory)
    ans=pd.DataFrame({"组名":name,Name_CH[0]:_CP0,
                      Name_CH[1]:_CP1,Name_CH[2]:_CP2,Name_CH[3]:_CP3,
                      Name_CH[4]:_CP4,Name_CH[5]:_CP5,Name_CH[6]:_CP6,
                      Name_CH[7]:_CP7,Name_CH[8]:_CP8,Name_CH[10]:_CP10,})
    #print(ans)
    path_to_excel=os.path.join(args.directory,"collect.xlsx")
    ans.to_excel(path_to_excel)