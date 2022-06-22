import pprint

data = [
  {
    'nama': "Matematika",
    'harga': 30000,
  },
  {
    'nama': "Bahasa Inggris",
    'harga': 200000,
  },
  {
    'nama': "Kimia",
    'harga': 250000,
  },
  {
    'nama': "Bahasa Jawa",
    'harga': 150000,
  },
  {
    'nama': "Bahasa Jerman",
    'harga': 175000,
  },
  {
    'nama': "Fisika",
    'harga': 225000,
  },
  {
    'nama': "Biologi",
    'harga': 100000,
  },
  {
    'nama': "Bahasa Mandarin",
    'harga': 150000,
  },
  {
    'nama': "Geografi",
    'harga': 75000,
  },
  {
    'nama': "Ekonomi",
    'harga': 85000,
  },
  {
    'nama': "Bahasa Arab",
    'harga': 125000,
  },
  {
    'nama': "Sastra Indonesia",
    'harga': 275000,
  }
]

def bubble_sort(data):
    # membuat nested for untuk membandingkan 2 harga awal yang ada
    for i in range(0, len(data)):
        for j in range(1, len(data) - i - 1):
            if data[j]['harga'] > data[j + 1]['harga']:
                #  menyimpan object berharga terbesar awal pada variabel "temp"
                temp = data[j]
                # menukar data pada object sekarang ke object selanjutnya
                data[j] = data[j + 1]
                data[j + 1] = temp

pprint.pprint(data)
bubble_sort(data)
print('\n')
pprint.pprint(data)