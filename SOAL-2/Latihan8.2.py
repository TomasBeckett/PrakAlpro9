# LATIHAN 8.2

pertanyaan = []  

with open('SOAL-2/soal.txt', 'r') as file:
    for line in file:
        soal, jawab = line.strip().split('||')
        pertanyaan.append((soal.strip(), jawab.strip()))  

total_pertanyaan = len(pertanyaan)  

for i in range(total_pertanyaan):
    soal, jawab = pertanyaan[i]
    print(f"{soal}")
    jawab_user = input("Jawab: ").strip()

    if jawab_user.lower() == jawab.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah")

