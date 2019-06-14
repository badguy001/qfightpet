# -*- coding: UTF-8 -*-

import scrapy
import re


class Daemon(scrapy.Spider):
    name = "qfightpet"
    start_urls = ["http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0", "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=missionassign&subtype=0"]
    allowed_domains = ["dld.qzapp.z.qq.com"]
    not_allow_texts = [u"商店",
                       u"购买",
                       u"速购",
                       u"返回",
                       u"退出",
                       u"退帮",
                       u"供奉",
                       u"升级",
                       u"兑换",
                       u"使用",
                       u"重置分享",
                       u"神匠坊",
                       u"兵法",
                       u"五行",
                       u"助阵",
                       u"佣兵",
                       u"经脉",
                       u"镶嵌",
                       u"充能",
                       u"强化",
                       u"神装",
                       u"专精",
                       u"星盘",
                       u"铭刻",
                       u"觉醒",
                       u"奥义",
                       u"元婴",
                       u"神魔录",
                       u"神将录",
                       u"斗技",
                       u"合成",
                       u"vip",
                       u"变强",
                       u"恢复",
                       u"达人",
                       u"觉醒",
                       u"充值",
                       u"入魂",
                       u"复活",
                       u"助手",
                       u"镶嵌",
                       u"分解",
                       u"打造",
                       u"排行",
                       u"论坛",
                       u"离婚",
                       u"结拜",
                       u"收徒",
                       u"查找",
                       u"购",
                       u"提升",
                       u"仙化",
                       u"详情",
                       u"说明",
                       u"摘除",
                       u"开启",
                       u"规则",
                       u"充能",
                       u"关闭",
                       u"融合",
                       u"传功",
                       u"还童",
                       u"突飞",
                       u"突破",
                       u"研习",
                       u"打造",
                       u"记录",
                       u"QQ",
                       u"修炼",
                       u"变更为",
                       u"窥视",
                       u"开通",
                       u"战斗力",
                       u"变强",
                       u"替换任务",
                       u"逐出帮派",
                       u"调换",
                       u"逐出师门",
                       u"踢出",
                       u"已乐斗",
                       u"点击交易",
                       u"回来玩吧",
                       u"赠与",
                       u"分解",
                       u"放弃",
                       u"师徒妻拜"]

    def parse(self, response):
        assert isinstance(response, scrapy.http.response.Response)
        hrefs = response.xpath('//a')
        for href in hrefs:
            text = href.xpath('./text()').extract()
            if len(text) == 0:
                continue
            text = text[0]
            follow = True
            for t in self.not_allow_texts:
                if text.find(t) != -1:
                    follow = False
                    break
            if not follow:
                continue
            url = href.xpath('./@href').extract()
            if len(url) == 0:
                continue
            url = url[0]
            if url.find("cmd=view&") != -1:
                continue
            if url.find("cmd=missionassign&subtype=6") != -1:
                continue
            yield scrapy.Request(url=url, callback=self.parse)

    def start_requests(self):
        with open('cookies.txt', 'r') as f:
            cookiejar = f.read()
            p = re.compile(r'([^\n]+)')
            cookies = re.findall(p, cookiejar)
            cookies = (cookie.split('=', 1) for cookie in cookies)
            cookies = dict(cookies)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)
