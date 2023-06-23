from helpers import filedialog,saveDirectory
from colorama import Fore, just_fix_windows_console,init
from pathlib import Path
import subprocess
import os
import gnupg


# Fix colors not showing on CMD
just_fix_windows_console()
init(autoreset=True)

# Check if GPG is installed
check_exist = subprocess.run(["gpg" ,"--version"],stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True,text=True)


if check_exist.returncode == 0:
    
    # Initialize GPG    
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    
    # Get userID of existing public keys
    keys = gpg.list_keys()
    keys_userid = [key["uids"][0].split(" ")[0] for key in keys]
    
    
    # Print script banner
    print("-----------------------------------------------")
    print(Fore.CYAN+"    GPG AUTOMATOR")
    print(Fore.CYAN+"           version:v0.1.0-beta1")
    print(Fore.CYAN+"           Source: www.github.com/LunaOzma")
    print("-----------------------------------------------")
    
    # Prompt 1
    prompt1 = input("\n1. Import Keys\n2. Encrypt data\n> ")
    
    # Import public keys
    if prompt1 == "1":
        
        to_import = filedialog()   
        for key in to_import:
            print("------------------------------------------------")
            print("Key: "+Fore.YELLOW+key)
            print(Fore.YELLOW+"\n> importing key...")
            import_result = gpg.import_keys_file(key)
            
            print(Fore.GREEN+"> Imported key successfully") 
            print("------------------------------------------------")          

    # Encrypt a message
    elif prompt1 == "2":
        
        # Prompt 2
        prompt2 = input("\n1. Generate data\n2. Select a file\n> ")
        
        # Enter text manually and encrypt it
        if prompt2 == "1":
            
            print("> Enter/Paste your text. Ctrl-D or Ctrl-Z (Windows) to save it.")
            text = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                text.append(line)
              
            text = "\n".join(text)    
            # print(text)

            # Prompt user for recipients
            while True:    
                recipients = input("\nRecipients names (r1, r2,..):\n> ")
                recipients = recipients.strip().split(",")
                
                valid = [recipient for recipient in recipients if recipient in keys_userid]
                if len(recipients) == len(valid):
                    break
                else:
                    print(Fore.RED+"> Error: Some recipients you entered don't exist!, try again!")
                    
                    
            
            # Prompt user for output directory
            outdir = input("\nOutput directory:\n1.Current directory\n2.Select directory\n")
            if outdir == "1":
                save_directory = os.getcwd()
            elif outdir == "2":    
                save_directory = saveDirectory()
            
            
            # Encrypt text for each recipient          
            for recipient in recipients:

                print("------------------------------------------------")

                outputfile = str(Path((save_directory,input("Enter output filename:"))))
                print ('\033[1A' +"output file: "+Fore.YELLOW+outputfile+ '\033[K')
                print("recipients: "+Fore.YELLOW+recipient)
                print(Fore.YELLOW+"\n> encrypting... ")
                encrypted_ascii_data = gpg.encrypt(text , recipient,always_trust=True,output=outputfile,extra_args=['--yes'],armor=True)
                print(Fore.GREEN+"> encrypted message successfully!")
                
                print("------------------------------------------------")
        
        # Select a file and encrypt it
        elif prompt2 == "2":    
                       
            to_encrypt = filedialog()

            # Prompt user for recipients
            while True:    
                recipients = input("\nRecipients names (r1, r2,..):\n> ")
                recipients = recipients.strip().split(",")
                
                valid = [recipient for recipient in recipients if recipient in keys_userid]
                if len(recipients) == len(valid):
                    break
                else:
                    print(Fore.RED+"> Error: Some recipients you entered don't exist!, try again!")
                       
            
            outdir = input("\nOutput directory:\n1.Current directory\n2.Select directory\n")
            if outdir == "1":
                save_directory = os.getcwd()
            elif outdir == "2":    
                save_directory = saveDirectory()
            

            name_format = input("\nOutput filename format:\n1.filename_recipient.sig\n2.Enter filename manually\n> ")
            

            
            for inputfile in to_encrypt:                
                for recipient in recipients:

                    inputfile = str(Path(inputfile))
                    print("------------------------------------------------")
                    print("input file: "+Fore.YELLOW+inputfile)

                    if name_format == "1":
                        outputfile = str(Path(save_directory,os.path.basename(inputfile)+"_"+recipient+".sig")) 
                        print("output file: "+Fore.YELLOW+outputfile)
                    elif  name_format == "2":
                        outputfile = str(Path(save_directory,input("Enter output filename:")))
                        print ('\033[1A' +"output file: "+Fore.YELLOW+outputfile+ '\033[K')

                    print("recipients: "+Fore.YELLOW+recipient)
                    print(Fore.YELLOW+"\n> encrypting... ")

                    encrypted_ascii_data = gpg.encrypt_file(inputfile , recipient,always_trust=True,output=outputfile,extra_args=['--yes'],armor=True)
                    
                    print(Fore.GREEN+"> encrypted file successfully!")
                    print("------------------------------------------------")


else:
    print("GPG is not installed")
        

