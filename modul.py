import sys
from urllib2 import *
from time import *
from random import *
from subprocess import *
from hashlib import *
#importing
finder = [
	"admin",
	"admin.php",
	"admin.html",
	"admin1.php",
	"admin1.html",
	"admin2.php",
	"admin2.html",
	"login",
	"login.php",
	"login.html",
	"yonetim.php",
	"yonetim.html",
	"yonetici.php",
	"yonetici.html",
	"ccms/",
	"ccms/login.php",
	"ccms/index.php",
	"maintenance/",
	"webmaster/",
	"adm/",
	"configuration/",
	"configure/",
	"websvn/",
	"admin/",
	"admin/account.asp",
	"admin/account.html",
	"admin/account.php",
	"admin/add_banner.php/",
	"admin/addblog.php",
	"admin/add_gallery_image.php",
	"admin/add.php",
	"admin/add-room.php",
	"admin/add-slider.php",
	"admin/add_testimonials.php",
	"admin/admin/",
	"administrator",
	"admin/adminarea.php",
	"admin/admin.asp",
	"admin/AdminDashboard.php",
	"admin/admin-home.php",
	"admin/AdminHome.php",
	"admin/admin.html",
	"admin/admin_index.php",
	"admin/admin_login.asp",
	"admin/admin-login.asp",
	"admin/adminLogin.asp",
	"admin/admin_login.html",
	"admin/admin-login.html",
	"admin/adminLogin.html",
	"admin/admin_login.php",
	"admin/admin-login.php",
	"admin/adminLogin.php",
	"admin/admin_management.php",
	"admin/admin.php",
	"admin/admin_users.php",
	"admin/adminview.php",
	"admin/adm.php",
	"admin_area/",
	"adminarea/",
	"admin_area/admin.asp",
	"adminarea/admin.asp",
	"admin_area/admin.html",
	"adminarea/admin.html",
	"admin_area/admin.php",
	"adminarea/admin.php",
	"admin_area/index.asp",
	"adminarea/index.asp",
	"admin_area/index.html",
	"adminarea/index.html",
	"admin_area/index.php",
	"adminarea/index.php",
	"admin_area/login.asp",
	"adminarea/login.asp",
	"admin_area/login.html",
	"adminarea/login.html",
	"admin_area/login.php",
	"adminarea/login.php",
	"admin.asp",
	"admin/banner.php",
	"admin/banners_report.php",
	"admin/category.php",
	"admin/change_gallery.php",
	"admin/checklogin.php",
	"admin/configration.php",
	"admincontrol.asp",
	"admincontrol.html",
	"admincontrol/login.asp",
	"admincontrol/login.html",
	"admincontrol/login.php",
	"admin/control_pages/admin_home.php",
	"admin/controlpanel.asp",
	"admin/controlpanel.html",
	"admin/controlpanel.php",
	"admincontrol.php",
	"admincontrol.php/",
	"admin/cpanel.php",
	"admin/cp.asp",
	"admin/CPhome.php",
	"admin/cp.html",
	"admincp/index.asp",
	"admincp/index.html",
	"admincp/login.asp",
	"admin/cp.php",
	"admin/dashboard/index.php",
	"admin/dashboard.php",
	"admin/dashbord.php",
	"admin/dash.php",
	"admin/default.php",
	"adm/index.asp",
	"adm/index.html",
	"adm/index.php",
	"admin/enter.php",
	"admin/event.php",
	"admin/form.php",
	"admin/gallery.php",
	"admin/headline.php",
	"admin/home.asp",
	"admin/home.html",
	"admin_home.php",
	"admin/home.php",
	"admin.html",
	"admin/index.asp",
	"admin/index-digital.php",
	"admin/index.html",
	"admin/index.php",
	"admin/index_ref.php",
	"admin/initialadmin.php",
	"admin.php",
	"admin.html",
	"admin/cp.php",
	"admin/cp.html",
	"cp.php",
	"cp.html",
	"administrator/",
	"administrator/index.html",
	"administrator/index.php",
	"administrator/login.html",
	"administrator/login.php",
	"administrator/account.html",
	"administrator/account.php",
	"administrator.php",
	"administrator.html",
	"login.php",
	"login.html",
	"modelsearch/login.php",
	"moderator.php",
	"moderator.html",
	"moderator/login.php",
	"moderator/login.html",
	"moderator/admin.php",
	"moderator/admin.html",
	"moderator/",
	"account.php",
	"account.html",
	"controlpanel/",
	"controlpanel.php",
	"controlpanel.html",
	"admincontrol.php",
	"admincontrol.html",
	"adminpanel.php",
	"adminpanel.html",
	"admin1.asp",
	"admin2.asp",
	"yonetim.asp",
	"yonetici.asp",
	"admin/account.asp",
	"admin/index.asp",
	"admin/login.asp",
	"admin/home.asp",
	"admin/controlpanel.asp",
	"admin.asp",
	"admin/cp.asp",
	"cp.asp",
	"administrator/index.asp",
	"administrator/login.asp",
	"administrator/account.asp",
	"administrator.asp",
	"login.asp",
	"modelsearch/login.asp",
	"moderator.asp",
	"moderator/login.asp",
	"moderator/admin.asp",
	"account.asp",
	"controlpanel.asp",
	"admincontrol.asp",
	"adminpanel.asp",
	"fileadmin/",
	"fileadmin.php",
	"fileadmin.asp",
	"fileadmin.html",
	"administration/",
	"administration.php",
	"administration.html",
	"sysadmin.php",
	"sysadmin.html",
	"phpmyadmin/",
	"myadmin/",
	"sysadmin.asp",
	"sysadmin/",
	"ur-admin.asp",
	"ur-admin.php",
	"ur-admin.html",
	"ur-admin/",
	"Server.php",
	"Server.html",
	"Server.asp",
	"Server/",
	"wp-admin/",
	"administr8.php",
	"administr8.html",
	"administr8/",
	"administr8.asp",
	"webadmin/",
	"webadmin.php",
	"webadmin.asp",
	"webadmin.html",
	"administratie/",
	"admins/",
	"admins.php",
	"admins.asp",
	"admins.html",
	"administrivia/",
	"Database_Administration/",
	"WebAdmin/",
	"useradmin/",
	"sysadmins/",
	"admin1/",
	"system-administration/",
	"administrators/",
	"pgadmin/",
	"directadmin/",
	"staradmin/",
	"ServerAdministrator/",
	"SysAdmin/",
	"administer/",
	"LiveUser_Admin/",
	"sys-admin/",
	"typo3/",
	"panel/",
	"cpanel/",
	"cPanel/",
	"cpanel_file/",
	"platz_login/",
	"rcLogin/",
	"blogindex/",
	"formslogin/",
	"autologin/",
	"support_login/",
	"meta_login/",
	"manuallogin/",
	"simpleLogin/",
	"loginflat/",
	"utility_login/",
	"showlogin/",
	"memlogin/",
	"members/",
	"login-redirect/",
	"sub-login/",
	"wp-login/",
	"login1/",
	"dir-login/",
	"login_db/",
	"xlogin/",
	"smblogin/",
	"customer_login/",
	"UserLogin/",
	"login-us/",
	"acct_login/",
	"admin_area/",
	"bigadmin/",
	"project-admins/",
	"phppgadmin/",
	"pureadmin/",
	"sql-admin/",
	"radmind/",
	"openvpnadmin/",
	"wizmysqladmin/",
	"vadmind/",
	"ezsqliteadmin/",
	"hpwebjetadmin/",
	"newsadmin/",
	"adminpro/",
	"Lotus_Domino_Admin/",
	"bbadmin/",
	"vmailadmin/",
	"Indy_admin/",
	"ccp14admin/",
	"irc-macadmin/",
	"banneradmin/",
	"sshadmin/",
	"phpldapadmin/",
	"macadmin/",
	"administratoraccounts/",
	"admin4_account/",
	"admin4_colon/",
	"radmind-1/",
	"Super-Admin/",
	"AdminTools/",
	"cmsadmin/",
	"SysAdmin2/",
	"globes_admin/",
	"cadmins/",
	"phpSQLiteAdmin/",
	"navSiteAdmin/",
	"server_admin_small/",
	"logo_sysadmin/",
	"server/",
	"database_administration/",
	"power_user/",
	"system_administration/",
	"ss_vms_admin_sm/",
	"admins",
	"mail",
	"adm",
	"party",
	"admin",
	"administration",
	"administrator",
	"administrators",
	"database",
	"admin.php",
	"admin.asp",
	"administrator.php",
	"administrator.asp",
	"administrators.asp",
	"administrators.asp",
	"login.php",
	"login.asp",
	"logon.asp",
	"logon.php",
	"quanly.asp",
	"quanly.php",
	"quantri.php",
	"quantri.asp",
	"quantriweb.asp",
	"quantriweb.asp",
	"admin_index.asp",
	"admin_index.php",
	"password.asp",
	"password.php",
	"dangnhap.asp",
	"dangnhap.php",
	"user.php",
	"user.asp",
	"phpinfo.",
	"logs.",
	"log.",
	"adminwww",
	"db.",
	"Readme.",
	"urllist.",
	"admin_file",
	"admin_files",
	"admin_login",
	"cpg",
	"inc_lib",
	"inc_conf",
	"inc_config",
	"lib_config",
	"login",
	"logon",
	"forum",
	"forums",
	"diendan",
	"restricted",
	"forum1",
	"forum2",
	"forum3",
	"diendan1",
	"diendan2",
	"foto",
	"diendan3",
	"php",
	"phpbb",
	"awstats",
	"test",
	"img-sys",
	"cgi-sys",
	"java-sys",
	"php-sys",
	"adserver",
	"login-sys",
	"admin-sys",
	"community",
	"cgi-sys/mchat.",
	"demo",
	"download",
	"temp",
	"tmp",
	"ibf",
	"ipb",
	"vbb",
	"vbb1",
	"vbb2",
	"adminp",
	"vbb3",
	"README",
	"INSTALL",
	"install",
	"docs",
	"document",
	"documents",
	"DOC",
	"CHANGELOG",
	"guest",
	"phpMyAdmin",
	"phpbb1",
	"phpbb2",
	"phpBB",
	"phpBB2",
	"PHPBB",
	"hackconkec",
	"12931293",
	"secret",
	"root",
	"cgi-bin",
	"files",
	"scripts",
	"nobody",
	"home",
	"manager",
	"manage",
	"live",
	"exec",
	"livehelp",
	"livechat",
	"chat",
	"phplive",
	"php.",
	"ko",
	"khong",
	"khongdungnua",
	"kodungnua",
	"vut",
	"cuc",
	"cut",
	"db",
	"data",
	"site",
	"cgi",
	"taolao",
	"class",
	"online",
	"common",
	"shop",
	"shopadmin",
	"thesun",
	"news",
	"store",
	"text",
	"source",
	"sources",
	"control",
	"controls",
	"console",
	"cp",
	"admincp",
	"web",
	"modules",
	"_admin",
	"_admin_file",
	"admin_site",
	"_login",
	"pages",
	"access",
	"password",
	"pwd",
	"pass",
	"user",
	"users",
	"_users",
	"admin_user",
	"admin_users",
	"content",
	"cart",
	"carts",
	"cc",
	"paypal",
	"cvv",
	"cvv2",
	"main1",
	"main",
	"webalizer",
	"widgets",
	"acc",
	"accounts",
	"achive",
	"nhanvien",
	"domain",
	"gallerry",
	"mysql",
	"order",
	"orders",
	"4rum",
	"photo",
	"phpmyadmin",
	"share",
	"save",
	"help",
	"admin_",
	"login_",
	"webmaster"
	]
