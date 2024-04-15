#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path
import os
import shutil
import glob

nam = []
mail = []

source_folder = r"C:\\Users\\abdel\\Desktop\\Python_Workspace\\Mail Merge Project Start\\"
destination_folder = r"C:\\Users\\abdel\\Desktop\\Python_Workspace\\Mail Merge Project Start\\Output\\ReadyToSend\\"
pattern = "\*.txt"

with open("./Input/Letters/starting_letter.txt","r") as text:
    txt = text.read()

    with open("./Input/Names/invited_names.txt","r") as names:
        for name in names:
            x = txt.replace("[name]", name.rstrip())
            nam.append(name.rstrip())
            mail.append(x)
    
    for isem in range (len(nam)):
        with open(f"./Output/ReadyToSend/{nam[isem]}_mail.txt", "w") as mL:
            mL.write(mail[isem])
             
#___________________________________________________

#looking for Files in the sourceFolder which has the path which is saved in source_folder but with the type of the 'pattern' like txt.
# the glob is searche from that type of files
# it initialized it on files, generate like a list      
##files = glob.glob(source_folder + pattern)

#for file in files:

   # file_name = os.path.basename(file)
   # shutil.move(file, destination_folder + file_name)
   # print('Moved: ', file)
