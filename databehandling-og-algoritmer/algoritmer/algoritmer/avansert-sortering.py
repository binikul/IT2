personer = [
    {
        "navn": "Ravi",
        "alder": 39
    },

    {
        "navn": "Thor",
        "alder": 33
    },

    {
        "navn": "Ingrid",
        "alder": 21
    }

]


# Sorterer listen med ordbøker (personer) i synkende rekkefølge på nøkkelen alder
# Reverse=True --> synkende rekkefølge
# Reverse=False --> stigende rekkefølge
# Ingen reverse=... --> stigende rekkefølge
sortert_personer = sorted(personer, key=lambda person:person["alder"], reverse = True)
topp_2 = sortert_personer[:2]
print(topp_2)