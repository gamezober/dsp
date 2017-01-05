import csv

def main():
    fac = csv.reader(open("faculty.csv"))

    email_file = open("emails.csv", 'w+')

    emails = [i[3] for i in fac]

    for i in emails:
        email_file.write(i + '\n')

    email_file.close()

if __name__ == '__main__':
    main()
