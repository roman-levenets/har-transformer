from locust import HttpUser, task, events, between, LoadTestShape
import gevent
import json
import greenlet
import random
from datetime import datetime, timedelta
import math


class LoadTestScenario(HttpUser):
    wait_time = between(1, 5)
    test_data = {}
    v_user_list = dict()
    current_v_user_row = int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.client.auth = ('test-user', 'test-password')

    @events.init.add_listener
    def on_locust_init(environment, **kwargs):
        LoadTestScenario.load_test_data()

    @task
    def test_task(self):
        v_user_id = greenlet.getcurrent().minimal_ident

        max_v_user_row = max(LoadTestScenario.v_user_list.values(), default=-1)
        LoadTestScenario.v_user_list[v_user_id] = max_v_user_row + 1
        self.current_v_user_row = LoadTestScenario.v_user_list[v_user_id]

        self.execute_local_requests()
        self.execute_remote_requests()

    def execute_local_requests(self):
        self.client.get('/search?source=hp&ei=SwxoW9akCsLGkwWmuonwBQ&q=har+file&oq=har+file&gs_l=psy-ab.3..0l10.3193.3930.0.4082.8.8.0.0.0.0.77.543.8.8.0....0...1.1.64.psy-ab..0.8.541....0.oZrZVD2aUIo')
        self.client.get('/')
        self.client.get('/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png')
        self.client.get('/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
        self.client.post('/gen_204?s=webaft&t=aft&atyp=csi&ei=SwxoW9akCsLGkwWmuonwBQ&rt=wsrt.238,aft.237,prt.237',
            json={})
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/m=sx,sb,cdos,elog,hsm,jsa,r,d,csi/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ')
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/exm=sx,sb,cdos,elog,hsm,jsa,r,d,csi/ed=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ/m=aa,abd,async,dvl,foot,ipv6,lu,m,mu,sf,sonic,spch,d3l,cbin,tnqaT,cbhb,fEVMic,WgDvvc?xjs=s1')
        self.client.get('/textinputassistant/tia.png')
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/exm=sx,sb,cdos,elog,hsm,jsa,r,d,csi,aa,abd,async,dvl,foot,ipv6,lu,m,mu,sf,sonic,spch,d3l,cbin,tnqaT,cbhb,fEVMic,WgDvvc/ed=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ/m=RMhBfe?xjs=s2')
        self.client.post('/gen_204?atyp=i&ei=SwxoW9akCsLGkwWmuonwBQ&vet=10ahUKEwiW9teshtjcAhVC46QKHSZdAl4QsmQIDw..s&zx=1533545547778',
            json={})
        self.client.get('/domainless/write?igu=1&data=&xsrf=ALAmJdF0UotA5MkZXPxw4Gk4rQRoEMl6uQ:1533545547198')
        self.client.get('/images/nav_logo242.png')
        self.client.post('/gen_204?atyp=csi&ei=SwxoW9akCsLGkwWmuonwBQ&s=webhp&t=all&imc=3&imn=3&imp=1&adh=&conn=onchange&ima=1&ime=0&imeb=0&imeo=0&mem=ujhs.13,tjhs.15,jhsl.2330,dm.8&net=dl.10000,ect.4g,rtt.100&sys=hc.4&rt=aft.237,dcl.240,iml.1359,ol.1361,prt.237,xjs.418,xjsee.418,xjses.358,xjsls.255,wsrt.238,cst.76,dnst.1,rqst.135,rspt.46,sslt.54,rqstt.99,unt.20,cstt.22,dit.478&zx=1533545548658',
            json={})
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=1&gs_id=2&q=h&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=2&gs_id=5&q=ha&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=3&gs_id=9&q=har&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=4&gs_id=e&q=har%20&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=5&gs_id=i&q=har%20f&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=6&gs_id=m&q=har%20fi&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=7&gs_id=q&q=har%20fil&xhr=t')
        self.client.get('/complete/search?client=psy-ab&hl=en-DE&gs_rn=64&gs_ri=psy-ab&ei=SwxoW9akCsLGkwWmuonwBQ&cp=8&gs_id=t&q=har%20file&xhr=t')
        self.client.get('/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png')
        self.client.get('/images/nav_logo242.png')
        self.client.post('/gen_204?s=webaft&t=aft&atyp=csi&ei=TwxoW_OUMurOgAa5t5zgBg&rt=wsrt.112,aft.334,prt.334,sct.244',
            json={})
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/m=sx,sb,cdos,elog,hsm,jsa,r,d,csi/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ')
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/exm=sx,sb,cdos,elog,hsm,jsa,r,d,csi/ed=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ/m=aa,abd,aspn,async,dvl,foot,ipv6,lu,m,mu,sf,sonic,spch,tl,vs,d3l,tnv,cbin,tnqaT,exdp,shrb,qtf,tcc,atn,aam1T,yyqeUd,fEVMic,WgDvvc,TxZWcc,VugqBb?xjs=s1')
        self.client.get('/textinputassistant/tia.png')
        self.client.get('/client_204?&atyp=i&biw=1680&bih=589&dpr=2&ei=TwxoW_OUMurOgAa5t5zgBg')
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/exm=sx,sb,cdos,elog,hsm,jsa,r,d,csi,aa,abd,aspn,async,dvl,foot,ipv6,lu,m,mu,sf,sonic,spch,tl,vs,d3l,tnv,cbin,tnqaT,exdp,shrb,qtf,tcc,atn,aam1T,yyqeUd,fEVMic,WgDvvc,TxZWcc,VugqBb/ed=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ/m=IkchZc,Uuupec?xjs=s2')
        self.client.post('/gen_204?atyp=i&ei=TwxoW_OUMurOgAa5t5zgBg&vet=12ahUKEwiz-POuhtjcAhVqJ8AKHbkbB2wQ_R0oAzANegQIChAO..s;2ahUKEwiz-POuhtjcAhVqJ8AKHbkbB2wQ_R0oBDAOegQIChAQ..s;2ahUKEwiz-POuhtjcAhVqJ8AKHbkbB2wQ_R0oBTAPegQIChAS..s&zx=1533545552486',
            json={})
        self.client.post('/gen_204?atyp=i&ei=TwxoW_OUMurOgAa5t5zgBg&ct=kptm:il&iw=1680&ih=589&r=0&sh=1050&sw=1680&tmw=454&tmh=319&nvi=6&lc=1&bw=454&zx=1533545552489',
            json={})
        self.client.get('/xjs/_/js/k=xjs.s.en.0Bn-s8TsPUI.O/am=YBZhP_4BJP-_YEBRsBWMsMAMCoZN/rt=j/d=1/exm=sx,sb,cdos,elog,hsm,jsa,r,d,csi,aa,abd,aspn,async,dvl,foot,ipv6,lu,m,mu,sf,sonic,spch,tl,vs,d3l,tnv,cbin,tnqaT,exdp,shrb,qtf,tcc,atn,aam1T,yyqeUd,fEVMic,WgDvvc,TxZWcc,VugqBb,IkchZc,Uuupec/ed=1/dg=0/rs=ACT90oFW3E4N-xU9U4Q4GTJsa8EDYpUzqQ/m=RMhBfe?xjs=s2')
        self.client.post('/gen_204?atyp=i&ei=TwxoW_OUMurOgAa5t5zgBg&vet=10ahUKEwiz-POuhtjcAhVqJ8AKHbkbB2wQtWQIJygE..s&zx=1533545552570',
            json={})
        self.client.post('/gen_204?atyp=csi&ei=TwxoW_OUMurOgAa5t5zgBg&s=web&t=all&imc=8&imn=8&imp=7&adh=&conn=onchange&ima=1&ime=0&imeb=6&imeo=0&mem=ujhs.13,tjhs.15,jhsl.2330,dm.8&net=dl.10000,ect.4g,rtt.100&sys=hc.4&rt=aft.334,dcl.385,iml.945,ol.1163,prt.334,xjs.500,xjsee.500,xjses.448,xjsls.361,sct.244,wsrt.112,cst.0,dnst.0,rqst.416,rspt.339,rqstt.7,unt.6,cstt.6,dit.497&zx=1533545553078',
            json={})

    def execute_remote_requests(self):
        self.client.get('https://consent.google.com/status?continue=https://www.google.com&pc=s&timestamp=1533545547&gl=DE')
        self.client.get('https://ssl.gstatic.com/gb/images/i2_2ec824b0.png')
        self.client.get('https://www.gstatic.com/og/_/js/k=og.og2.en_US.8o90Q1jvcz8.O/rt=j/m=def/exm=in,fot/d=1/ed=1/rs=AA2YrTtrEMX8tHNUxrW5Zf3KnK4jChYyag')
        self.client.get('https://www.google.de/domainless/read?igu=1')
        self.client.get('https://apis.google.com/_/scs/abc-static/_/js/k=gapi.gapi.en.yK0z3MKtgaU.O/m=gapi_iframes,googleapis_client,plusone/rt=j/sv=1/d=1/ed=1/rs=AHpOoo-SafOYj4n3budMysbWxppU-lxJeg/cb=gapi.loaded_0')
        self.client.get('https://adservice.google.com/adsid/google/ui')
        self.client.get('https://ssl.gstatic.com/gb/images/i2_2ec824b0.png')
        self.client.get('https://consent.google.com/status?continue=https://www.google.com&pc=s&timestamp=1533545552&gl=DE')
        self.client.get('https://id.google.com/verify/AJVNx7pP7CNSPxtEXEreWhc1EiB_Od3LXVFlk14BJ-ffuRNhf6w7jqY3Cx1pKc-0B0QMt48b5QS1UUfoDOJS2sMciA0XT9CV8XHr4iPQAemYO5UjfqO4ctE')
        self.client.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrAM5arKEJmW1yQzG71pIrbJPFD_9fVz5v9K9TNDepkBToKSQi3K78D8_4')
        self.client.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdPWDwpaUSZQQpt1IW-DbZtR3Re2Cl2jKiVpLisvHLNh71XPp1ZHdl-waDJg')
        self.client.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuFJJEmq-bM5nLvSVAfJeU5FyDigCZ4QedDv6qq21hzj8alZhjIW01QIgI')
        self.client.get('https://www.gstatic.com/og/_/js/k=og.og2.en_US.8o90Q1jvcz8.O/rt=j/m=def/exm=in,fot/d=1/ed=1/rs=AA2YrTtrEMX8tHNUxrW5Zf3KnK4jChYyag')
        self.client.get('https://apis.google.com/_/scs/abc-static/_/js/k=gapi.gapi.en.yK0z3MKtgaU.O/m=gapi_iframes,googleapis_client,plusone/rt=j/sv=1/d=1/ed=1/rs=AHpOoo-SafOYj4n3budMysbWxppU-lxJeg/cb=gapi.loaded_0')
        self.client.get('https://adservice.google.com/adsid/google/ui')

    @staticmethod
    def load_test_data():
        with open('data.json') as data_file:
            LoadTestScenario.test_data = json.load(data_file)

    class StagesShape(LoadTestShape):
        """
        A step load shape
        Keyword arguments:
            step_time -- Time between steps
            step_load -- User increase amount at each step
            spawn_rate -- Users to stop/start per second at every step
            time_limit -- Time limit in seconds
        """

        step_time = 300
        step_load = 5
        spawn_rate = 5
        time_limit = 3600

        def tick(self):
            run_time = self.get_run_time()

            if run_time > self.time_limit:
                return None

            current_step = math.floor(run_time / self.step_time) + 1
            return (current_step * self.step_load, self.spawn_rate)
