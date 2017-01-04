import webbrowser,multiprocessing,subprocess,time

def __run__():
	subprocess.Popen("python run.py",shell=True)

def __start__():
	time.sleep(2)
	webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
	multiprocessing.freeze_support()
	p1 = multiprocessing.Process(target=__run__)
	p2 = multiprocessing.Process(target=__start__)
	p1.start()
	p2.start()
	p1.join()
	p2.join()