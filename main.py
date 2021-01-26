import smtplib, ssl, csv

# process of opening the connection used from:
#https://realpython.com/python-send-email/?__cf_chl_captcha_tk__=fc6dfa9cde49e73d1f263d8c768491923f0391a4-1607023514-0-AfAvPq1EhfPFL1iLQQPc8541g3mDaKiJMigD2TNzGiMcZhDuPAo8PHSOPN38f1oo9UY0fzK7S8ShLiaMxTEDD46IRDIInKO2nzR7R4RPcacjYkmTc50dbITRobi--VcBcEoLzOJ4COVM2ILTGsIGfcOvLcd3BZlRKE5NeCoECXJUxJgK0ydFMLvFNjB7syL8tMeqRn8EtYsINdte0GqQUnUg84ylII_2odshFZlNidKIlC6_2plnrV1gk90cHZvZUEwnTOWvRVPMAqiVtw59MrTlvsLLd3Qcp0yUoA8cyPJOcHxTjclL97yDW7iD1bt0j8Pr85Im67gNiEE-Mm0ilf4yIzXkQf3_CZ1bLVblLQqxZ8xch1bkeLUTIEUI2s2kLMMvYj8ZZPUG5yXendAD-COe0IoSNXSU3C77wibrdNXGQVpG_C-BEtBj9Lgpkn1W_7dx64c2xdz8OLhOcPzMvM0VWVh_Ps4JIRXvfIAQBavWQp1kNBX22jrIf_TJR2aVEDJsA8TxMdAyv-MV1hS8bnze5Fa3GEYlYA0DdtzXUrm_nIpTuDX9TPAllqKO2jMgUY0Yi7FtX-2fUoqSQ94Bg6mZpHd3X0Y9wUV7DfEBB2qq

port = 465 # for SSl -> Secure Sockets Layer

sender = input("Type your email address: ")
password = input("Type your password: ")
   
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(sender, password)
    except:
        print("ERROR: Invalid email address or password")
    
    try:
        with open('candidateList.txt') as candidateList:
            reader = csv.DictReader(candidateList, delimiter=',') 
            
            for row in reader:
                # if you want to insert more data insert it here --> the name inside the brackets is the name of the column in candidateList.txt
                name = row["name"]
                receiver = row["address"]
                update = row["update"] # update is the reason for writing this email | different .txt files for different updates 
                
                try:
                    with open("updates/" + update + ".txt", encoding='utf-8') as msg:
                        message = f"{msg.read()}".format(**locals()).encode('utf-8')
                        try:
                            server.sendmail(sender, receiver, message)
                        except:
                            print("ERROR: Email could not be sent")
                except:
                    print("FAIL: " + update + ".txt" + " not found")
    except:
        print("FAIL: candidateList.txt not found or missing columns")