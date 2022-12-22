class mahasiswa:
  def _init_(mahasiswa, nama, umur, semester):
    mahasiswa.nama = nama
    mahasiswa.umur = umur
    
  def _str_(mahasiswa):
    return f"({mahasiswa.nama},{mahasiswa.umur})"    

p1 = ("Nisa",19)
p3 = ("Diana",20)
p4 = ("Dania",22,)
p2 = ("Dirgantara",21)
p5 = ("Aryo",19,)

print(p1,p2,p3,p4,p5)
#outputnya ialah ('Nisa',19)('Dirgantara',21)('Diana',20)('Dania'22)('Aryo'19)