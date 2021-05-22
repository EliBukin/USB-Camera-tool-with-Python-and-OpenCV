#!/bin/bash 

### this section is for YAML parsing, inspired by https://gist.github.com/pkuczynski/8665367
# include parse_yaml function
. parse-yaml.sh

# read yaml file
eval $(parse_yaml configfile.yaml "config_")

# access yaml content
echo $config_development_percentage
echo $config_development_dest_folder
###

while [ True ]
do
   
#Usage = sh limit_folder_size_size.sh 
#source=("/home/pi/Desktop/dash_cam_1.8.2/dc.config" = the directory to be limited / "$folder_to_limit"=the percentage of the total partition this directory is allowed to use / "1"=the number of files to be deleted every time the script loops (while $Directory_Percentage > $Max_Directory_Percentage) 

  

#Directory to limit 

Watched_Directory=$config_development_dest_folder

echo "Directory to limit="$Watched_Directory 

  

#Percentage of partition this directory is allowed to use 

Max_Directory_Percentage=$config_development_percentage

echo "Percentage of partition this directory is allowed to use="$Max_Directory_Percentage 

  

#Current size of this directory 

Directory_Size=$( du -sk "$Watched_Directory" | cut -f1 ) 

echo "Current size of this directory="$Directory_Size 

  

#Total space of the partition = Used+Available 

Disk_Size=$(( $(df $Watched_Directory | tail -n 1 | awk '{print $3}')+$(df $Watched_Directory | tail -n 1 | awk '{print $4}') ))        

echo "Total space of the partition="$Disk_Size 

  

#Curent percentage used by the directory 

Directory_Percentage=$(echo "scale=2;100*$Directory_Size/$Disk_Size+0.5" | bc | awk '{printf("%d\n",$1 + 0.5)}') 

echo "Curent percentage used by the directory="$Directory_Percentage 

  

#number of files to be deleted every time the script loops (can be set to "1" if you want to be very accurate but the script is slower) 

Number_Files_Deleted_Each_Loop=1

echo "number of files to be deleted every time the script loops="$Number_Files_Deleted_Each_Loop 

  

#While the current percentage is higher than allowed percentage, we delete the oldest files 

while [ $Directory_Percentage -gt $Max_Directory_Percentage ] ; do 

    #we delete the files 

    find $Watched_Directory -type f -printf "%T@ %p\n" | sort -nr | tail -$Number_Files_Deleted_Each_Loop | cut -d' ' -f 2- | xargs rm 

    ##we delete the empty directories 
    #find $Watched_Directory -type d -empty -delete 

    #we re-calculate $Directory_Percentage 

    Directory_Size=$( du -sk "$Watched_Directory" | cut -f1 ) 

    Directory_Percentage=$(echo "scale=2;100*$Directory_Size/$Disk_Size+0.5" | bc | awk '{printf("%d\n",$1 + 0.5)}') 

done 
sleep 300
done 
