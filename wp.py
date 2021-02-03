# dataset type = {"whatsapp number with country code":"amount to be pay"}

pending_dues = {"+918888888888":"10", "+918888888888":"10"} # place ',' after each dataset

def get_current_time():
	import datetime
	current_time_hour = datetime.datetime.now().hour
	current_time_minute = datetime.datetime.now().minute
	return current_time_hour,current_time_minute

def minute_check(current_time_hour, current_time_minute):
	current_time_minute += 2
	if current_time_minute >=60:
		current_time_minute = current_time_minute - 60
		current_time_hour +=1
		if current_time_hour == 24:
			current_time_hour = 00
	return current_time_hour, current_time_minute


current_time_hour, current_time_minute=get_current_time()
current_time_hour, current_time_minute=minute_check(current_time_hour, current_time_minute)
import pywhatkit	
for number, amount in pending_dues.items():
	amount_message = "Hello dear, It's a gentle reminder that you have pending due of Rs."+amount+"/-. \nYou can pay through 'contribute' section through our app."
	pywhatkit.sendwhatmsg(number,amount_message,current_time_hour,current_time_minute)
	current_time_hour, current_time_minute=minute_check(current_time_hour, current_time_minute)
