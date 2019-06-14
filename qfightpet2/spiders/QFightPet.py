# -*- coding: UTF-8 -*-

import scrapy
import re
import urlparse


class Daemon(scrapy.Spider):
    name = "qfightpet"
    start_urls = ["http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0",
                  "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=missionassign&subtype=0"]
    allowed_domains = ["dld.qzapp.z.qq.com"]
    not_allow_texts = list()
    not_allow_texts.append(u"商店")
    not_allow_texts.append(u"购买")
    not_allow_texts.append(u"速购")
    not_allow_texts.append(u"返回")
    not_allow_texts.append(u"退出")
    not_allow_texts.append(u"退帮")
    not_allow_texts.append(u"供奉")
    not_allow_texts.append(u"升级")
    not_allow_texts.append(u"兑换")
    not_allow_texts.append(u"使用")
    not_allow_texts.append(u"重置分享")
    not_allow_texts.append(u"神匠坊")
    not_allow_texts.append(u"兵法")
    not_allow_texts.append(u"五行")
    not_allow_texts.append(u"助阵")
    not_allow_texts.append(u"佣兵")
    not_allow_texts.append(u"经脉")
    not_allow_texts.append(u"镶嵌")
    not_allow_texts.append(u"充能")
    not_allow_texts.append(u"强化")
    not_allow_texts.append(u"神装")
    not_allow_texts.append(u"专精")
    not_allow_texts.append(u"星盘")
    not_allow_texts.append(u"铭刻")
    not_allow_texts.append(u"觉醒")
    not_allow_texts.append(u"奥义")
    not_allow_texts.append(u"元婴")
    not_allow_texts.append(u"神魔录")
    not_allow_texts.append(u"神将录")
    not_allow_texts.append(u"斗技")
    not_allow_texts.append(u"合成")
    not_allow_texts.append(u"vip")
    not_allow_texts.append(u"变强")
    not_allow_texts.append(u"恢复")
    not_allow_texts.append(u"达人")
    not_allow_texts.append(u"觉醒")
    not_allow_texts.append(u"充值")
    not_allow_texts.append(u"入魂")
    not_allow_texts.append(u"复活")
    not_allow_texts.append(u"助手")
    not_allow_texts.append(u"镶嵌")
    not_allow_texts.append(u"分解")
    not_allow_texts.append(u"打造")
    not_allow_texts.append(u"排行")
    not_allow_texts.append(u"论坛")
    not_allow_texts.append(u"离婚")
    not_allow_texts.append(u"结拜")
    not_allow_texts.append(u"收徒")
    not_allow_texts.append(u"查找")
    not_allow_texts.append(u"购")
    not_allow_texts.append(u"提升")
    not_allow_texts.append(u"仙化")
    not_allow_texts.append(u"详情")
    not_allow_texts.append(u"说明")
    not_allow_texts.append(u"摘除")
    not_allow_texts.append(u"开启")
    not_allow_texts.append(u"规则")
    not_allow_texts.append(u"充能")
    not_allow_texts.append(u"关闭")
    not_allow_texts.append(u"融合")
    not_allow_texts.append(u"传功")
    not_allow_texts.append(u"还童")
    not_allow_texts.append(u"突飞")
    not_allow_texts.append(u"突破")
    # not_allow_texts.append(u"研习")
    not_allow_texts.append(u"打造")
    not_allow_texts.append(u"记录")
    not_allow_texts.append(u"QQ")
    not_allow_texts.append(u"变更为")
    not_allow_texts.append(u"窥视")
    not_allow_texts.append(u"开通")
    not_allow_texts.append(u"战斗力")
    not_allow_texts.append(u"变强")
    not_allow_texts.append(u"替换任务")
    not_allow_texts.append(u"逐出帮派")
    not_allow_texts.append(u"调换")
    not_allow_texts.append(u"逐出师门")
    not_allow_texts.append(u"踢出")
    not_allow_texts.append(u"已乐斗")
    not_allow_texts.append(u"点击交易")
    not_allow_texts.append(u"回来玩吧")
    not_allow_texts.append(u"赠与")
    not_allow_texts.append(u"分解")
    not_allow_texts.append(u"放弃")
    not_allow_texts.append(u"师徒妻拜")
    not_allow_texts.append(u"背包")

    not_allow_url_parameters = list()
    not_allow_url_parameters.append({'cmd': 'lottery'})  # 武器弹珠
    not_allow_url_parameters.append({'cmd': 'cargo', 'op': '18'})  # 查看镖车
    not_allow_url_parameters.append({'cmd': 'view'})  # 查看
    not_allow_url_parameters.append({'cmd': 'missionassign', 'subtype': '6'})  # 查看镖车

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
            follow = True
            url_parameters = urlparse.parse_qs(urlparse.urlparse(url).query)
            for not_allow_url_parameter in self.not_allow_url_parameters:
                if len(not_allow_url_parameter) > 0 and all((k in url_parameters and v in url_parameters[k]) for k, v in
                                                            not_allow_url_parameter.iteritems()):
                    follow = False
                    break
            if not follow:
                continue
            br_text = self.get_same_br_text(href)
            if response.url.find('cmd=index&') == -1:
                if (br_text.find(u"斗豆") != -1 or br_text.find(u"斗币") != -1) and br_text.find(
                        u"领") == -1 and br_text.find(u"免费") == -1:
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

    def get_same_br_text(self, href):
        precedings = href.xpath('./preceding-sibling::*')
        followings = href.xpath('./following-sibling::*')
        result = href.xpath('./text()').extract()
        if len(result) > 0:
            result = result[0]
        for preceding in reversed(precedings):
            if 'br' in preceding.xpath('name(.)').extract():
                break
            else:
                for text in reversed(preceding.xpath('./descendant-or-self::*/text()').extract()):
                    result = text + '\n' + result
        for following in followings:
            if 'br' in following.xpath('name(.)').extract():
                break
            else:
                for text in following.xpath('./descendant-or-self::*/text()').extract():
                    result = result + '\n' + text
        return result