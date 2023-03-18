import PyPDF2
import argparse
import os
import pandas as pd


def collect_gas(pdf_reader,pdf_name):
    CH4=C2H4=C2H2=CO2=O2=CO=H2=N2=0.0
    name.append(pdf_name)
    page = pdf_reader.pages[1]
    text = page.extract_text()
    for i in range(len(text)):
        if text[i]=="甲":
            if(text[i-12]==" "):
                CH4=float(0)
            else:
                CH4=round(float(text[i-12:i-4]),3)
            _CH4.append(CH4)
        if text[i]=="乙" and text[i+1]=="烯":
            if(text[i-12]==" "):
                C2H4=float(0)
            else:
                C2H4=round(float(text[i-12:i-4]),3)
            _C2H4.append(C2H4)
        if text[i]=="乙" and text[i+1]=="炔":
            if(text[i-12]==" "):
                C2H2=float(0)
            else:
                C2H2=round(float(text[i-12:i-4]),3)
            _C2H2.append(C2H2)
        if text[i]=="C" and text[i+1]=="O" and text[i+2]=="2":
            if(text[i-12]==" "):
                CO2=float(0)
            else:
                CO2=round(float(text[i-12:i-4]),3)
            _CO2.append(CO2)
        if text[i-1]!="C" and text[i]=="O" and text[i+1]=="2":
            if(text[i-12]==" "):
                O2=float(0)
            else:
                O2=round(float(text[i-12:i-4]),3)
            _O2.append(O2)
        if text[i]=="N":
            N2=round(float(text[i-13:i-4]),3)
            _N2.append(N2)
        if text[i]=="C" and text[i+1]=="O" and text[i+2]!="2":
            if(text[i-12]==" "):
                CO=float(0)
            else:
                CO=round(float(text[i-12:i-4]),3)
            _CO.append(CO)
        if text[i]=="H"and text[i+1]=="2"and text[i+2]!="S":
            if(text[i-12]==" "):
                H2=float(0)
            else:
                H2=round(float(text[i-12:i-4]),3)
            _H2.append(H2)
            break
def parse_args():
    parser = argparse.ArgumentParser(description='Process PDF files')
    parser.add_argument('directory',help='Path to directory containing PDF files')
    return parser.parse_args()

def process_pdf_file(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        i=-1
        for i in range(-1,-15,-1):
            if pdf_file_path[i]=="/":
                break
        if pdf_file_path[i+1]=="G":
            i+=1
        pdf_name=pdf_file_path[i+1:-4]
        collect_gas(pdf_reader,pdf_name)

def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(directory_path, filename)
            try:
                process_pdf_file(pdf_file_path)
            except:
                print(pdf_file_path)



if __name__ == '__main__':
    name=[]
    _CH4=[]
    _C2H4=[]
    _C2H2=[]
    _CO2=[]
    _O2=[]
    _CO=[]
    _H2=[]
    _N2=[]
    args = parse_args()
    process_directory(args.directory)
    print(_H2)
    ans=pd.DataFrame({"组名":name,"CH4":_CH4,"C2H4":_C2H4,"C2H2":_C2H2,"CO2":_CO2,"O2":_O2,"N2":_N2,"CO":_CO,"H2":_H2})
    print(ans)
    path_to_excel=os.path.join(args.directory,"collect.xlsx")
    ans.to_excel(path_to_excel)