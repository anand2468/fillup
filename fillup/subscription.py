import time

start_time = 1759206143.3156748
total_seconds = 2592000

def check_sub():
    if (time.time()-start_time > total_seconds):
        return False
    else:
        return True
    
if __name__ == "__main__":
    check_sub()