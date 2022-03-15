""" UGALOKNIG TAN NARXINI CHIQARUVCHI DASTUR"""
# #     STOLCHA 9LIK TAXTA

# print("Stulchaning o'lchamlarini kiriting!")
# t1,t2 = map(int,(input("90, 45(2 ta o'lcham): ")).split(" "))
# t3,t4 = map(int,(input("57, 63(2 ta o'lcham): ")).split(" "))
# t5,t6 = map(int,(input("45, 26(2 ta o'lcham): ")).split(" "))
# t7 = int(input(" 37(1 ta o'lcham): "))
# n9 = int(input("9lik taxta narx: "))
# m1 = n9/6
# tx = ((t1 * 8)+(t2 * 4)+(t3 * 4)+(t4 * 4)+(t5 * 4)+(t6 * 4)+(t7 * 16))/100
# un = m1 * tx

#         # FIGURALI CHUPLAR
# print("Figurali cho'plar o'lchamlarni kiriing!")
# a108,a68 = map(int,(input("figurali cho'p (108 68) 2ta o'lcham: ")).split(" "))
# a117 = int(input("figurali cho'p(117) 1 ta o'lcham: "))
# a36 = int(input("figurali cho'p (36) 1 ta o'lcham: "))
# s90 = int(input(" 90lik sarga: "))
# arka = (a108+a68+a117+(a36*2)+(2*s90))/100 
# fchnarx = arka*m1


# #     # 6 LIK CHUPLAR
# print("6 lik cho'p o'lchamlarini kiriting!")
# ch108,ch68= map(int,(input("6lik chop(108,68) 2ta olcham: ")).split(" "))
# ch120,ch80= map(int,(input("stol reykasi(120 80) 2 ta o'lcham: ")).split(" "))
# ch36 = int(input("6lik cho'p(36) 1ta o'lcham kiriting: "))
# ch28 = int(input("6lik cho'p (28) 1ta o'lcham kiriting: "))
# unikki = int(input("un ikkilik taxta narxi: "))
# un1mt = unikki/6
# raz6chup = (((ch108+ch68)+(ch120*2)+(ch80*2)+(ch36*6)+(28*3))/100)/2
# umunikinrx = un1mt*raz6chup
# dy1,dy2 = map(int,(input("Dyumovkaning o'lchamlarini kiriting(108,68):  ")).split(" "))
# dyumovka = int(input(" Dyumovkaning narxini kiriting: "))
# dyumnr = dyumovka/6
# dyn = ((dy1 + dy2)/100)*dyumnr

# bur = un+fchnarx+umunikinrx+dyn

# # print(f"Ugalok taxtasining umumiy tannarxi {bur} so'mga teng! \n Shulardan figuralik cho'plarga: {fchnarx} so'm \n6 lik cho'plariga: {umunikinrx} so'mga teng!")          

# print("DSP ning o'lchamlarini kiriting!")
# dsp1,dsp2 =map(int,(input("Stol o'lchami(2 ta o'lcham): ").split(" ")))
# dsp3,dsp4 =map(int,(input("108 o'lchami utirg'ich(2ta o'lcham): ").split(" ")))
# dsp5,dsp6 =map(int,(input("68 o'lchami utirg'ich(2ta o'lcham kiriting): ").split(" ")))
# dsp7,dsp8 =map(int,(input("ugl o'lchami(2ta o'lcham kiriting): ").split(" ")))
# dsp9,dsp10 =map(int,(input("108 spinka o'lchami(2ta o'lcham kiriting): ").split(" ")))
# dsp7,dsp8 =map(int,(input("68 spinka o'lchami(2ta o'lcham kiriting): ").split(" ")))
# dsp7,dsp8 =map(int,(input("pufik o'lchami(2ta o'cham): ").split(" ")))
# dsp9,dsp10 = map(int,input("stulchaning utirg'ichini qo'shing: ").split(" "))
# dspnrx = int(input("Dspning 1kv metr narxi: "))
# dspkv = ((dsp1*dsp2)+ (dsp3*dsp4)+ (dsp5*dsp6)+ (dsp8*dsp7)+ (dsp10*dsp9))/10000
# dspkvmnrx = dspkv*dspnrx
# # print(f"\n\nUgalokga umumiy {dspkv} kvadrat metr dsp ishlatilgan.\nDspning bir kvadrat metri {dspnrx} so'mga teng!\nIshlatilgan dspning umumiy narxi {dspkvmnrx} som'ga teng!\a ")
# print("MDFning o'lchamlarini kiriting!")
# mdf,mdf1 = map(float,input("MDF olchami: ").split(" "))
# mdfnarx = int(input("MDFning narxi: "))
# sandiq1,sandiq2 = map(float,input("Sandiq o'lchamlari(2 ta o'lcham 108_45): ").split(" "))
# sandiq3,sandiq4 = map(float,input("Sandiq o'lchamlari(2 ta o'lcham 68_45): ").split(" "))
# mdf_kv = mdf*mdf1
# mdf_kv_narx = mdfnarx/mdf_kv
# sandiq_kv = (sandiq1*sandiq2)+(sandiq3*sandiq4)
# sandiq_kv_narx = sandiq_kv * mdf_kv_narx
# # print(f"ugalok sandig'ining tagiga ishlatiladigan MDFning narxi{ sandiq_kv_narx} so'ga teng! ")
# print("plastikning o'lchamlarini kiriting!")
# plastik,plastik1 = map(int,input("Plastik listining o'lchamlari(bo'yi, eni):  ").split(" "))
# s_plastik,s_plastik1 = map(int,input("Stol ustiga mo'ljallangan plastik o'lchami(bo'yi, eni):  ").split(" "))
# plastik_narx = int(input("plastikning narxi(so'mda): "))
# plastik_kv = plastik * plastik1
# plastik_kv_narx = plastik_narx / plastik_kv
# stol_plastik_kv = s_plastik * s_plastik1
# stol_plastik_narx = stol_plastik_kv * plastik_kv_narx
# # print(stol_plastik_narx)  # plastik narxi

