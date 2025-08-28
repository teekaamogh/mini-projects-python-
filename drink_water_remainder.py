#Drink water remainder

from datetime import datetime
import  time
from plyer import notification
import winsound

#To input number of remainders per day
number_of_remainders=int(input("Enter the number of remainders per day:"))
start_remainder=int(input("Enter the start time of remainder (in 24 hour format):"))
end_remainder=int(input("Enter the end time of remainder (in 24 hour format):"))

#To get current time
current_hour=datetime.now().hour


if current_hour<start_remainder:
  print(f"Its too early, remainder starts at {start_remainder}:00")
elif current_hour>=end_remainder:
  print(f"Too late, remainder ended at {end_remainder}:00")
else:
  remaining_hours = end_remainder - current_hour
  interval=(remaining_hours*3600)/number_of_remainders

  if current_hour>=start_remainder and current_hour<end_remainder:
    for i in range(0,number_of_remainders):
      notification.notify(title="Drink water remainder",message="please stay hydrated",app_icon="water-bottle.ico",timeout=10)
      winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
      time.sleep(interval)            
 

