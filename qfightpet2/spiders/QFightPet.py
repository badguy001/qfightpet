# -*- coding: UTF-8 -*-

import scrapy
import re
import urlparse
import json
import time


class Daemon(scrapy.Spider):
    name = "qfightpet"
    username = str()
    time_limit = {}
    limit_file = 'time_limit.json'
    handle_httpstatus_list = [404]
    stat = dict({'null': 0})

    start_urls = list()
    start_urls.append("http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0")
    # start_urls.append("http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=missionassign&subtype=0")
    # start_urls.append("http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=buy&id=3108&num=1&type=1")  # 购买月卡
    # start_urls.append("http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=use&id=3108")  # 使用月卡

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
    # not_allow_texts.append(u"vip")
    not_allow_texts.append(u"变强")
    not_allow_texts.append(u"恢复")
    # not_allow_texts.append(u"达人")
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
    not_allow_texts.append(u"进阶")

    not_allow_url_parameters = list()
    not_allow_url_parameters.append({'cmd': 'lottery'})  # 武器弹珠
    not_allow_url_parameters.append({'cmd': 'cargo', 'op': '18'})  # 查看镖车
    not_allow_url_parameters.append({'cmd': 'view'})  # 查看
    not_allow_url_parameters.append({'cmd': "missionassign", 'subtype': '6'})  # 查看镖车
    not_allow_url_parameters.append({'cmd': 'friendlist', 'type': '1'})  # 斗友
    not_allow_url_parameters.append({'cmd': 'fame_hall'})  # 名人堂
    not_allow_url_parameters.append({'cmd': 'viewgoods'})  # 查看各种物品
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '1'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '2'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '3'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '4'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '5'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '6'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '7'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '8'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '9'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '10'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '11'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '12'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '13'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '14'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '15'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '16'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '17'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '18'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'mappush', 'subtype': '2', 'mapid': '19'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'factionhr', 'subtype': '5'})  # 不要变更帮派成员的职位
    not_allow_url_parameters.append({'cmd': 'sundry'})  # 禁用助手里面的设置
    not_allow_url_parameters.append({'cmd': 'forage_war', 'subtype': '3'})  # 掠夺战况
    not_allow_url_parameters.append({'cmd': 'forage_war', 'subtype': '2', 'op': '1'})  # 掠夺粮仓情况
    not_allow_url_parameters.append({'cmd': 'brofight', 'subtype': '13', 'detail': '1'})  # 不要查看结拜赛的队伍信息
    not_allow_url_parameters.append({'cmd': 'brofight', 'subtype': '12', 'detail': '1'})  # 不要查看兵法技能详情

    def parse(self, response):
        assert isinstance(response, scrapy.http.response.Response)
        tmp = urlparse.parse_qs(urlparse.urlparse(response.url).query)
        if "cmd" in tmp and len(tmp["cmd"]) > 0:
            if tmp["cmd"][0] in self.stat:
                self.stat[tmp["cmd"][0]] = self.stat[tmp["cmd"][0]] + 1
            else:
                self.stat[tmp["cmd"][0]] = 1
        else:
            self.stat["null"] = self.stat["null"] + 1
        self.judge_and_add_limit(response)
        if response.meta['depth'] >= self.settings.attributes['DEPTH_LIMIT'] or response.status == 404:
            return
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
            if self.judge_over_limit(url_parameters):
                continue
            self.judge_and_add_commit(url_parameters)
            yield scrapy.Request(url=url, callback=self.parse)

    def start_requests(self):
        with open('cookies.txt', 'r') as f:
            cookiejar = f.read()
            p = re.compile(r'([^\n]+)')
            cookies = re.findall(p, cookiejar)
            cookies = (cookie.split('=', 1) for cookie in cookies)
            cookies = dict(cookies)
        if "uin" in cookies:
            self.username = cookies["uin"]
        self.init_time_limit()
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    def closed(self, reason):
        print self.stat
        if len(self.time_limit) != 0:
            with open(self.limit_file, mode='w') as f:
                f.write(json.dumps(self.time_limit, indent=2, ensure_ascii=False).encode('utf-8'))

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

    # 访问返回结果后对访问次数进行增加
    def judge_and_add_limit(self, response):
        is_success = True
        if response.status == 404 or \
                any(text.find(u"很抱歉，系统繁忙，请稍后再试!") != -1 for text in response.xpath('//text()').extract()):
            is_success = False
        url_parameters = urlparse.parse_qs(urlparse.urlparse(response.url).query)
        for idx, one_par_limit in enumerate(self.time_limit["parameters_limits"]):
            if len(one_par_limit["par"]) > 0 and all((k in url_parameters and v in url_parameters[k]) for k, v in
                                                            one_par_limit["par"].iteritems()):
                if is_success:
                    self.time_limit["parameters_limits"][idx]["one_count"][self.username] = \
                        self.time_limit["parameters_limits"][idx]["one_count"][self.username] + 1
                    self.time_limit["parameters_limits"][idx]["day_count"][self.username] = \
                        self.time_limit["parameters_limits"][idx]["day_count"][self.username] + 1
                # 减少已经提交request但未返回的数量
                self.time_limit["parameters_limits"][idx]["commit_count"][self.username] = \
                    self.time_limit["parameters_limits"][idx]["commit_count"][self.username] - 1

    def judge_and_add_commit(self, url_parameters):
        for idx, one_par_limit in enumerate(self.time_limit["parameters_limits"]):
            if len(one_par_limit["par"]) > 0 and \
                    all((k in url_parameters and v in url_parameters[k]) for k, v in one_par_limit["par"].iteritems()):
                self.time_limit["parameters_limits"][idx]["commit_count"][self.username] = \
                    self.time_limit["parameters_limits"][idx]["commit_count"][self.username] + 1

    # 判断url是否超过了最大访问次数，考虑已经提交request但未返回的数据量
    def judge_over_limit(self, url_parameters):
        for one_par_limit in self.time_limit["parameters_limits"]:
            if len(one_par_limit["par"]) > 0 and \
                    all((k in url_parameters and v in url_parameters[k]) for k, v in one_par_limit["par"].iteritems()):
                if one_par_limit["day_limit"][self.username] != -1 and one_par_limit["day_count"][self.username] + \
                        one_par_limit["commit_count"][self.username] >= one_par_limit["day_limit"][self.username]:
                    return True
                if one_par_limit["one_limit"][self.username] != -1 and one_par_limit["one_count"][self.username] + \
                        one_par_limit["commit_count"][self.username] >= one_par_limit["one_limit"][self.username]:
                    return True
        return False

    def init_time_limit(self):
        default_username = "username"
        if self.username is None or self.username == "":
            return
        with open(self.limit_file, mode='r') as f:
            self.time_limit = json.loads(f.read())
        if self.username in self.time_limit["update_time"]:
            self.time_limit["last_update_time"][self.username] = self.time_limit["update_time"][self.username]
        else:
            self.time_limit["last_update_time"][self.username] = self.get_now_time()
        self.time_limit["update_time"][self.username] = self.get_now_time()
        is_diff_day = False
        if self.time_limit["update_time"][self.username][0:8] != \
                self.time_limit["last_update_time"][self.username][0:8]:
            is_diff_day = True
        for idx, one_par_limit in enumerate(self.time_limit["parameters_limits"]):
            if self.username not in one_par_limit["day_limit"]:
                self.time_limit["parameters_limits"][idx]["day_limit"][self.username] = \
                    self.time_limit["parameters_limits"][idx]["day_limit"][default_username]
            if self.username not in one_par_limit["one_limit"]:
                self.time_limit["parameters_limits"][idx]["one_limit"][self.username] = \
                    self.time_limit["parameters_limits"][idx]["one_limit"][default_username]
            self.time_limit["parameters_limits"][idx]["one_count"][self.username] = 0
            if is_diff_day or self.username not in one_par_limit["day_count"]:
                self.time_limit["parameters_limits"][idx]["day_count"][self.username] = 0
            self.time_limit["parameters_limits"][idx]["commit_count"][self.username] = 0

    def get_now_time(self):
        return time.strftime("%Y%m%d%H%M%S", time.localtime())
