def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 zankova")
        return 
    
    veliko_slovo = any(x.isupper() for x in lozinka)
    ima_broj = any(x.isdigit() for x in lozinka)
    if not (veliko_slovo and ima_broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    
    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return
    
    print("Lozinka je jaka!")

lozinka = input("Unesite lozinku: ")
provjera_lozinke(lozinka)
 