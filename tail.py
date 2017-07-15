import pandas as pd 

tail = pd.DataFrame(columns = ['Command','NL Queries'])

tail = tail.append({'Command':'tail -c 500 /var/log/messages','NL Queries':['Show last 500 bytes of /var/log/messages.','How do I see ending of /var/log/messages? I want to see only last 500 bytes.']},ignore_index=True)
tail = tail.append({'Command':'tail -f /var/log/secure /var/log/cron','NL Queries':['Show last few lines of /var/log/secure and /var/log/cron.','How do I see ending of /var/log/cron and /var/log/secure?']},ignore_index=True)

print tail


