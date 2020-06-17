import pickle
import re

def main():
    user_name = input('mail>')
    password = input('password>')
    user_data = [user_name,password]
    while True:
        print("Enter execution time(format hh:mm)")
        time = input('execution time>')
        if time[0] == "0":
            if len(time) > 3:
                time = time.lstrip('0')
        if not re.match(r'[0-9]{,2}:[0-9]{2}',time):
            print("[+]Your input is ininvalid")
        else:
            break
    data = {
        "time":time,
        "user":user_data
    }
    try:
        with open('config.txt',mode='ab') as f:
            pickle.dump(data,f)
        print('[+]Create config file')
        print('[+]Setup successful')
    except:
        print('[-]Create config file')
        print('[-]Failed setup')
    exit()
if __name__ == "__main__":
    main()