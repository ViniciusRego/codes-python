def process_services():
    men_services = {"corte": 0, "barba": 0}
    women_services = {"corte": 0, "penteado": 0, "maquiagem": 0}
    total_revenue = 0.0

    while True:
        sex = input().lower()
        if sex != "m" and sex != "f":
            break

        service = input().lower()

        if sex == "m":
            if service == "corte":
                men_services["corte"] += 1
                total_revenue += 25.00
            elif service == "barba":
                men_services["barba"] += 1
                total_revenue += 15.00
        elif sex == "f":
            if service == "corte":
                women_services["corte"] += 1
                total_revenue += 40.00
            elif service == "penteado":
                women_services["penteado"] += 1
                total_revenue += 50.00
            elif service == "maquiagem":
                women_services["maquiagem"] += 1
                total_revenue += 70.00

    men_max_service = max(men_services, key=men_services.get)
    men_max_count = men_services[men_max_service]

    if men_max_count == 0 or men_services["corte"] == men_services["barba"]:
        most_used_service = "AMBOS"
    else:
        most_used_service = men_max_service.upper()

    return most_used_service, total_revenue


# Processa os serviços e obtém o resultado
most_used_service, total_revenue = process_services()

# Imprime o serviço mais usado pelos homens e o faturamento total
print(most_used_service)
print(f"{total_revenue:.2f}")
