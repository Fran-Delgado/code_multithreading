import threading
import datetime

def print_x2(num):
    for num in range(1000):
        print("x^2: {}".format(num ^2))
def print_x3(num):
    for num in range(1000):
        print("x^3: {}".format(num ^3))
def print_x4(num):
    for num in range(1000):
        print("x^4: {}".format(num ^4))
def print_x5(num):
    for num in range(1000):
        print("x^5: {}".format(num ^5))
def print_x6(num):
    for num in range(1000):
        print("x^6: {}".format(num ^6))
def print_x7(num):
    for num in range(1000):
        print("x^7: {}".format(num ^7))
def print_x8(num):
    for num in range(1000):
        print("x^8: {}".format(num ^8))
def print_x9(num):
    for num in range(1000):
        print("x^9: {}".format(num ^9))


def target_hilos(print_x2,
                 print_x3, 
                 print_x4, 
                 print_x5, 
                 print_x6, 
                 print_x7,
                 print_x8,
                 print_x9):
    t1 = threading.Thread(target=print_x2, args=(1,))
    t2 = threading.Thread(target=print_x3, args=(1,))
    t3 = threading.Thread(target=print_x4, args=(1,))
    t4 = threading.Thread(target=print_x5, args=(1,))
    t5 = threading.Thread(target=print_x6, args=(1,))
    t6 = threading.Thread(target=print_x7, args=(1,))
    t7 = threading.Thread(target=print_x8, args=(1,))
    t8 = threading.Thread(target=print_x9, args=(1,))
    
    return t1,t2,t3,t4,t5,t6,t7,t8  
 
def start_hilos(t1,
                t2,
                t3,
                t4,
                t5,
                t6,
                t7,
                t8):
    time_ini_hilo_1 = datetime.datetime.now()
    t1.start()
    time_ini_hilo_2 = datetime.datetime.now()
    t2.start()
    time_ini_hilo_3 = datetime.datetime.now()
    t3.start()
    time_ini_hilo_4 = datetime.datetime.now()
    t4.start()
    time_ini_hilo_5 = datetime.datetime.now()
    t5.start()
    time_ini_hilo_6 = datetime.datetime.now()
    t6.start()
    time_ini_hilo_7 = datetime.datetime.now()
    t7.start()
    time_ini_hilo_8 = datetime.datetime.now()
    t8.start()

    return time_ini_hilo_1,time_ini_hilo_2,time_ini_hilo_3,time_ini_hilo_4,time_ini_hilo_5,time_ini_hilo_6,time_ini_hilo_7,time_ini_hilo_8

def join_hilos(t1,
               t2,
               t3,
               t4,
               t5,
               t6,
               t7,
               t8):
    t1.join()
    time_fin_hilo_1 = datetime.datetime.now()
    t2.join()
    time_fin_hilo_2 = datetime.datetime.now()
    t3.join()
    time_fin_hilo_3 = datetime.datetime.now()
    t4.join()
    time_fin_hilo_4 = datetime.datetime.now()
    t5.join()
    time_fin_hilo_5 = datetime.datetime.now()
    t6.join()
    time_fin_hilo_6 = datetime.datetime.now()
    t7.join()
    time_fin_hilo_7 = datetime.datetime.now()
    t8.join()
    time_fin_hilo_8 = datetime.datetime.now()
    return time_fin_hilo_1,time_fin_hilo_2,time_fin_hilo_3,time_fin_hilo_4,time_fin_hilo_5,time_fin_hilo_6,time_fin_hilo_7,time_fin_hilo_8

def print_duracion(time_ini_hilo_1, 
                   time_ini_hilo_2, 
                   time_ini_hilo_3, 
                   time_ini_hilo_4,
                   time_ini_hilo_5,
                   time_ini_hilo_6,
                   time_ini_hilo_7,
                   time_ini_hilo_8,
                   time_fin_hilo_1, 
                   time_fin_hilo_2, 
                   time_fin_hilo_3, 
                   time_fin_hilo_4, 
                   time_fin_hilo_5, 
                   time_fin_hilo_6, 
                   time_fin_hilo_7, 
                   time_fin_hilo_8): 
    print(f" Duración del proceso hilo 1 = {time_fin_hilo_1 - time_ini_hilo_1}")
    print(f" Duración del proceso hilo 2 = {time_fin_hilo_2 - time_ini_hilo_2}")
    print(f" Duración del proceso hilo 3 = {time_fin_hilo_3 - time_ini_hilo_3}")
    print(f" Duración del proceso hilo 4 = {time_fin_hilo_4 - time_ini_hilo_4}")
    print(f" Duración del proceso hilo 5 = {time_fin_hilo_5 - time_ini_hilo_5}")
    print(f" Duración del proceso hilo 6 = {time_fin_hilo_6 - time_ini_hilo_6}")
    print(f" Duración del proceso hilo 7 = {time_fin_hilo_7 - time_ini_hilo_7}")
    print(f" Duración del proceso hilo 8 = {time_fin_hilo_8 - time_ini_hilo_8}")

if __name__ == "__main__":
    t1, t2, t3, t4, t5, t6, t7, t8 = target_hilos(print_x2,
                                                  print_x3, 
                                                  print_x4, 
                                                  print_x5, 
                                                  print_x6, 
                                                  print_x7, 
                                                  print_x8, 
                                                  print_x9)
    time_ini_hilo_1, time_ini_hilo_2, time_ini_hilo_3, time_ini_hilo_4, time_ini_hilo_5, time_ini_hilo_6, time_ini_hilo_7, time_ini_hilo_8 = start_hilos(t1,
                                                                                                                                                         t2,
                                                                                                                                                         t3,
                                                                                                                                                         t4,
                                                                                                                                                         t5,
                                                                                                                                                         t6,
                                                                                                                                                         t7,
                                                                                                                                                         t8)
    time_fin_hilo_1, time_fin_hilo_2, time_fin_hilo_3, time_fin_hilo_4, time_fin_hilo_5, time_fin_hilo_6, time_fin_hilo_7, time_fin_hilo_8 = join_hilos(t1,
                                                                                                                                                        t2,
                                                                                                                                                        t3,
                                                                                                                                                        t4,
                                                                                                                                                        t5,
                                                                                                                                                        t6,
                                                                                                                                                        t7,
                                                                                                                                                        t8)
    print_duracion(time_ini_hilo_1, 
                   time_ini_hilo_2, 
                   time_ini_hilo_3, 
                   time_ini_hilo_4,
                   time_ini_hilo_5,
                   time_ini_hilo_6,
                   time_ini_hilo_7,
                   time_ini_hilo_8,
                   time_fin_hilo_1, 
                   time_fin_hilo_2, 
                   time_fin_hilo_3, 
                   time_fin_hilo_4, 
                   time_fin_hilo_5, 
                   time_fin_hilo_6, 
                   time_fin_hilo_7, 
                   time_fin_hilo_8)
    
    print("Done!")
