from apscheduler.schedulers.background import BackgroundScheduler
import sensors.dht11 as dht11

def init():    
    print('Background Job: Initializing.')
    sched = BackgroundScheduler()
    sched.add_job(dht11.read_sensor, 'interval', minutes=1)
    sched.start()
    print('Background Job: Initialized.')