# # umumiy_tannarx = bur + dspkvmnrx + sandiq_kv_narx + stol_plastik_narx + m_sarfi +g_sarfi + l_sarfi+ r_sarfi+ n_sarfi+k_sarfi+s_sarfi+ q_s_sarfi

# # print(f"ugalokning umumiy tannarxi {umumiy_tannarx} ga teng! ")
# print("Material o'lchami va narxini kiriting!")
# materal = float(input("material metri: "))
# m_narxi = int(input("material narxi: ")) 
# m_sarfi = materal * m_narxi
# # print(f" materiaj {m_sarfi}")
# print("gupkaning soni va narxini kiriting:")
# gupka = float(input("Gubkaning soni: "))
# g_narx = int(input("1 list gupkaning narxi: "))
# g_sarfi = gupka * g_narx
# # print(g_sarfi)

# lak = float(input("Lakning miqdori: "))
# l_narx = int(input("Lakning narxi: "))
# l_sarfi = lak * l_narx
# #print(l_sarfi)

# nlak = float(input("Nitro lak sarfi: "))
# n_narx = int(input("Nitro lak narxi: "))
# n_sarfi = nlak * n_narx
# # print(n_sarfi)

# rastvor = float(input("Rastvoritel sarfi: "))
# r_narx = int(input("Rastvoritel narxi: "))
# r_miqdor = int(input("Rastvoritel miqdori(litrda): "))
# r_litr = r_narx / r_miqdor
# r_sarfi = rastvor * r_litr
# # print(r_sarfi)

# kley = float(input("Kley(PVA) sarfi: "))
# k_narx = int(input("Kleyning(PVA) narxi: "))
# k_sarfi = kley * k_narx
# # print(k_sarfi)

# samorez = float(input("Sariq samorez sarfi: "))
# s_narxi = int(input("Sariq samorezning narxi: "))
# s_sarfi = samorez * s_narxi
# # print(s_sarfi)

# q_samorez = float(input("qora samarez sarfi: "))
# q_s_narxi = int(input("Qora samorez narxi: "))
# q_s_sarfi = q_samorez * q_s_narxi
# # print(q_s_sarfi)

# elektr_e = int(input("Elektrning energiyasining taxminiy miqdori(so'mda): "))

# shukurka = int(input("Shukurkaning taxminiy narxi(so'mda): "))

# oshiq_m = int(input("Oshiq moshiq sarfi: "))
# oshiq_m_n = int(input("Oshiq moshiq narxi: "))
# oshiq_s = oshiq_m * oshiq_m_n


# ish_haq = int(input("Ish haqqi miqdorini kiriting(so'mda): "))


# umumiy_tannarx = bur +oshiq_s +ish_haq+elektr_e + dspkvmnrx + sandiq_kv_narx +ish_haq + stol_plastik_narx + m_sarfi +g_sarfi + l_sarfi+ r_sarfi+ n_sarfi+k_sarfi+s_sarfi+ q_s_sarfi
# print(f"ugalokning umumiy tan narxi {umumiy_tannarx} ga teng! ")


""" IKKI QAVATLI KROVATNING TANNARXINI CHIQARUVCHI DASTUR"""



