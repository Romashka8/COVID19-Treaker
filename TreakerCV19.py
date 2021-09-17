from COVID19Py import *
from colorama import *

init()


def set_country_code():
    print(Fore.YELLOW + "Input your country code: ")
    ucc = input()
    return ucc


def last_changes():
    changes = covid19.getLatestChanges()

    for i in changes:
        if i == 'confirmed':
            print(Fore.BLUE + i, changes[i])
        elif i == 'deaths':
            print(Fore.RED + i, changes[i])
        else:
            print(Fore.GREEN + i, changes[i])


def country_statistic(ucc):
    location = covid19.getLocationByCountryCode(ucc)
    inf = location[0]
    j = inf['latest']
    cn = inf['country']  # название страны
    cp = inf['country_population']  # население страны
    print('Country: ', cn)
    print('Population: ', cp)

    for i in j:
        if i == 'confirmed':
            print(Fore.BLUE + i, j[i])
        elif i == 'deaths':
            print(Fore.RED + i, j[i])
        else:
            print(Fore.GREEN + i, j[i])


covid19 = COVID19()
run = True
print(
    Fore.WHITE + "Hi, this app show you COVID19 statistic for the last time(below all word statistic for the last time).")
latest = covid19.getLatest()

for i in latest:
    if i == 'confirmed':
        print(Fore.BLUE + i, latest[i])
    elif i == 'deaths':
        print(Fore.RED + i, latest[i])
    else:
        print(Fore.GREEN + i, latest[i])
print(Fore.WHITE + "First of all, input country code(RU,US - for example) of country, that statistic you want to see.")

while run:
    ucc = set_country_code()
    if ucc != "Last changes" and ucc != "Exit":
        country_statistic(ucc)
    elif ucc == "Last changes":
        last_changes()
    elif ucc == "Exit":
        run = False
        break
