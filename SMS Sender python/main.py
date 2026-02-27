from twilio.rest import Client
import random

random_msgs = ["Test Message 1", "Test Message 2",
               "Test Message 3", "Test Message 4", "Test Message 5"]

msg_to_send = random.choice(random_msgs)
phone_number_list = ['+91646454468', '+91123646554',
                     '+91955651133', '+91989465469',
                     '+91949849845']

account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

for number in phone_number_list:
    message = client.messages.create(
        body = msg_to_send,  
        from_='+12087958283',  
        to = number  
    )

print(f"Message sent with SID: {message.sid}")
