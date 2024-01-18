areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("El primer element es",areas_pis[0],areas_pis[1])

print("L'ultim element es", areas_pis[-2],areas_pis[-1])

index_terrassa = areas_pis.index("Terrassa")
print("Larea de la terrassa es",areas_pis[index_terrassa + 1])

print("El primer,segon y tercer element son", areas_pis[:6])

print("Imprimir del tercer a l'utlim element", areas_pis[4:])

index_habitacio1 = areas_pis.index("Habitació1")
index_habitacio2 = areas_pis.index("Habitació2")
total_area_habitacions = areas_pis[index_habitacio1 + 1] + areas_pis[index_habitacio2 + 1]
print("El total de l'àrea  de les habitacions 1 i 2 són:", total_area_habitacions)

index_lavabo = areas_pis.index("Lavabo")
areas_pis[index_lavabo + 1] = 8.5
print("La nova llista area amb el lavabo modificat es:", areas_pis)

areas_pis.extend(["Pati interior", 2.78])
print("La llista d'àrees amb Pati interior afegit es:", areas_pis)

# Imprimir el total de l’àrea del pis.
total_area_pis = sum(areas_pis[1::2])
print("L'area total del pis es:", total_area_pis)
