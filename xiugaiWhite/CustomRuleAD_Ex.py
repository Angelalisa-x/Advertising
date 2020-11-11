# coding=utf-8

import csv, requests, re
import shutil
import os
import sys

static_Blackmatrix_num = 0  #Blackmatrix7行数

########################## 去重 #################################
def quchong(writePath,readPath):
    lines_seen=set()
    outfiile=open(writePath,'w+')
    f=open(readPath,'r')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)

    outfiile.close()
    f.close()

######################### 获取文件的行数 ########################
def getFileLineNum(fileName):
    with open(fileName, 'r') as f:
        line_num = sum(1 for line in f)
        print("%s: 总行数为%s: 行"%(fileName,line_num))
    f.close()
    return line_num

#################### pull Blackmatrix 规则，去掉前后缀 #############
def pullBlackmatrix7():
    url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AdvertisingTest/AdvertisingTest.list'
    #url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Advertising/Advertising.list'
    html = requests.get(url).text
    #print(html)
    with open("1.txt","w") as f:
        f.write(html)
    f.close()

    BlackmatrixBackups = open("BlackmatrixBackups.txt","w")
    BlackmatrixBackups.write(html)
    BlackmatrixBackups.close()

    with open("blackmatrix7.txt","w+") as fin7:
        for line in open("1.txt"):
            if "#" in line:
                #print(line)
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "$" in line:
                continue
            if "。" in line:
                continue
            str=[]
            str = line
            str = str[str.find(',')+1: str.rfind(',')] + "\n"
            fin7.write(str)
    fin7.close()

########################### 切割文本文件 #################################
def qiegeFile(writePath,readPath,num):
    file = open(readPath,"r")
    fin = open(writePath,"w")
    for num1,line in enumerate(file):
        if num1 >= num:
            fin.write(line)
    file.close()
    fin.close()

########################## 合并文本文件 ##################################
def hebingFile(targetFile,mergeFile):
    fin = open(targetFile, "a+")
    for line in open(mergeFile,"r"):
        fin.write(line)
    fin.close()

########################## QX格式处理 ####################################
def geshiProcess(targetFile,readPath):
    fin = open(targetFile,"w")
    for line in open(readPath,"r"):
        str = []
        str = line
        str = str[0:str.find("\n")]
        str = "HOST-SUFFIX," + str + ",REJECT" + "\n"
        fin.write(str)
    fin.close()

