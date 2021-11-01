import vk_api
import datetime
import time

   
vk = vk_api.VkApi(token="9528d2c4b073a781640aae4604cbb37143274fe43f96f2f33d0b058a268f0c14e567e4ea723826968083e")
session=vk.get_api()


while True:
    t =500+(datetime.datetime(2021, 7, 21,0,0)-datetime.datetime.now()).days
    print(t)
    oldStatus = vk.method("status.get",{ "user_id" : 416973121 } )['text']
    print("old status ="+ oldStatus)
    newStatus=f"Осталось: {t}"
    print("new status= "+ newStatus)
    if(newStatus<oldStatus):
        vk.method("status.set",{'text': newStatus})
        print("Changes complited")
    else: 
        print("iteration complited")
        time.sleep(5)


    
   
    
