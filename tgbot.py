from telethon import TelegramClient,events,sync
import psycopg2
from telethon.sessions import StringSession
from telethon import utils
import os
##real_id, peer_type = utils.resolve_id
api_id=os.environ.get('api_id')
api_hash=os.environ.get('api_hash')
str_sess=os.environ.get('str_sess')
client = TelegramClient(StringSession(str_sess), api_id, api_hash)
conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
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
     if event.raw_text=='/reset':
          cur.execute(f"DELETE FROM ATTENDENCE WHERE ID = {s}")
          conn.commit()
          
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

