                                                           #"FILE ORGANIZER MINI PROJECT BASED ON FILE EXTENTIONS"
                                                          


#in this project we import these two modules as it is in below,in which all the necessary funtions are defined which are needed to build this mini project
import os
import shutil
#to take input directory to organize
initialdir = input("enter the directory which you want to organize:")
#to check the directory path exists or not
if os.path.exists(initialdir)and os.path.isdir(initialdir):
 print("the process will proceed")
else:
    print(" please enter the valid directory")
#to get the list of all files which are present inside the input directory    
filelist = os.listdir(initialdir)
print(filelist)
#categories list contains different file type and their different extentions
categories = {'images':['.jpg','.jpeg','.png','.gif','.JPG'],'documents':['.pdf','docx','.txt'],'videos':['.mp4','.mkv','.avi'],'audio':['.mp3','.wav'],'text_file':['.txt'],'lnkapp':['.lnk']}
for category in categories.keys():
    #to create particular directories inside input directory to move the specific type of files 
     destination_directory = os.path.join(initialdir,category)
     #next step is to check if the path that is the specific file which is to moved is already exists or not,if not exists then to create new one
     if  os.path.exists(destination_directory):
         print(f"directory already exists:{destination_directory}")
     else:
         os.mkdir(destination_directory)
         print(f"destination directory created are :{destination_directory}")
#to create a file path for files which are inside the input directory
for file in filelist:
    file_path = os.path.join(initialdir,file)
    #to check if it is file or not 
    if os.path.isfile(file_path):     
        #to check if file extention matches with the extentions inside the category
         for category,extensions in categories.items():
             if  os.path.splitext(file)[1].lower()  in extensions:
               #if it matches then move to particular category file created earliar 
              shutil.move(file_path,os.path.join(initialdir,category,file))
              print(f"moving {file_path} to {os.path.join(initialdir,category,file)}")
              break
             

#this mini projects has some limitations as i am a beginner and i tried to build my own mini project and will definetly make next project which can handle complex situations
#thank you for reading my code
         
    
         

         
