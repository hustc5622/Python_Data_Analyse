import PyPDF2
import os
with open("/Users/cuijie/Desktop/桌面同步文件/我的课题/实验安排及实验数据/测试数据(原始数据)/液相GC-MS/汇总/700_Report.pdf",'rb')as pdf_file:
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    text=pdf_reader.pages[13].extract_text()
    for i in range(len(text)):
        if text[i:i+len("Compound Name")]=="Compound Name":
            i=i+81
            if text[i]>="0"and text[i]<="9":
                i=i+1
            print(text[i:i+39])
            # flag=0
            # while i<len(text):
            #     if text[i]==" "and text[i+1]!=" ":
            #         flag+=1
            #         if flag==2:
            #             if text[i+2]==" ":
            #                 mass=float(text[i:i+2])
            #             else:
            #                 mass=float(text[i:i+3])
            #             print(mass)
            #         if flag==3:
            #             i=i+1
            #             if text[i+4]==" ":
            #                 #print(text[i:i+4])
            #                 temp=float(text[i:i+4])
            #             else:
            #                 #print(text[i:i+5])
            #                 temp=float(text[i:i+5])
            #         if flag==4:
            #             i=i+1
            #             #print(text[i:i+5])
            #             Proba=float(text[i:i+5])
            #             break
            #     i=i+1