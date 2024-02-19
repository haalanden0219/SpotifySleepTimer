#https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
import psutil #provides interface for retrieving information
import time
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter(): #iterating through lists of prunning processes
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): #checks for 3 cases in which there could be an issue
            pass
    return False


def getPid(process_name):
    pids = []
    for process in psutil.process_iter(['pid' , 'name']):
        if process.info['name'] == process_name:
             pids.append(process.info['pid'])
    return pids

def terminate_process(pids):
    for pid in pids:
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Process with PID {pid} terminated successfully.")
        except psutil.NoSuchProcess as e:
         print(f"Error: Process with PID {pid} not found.")
        except psutil.AccessDenied as e:
            print(f"Error: Access denied. You may not have permission to terminate the process.")
        except Exception as e:
         print(f"Error: {e}")

print("Spotify Sleep Timer")
print()


time.sleep(1)

wait_time = float(input("Enter how many minutes before termination: "))

print("Wait Time: ", wait_time , "minutes")
print()


process_name = "Spotify.exe"

pid = getPid(process_name)

if pid:
    print(f"The process ID of {process_name} is: {pid}")
else:
    print(f"No running process found with the name {process_name}")

if checkIfProcessRunning('Spotify'):
    print('Spotify is currently running and awaiting its execution') #if spotify is found 
else:
    print('Spotify is not detected as running') #if spotify is not found.
    exit() #exit out

time.sleep(wait_time *60) #change back to 60
terminate_process(pid)


if checkIfProcessRunning('Spotify'):
    print('Spotify is currently running and -- failed execution') #if spotify is found 
else:
    print('Spotify is not detected as running -- terminated successfully') #if spotify is not found.
    exit() #exit out

    #I need to find a way to delete the process and then verify its deletion.
    #I want to add more text this time to show if there are errors and show which step it is at.
    #I need to get and store the PID so I can use it to close down each detection of spotify.
    #Have an option that lets you see the process id for spotify.

    #why does spotify have like 8 different processes?
    #how do I find them all and close them at once

    #when I close the process it just creats a new one, how do I fix this?
    #what order is the process reading it in