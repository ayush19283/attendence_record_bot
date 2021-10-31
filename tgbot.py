from telethon import TelegramClient,events,sync
import psycopg2
from telethon.sessions import StringSession
from telethon import utils
##real_id, peer_type = utils.resolve_id
api_id=8925256
api_hash='d3a68074d2204bb004ca255cd009d337'
str_sess='1BVtsOJgBu52QxyQPugSCETjHw-5YUvM6RB4mviNcpDEV3e0n0MW6aDlCgvi__m7DzL-lSESXjRK_OB_9l31rQ5n1uqhsoPbdXIij5uXiPRGvrH38g45e-Hd6a2WHvZUJjWORU7KowKpUzFSYhC1tBPjwyAFd7bSR0n2EvhxXhC-tPyB7Vv0V9TxBzdVl_3EjLzkPrIfQPGgQcRKTiXcSMiygXJqacx5MSftCqacc_uriHK7qHdat9fF81LMQKlQCmN_7WMTrKkSh2BgJAqMzxINCpc5WVqnjZl69MuLu7yVeRF0_x_LWAWXKoboIM1Z8vI0Cr-SGjVNzAV5pCFU1fiDcpfQie7Y='
client = TelegramClient(StringSession(str_sess), api_id, api_hash)
conn = psycopg2.connect(database="d3ekcujj7lq6fc", user = "rqzgbqclathhzp", password = "65267788f7c2a21a536f469ae11870ff33324d515f4fc6e1fa784a99ac0f39ce", host = "ec2-3-217-91-165.compute-1.amazonaws.com", port = "5432")
cur = conn.cursor()

##peer = peer_type(real_id)
client.start()
 
@client.on(events.NewMessage)
async def handler(event):
     sender = await event.get_sender()
     #cur.execute(f"INSERT INTO ATTENDENCE (ID,TD,PD) VALUES ({sender.id},0,0)")
     s=sender.id
     cur.execute("select id from attendence")
     temp1=[i[0] for i in cur.fetchall()]
     #print(temp1)
     if sender.id not in temp1:
          cur.execute(f"INSERT INTO ATTENDENCE (ID,TD,PD) VALUES ({sender.id},0,0)")
          conn.commit()
     
     #print(sender.id)    
     if event.raw_text=='/absent':
         cur.execute(f"SELECT TD FROM ATTENDENCE WHERE ID = {s}")
         td=cur.fetchall()
         cur.execute(f"UPDATE ATTENDENCE set TD = {td[0][0]+1} where ID = {s}")
         conn.commit()
     if event.raw_text=='/present':
         cur.execute(f"SELECT TD,PD FROM ATTENDENCE WHERE ID = {s}")
         td=cur.fetchall()
         cur.execute(f"UPDATE ATTENDENCE set TD = {td[0][0]+1} where ID = {s}")
         cur.execute(f"UPDATE ATTENDENCE set PD = {td[0][1]+1} where ID = {s}")
         conn.commit()
     if event.raw_text=='/show':
          cur.execute(f"SELECT TD,PD FROM ATTENDENCE WHERE ID = {s}")
          temp=cur.fetchall()
          print(temp)
          c=str(temp)
          await event.reply(c)
          
        # rows = cur.fetchall()
        

##         for row in rows:
##             if sender.id==row[0]:
##                 print("total days = ", row[1])
##                 print("present days = ",row[2])
##     conn.close()
         
     #await client.send_message(event.sender_id, 'Hi')
##     sender=await event.get_sender()
##     print(sender.id)
####       
  #  """Echo the user message."""
    #await event.respond(event.text)
#client.get_messages()

        
    
client.start()
client.run_until_disconnected()

