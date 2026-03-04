abo_kg = float(input("Ievadit savu abolu masu kilogramos: "))
abo_eurkg = float(input("Ievadit savu abolu cenu pec vienu kilogramu: "))
cuk_eurkg = float(input("Ievadit savu cukura cenu pec vienu kilogramu: "))

def Masa():
    cuk_kg = abo_kg/2
    iev_kg = (abo_kg+cuk_kg)*0.90
    return cuk_kg, iev_kg

def Preces(cuk_kg):
    abo_cen = abo_kg * abo_eurkg
    cuk_cen = cuk_kg * abo_eurkg
    iev_cen = abo_cen+cuk_cen
    return iev_cen

xy = Masa()
cukura_masa = xy[0]
ievarijuma_masa = xy[1]

Preces(cukura_masa)

print()