########################### 白名单过滤 ##################################
def baimingdangProcess(targetFile,readPath):
    fin = open(targetFile,"w")
    for line in open(readPath,"r"):
        if "music.126.net" in line:
            continue
        if ".snssdk.com" in line:
            continue
        if ".pstatp.com" in line:
            continue
        if ".mkey.163.com" in line:
            continue
        if "jr.jd.com" in line:
            continue
        if ".netease.com" in line:
            continue
        if "gia.jd.com" in line:
            continue
        if ".m.jd.com" in line:
            continue
        if "mapi.m.jd.com" in line:
            continue
        if "pornhub.com" in line:
            continue
        if ".effirst.com" in line:
            continue
        if "uland.taobao.com" in line:
            continue
        if "s.youtube.com" in line:
            continue
        if ".ourplay.net" in line:
            continue
        if ".cdntip.com" in line:
            continue
        if "s.click.tmall.com" in line:
            continue
        if ".alipaydns.com" in line:
            continue
        if ".elemecdn.com" in line:
            continue
        if "astat.bugly.qq.com" in line:
            continue
        if "bugly.qq.com" in line:
            continue
        if ".shifen.com" in line:
            continue
        if "shifen.com" in line:
            continue
        if "api-shoulei-ssl.xunlei.com" in line:
            continue
        if ".ydstatic.com" in line:
            continue
        if ".sankuai.com" in line:
            continue
        if ".dianping.com" in line:
            continue
        if ".meituan.net" in line:
            continue
        if ".meituan.com" in line:
            continue
        if ".cdninstagram.com" in line:
            continue
        if "update.miui.com" in line:
            continue
        if "im.qq.com" in line:
            continue
        if ".ele.me" in line:
            continue
        if ".happyelements.cn" in line:
            continue
        if "api.sec.miui.com" in line:
            continue
        if "cdn.ark.qq.com" in line:
            continue
        if ".bdimg.com" in line:
            continue
        if "t1.baidu.com" in line:
            continue
        if "t2.baidu.com" in line:
            continue
        if "t3.baidu.com" in line:
            continue
        if "t4.baidu.com" in line:
            continue
        if "t5.baidu.com" in line:
            continue
        if "t6.baidu.com" in line:
            continue
        if "t7.baidu.com" in line:
            continue
        if "t8.baidu.com" in line:
            continue
        if "t9.baidu.com" in line:
            continue
        if "t10.baidu.com" in line:
            continue
        if "t11.baidu.com" in line:
            continue
        if "t12.baidu.com" in line:
            continue
        if "gia.jd.com" in line:
            continue
        if "wl.jd.com" in line:
            continue
        if "mos.m.taobao.com" in line:
            continue
        if "cmshow.qq.com" in line:
            continue
        if ".api.adidas.com.cn" in line:
            continue
        if "at.umeng.com" in line:
            continue
        if "api.video.xiaomi.com" in line:
            continue
        if ".mi-img.com" in line:
            continue
        if "soft.tbs.imtt.qq.com" in line:
            continue
        if "pingjs.qq.com" in line:
            continue
        if "pingtcss.qq.com" in line:
            continue
        if "cl2.webterren.com" in line:
            continue
        if ".imtt.qq.com" in line:
            continue
        if "wbapp.mobile.sina.cn" in line:
            continue
        if "free.sinaimg.cn" in line:
            continue
        if "appmsg.gzmtr.cn" in line:
            continue
        if "dldir1.qq.com" in line:
            continue
        if "weixin.qq.com" in line:
            continue
        if ".img.mobile.sina.cn" in line:
            continue
        if ".126.net" in line:
            continue
        if "quan.suning.com" in line:
            continue
        if "mparticle.uc.cn" in line:
            continue
        if "g.shumafen.cn" in line:
            continue
        if "dd.myapp.com" in line:
            continue
        if "s.click.taobao.com" in line:
            continue
        if "zkres.myzaker.com" in line:
            continue
        if ".video.xiaomi.com" in line:
            continue
        if "inews.gtimg.com" in line:
            continue
        if "duapps.com" in line:
            continue
        if ".snssdk.com" in line:
            continue
        if "mobile.appchina.com" in line:
            continue
        if "connect.rom.miui.com" in line:
            continue
        if "get.sogou.com" in line:
            continue
        if "twimg.com" in line:
            continue
        if "mam.netease.com" in line:
            continue
        if "pp.myapp.com" in line:
            continue
        if "duiba.com.cn" in line:
            continue
        if "t.me" in line:
            continue
        if "btrace.qq.com" in line:
            continue
        if "graph.qq.com" in line:
            continue
        if "api.account.xiaomi.com" in line:
            continue
        if "metok.sys.miui.com" in line:
            continue
        if "mibi.api.xiaomi.com" in line:
            continue
        if "t.cn" in line:
            continue
        if "work.weixin.qq.com" in line:
            continue
        if ".aliyun.com" in line:
            continue
        if "toutiaocdn.com" in line:
            continue
        if ".qlogo.cn" in line:
            continue
        if ".sm.cn" in line:
            continue
        if "sina.cn" in line:
            continue
        if "broccoli.uc.cn" in line:
            continue
        if "t.co" in line:
            continue
        if "youtu.be" in line:
            continue
        if "vdun.weibo.com" in line:
            continue
        if "pingfore.qq.com" in line:
            continue
        if "stat.y.qq.com" in line:
            continue
        if "api.comm.miui.com" in line:
            continue
        if "yun.rili.cn" in line:
            continue
        if "lhl.zxcs.linghit.com" in line:
            continue
        if "iflow.uc.cn" in line:
            continue
        if "ctrip.com" in line:
            continue
        if "wx2.sinaimg.cn" in line:
            continue
        if "c.y.qq.com" in line:
            continue
        if "api.rikka.app" in line:
            continue
        if "oppo.yidianzixun.com" in line:
            continue
        if "ib11.go2yd.com" in line:
            continue
        if "lpl.qq.com" in line:
            continue
        if "logs.game.qq.com" in line:
            continue
        if ".lol.qq.com" in line:
            continue
        if "ip.cn" in line:
            continue
        if "suo.im" in line:
            continue
        if "bigota.d.miui.com" in line:
            continue
        if "api.jr.mi.com" in line:
            continue
        if "kyaru-concat.now.sh" in line:
            continue
        if "api.zhihu.com" in line:
            continue
        if "appcloud.zhihu.com" in line:
            continue
        if "weidian.com" in line:
            continue
        if "h5.m.taobao.com" in line:
            continue
        if "api.io.mi.com" in line:
            continue
        if "tvepg.pandora.xiaomi.com" in line:
            continue
        if ".bmap6.cn" in line:
            continue
        if "mobile.controller.duokanbox.com" in line:
            continue
        if "api.ts.feedback.qy.net" in line:
            continue
        if "feedback.miui.com" in line:
            continue
        if "akamaized.net" in line:
            continue
        if "duckduckgo.com" in line:
            continue
        if ".recaptcha.net" in line:
            continue
        if "bonuscloud.io" in line:
            continue
        if "computemaster.bxcearth.com" in line:
            continue
        if "simg.sinajs.cn" in line:
            continue
        if "pinghot.qq.com" in line:
            continue
        if ".y.qq.com" in line:
            continue
        if "yun.duiba.com.cn" in line:
            continue
        if ".gtimg.cn" in line:
            continue
        if "input.shouji.sogou.com" in line:
            continue
        if "ip.taobao.com" in line:
            continue
        if "cn.ultraiso.net" in line:
            continue
        if "sqimg.qq.com" in line:
            continue
        if "imtt.dd.qq.com" in line:
            continue
        if "image.uc.cn" in line:
            continue
        if "m.video.9ddm.com" in line:
            continue
        if "o2o.api.xiaomi.com" in line:
            continue
        if ".xiaomi.net" in line:
            continue
        if "c.pc.qq.com" in line:
            continue
        if ".jiaoyimao.com" in line:
            continue
        if "res.imtt.qq.com" in line:
            continue
        if "recmd.html5.qq.com" in line:
            continue
        if "debugtbs.qq.com" in line:
            continue
        if "3gimg.qq.com" in line:
            continue
        if ".m.qq.com" in line:
            continue
        if ".map.qq.com" in line:
            continue
        if "dnet.mb.qq.com" in line:
            continue
        if "web.vip.miui.com" in line:
            continue
        if "app.zhuanzhuan.com" in line:
            continue
        if "client.wns.windows.com" in line:
            continue
        if "gcable.com.cn" in line:
            continue
        if "uee.me" in line:
            continue
        if "baike.so.com" in line:
            continue
        if "tracker.ai.xiaomi.com" in line:
            continue
        if "img.zuoyebang.cc" in line:
            continue
        if "p2p.huya.com" in line:
            continue
        if "translator.qq.com" in line:
            continue
        if ".alipay.com" in line:
            continue
        if "mail.qq.com" in line:
            continue
        if "mjrpay.jd.com" in line:
            continue
        if "cfm.jd.com" in line:
            continue
        if "jr.jd.com" in line:
            continue
        if "qun.qzone.qq.com" in line:
            continue
        if "ohssr.cn" in line:
            continue
        if ".alicdn.com" in line:
            continue
        if ".ykimg.com" in line:
            continue
        if ".market.xiaomi.com" in line:
            continue
        if "dmm.co.jp" in line:
            continue
        if "upgrade.ptmi.gitv.tv" in line:
            continue
        if "images.uc.cn" in line:
            continue
        if "restapi.amap.com" in line:
            continue
        if "plbslog.umeng.com" in line:
            continue
        if ".gdt.qq.com" in line:
            continue
        if ".duoku.com" in line:
            continue
        if ".netease.com" in line:
            continue
        if ".mkey.163.com" in line:
            continue
        if ".mipay.com" in line:
            continue
        if ".miwifi.com" in line:
            continue
        if ".data.microsoft.com" in line:
            continue
        if ".qualtrics.com" in line:
            continue
        if ".southcn.com" in line:
            continue
        if "youtubei.googleapis.com" in line:
            continue
        if "account.xiaomi.com" in line:
            continue
        if "data.mistat.intl.xiaomi.com" in line:
            continue
        if "tsmclient.miui.com" in line:
            continue
        if ".app.qq.com" in line:
            continue
        if ".tencent-cloud.net" in line:
            continue
        if "cnbj1.fds.api.xiaomi.com" in line:
            continue
        if ".qzone.qq.com" in line:
            continue
        if "sourl.cn" in line:
            continue
        if "alissl.ucdl.pp.uc.cn" in line:
            continue
        if "ynuf.aliapp.org" in line:
            continue
        if "tv.sohu.com" in line:
            continue
        if "m.youtube.com" in line:
            continue
        if ".aliyuncs.com" in line:
            continue
        if ".alibabausercontent.com" in line:
            continue
        if "s.click.ele.me" in line:
            continue
        if ".mybank.cn" in line:
            continue
        if "www.qq.com" in line:
            continue
        if "cn.bing.com" in line:
            continue
        if "360.cn" in line:
            continue
        if "dlied6.qq.com" in line:
            continue
        if "misc.wcd.qq.com" in line:
            continue
        if "pingtas.qq.com" in line:
            continue
        if "android.bugly.qq.com" in line:
            continue
        if "guanjia.qq.com" in line:
            continue
        if "m.qpic.cn" in line:
            continue
        if ".doglobal.net" in line:
            continue
        if "facebook.com" in line:
            continue
        if "www.google.com" in line:
            continue
        if "connectivitycheck.gstatic.com" in line:
            continue
        if "www.youtube.com" in line:
            continue
        if "apis.google.com" in line:
            continue
        if "clients.l.google.com" in line:
            continue
        if "clients1.google.com" in line:
            continue
        if "gstatic.com" in line:
            continue
        if "manifest.googlevideo.com" in line:
            continue
        if "i.ytimg.com" in line:
            continue
        if "www.gstatic.com" in line:
            continue
        if "www.youtube-nocookie.com" in line:
            continue
        if "youtube-nocookie.com" in line:
            continue
        if "r4---sn-qxo7rn7e.googlevideo.com" in line:
            continue
        if "r5---sn-4g5ednsl.googlevideo.com" in line:
            continue
        if "r4---sn-a5meknek.googlevideo.com" in line:
            continue
        if "xn--ngstr-lra8j.com" in line:
            continue
        if "r3---sn-a5mlrn7r.googlevideo.com" in line:
            continue
        if "api.device.xiaomi.net" in line:
            continue
        if "api.micloud.xiaomi.net" in line:
            continue
        if "api.miui.security.xiaomi.com" in line:
            continue
        if "app.market.xiaomi.com" in line:
            continue
        if "f8.market.xiaomi.com" in line:
            continue
        if "file.market.xiaomi.com" in line:
            continue
        if "cn.app.chat.xiaomi.net" in line:
            continue
        if "connect.rom.miui.com/generate_204" in line:
            continue
        if "m.video.xiaomi.com" in line:
            continue
        if "migrate.driveapi.micloud.xiaomi.net" in line:
            continue
        if "pdc.micloud.xiaomi.net" in line:
            continue
        if "phonecallapi.micloud.xiaomi.net" in line:
            continue
        if "resolver.msg.xiaomi.net" in line:
            continue
        if "sfsapi.micloud.xiaomi.net" in line:
            continue
        if "ssl-cdn.static.browser.mi-img.com" in line:
            continue
        if "ts.market.mi-img.com" in line:
            continue
        if "cdn.cnbj1.fds.api.mi-img.com" in line:
            continue
        if "app-measurement.com" in line:
            continue
        if "exp.sug.browser.miui.com" in line:
            continue
        if "mi.com" in line:
            continue
        if "xzz.xiaomin.tech" in line:
            continue
        if ".micloud.xiaomi.net" in line:
            continue
        if "mi-img.com" in line:
            continue
        if "mivideo.cdn.pandora.xiaomi.com" in line:
            continue
        if "v*-dc-ad.ixigua.com" in line:
            continue
        if "wallpaper.cdn.pandora.xiaomi.com" in line:
            continue
        if "package.wallpaper.cdn.pandora.xiaomi.com.lan" in line:
            continue
        if "w.pandora.xiaomi.com" in line:
            continue
        if "sec-cdn.static.xiaomi.net" in line:
            continue
        if "fgc0.market.xiaomi.com" in line:
            continue
        if "fga0.market.xiaomi.com" in line:
            continue
        if "t3.market.mi-img.com" in line:
            continue
        if "sec.resource.xiaomi.net" in line:
            continue
        if ".market.mi-img.com" in line:
            continue
        if "f*.market.xiaomi.com" in line:
            continue
        if "f*.market.mi-img.com" in line:
            continue
        if "market.mi-img.com" in line:
            continue
        if "aliyun.com" in line:
            continue
        if "uczzd.cn" in line:
            continue
        if "downum.game.uc.cn" in line:
            continue
        if "unet.ucweb.com" in line:
            continue
        if "alicdn.com" in line:
            continue
        if "dj.1688.com" in line:
            continue
        if "click.simba.taobao.com" in line:
            continue
        if "na61-na62.wagbridge.advertisement.alibabacorp.com.gds.alibabadns.com" in line:
            continue
        if "na61-na62.wagbridge.advertisement.alibabacorp.com" in line:
            continue
        if "dns.weixin.qq.com" in line:
            continue
        if "cfg.imtt.qq.com" in line:
            continue
        if "tbs.imtt.qq.com" in line:
            continue
        if "vectorsdk.map.qq.com" in line:
            continue
        if "qlogo.cn" in line:
            continue
        if "thirdwx.qlogo.cn" in line:
            continue
        if "imgcache.qq.com" in line:
            continue
        if "appsupport.qq.com" in line:
            continue
        if "lol.qq.com" in line:
            continue
        if "cn.ekg.riotgames.com" in line:
            continue
        if "view.inews.qq.com" in line:
            continue
        if "tdid.m.qq.com" in line:
            continue
        if "cc.map.qq.com" in line:
            continue
        if "map.qq.com" in line:
            continue
        if "126.net" in line:
            continue
        if "163.com" in line:
            continue
        if "passport.youdao.com" in line:
            continue
        if "c.tieba.baidu.com" in line:
            continue
        if "mbd.baidu.com" in line:
            continue
        if "cpu.baidu.com" in line:
            continue
        if "u1.img.mobile.sina.cn" in line:
            continue
        if "weibo.cn" in line:
            continue
        if "snssdk.com" in line:
            continue
        if "pstatp.com" in line:
            continue
        if "raw.githubusercontent.com" in line:
            continue
        if "self.events.data.microsoft.com" in line:
            continue
        if "bing.com" in line:
            continue
        if "instagram.com" in line:
            continue
        if ".twimg.com" in line:
            continue
        if "reddit" in line:
            continue
        if "www.recaptcha.net" in line:
            continue
        if "spotifycdn.net" in line:
            continue
        if "spotify.com" in line:
            continue
        if "spclient.wg.spotify.com" in line:
            continue
        if "cdn.jsdelivr.net" in line:
            continue
        if "vmware.com" in line:
            continue
        if "adidasapp.api.adidas.com.cn" in line:
            continue
        if "mobile.yangkeduo.com" in line:
            continue
        if "sm.cn" in line:
            continue
        if "statics.itc.cn" in line:
            continue
        if "iface2.iqiyi.com" in line:
            continue
        if "ykimg.com" in line:
            continue
        if "www.jiaoyimao.com" in line:
            continue
        if "m.jiaoyimao.com" in line:
            continue
        if "data.bilibili.com" in line:
            continue
        if "jumpluna.58.com" in line:
            continue
        if "oss-asq-static.11222.cn" in line:
            continue
        if "zxcs.me" in line:
            continue
        if "dxx.wwwtop.top" in line:
            continue
        if "f.51240.com" in line:
            continue
        if "hosts-file.net" in line:
            continue
        if "counter-strike.net" in line:
            continue
        if "www.chemdraw.com.cn" in line:
            continue
        if "pool.v6.bt.n0808.com" in line:
            continue
        if "upload.cc" in line:
            continue
        if "parked-content.godaddy.com" in line:
            continue
        if "ydstatic.com" in line:
            continue
        if "iteye.com" in line:
            continue
        if "bmap6.cn" in line:
            continue
        if "96956.com.cn" in line:
            continue
        if "www.kanjiantu.com" in line:
            continue
        if "digac.cc" in line:
            continue
        if "digac.top" in line:
            continue
        if "pthome.net" in line:
            continue
        if "vnas.me" in line:
            continue
        if "digac.tk" in line:
            continue
        if "gaytube.com" in line:
            continue
        if "github.com" in line:
            continue
        if "s3.amazonaws.com" in line:
            continue
        if "2dbook.com" in line:
            continue
        if "4tern.com" in line:
            continue
        if "tampermonkey.net" in line:
            continue
        if "qiong.ru" in line:
            continue
        if "zeronet.io" in line:
            continue
        if "aeventlog.beacon.qq.com" in line:
            continue
        if "oth.eve.mdt.qq.com" in line:
            continue
        if "gaytorrent.tw" in line:
            continue
        if "qafone.co" in line:
            continue
        if "qafone.org" in line:
            continue
        if "qafone.net" in line:
            continue
        if "gay-torrents.net" in line:
            continue
        if "gay-torrents.org" in line:
            continue
        if "boyfriendtv.com" in line:
            continue
        if "merlinblog.xyz" in line:
            continue
        if "www.lduhtrp.net" in line:
            continue
        if "www.awltovhc.com" in line:
            continue
        if "www.yceml.net" in line:
            continue
        if "www.tqlkg.com" in line:
            continue
        if "www.ftjcfx.com" in line:
            continue
        if "cj.com" in line:
            continue
        if "web.umeng.com" in line:
            continue
        if "moonbit.co.in" in line:
            continue
        if "fuwu.biz.weibo.com" in line:
            continue
        if "tongji.baidu.com" in line:
            continue
        if "tongji.digac.cc" in line:
            continue
        if "mdevstat.qqlive.qq.com" in line:
            continue
        if "rs1.qq.com" in line:
            continue
        if "t-flow.flyme.cn" in line:
            continue
        if "rs2.qq.com" in line:
            continue
        if "qappcenterv6.3g.qq.com" in line:
            continue
        if "y.gtimg.cn" in line:
            continue
        if "union-click.jd.com" in line:
            continue
        if "get.adobe.com" in line:
            continue
        if "imedl.sogoucdn.com" in line:
            continue
        if "update.sdk.jiguang.cn" in line:
            continue
        if "c.isdspeed.qq.com" in line:
            continue
        if "v2.get.sogou.com" in line:
            continue
        if "qzone.qq.com" in line:
            continue
        if "console.bce.baidu.com" in line:
            continue
        if "ssl.google-analytics.com" in line:
            continue
        if "cws-cctv.conviva.com" in line:
            continue
        if "tools.3g.qq.com" in line:
            continue
        if "cloud.xdrig.com" in line:
            continue
        if "adash.man.aliyuncs.com" in line:
            continue
        if "dig.bdurl.net" in line:
            continue
        if "dp3.qq.com" in line:
            continue
        if "me.xdrig.com" in line:
            continue
        if "cm.bilibili.com" in line:
            continue
        if "fp-it.fengkongcloud.com" in line:
            continue
        if "zhihu-web-analytics.zhihu.com" in line:
            continue
        if "jpush.html5.qq.com" in line:
            continue
        if "data.yd126.com" in line:
            continue
        if "acs.m.taobao.com" in line:
            continue
        if "www.360kuai.com" in line:
            continue
        if "h5.mse.360.cn" in line:
            continue
        if "ali-stats.jpush.cn" in line:
            continue
        if "www.google-analytics.com" in line:
            continue
        if "stat.hao.uc.cn" in line:
            continue
        if "hao.uc.cn" in line:
            continue
        if "b.bdstatic.com" in line:
            continue
        if "c.bing.com" in line:
            continue
        if "otf.msn.com" in line:
            continue
        if "woodpecker.uc.cn" in line:
            continue
        if "www.huabian.com" in line:
            continue
        if "uxip.meizu.com" in line:
            continue
        if "vs.biz.weibo.com" in line:
            continue
        if "ef-dongfeng.tanx.com" in line:
            continue
        if "wup.imtt.qq.com" in line:
            continue
        if "ark.letv.com" in line:
            continue
        if "adm.zookingsoft.com" in line:
            continue
        if "d1.sina.com.cn" in line:
            continue
        if "beacon.sina.com.cn" in line:
            continue
        if "woocall.sina.com.cn" in line:
            continue
        if "d.s11.cn" in line:
            continue
        if "update.360safe.com" in line:
            continue
        if "ucus.ucweb.com" in line:
            continue
        if "updatecenter.qq.com" in line:
            continue
        if "c.msn.com" in line:
            continue
        if "int.dpool.sina.com.cn" in line:
            continue
        if "scdown.qq.com" in line:
            continue
        if "displaycatalog.mp.microsoft.com" in line:
            continue
        if "windows.policies.live.net" in line:
            continue
        if "mapi.m.jd.com" in line:
            continue
        if "eimg.smzdm.com" in line:
            continue
        if "mazu.3g.qq.com" in line:
            continue
        if "mountain.zhidao.baidu.com" in line:
            continue
        if "openapi.guanjia.qq.com" in line:
            continue
        if "httpring.qq.com" in line:
            continue
        if "masdkv6.3g.qq.com" in line:
            continue
        if "cn.register.xmpush.xiaomi.com" in line:
            continue
        if "lf.snssdk.com" in line:
            continue
        if "android.rqd.qq.com" in line:
            continue
        if "r6.mo.baidu.com" in line:
            continue
        if "web.vortex.data.microsoft.com" in line:
            continue
        if "sf6-ttcdn-tos.pstatp.com" in line:
            continue
        if "sf1-ttcdn-tos.pstatp.com" in line:
            continue
        if "info.pinyin.sogou.com" in line:
            continue
        if "account.migc.g.mi.com" in line:
            continue
        if "data.mistat.xiaomi.com" in line:
            continue
        if "data.flurry.com" in line:
            continue
        if "s.jpush.cn" in line:
            continue
        if "sdkclick.mobile.sina.cn" in line:
            continue
        if "dp.im.weibo.cn" in line:
            continue
        if "g.live.com" in line:
            continue
        if "g0.baidu.com" in line:
            continue
        if "gw5.push.mcp.weibo.cn" in line:
            continue
        if "commdata.v.qq.com" in line:
            continue
        if "dw-online.ksosoft.com" in line:
            continue
        if "show-g.mediav.com" in line:
            continue
        if "news.qhstatic.com" in line:
            continue
        if "bbs.8023ak.cn" in line:
            continue
        if "statusapi.micloud.xiaomi.net" in line:
            continue
        if "cgi.connect.qq.com" in line:
            continue
        if "d3g.qq.com" in line:
            continue
        if "dxp.baidu.com" in line:
            continue
        if "pmm.people.com.cn" in line:
            continue
        if "zconfig.alibabausercontent.com" in line:
            continue
        if "oth.str.mdt.qq.com" in line:
            continue
        if "2052.flash2-http.qq.com" in line:
            continue
        if "e.crashlytics.com" in line:
            continue
        if "b.qchannel03.cn" in line:
            continue
        if "cmshow.gtimg.cn" in line:
            continue
        if "crl.microsoft.com" in line:
            continue
        if "kepler.jd.com" in line:
            continue
        if "info.3g.qq.com" in line:
            continue
        if "tj.youzanyun.com" in line:
            continue
        if "hub5idx.shub.sandai.net" in line:
            continue
        if "stat.download.xunlei.com" in line:
            continue
        if "etl-xlmc-ssl.sandai.net" in line:
            continue
        if "tianshu.gtimg.cn" in line:
            continue
        if ".tieba.baidu.com" in line:
            continue
        if "www.baidu.com" in line:
            continue
        if "sofire.baidu.com" in line:
            continue
