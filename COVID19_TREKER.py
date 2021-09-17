from COVID19Py import *


def country_code():
    run = True
    while run:
        ucc = input("Input your country code: ")  # user country code
        try:
            covid19.getLocationByCountryCode(ucc)
            run = False
            return ucc
            break
        except HTTPError:
            print("Your country code does not exist!")
            continue


def set_country_code():
    ucc = input("Input your country code: ")
    return ucc


def show_all_word_statistic():
    data = covid19.getAll()
    for i in data:
        print(i)


def country_statistic(ucc):
    location = covid19.getLocationByCountryCode(ucc)
    # print(location['deaths'])
    for i in location:
        print(i)


def last_changes():
    changes = covid19.getLatestChanges()
    for i in changes:
        print(i, changes[i])


covid19 = COVID19()
run = True
print("Hi, this app show you COVID19 statistic for the last time(below all word statistic).")
latest = covid19.getLatest()
for i in latest:
    print(i, latest[i])
print("First of all, input country code(RU,US - for example) of country, that statistic you want to see.")
while run:
    ucc = set_country_code()
    if ucc != "All word" and ucc != "Last changes" and ucc != "Exit":
        country_statistic(ucc)
    elif ucc == "Last changes":
        last_changes()
    elif ucc == "Exit":
        run = False
        break
