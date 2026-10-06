correos = ["correoMalo", "otro@malo", "uno@bueno.si", "otro@tal.vez", "casi.bueno"]
print(
    list(filter(
        lambda c: c.find("@")!=-1 
            and c.find(".", c.find("@")) != -1, correos
    ))
)