######### yudong white #############
        if "wl.jd.com" in line:
            continue
        if "union-click.jd.com" in line:
            continue
        if "dig.bdurl.net" in line:
            continue
        if "mjrpay.jd.com" in line:
            continue
        if "cfm.jd.com" in line:
            continue
        if "app-measurement.com" in line:
            continue
        if "ynuf.aliapp.org" in line:
            continue
        if "uland.taobao.com" in line:
            continue
        if "mos.m.taobao.com" in line:
            continue
        if "s.click.taobao.com" in line:
            continue
        if "h5.m.taobao.com" in line:
            continue
        if "ip.taobao.com" in line:
            continue
        if "acs.m.taobao.com" in line:
            continue
        if ",lianmeng," in line:
            continue
        if ",analytics," in line:
            continue
        if ",aliapp.org," in line:
            continue
        str=[]
        str = line
        str = str[0:str.find('/n')]
        if "meituan.net" == str:
            continue
        if "meituan.com" == str:
            continue
        if "kepler.jd.com" == str:
            continue
        if "analytics" == str:
            continue
        fin.write(line)
    fin.close()   



############################ 自己整理的规则 ###############################
def pullEach():
            ###################### 梵 Start #########################
    url = 'https://raw.githubusercontent.com/Potterli20/filtering/master/purification'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","w+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()
            ################### 梵 End ########################

            ################## kbsmlDns Start ####################
    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("..\WhiteList\kbsmlDns.txt","r",encoding='UTF-8'):
        #for line in open("WhiteList\kbsmlDns.txt","r",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                #print(line)
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if ":" in line:
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if "@@" in line:
                continue
            if "/" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "0.0.0.0" in line:
                str = str[str.find("0.0.0.0   ")+10:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()
            ############### kbsmlDns End ####################

            ################## GoodbyeAds Start ####################
    # url = 'https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Formats/GoodbyeAds-AdBlock-Filter.txt'
    # html = requests.get(url).text
    # with open("1.txt","w",encoding='UTF-8') as f:
    #     f.write(html)
    # f.close()

    # with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
    #     for line in open("1.txt",encoding='UTF-8'):
    #         str=[]
    #         str = line
    #         if "#" in line:
    #             continue
    #         if "!" in line:
    #             continue
    #         if line == '\n':
    #             continue
    #         if "。" in line:
    #             continue
    #         if "@" in line:
    #             continue
    #         if ":" in line:
    #             continue
    #         if "||*." in line:
    #             str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||." in line:
    #             str = str[str.find("||.")+3:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||*" in line:
    #             str = str[str.find("||*")+3:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "||" in line:
    #             str = str[str.find("||")+2:str.rfind("^")] + "\n"
    #             fin7.write(str)
    #             continue
    #         if "$" in line:
    #             continue
    #         fin7.write(str)
    # fin7.close()
            ################## GoodbyeAds End ####################

            ################## AdGuardDNS Start ####################
    url = 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if '\/' in line:
                continue
            if ":" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()
            ################## AdGuardDNS End ####################

            ################## 1Hosts-Pro Start ###################
    url = 'https://badmojr.github.io/1Hosts/Lite/domains.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "$" in line:
                continue
            fin7.write(str)
    fin7.close()            
            ################## 1Hosts-Pro End #####################

            ################## AdAway Start #####################
    url = 'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "localhost" in line:
                continue
            if "127.0.0.1 " in line:
                str = str[str.find("127.0.0.1 ")+10:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()  
            ################## AdAway End   #####################

            ################## iOSAdblockList Start  #####################
    url = 'https://raw.githubusercontent.com/BlackJack8/iOSAdblockList/master/iPv4Hosts.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "0.0.0.0 " in line:
                str = str[str.find("0.0.0.0 ")+8:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()              
            ################## iOSAdblockList End    #####################

            ################## VeleSila Star    #####################
    url = 'https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "127.0.0.1 " in line:
                str = str[str.find("127.0.0.1 ")+10:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()               
            ################## VeleSila End     #####################

            ################## sbc.io-hosts Star    #####################
    url = 'http://sbc.io/hosts/hosts'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "0.0.0.0 0.0.0.0" in line:
                continue
            if "0.0.0.0 " in line:
                str = str[str.find("0.0.0.0 ")+8:str.rfind("\n")] + "\n"
                fin7.write(str)
                continue
    fin7.close()               
            ################## sbc.io-hosts End     #####################

            ################## damengzhudamengzhu Star    #####################
    url = 'https://gitee.com/damengzhudamengzhu/guanggaoguolv/raw/master/jiekouAD.txt'
    html = requests.get(url).text
    with open("1.txt","w",encoding='UTF-8') as f:
        f.write(html)
    f.close()

    with open("KnightAD.txt","a+",encoding='UTF-8') as fin7:
        for line in open("1.txt",encoding='UTF-8'):
            str=[]
            str = line
            if "#" in line:
                continue
            if "!" in line:
                continue
            if line == '\n':
                continue
            if "。" in line:
                continue
            if "@" in line:
                continue
            if ":" in line:
                continue
            if "," in line:
                continue
            if ":" in line:
                continue
            if "=" in line:
                continue
            if "||*." in line:
                str = str[str.find("||*.")+4:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||." in line:
                str = str[str.find("||.")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||*" in line:
                str = str[str.find("||*")+3:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            if "||" in line:
                str = str[str.find("||")+2:str.rfind("^")] + "\n"
                fin7.write(str)
                continue
            fin7.write(str)

    fin7.close()              
            ################## damengzhudamengzhu End     #####################




###################### 执行函数 Start ########################
def doProcessCustomRuleAD():
    pullBlackmatrix7()
    pullEach()


    quchong("KnightAD_1.txt","KnightAD.txt")
    quchong("blackmatrix7_1.txt","blackmatrix7.txt")
    blackmatrix7_num = getFileLineNum("blackmatrix7_1.txt")

    quchong("BlackmatrixBackups_1.txt","BlackmatrixBackups.txt")
    baimingdangProcess("BlackmatrixBackups.list","BlackmatrixBackups_1.txt")

    hebingFile("blackmatrix7_1.txt","KnightAD_1.txt")
    quchong("blackmatrix7_2.txt","blackmatrix7_1.txt")

    qiegeFile("KnightAD_2.txt","blackmatrix7_2.txt",blackmatrix7_num)
    baimingdangProcess("KnightAD_3.txt","KnightAD_2.txt")
    geshiProcess("KnightAD.list","KnightAD_3.txt")


    os.remove("1.txt")
    os.remove("blackmatrix7.txt")
    os.remove("blackmatrix7_1.txt")
    os.remove("blackmatrix7_2.txt")
    os.remove("BlackmatrixBackups.txt")
    os.remove("BlackmatrixBackups_1.txt")
    os.remove("KnightAD.txt")
    os.remove("KnightAD_1.txt")
    os.remove("KnightAD_2.txt")
    os.remove("KnightAD_3.txt")
###################### 执行函数 End ########################

if __name__ == '__main__':
    pullBlackmatrix7()
    pullEach()


    quchong("KnightAD_1.txt","KnightAD.txt")
    quchong("blackmatrix7_1.txt","blackmatrix7.txt")
    blackmatrix7_num = getFileLineNum("blackmatrix7_1.txt")

    quchong("BlackmatrixBackups_1.txt","BlackmatrixBackups.txt")
    baimingdangProcess("BlackmatrixBackups.list","BlackmatrixBackups_1.txt")

    hebingFile("blackmatrix7_1.txt","KnightAD_1.txt")
    quchong("blackmatrix7_2.txt","blackmatrix7_1.txt")

    qiegeFile("KnightAD_2.txt","blackmatrix7_2.txt",blackmatrix7_num)
    baimingdangProcess("KnightAD_3.txt","KnightAD_2.txt")
    geshiProcess("KnightAD.list","KnightAD_3.txt")


    os.remove("1.txt")
    os.remove("blackmatrix7.txt")
    os.remove("blackmatrix7_1.txt")
    os.remove("blackmatrix7_2.txt")
    os.remove("BlackmatrixBackups.txt")
    os.remove("BlackmatrixBackups_1.txt")
    os.remove("KnightAD.txt")
    os.remove("KnightAD_1.txt")
    os.remove("KnightAD_2.txt")
    os.remove("KnightAD_3.txt")
