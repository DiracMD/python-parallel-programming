import multiprocessing 
def foo(i):
    print("process: %s" %i)

if __name__=="__main__":
    Process_jobs=[]
    for i in range(5):
        p=multiprocessing.Process(target=foo,args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