# tx_1,tx_2 = map(int,input("9lik taxtani o'lchamini kiriting(150,77): ").split(" "))
# tx_9 = int(input("9 lik taxtaning narxini kiriting: "))
# tx_m = tx_9 / 6
# tx_u = ((tx_1 * 4) + (tx_2 * 2))/100
# tx_n = tx_m * tx_u
# """9 lik taxtaning miqdori va narxi"""


# sarga = int(input("sarganing o'lchamini kiriting(190): "))
# rishotka_1,rishotka_2 = map(int,input("Rishotkalarning o'lchamlari(135,85): ").split(" "))
# peremichka = int(input("peremichka (77): "))
# narvon_1,narvon_2 = map(int,input("narvon o'lchamlari(110,45): ").split(" "))
# ruchka = int(input("ruchka o'lchami(38): "))
# un_n = int(input("12 lik taxtaning narxi: "))
# un_m = un_n / 6
# un_miq = ((sarga * 6) + (rishotka_1 + rishotka_2) + (peremichka * 10)+ (narvon_1 + (narvon_2*2)) + (ruchka * 2)) / 100
# un_tan = un_miq * un_m
# """12 lik taxtaning miqdori va narxi"""


# laga = int(input("LagaNING o'lchamlari(80): "))
# laga_n = int(input("Laganing narxi: "))
# laga_m = laga_n / 2.80
# laga_miq = (((laga * 10)/100) / 3) * laga_m 
# """Laganing miqdori va narxi"""


# dvx_dsp_1,dvx_dsp_2 = map(int,input("matras dsp o'lchami(190 80): ").split(" "))
# dsp_n = int(input("Dspning kvadrat metri narxi: "))
# dsp_m = (((dvx_dsp_1 * dvx_dsp_2) * 2) / 10000) * dsp_n
# """DVX dspsining miqdori va narxi"""


# gupka = float(input("Gubkaning soni: "))
# g_narx = int(input("1 list gupkaning narxi: "))
# g_sarfi = gupka * g_narx
# """Gupkaning miqdori va narxi"""



# materal = float(input("material metri: "))
# m_narxi = int(input("material narxi: ")) 
# m_sarfi = materal * m_narxi
# """Material sarfi narxi"""


# lak = float(input("Lakning miqdori: "))
# l_narx = int(input("Lakning narxi: "))
# l_sarfi = lak * l_narx
# """lakning sarfi va narxi"""


# rastvor = float(input("Rastvoritel sarfi: "))
# r_narx = int(input("Rastvoritel narxi: "))
# r_miqdor = int(input("Rastvoritel miqdori(litrda): "))
# r_litr = r_narx / r_miqdor
# r_sarfi = rastvor * r_litr 
# """rastvoritel naxi"""


# kley = float(input("Kley(PVA) sarfi: "))
# k_narx = int(input("Kleyning(PVA) narxi: "))
# k_sarfi = kley * k_narx
# """kleyning miqdori va narxi"""


# samorez = float(input("Sariq samorez sarfi: "))
# s_narxi = int(input("Sariq samorezning narxi: "))
# s_sarfi = samorez * s_narxi
# """samorez miqdori va narxi"""


# elektr_e = int(input("Elektrning energiyasining taxminiy miqdori(so'mda): "))

# shukurka = int(input("Shukurkaning taxminiy narxi(so'mda): "))

# ish_haqi = int(input("ish haqqini kiriting: "))
 
# umumiy_tannarx =  tx_n+un_tan+laga_miq+dsp_m+g_sarfi+m_sarfi+l_sarfi+r_sarfi+k_sarfi+s_sarfi+elektr_e+shukurka+ish_haqi

# print(umumiy_tannarx)
# print(tx_n,un_tan,laga_miq,dsp_m,g_sarfi,m_sarfi,l_sarfi,r_sarfi,k_sarfi,s_sarfi,elektr_e,shukurka,ish_haqi)




"""STOL STULCHANING TAN NARXI"""
t1,t2 = map(int,(input("90, 45(2 ta o'lcham): ")).split(" "))
t3,t4 = map(int,(input("57, 63(2 ta o'lcham): ")).split(" "))
t5,t6 = map(int,(input("45, 26(2 ta o'lcham): ")).split(" "))
t7 = int(input(" 37(1 ta o'lcham): "))
n9 = int(input("9lik taxta narx: "))
m1 = n9/6
tx = ((t1 * 8)+(t2 * 4)+(t3 * 4)+(t4 * 4)+(t5 * 8)+(t6 * 8)+(t7 * 16))/100
un = m1 * tx     # un + sarf+ch_sarf+dsp_sarf