m = "\033[91m"
g = "\033[92m"
k = "\033[93m"
b = "\033[94m"
u = "\033[95m"
bm = "\033[96m"
p = "\033[97m"
r = "\033[0m"
def run(edan):
		for yopie in edan + "\n":
			sys.stdout.write(yopie)
			sys.stdout.flush()
			sleep(8. /90)
lilo_gila = raw_input("siapa namamu: ")
lilo_edan = call("clear", shell = True)
lilo_stres = lilo_edan,run(g+'''
			assallamualaikum.wr.wb :)
			'''
			+"hay "+lilo_gila+'''
			welcome to my tools:v
			you jenius and me noob jahat :(''')
rdm = randint(0,100000009)
im3 = choice([62855,62814,62815,62816,62856,62857,62858])
three = choice([62895,62896,62897,62898,62899])
xl = choice([62817,62818,62819,62859,62877,62878])
telkomsel = choice([62811,62812,62813,62822,62821,62823,62852,62851,62853])
smartfren = choice([62881,62882,62883,62884,62885,62886,62887,62888,62889])
exis = choice([62838,62831,62832,62833])
eks1 = "%s%s"%(im3,rdm)
eks2 = three+rdm
eks3 = xl+rdm
eks4 = telkomsel+rdm
eks5 = smartfren+rdm
eks6 = exis+rdm
def wa():
		call("clear", shell = True)
		print "[1].im3\n[2].three\n[3].xl\n[4].telkomsel\n[5].smartfren\n[6].exis\n"
		pilih = raw_input("enter your choice: ")
		pilih2 = input("butuh berapa nomer?: ")
		if pilih or pilih2 is True:
			if pilih == '1':
				sys.stdout.write(" mencari nomor whatsapp im3...\r")
				sys.stdout.flush()
				if pilih.startswith("https://") is False:
					link = "api.whatsapp.com/send?phone="+ str(eks1) +"&text=ping:)"
					rizqi = "https://" + link
				for i in range(1,pilih2):
					target = rizqi
					try:
						yop = Request(target)
						buka = urlopen(yop)
						sleep(1.5)
						print g + "ADA" + k + " => " + r + target
					except URLError,HTTPError:
						print m + "TIDAK ADA" + k + " => " + r + target
					except KeyboardInterrupt:
						pilih()
		else:
		 	 print "belum memasukan pilihan bos!"
		 	 pilih()
		 	 
def hashing():
		call("clear", shell = True)
		print "\nhashing md5 by Mr.w0n63d4n\ntesting script\n"
		print "\nsilahkan pilih jenis hash\n\n[1].md5\n[2].SHA1\n[3].SHA224\n[4].SHA256\n[5].SHA384\n[6].SHA512\n"
		susu = raw_input("pilih salah satu: ")
		if susu == '1' or susu == 'satu':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = md5()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		if susu == '2' or susu == 'dua':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = sha1()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		if susu == '3' or susu == 'tiga':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = sha224()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		if susu == '4' or susu == 'empat':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = sha256()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		if susu == '5' or susu == 'lima':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = sha384()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		if susu == '6' or susu == 'enam':
			try:
				ceck = raw_input("masukan yang mau dihash: ")
				hasin = sha512()
				hasil = hasin.update(ceck)
				hajar = hasin.hexdigest()
				joni = "hasil hashing "+k+"=> "+u+hajar+g
				sleep(0.5)
				print joni
				sleep(0.5)
				print ""
			except KeyboardInterrupt:
				pilih()
		else:
			print "bila suka jangan lupa kasih bintang digithub saya :D"
			pass
    