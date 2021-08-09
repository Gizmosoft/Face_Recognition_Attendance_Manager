from csv import writer
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def update(name):
    if __name__ == '__update__':
        update(name)

    List = [name, get_current_time(), 'P']

    with open('../database/attendance_report.csv', 'a+', newline='') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        #Close the file object
        f_object.close()



