import subprocess
import re


class _core_process: #class name

    @staticmethod #class decorator
    def service_info_process_info_child_info(): #class method definition
        #Get-Service
        services=subprocess.check_output(['powershell','Get-Service']).decode('utf-8').split('\n'); #get service running on the system

        #Get-Process
        processes=subprocess.check_output(['powershell','Get-Process']).decode('utf-8').split('\n'); #getall processes runing on the system

        #Get-ChildItem
        child_info=subprocess.check_output(["powershell",r"Get-ChildItem 'C:\Users\chidalu craving' | Select-Object Name,CreationTime,@{Name='Size_In_Kb'; Expression={$_.length/1kb}}"]).decode('utf-8').split('n'); #show child name,creationtime,size in kb
        #    Name     CreationTime     Size_In_Kb
        #    file.txt 02/010/2020      200.200

        #SYSTEMINFO
        systeminfo=subprocess.check_output(['SYSTEMINFO']).decode('utf-8').split('\n'); #get system information

        return services,processes,child_info,systeminfo;



all_core_information=str(_core_process.service_info_process_info_child_info()); #class method call
print(type(all_core_information));

'''pattern=re.compile(r'Syst\w*\W*'); #pattern to search for
matches=pattern.finditer(all_core_information); #search for pattern in all_core_information
for match in matches:
    print(match);'''

print(all_core_information[34561:39000]); #string slicing
