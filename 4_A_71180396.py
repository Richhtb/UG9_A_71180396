print("="*20 , "CAFE","="*20)
print("="*10,"MASUKKAN JUMLAH PESANAN","="*10)
cappucino = int(input("CAPPUCINO\tDISKON 50%\tRp 25.000\t: "))
VanillaLatte = int(input("VANILLA LATTE\tDISKON 65%\tRp 22.000\t: "))
Americano = int(input("AMERICANO\tDISKON 35%\tRp 30.000\t: "))
BrewedCoffee = int(input("BREWED COFFEE\tDISKON 40%\tRp 20.000\t: "))

TotalCapp = (25_000 * cappucino) -( 25_000 * cappucino * 0.5)
TotalVaniLatt= (22_000 * VanillaLatte) - (22_000 * VanillaLatte * 0.65)
TotalAmerican= (30_000 * Americano) - (30_000 * Americano * 0.35)
TotalBrewed = ((20_000 * BrewedCoffee) - (20_000 * BrewedCoffee * 0.4))
totalAll = TotalCapp + TotalVaniLatt + TotalAmerican + TotalBrewed


print("="*10,"TOTAL","="*10)
print(f"TOTAL CAPPUCINO \t: Rp {round(TotalCapp)}")
print(f"TOTAL VANILLA LATTE \t: Rp {round(TotalVaniLatt)}")
print(f"TOTAL AMERICANO \t: Rp {round(TotalAmerican)}")
print(f"TOTAL BREWED COFFEE \t: Rp {round(TotalBrewed)}")
print(f"Jumlah total biaya yang harus dibayar adalah Rp {totalAll}")