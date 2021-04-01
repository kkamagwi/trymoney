trata = 0


def podschet(day):
    global trata
    trata += day

podschet(17)
podschet(20)
podschet(21)
print(trata)


def podschet2(*trata1):
    for day in trata1:
        day += day
    return day

print(podschet2(56, 14, 17, 56))
