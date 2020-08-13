import sys
from uri import uri
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        prblem_line=event.src_path.replace('./problems\\','')
        print(f"Found {prblem_line}")
        wbsite,problem= prblem_line.split()
        prblm, lang=problem.split('.')
        if wbsite=="uri":
            with open('uri.txt','r') as f:
                user,pwd=f.readline().split()
            print("Starting the browser ")
            a= uri(user,pwd)
            print("log into uri website")
            a.login()
            print("start Submiting the problem")
            a.submit(prblm)
            print("getting the result of the submission")
            a.lasttry()
            
        

if __name__ == "__main__":
    path = './problems'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()