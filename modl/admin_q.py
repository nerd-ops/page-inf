# code by : nerd-ops

import requests
from requests.exceptions import *
from sys import stdout

def process_find(web):
    results = []
    if not web.startswith("http"):
        web = f"http://{web}/"
    admin_list = ['admin', 'administrator', 'webadmin', 'wp-login.php', 'wp-admin.php', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin/login.php', 'admin/login',
	'adminarea', 'admin/index.php', 'memberadmin', 'admin.aspx', 'admin.asp', 'admin.php', 'administrator.php', 'administrator.aspx', 'administrator.asp', 'login.html', 'cpanel',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
	'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
	'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
	'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
	'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
	'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
	'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
	'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
	'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php']
    a = 0
    for i in admin_list:
        try:
            req  = requests.get(f"{web}{i}")
            if req.status_code < 200 or req.status_code <= 201:
                yield f'{web.replace("http://","")}{i}'
            else:
                pass
        except Exception as e:
            yield f"[W] {e}"
            break
