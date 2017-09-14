import threading


def print_quote():
    print "This is my thread!"


def main():

    our_thread = threading.Thread(target = print_quote)
    our_thread.start()
    
    print threading.active_count()   #prints number of threads running
    print threading.enumerate()      #lists out the threads running
    print threading.current_thread() #list out the current thread running

if ( __name__ == "__main__" ):
    main()