"""figuralik chuplar"""

ch_1 = int(input("figuralik 36(1 ta o'lcham'): "))
s_1 = int(input("stol sarga(1 ta o'lcham: "))

miq_1 = ((ch_1 * 4) + (s_1 * 2))/100
sarf = miq_1 * m1     #sarf


"""6 cho'p"""

chup_1 = int(input("36 cho'p (1 ta o'lcham): "))
chup_2 = int(input("26 cho'p (1 ta o'lcham): ")) 
ch_miq = (((chup_1 * 16) + (chup_2 * 6)) / 100)/2
un_12 = int(input("12 lik taxta narxi: "))
un_m = un_12 / 6
ch_sarf = ch_miq * un_m      #ch_sarf

"""dsp"""
dsp1,dsp2 =map(int,(input("Stol o'lchami(2 ta o'lcham): ").split(" ")))
dsp7,dsp8 =map(int,(input("pufik o'lchami(2ta o'cham): ").split(" ")))
dsp9,dsp10 = map(int,input("stulchaning utirg'ichini qo'shing: ").split(" "))
dsp3,dsp4 = map(int,input("stulcha spinkasi (2ta o'lcham): ").split(" "))
dsp_miq = ((dsp1*dsp2) + (dsp7*dsp8) + (dsp9*dsp10) + (dsp3*dsp4)) /10000
dspnrx = int(input("Dspning 1kv metr narxi: "))
dsp_sarf = dspnrx * dsp_miq     #dsp_sarf

"""plasatik"""

plastik,plastik1 = map(int,input("Plastik listining o'lchamlari(bo'yi, eni):  ").split(" "))
s_plastik,s_plastik1 = map(int,input("Stol ustiga mo'ljallangan plastik o'lchami(bo'yi, eni):  ").split(" "))
plastik_narx = int(input("plastikning narxi(so'mda): "))
plastik_kv = plastik * plastik1
plastik_kv_narx = plastik_narx / plastik_kv       # un + sarf+ch_sarf+dsp_sarf+stol_plastik_narx+m_narxi+
stol_plastik_kv = s_plastik * s_plastik1
stol_plastik_narx = stol_plastik_kv * plastik_kv_narx   #stol_plastik_narx

"""mateial"""

materal = float(input("material metri: "))
m_narxi = int(input("material narxi: ")) 
m_sarfi = materal * m_narxi


"""gupka"""


gupka = float(input("Gubkaning soni: "))
g_narx = int(input("1 list gupkaning narxi: "))
g_sarfi = gupka * g_narx

"""lak"""      # un + sarf+ch_sarf+dsp_sarf+stol_plastik_narx+m_narxi+g_narx+l_sarfi +n_sarfi+r_sarfi+k_sarfi+s_sarfi 

lak = float(input("Lakning miqdori: "))
l_narx = int(input("Lakning narxi: "))
l_sarfi = lak * l_narx

"""nitrolak"""
nlak = float(input("Nitro lak sarfi: "))
n_narx = int(input("Nitro lak narxi: "))
n_sarfi = nlak * n_narx
# print(n_sarfi)

"""rasrtoritel"""
rastvor = float(input("Rastvoritel sarfi: "))
r_narx = int(input("Rastvoritel narxi: "))
r_miqdor = int(input("Rastvoritel miqdori(litrda): "))
r_litr = r_narx / r_miqdor
r_sarfi = rastvor * r_litr
# print(r_sarfi)


"""kley"""
kley = float(input("Kley(PVA) sarfi: "))
k_narx = int(input("Kleyning(PVA) narxi: "))
k_sarfi = kley * k_narx
# print(k_sarfi)

"""samorez"""
samorez = float(input("Sariq samorez sarfi: "))
s_narxi = int(input("Sariq samorezning narxi: "))
s_sarfi = samorez * s_narxi
# print(s_sarfi)

"""qora samorez"""
q_samorez = float(input("qora samarez sarfi: "))
q_s_narxi = int(input("Qora samorez narxi: "))
q_s_sarfi = q_samorez * q_s_narxi
# print(q_s_sarfi)

elektr_e = int(input("Elektrning energiyasining taxminiy miqdori(so'mda): "))

shukurka = int(input("Shukurkaning taxminiy narxi(so'mda): "))

umumiy_tannarx = un + sarf+ch_sarf+dsp_sarf+stol_plastik_narx+m_narxi+g_narx+l_sarfi +n_sarfi+r_sarfi+k_sarfi+s_sarfi +q_s_sarfi+elektr_e+shukurka
print(f"stulchaning tannarxi{umumiy_tannarx}")





