# -*- coding: UTF-8 -*-

import scrapy
import re
import urlparse
import json
import time
import random
from urllib import urlencode
import requests
from operator import itemgetter
import math


class Daemon(scrapy.Spider):
    name = "qfightpet"
    username = str()
    myqq = str()
    mypackage = list()
    time_limit = {}
    limit_file = 'time_limit.json'
    handle_httpstatus_list = [404]
    stat = dict({'null': 0})
    my_level = 0  # 等级
    cookies = dict()

    start_urls = list()
    # start_urls.append("http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0")
    # start_urls.append(
    #     "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=oblation&id=3089")  # 供奉还魂丹
    # start_urls.append(
    #     "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=oblation&id=3181")  # 供奉传功符
    # start_urls.append(
    #     "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=use&id=3108")  # 使用月卡
    # start_urls.append(
    #     "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=use&id=3112")  # 使用周卡
    # start_urls.append(
    #     "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=secttournament&op=getrankandrankingreward")  # 门派邀请赛领奖
    # start_urls.append(
    #     "https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&sid=&channel=0&g_ut=1&cmd=newAct&op=exchange&subtype=52&type=1223&times=1")  # 登录活动兑换黄金卷轴
    start_urls.append(
        u"https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=dreamtrip")  # 登录活动兑换黄金卷轴

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
    # not_allow_texts.append(u"兵法")
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
    # not_allow_texts.append(u"复活")
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
    not_allow_texts.append(u"研习")
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
    not_allow_texts.append(u"任务派遣中心")
    not_allow_texts.append(u"上层心法")

    not_allow_url_parameters = list()
    not_allow_url_parameters.append({'cmd': 'lottery'})  # 武器弹珠
    not_allow_url_parameters.append({'cmd': 'cargo', 'op': '18'})  # 查看镖车
    not_allow_url_parameters.append({'cmd': 'view'})  # 查看
    not_allow_url_parameters.append({'cmd': "missionassign", 'subtype': '6'})  # 查看镖车
    not_allow_url_parameters.append({'cmd': 'friendlist', 'type': '1'})  # 斗友
    not_allow_url_parameters.append({'cmd': 'fame_hall'})  # 名人堂
    not_allow_url_parameters.append({'cmd': 'viewgoods'})  # 查看各种物品
    not_allow_url_parameters.append({'cmd': 'mappush'})  # 历练只去最后一级
    not_allow_url_parameters.append({'cmd': 'factionhr', 'subtype': '5'})  # 不要变更帮派成员的职位
    not_allow_url_parameters.append({'cmd': 'sundry'})  # 禁用助手里面的设置
    # not_allow_url_parameters.append({'cmd': 'forage_war', 'subtype': '3'})  # 掠夺战况
    not_allow_url_parameters.append({'cmd': 'forage_war', 'subtype': '2', 'op': '1'})  # 掠夺粮仓情况
    not_allow_url_parameters.append({'cmd': 'brofight', 'subtype': '13', 'detail': '1'})  # 不要查看结拜赛的队伍信息
    not_allow_url_parameters.append({'cmd': 'brofight', 'subtype': '6'})  # 不要查看结更多战况信息
    not_allow_url_parameters.append({'cmd': 'brofight', 'subtype': '12', 'detail': '1'})  # 不要查看兵法技能详情
    not_allow_url_parameters.append({'cmd': 'factionarmy', 'op': 'viewRevive'})  # 帮派远征不能重生（消耗斗豆）
    not_allow_url_parameters.append({'cmd': 'luandou', 'op': '1'})  # 乱斗刷新
    not_allow_url_parameters.append({'cmd': 'element', 'subtype': '8'})  # 遥控骰子
    # not_allow_url_parameters.append({'cmd': 'zodiacdungeon', 'op': 'backtolife'})  # 十二宫花斗豆复活
    not_allow_url_parameters.append({'cmd': 'showwulintop'})  # 查看武林战况
    not_allow_url_parameters.append({'cmd': 'wulinrank'})  # 查看武林战况
    not_allow_url_parameters.append({'cmd': 'sect_task', 'subtype': '1'})  # 门派任务花斗豆刷新委托人
    not_allow_url_parameters.append({'cmd': 'secttournament', 'op': 'showinvitee'})  # 门派邀请赛，不要邀请
    not_allow_url_parameters.append({'cmd': 'secttournament', 'op': 'quitfromgroup'})  # 门派邀请赛，不要退出队伍
    not_allow_url_parameters.append({'cmd': 'factiontrain', 'type': '1'})  # 帮修

    def parse(self, response):
        assert isinstance(response, scrapy.http.response.Response)
        tmp = urlparse.parse_qs(urlparse.urlparse(response.url).query)
        # 统计每种cmd访问的次数
        if "cmd" in tmp and len(tmp["cmd"]) > 0:
            if tmp["cmd"][0] in self.stat:
                self.stat[tmp["cmd"][0]] = self.stat[tmp["cmd"][0]] + 1
            else:
                self.stat[tmp["cmd"][0]] = 1
        else:
            self.stat["null"] = self.stat["null"] + 1
        # 获取任务等级
        if 'index' in tmp.get('cmd', ['none']):
            for ttt in response.xpath('//text()').extract():
                p = re.compile(u"等级:([0-9]+)")
                for l in p.findall(ttt):
                    self.my_level = int(l)
                    break
                if self.my_level != 0:
                    break
        # 增加访问次数
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
            # 幻境场景内全部乐斗完了则可以返回场景选择
            if text == u"返回飘渺幻境":
                follow = True
            if not follow:
                continue
            url = href.xpath('./@href').extract()
            if len(url) == 0:
                continue
            url = url[0]
            follow = True
            url = urlparse.urljoin(response.url, url)
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
                        u"领") == -1 and br_text.find(u"免费") == -1 and text != u"取消" and text != u"启程护送":
                    continue
            if self.judge_over_limit(url_parameters):
                continue
            # 问鼎天下只攻占没人占领的
            if "tbattle" in url_parameters.get("cmd", ["none"]) and "occupy" in url_parameters.get("op", ["none"]):
                if br_text.find(u"暂无") != -1 and br_text.find(u"240") != -1:
                    pass
                else:
                    continue
            # 镖行天下--选择镖师，尽量不要选择蔡八斗
            if "cargo" in tmp.get("cmd", ["none"]) and \
                    ("7" in tmp.get("op", ["none"]) or "8" in tmp.get("op", ["none"])):
                if u"免费刷新次数：0" not in response.xpath("//text()").extract():
                    if u"当前镖师：蔡八斗" in response.xpath("//text()").extract():
                        if u"启程护送" == text:
                            # 在可以刷新的情况下，如果是蔡八斗则刷新一次
                            continue
                elif u"刷新押镖" == text:
                    # 只能刷新一次
                    continue
            # 抢地盘
            if "manorfight" in url_parameters.get("cmd", ["none"]) and "1" in url_parameters.get("fighttype", ["none"]):
                if br_text.find(u"(30级)") != -1 or self.get_now_time()[7:9] >= "20":
                    pass
                else:
                    continue
            # 梦幻机票
            if "dreamtrip" in url_parameters.get("cmd", ["none"]) and "3" in url_parameters.get("sub", ["none"]):
                for tmp_text in response.xpath("//text()").extract():
                    if tmp_text.find(u"未去过") != -1:
                        url = url + "&" + urlencode({'dest': tmp_text.split(" ")[0].encode("utf-8")})
                        break
            if "dreamtrip" in tmp.get("cmd", ["none"]) and "3" in tmp.get("sub", ["none"]) and "dest" in tmp:
                if text == u"去这里" and br_text.find(tmp.get("dest")[0].decode("utf-8")) != -1:
                    pass
                else:
                    continue
            ##########################################
            # 后面不能再过滤url
            #  乐斗boss不计数
            if 'fight' in url_parameters.get('cmd', ['none']) and \
                    'B_UID' in url_parameters and len(url_parameters['B_UID']) > 0 and \
                    len(url_parameters['B_UID'][0]) <= 5:
                pass
            else:
                self.judge_and_add_commit(url_parameters)
            ###################################
            # 顺序控制
            priority = 0
            if u"侠侣" == text:
                priority = 75
            elif u"好友" == text:
                priority = 25
            # 乐斗顺序
            if 'fight' in url_parameters.get('cmd', ['none']):
                if '10' in url_parameters.get('type', ['none']):
                    priority = 25  # 侠侣乐斗
                if 'B_UID' in url_parameters and len(url_parameters['B_UID']) > 0 and \
                        len(url_parameters['B_UID'][0]) <= 5:
                    priority = 75  # 乐斗boss
            # 十二宫
            if 'zodiacdungeon' in url_parameters.get('cmd', ['none']):
                # 十二宫优先进入等级比自己高10级的场景
                if 'showautofightpage' in url_parameters.get('op', ['none']) or \
                        'showfightpage' in url_parameters.get('op', ['none']):
                    if br_text.find(str(self.my_level + 20 - (self.my_level + 20) % 5) + '-' +
                                    str(self.my_level + 25 - (self.my_level + 25) % 5)) != -1:
                        priority = 75
                # 优先选择复活buff
                if 'choosebuff' in url_parameters.get('op', ['none']):
                    priority = 75
                if any(v.find(u"本次复活需要") != -1 for v in response.xpath('//text()').extract()):
                    # 如果复活需要斗豆，则跳过复活
                    if text == u"确认复活":
                        continue
                elif text == u"直接结束":
                    # 如果复活无需斗豆，则不结束
                    continue
            # 任务委派
            if u"missionassign" in url_parameters.get("cmd", ["none"]):
                if u"2" in url_parameters.get(u"subtype", ["none"]):
                    if br_text.find(u"-S") != -1:
                        priority = 100
                        url = url + "&level=30"
                    elif br_text.find(u"-A") != -1:
                        priority = 90
                        url = url + "&level=20"
                    elif br_text.find(u"-B") != -1:
                        priority = 80
                        url = url + "&level=10"
                if text == u"快速委派":
                    priority = 30 + int(tmp.get("level", ["0"])[0])
                elif text == u"开始任务":
                    priority = 25 + int(tmp.get("level", ["0"])[0])
            ################################
            dont_filter = False
            if 'facchallenge' in url_parameters.get('cmd', ['none']) and '3' in url_parameters.get('subtype', ['none']):
                dont_filter = True
            yield scrapy.Request(url=url, callback=self.parse, priority=priority, dont_filter=dont_filter)

    def start_requests(self):
        with open('cookies.txt', 'r') as f:
            cookiejar = json.loads(f.read())
        cookies = dict()
        for ck in cookiejar:
            cookies[ck.get("name")] = ck.get("value")
        self.cookies = cookies
        self.username = cookies.get("uin", "")
        self.myqq = cookies.get("uin", "").lstrip("o").lstrip("0")
        self.init_time_limit()
        random.shuffle(self.start_urls)
        for url in self.start_urls:
            url_parameters = urlparse.parse_qs(urlparse.urlparse(url).query)
            if self.judge_over_limit(url_parameters):
                continue
            self.judge_and_add_commit(url_parameters)
            yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)
        buy_vip_db_url = "http://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?zapp_uin=&B_UID=0&sid=&channel=0&g_ut=1&cmd=viewgoods&id=3112&pay_type=7"
        yield scrapy.Request(url=buy_vip_db_url, callback=self.parse_vip, cookies=cookies)
        self.assignment()
        self.update_mypackage()
        self.auto_use_goods()
        self.upgrade_weapon_or_skill()
        self.mappush()
        self.newmercenary()
        self.weapon_awaken()
        self.achievement()
        self.doppelganger_weapon()
        self.doppelganger_skill()
        self.element()
        self.pearl()
        self.intfmerid()
        self.formation()
        self.inscription()
        self.astrolabe()
        self.weapon_specialize()
        self.ancient_god()
        self.gift()
        self.skillEnhance()
        self.sect_trump()
        self.sect_art()
        self.brofight()
        self.factiontrain()

    def closed(self, reason):
        print self.stat
        if len(self.time_limit) != 0:
            with open(self.limit_file, mode='w') as f:
                f.write(json.dumps(self.time_limit, indent=2, ensure_ascii=False).encode('utf-8'))

    def get_same_br_text(self, href):
        precedings = href.xpath('./preceding-sibling::* | ./preceding-sibling::text()')
        followings = href.xpath('./following-sibling::* | ./following-sibling::text()')
        result = href.xpath('./text()').extract()
        if len(result) > 0:
            result = result[0]
        for preceding in reversed(precedings):
            label_name = preceding.xpath('name(.)').extract()
            if len(label_name) == 0:
                result = preceding.extract() + '\n' + result
            elif 'br' in preceding.xpath('name(.)').extract():
                break
            else:
                for text in reversed(preceding.xpath('./descendant-or-self::*/text()').extract()):
                    result = text + '\n' + result
        for following in followings:
            label_name = following.xpath('name(.)')
            if len(label_name) == 0:
                result = result + '\n' + following.extract()
            elif 'br' in following.xpath('name(.)').extract():
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
        if self.time_limit["update_time"][self.username][8:10] >= '07' and self.time_limit["last_update_time"][
                                                                               self.username][8:10] < '07':
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

    def get_form_url(self, form_selector):
        url = urlparse.urlparse(form_selector.xpath("./@action").extract()[0])
        parameters = dict()
        for input_selector in form_selector.xpath("./input[@type='hidden']"):
            parameters[input_selector.xpath("./@name").extract()[0]] = input_selector.xpath("./@value").extract()[0]
        if 'num' in parameters:
            parameters['num'] = '1'
        url_parts = list(url)
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(parameters)
        url_parts[4] = urlencode(query)
        url = urlparse.urlunparse(url_parts)
        return url

    def parse_vip(self, response):
        for form_selector in response.xpath("//form"):
            url = self.get_form_url(form_selector)
            url = urlparse.urljoin(response.url, url)
            yield scrapy.Request(url=url, callback=self.parse_vip)

    def myreq(self, url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh - CN, zh;q = 0.9",
            "Referer": "http://fight.pet.qq.com/"
        }
        resp = requests.get(url, headers=headers, cookies=self.cookies)
        try:
            return json.loads(resp.text)
        except:
            return json.loads(resp.text.replace('\\', ''))

    # 任务委派处理
    def assignment(self):
        urls = dict()
        urls["get_base"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&op=0"
        urls["refresh"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&op=1"
        urls["get_award"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&mission_id=%s&op=8"
        urls["select_mem"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&mission_id=%s&op=6"
        urls["start"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&mission_id=%s&op=7"
        urls["get_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=assignment&mission_id=%s&op=4"
        miss_type = {
            "S": "1",
            "A": "2",
            "B": "3"
        }
        base_info = self.myreq(urls.get("get_base"))  # 任务基本信息
        if base_info.get("result") != "0":
            return
        max_num = int(base_info.get("dayMissionNum"))  # 一天可以接受的最大任务数量
        accepted_num = int(base_info.get("acceptedMissionNum"))  # 已经接受的任务数量
        this_accepted_num = 0  # 本次执行接受的任务数量
        # 先领奖励
        for accepted in base_info.get("acceptedMissionInfo"):
            if accepted.get("remainTime") == "0":
                tmp = self.myreq(urls.get("get_award") % accepted.get("missionId"))
        if accepted_num >= max_num:
            # 已经没有任务可以做了
            return
        base_info = self.myreq(urls.get("get_base"))  # 领完任务后刷新一次基本信息
        doing_num = len(base_info.get("acceptedMissionInfo"))  # 正在进行中的任务数量
        refresh_need_doudou = int(base_info.get("refreshDoudouNum")) > 0  # 刷新任务列表是否需要斗豆
        mission_list = base_info.get("standyMissionInfo")

        if all(miss.get("accepted") == "1" for miss in mission_list):
            # 所有的任务都正在做，则退出等待任务执行完后再看
            return
        # 先处理当前所有可接受任务都是B级的情况
        all_acceptable_is_b = all(
            m.get("accepted") == "0" and m.get("type") == miss_type.get("B") for m in mission_list)
        if all_acceptable_is_b and doing_num > 0:
            # 还有正在执行的任务，则等任务执行完后再看
            return
        elif all_acceptable_is_b and doing_num == 0 and refresh_need_doudou:
            # 无法免费刷新了，又没有在做的任务，则先接受一个B级任务
            for m in [miss for miss in mission_list if miss.get("accepted") == "0"]:
                tmp = self.myreq(urls.get("select_mem") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                tmp = self.myreq(urls.get("start") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                this_accepted_num = this_accepted_num + 1
                return  # 成功接受一个B级任务后就可以退出了
            # 到这里说明无法接受现有任务，也无法免费刷新任务，只能退出，等新的一天到来
            return
        elif all_acceptable_is_b and doing_num == 0 and not refresh_need_doudou:
            # 到这里说明可以免费刷新，则刷新一次后再判断（递归调这个方法即可）
            self.myreq(urls.get("refresh"))
            self.assignment()
            return
        # 找出所有可以接受的任务列表
        acceptable_num = 0
        for m in [n for n in mission_list if n.get("accepted") == "0" and n.get("type") != miss_type.get("B")]:
            # 通过能否选择佣兵来测试能否做这个任务
            tmp = self.myreq(urls.get("select_mem") % m.get("missionId"))
            if tmp.get("result") == "0":
                m["acceptable"] = True
                acceptable_num = acceptable_num + 1
            else:
                m["acceptable"] = False
        if acceptable_num == 0 and doing_num > 0:
            # 等正在做的任务完成后再看有没有可以做的任务
            return
        if acceptable_num == 0 and doing_num == 0 and refresh_need_doudou:
            for m in [n for n in mission_list if n.get("accepted") == "0" and n.get("type") == miss_type.get("B")]:
                tmp = self.myreq(urls.get("select_mem") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                tmp = self.myreq(urls.get("start") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                this_accepted_num = this_accepted_num + 1
                return  # 成功接受一个B级任务后就可以退出了
            # 到这里说明无法接受现有任务，也无法免费刷新任务，只能退出，等新的一天到来
            return
        if acceptable_num == 0 and doing_num == 0 and not refresh_need_doudou:
            tmp = self.myreq(urls.get("refresh"))
            self.assignment()
            return
        if any(m.get("type") == miss_type.get("S") and not m.get("acceptable") for m in mission_list):
            tmp = self.myreq(urls.get("get_detail") % m.get("missionId"))
            if tmp.get("result") == "-1":
                return
            # 如果待接受任务中有S级任务，但是现在却可能是佣兵被占用了导致接受不了，则等任务结束后再看
            if any(p.get("isQualified") == "1" and p.get("status") == "2" for p in tmp.get("mercernaryInfo")):
                return
        # 先做S级，在做A级
        for t in [miss_type.get("S"), miss_type.get("A")]:
            for m in [n for n in mission_list if n.get("type") == t and n.get("acceptable")]:
                tmp = self.myreq(urls.get("select_mem") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                tmp = self.myreq(urls.get("start") % m.get("missionId"))
                if tmp.get("result") != "0":
                    continue
                this_accepted_num = this_accepted_num + 1

    def update_mypackage(self):
        url = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=0&sub=2&type=4&selfuin=%s"
        resp = self.myreq(url % self.myqq)
        if resp.get("result") == "0":
            self.mypackage = resp.get("bag")

    def auto_use_goods(self):
        url = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=use&selfuin=%s&id=%s"
        for g in self.mypackage:
            if g.get("canuse") != "1":
                continue
            if not (g.get("name").endswith(u"信物") or g.get("name").endswith(u"宝箱") or \
                    g.get("name").endswith(u"锦囊") or g.get("name").find(u"经验") != -1 or \
                    g.get("name").find(u"阅历") != -1 or g.get("name").find(u"叉烧包") != -1 or \
                    g.get("name").find(u"礼盒") != -1 or g.get("name").find(u"巅峰") != -1 or \
                    g.get("name").find(u"内丹") != -1 or g.get("name").find(u"生命洗刷刷") != -1):
                continue
            tmp = self.myreq(url % (self.myqq, g.get("id")))
            while tmp.get("result") == "0":
                g["num"] = str(int(g["num"]) - 1)
                tmp = self.myreq(url % (self.myqq, g.get("id")))

    def upgrade_weapon_or_skill(self):
        urls = dict()
        urls["get_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=updatelist"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=update&id=%s"
        weapon_list = dict()
        skill_list = dict()
        upgrade_num = 0
        resp = self.myreq(urls.get("get_list"))
        if resp.get("result") != "0" or resp.get("gold_scroll_num") == "0":
            return
        weapon_list = resp.get("item")
        skill_list = resp.get("item1")
        # 从低升到高
        for w in weapon_list:
            w["mynum"] = int(w.get("num"))
        for w in skill_list:
            w["mynum"] = int(w.get("num"))
        weapon_list.sort(key=itemgetter("mynum"))
        skill_list.sort(key=itemgetter("mynum"))
        for w in weapon_list:
            if w.get("flag") != "1" or w.get("num") == "0" or int(w.get("num")) > int(resp.get("gold_scroll_num")) or \
                    w.get("percent") != u"必成":
                continue
            tmp = self.myreq(urls.get("upgrade") % w.get("picid"))
            resp["gold_scroll_num"] = str(int(resp.get("gold_scroll_num")) - int(w.get("num")))
            upgrade_num = upgrade_num + 1
        for w in skill_list:
            if w.get("flag") != "1" or w.get("num") == "0" or int(w.get("num")) > int(resp.get("gold_scroll_num")) or \
                    w.get("percent") != u"必成":
                continue
            tmp = self.myreq(urls.get("upgrade") % w.get("id"))
            resp["gold_scroll_num"] = str(int(resp.get("gold_scroll_num")) - int(w.get("num")))
            upgrade_num = upgrade_num + 1

    # 历练
    def mappush(self):
        urls = dict()
        urls["get_map_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=mappush&mapid=%s&type=2"
        urls["fight_npc"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=mappush&npcid=%s&type=1"
        urls["get_newmercenary_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&sub=0"
        base_newmercenary = list()  # 能在历练获取到的佣兵，以及对应的获取地图
        base_newmercenary.append(
            {
                "name": [u"令狐冲", u"真・令狐冲"],
                "mapid": "2",
                "npc": "6034"
            })
        base_newmercenary.append(
            {
                "name": [u"丘处机", u"奥・丘处机"],
                "mapid": "4",
                "npc": "6074"
            })
        base_newmercenary.append(
            {
                "name": [u"小龙女", u"娇・小龙女"],
                "mapid": "5",
                "npc": "6094"
            })
        base_newmercenary.append(
            {
                "name": [u"丁春秋", u"毒・丁春秋"],
                "mapid": "3",
                "npc": "6054"
            })
        base_newmercenary.append(
            {
                "name": [u"韦小宝", u"义・韦小宝"],
                "mapid": "6",
                "npc": "6114"
            })
        base_newmercenary.append(
            {
                "name": [u"赵敏", u"灵・赵敏"],
                "mapid": "10",
                "npc": "6194"
            })
        base_newmercenary.append(
            {
                "name": [u"扫地僧", u"宗・扫地僧"],
                "mapid": "7",
                "npc": "6134"
            })
        base_newmercenary.append(
            {
                "name": [u"鹤笔翁", u"冥・鹤笔翁"],
                "mapid": "8",
                "npc": "6154"
            })
        base_newmercenary.append(
            {
                "name": [u"韦一笑", u"血・韦一笑"],
                "mapid": "9",
                "npc": "6174"
            })
        base_info = self.myreq(urls.get("get_newmercenary_info"))
        if base_info.get("result") != "0":
            return
        own_newmercenary = base_info.get("array")  # 已经拥有的佣兵
        own_debris = base_info.get("debris_arr")  # 还没有的佣兵，但已经有碎片了
        # 找出能获取，但又还没有的佣兵列表
        for b in base_newmercenary:
            b["own"] = any(o.get("name") in b.get("name") for o in own_newmercenary)
            b["debris_num"] = 50
        for o in own_newmercenary:
            for b in base_newmercenary:
                if o.get("name") in b.get("name"):
                    b["debris_num"] = int(o.get("debris_need")) - int(o.get("debris"))
                    if b["debris_num"] == 0:
                        b["debris_num"] = -1  # -1表示无需再获取碎片了
        for o in own_debris:
            for b in base_newmercenary:
                if o.get("name") in b.get("name"):
                    b["debris_num"] = int(o.get("debris_need")) - int(o.get("debris"))
                    if b["debris_num"] == 0:
                        b["debris_num"] = 50
        # 对需要的碎片数和地图进行升序排序，先获取需要的碎片数少的
        base_newmercenary.sort(key=itemgetter("debris_num", "mapid"))
        # 按顺序去打npc
        for b in base_newmercenary:
            map_info = self.myreq(urls.get("get_map_info") % b.get("mapid"))
            if map_info.get("result") != "0":
                continue
            for npc in map_info.get("monster_infos_"):
                if npc.get("monster_id_") == b.get("npc"):
                    if npc.get("challenge_times_") == "0":
                        continue  # npc 没有挑战次数了
                    for i in range(1, int(npc.get("challenge_times_")) + 1):
                        tmp = self.myreq(urls.get("fight_npc") % b.get("npc"))
                        if tmp.get("result") == "876":
                            return  # 没有活力了
                        elif tmp.get("result") == "-1":
                            return  # 不知道什么错误
        # 这里说明还有活力，从高到低打npc，获取无字天书
        for i in range(20, 0, -1):
            map_info = self.myreq(urls.get("get_map_info") % str(i))
            if map_info.get("result") != "0":
                continue
            for npc in reversed(map_info.get("monster_infos_")):
                if npc.get("challenge_times_") in ["0", "-1"]:
                    continue
                elif int(npc.get("challenge_times_")) > 0:
                    for j in range(1, int(npc.get("challenge_times_")) + 1):
                        tmp = self.myreq(urls.get("fight_npc") % npc.get("monster_id_"))
                        if tmp.get("result") == "876":
                            return  # 没有活力了
                        elif tmp.get("result") == "-1":
                            return  # 不知道什么错误

    # 佣兵升级悟性和资质和等级
    def newmercenary(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&sub=0"
        urls["upgrade_wuxing"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&id=%s&sub=4"
        urls["upgrade_zizhi"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&id=%s&type=1&sub=5"
        urls["upgrade_zizhi2"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&id=%s&type=2&sub=5"
        urls["upgrade_level"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=newmercenary&id=%s&count=10&tfl=1&sub=3"
        base_info = self.myreq(urls.get("get_base_info"))
        if base_info.get("result") != "0":
            return
        # 升级资质，到卓越就可以
        for n in [m for m in base_info.get("array") if m.get("quality") != "3"]:
            while int(base_info.get("htzj")) > 0 and n.get("quality") != "3":
                # 有还童卷轴
                tmp = self.myreq(urls.get("upgrade_zizhi") % n.get("id"))
                base_info["htzj"] = str(int(base_info.get("htzj")) - 1)  # 数量减一
                if tmp.get("result") != "0":
                    break
                if any(y.get("id") == n.get("id") and y.get("quality") == "3" for y in tmp.get("array")):
                    n["quality"] = "3"
                    break  # 已经达到卓越了
            while int(base_info.get("htts")) > 0 and n.get("quality") != "3":
                # 有还童天书
                tmp = self.myreq(urls.get("upgrade_zizhi2") % n.get("id"))
                base_info["htts"] = str(int(base_info.get("htts")) - 1)  # 数量减一
                if tmp.get("result") != "0":
                    break
                if any(y.get("id") == n.get("id") and y.get("quality") == "3" for y in tmp.get("array")):
                    n["quality"] = "3"
                    break  # 已经达到卓越了
        for m in base_info.get("array"):
            m["mylevel"] = int(m.get("savvy"))
        base_info.get("array").sort(key=itemgetter("mylevel"))
        # 升级悟性
        for n in [m for m in base_info.get("array") if m.get("savvy") != "10"]:
            while True:
                if n.get("savvy") != "10" and base_info.get("wxd") > int(n.get("savvy")) / 2 + 1:
                    tmp = self.myreq(urls.get("upgrade_wuxing") % n.get("id"))
                    base_info["wxd"] = str(int(base_info.get("wxd")) - int(n.get("savvy")) / 2 + 1)  # 数量减一
                    if tmp.get("result") != "0":
                        break
                    for x in [y for y in tmp.get("array") if y.get("id") == n.get("id")]:
                        n["savvy"] = x.get("savvy")
                else:
                    tmp = self.myreq("http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=3013&times=1&subtype=2&op=exchange")
                    if tmp.get("result") != "0":
                        break
                    if tmp.get("msg").find(u"成功") == -1:
                        break
                    base_info["wxd"] = str(int(base_info.get("wxd")) + 2)
            break
        # 卓越和悟性10的可以加经验
        for n in [m for m in base_info.get("array") if
                  m.get("savvy") == "10" and m.get("quality") == "3" and int(m.get("lvl")) < 20]:
            if int(base_info.get("yueli")) > 1000 and int(n.get("lvl")) < 20:
                tmp = self.myreq(urls.get("upgrade_level"))
                base_info["yueli"] = tmp.get("yueli", "0")
                n["lvl"] = tmp.get("lvl", n.get("lvl"))
                if tmp.get("result") != "0":
                    continue

    # 武器觉醒
    def weapon_awaken(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=awaken"
        urls["upgrade_weapon"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=awaken&op=upgrade&base=%s&times=%s"
        bless_got_when_fail = 2
        base_info = self.myreq(urls.get("get_base_info"))
        if base_info.get("result", "-1") != "0":
            return
        for weapon in [w for w in base_info.get("infos") if
                       w.get("owned_weapon_id") != "0" and w.get("awaken_level") != "10"]:
            consume_goods_num = int(weapon.get("consume_goods_num"))
            consume_goods_owned_num = int(weapon.get("consume_goods_owned_num"))
            bless = int(weapon.get("bless"))
            max_bless = int(weapon.get("max_bless"))
            needed_bless_count = math.ceil(((max_bless - bless) / bless_got_when_fail)) + 1
            # 判断物品够不够用来升级
            if consume_goods_owned_num >= needed_bless_count * consume_goods_num:
                # 先10次10次的升
                for i in range(0, int(needed_bless_count * consume_goods_num / 10)):
                    tmp = self.myreq(urls.get("upgrade_weapon") % (weapon.get("weapon_base_id"), '10'))
                    if tmp.get("result") != "0":
                        return
                    if tmp.get("msg").find("失败") != -1:
                        continue
                    else:
                        return
                # 然后再一个一个升
                for i in range(0, int(needed_bless_count * consume_goods_num % 10)):
                    tmp = self.myreq(urls.get("upgrade_weapon") % (weapon.get("weapon_base_id"), '1'))
                    if tmp.get("result") != "0":
                        return
                    if tmp.get("msg").find("失败") != -1:
                        continue
                    else:
                        return

    # 徽章升级
    def achievement(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=achievement"
        urls[
            "upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=achievement&achievement_id=%s&times=%s&op=upgradelevel"
        base_info = self.myreq(urls.get("get_base_info"))
        if base_info.get("result") != "0":
            return
        base_info.get("badges").sort(key=itemgetter("level"))
        for x in [y for y in base_info.get("badges") if y.get("status") == "1" and y.get("level") != "7"]:
            tmp = self.myreq(urls.get("upgrade") % (x.get("achievement_id"), "1"))
            if tmp.get("result") != "0":
                return

    # 仙化武器
    def doppelganger_weapon(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=doppelganger&subtype=%s&op=2"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=doppelganger&id=%s&op=7"
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=18"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        base_info = self.myreq(urls.get("get_base_info") % "0")
        if base_info.get("result") != "0":
            return
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        for i in range(1, 4):
            tmp = self.myreq(urls.get("get_base_info") % str(i))
            if tmp.get("result") != "0":
                return
            for t in tmp.get("weapon"):
                base_info["weapon"].append(t)
        for t in base_info.get("weapon"):
            t["need_goods_num"] = int(t.get("updateGoodsNum"))
        base_info.get("weapon").sort(key=itemgetter("need_goods_num"))
        for weapon in [w for w in base_info.get("weapon") if
                       w.get("successRate") == u"必成" and w.get("need_goods_num") <= int(
                           base_info.get("updateGoodsHave")) + can_exchange_num.get(
                           base_info.get("updateGoodsName")).get("can_exchange_num")]:
            for i in range(0, weapon.get("need_goods_num") - int(base_info.get("updateGoodsHave"))):
                tmp = self.myreq(
                    urls.get("exchange") % can_exchange_num.get(base_info.get("updateGoodsName")).get("type"))
                if tmp.get("result") != "0":
                    return
            tmp = self.myreq(urls.get("upgrade") % weapon.get("baseId"))
            return

    # 仙化技能
    def doppelganger_skill(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=doppelganger&subtype=%s&op=3"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=doppelganger&id=%s&op=8"
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=18"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        base_info = self.myreq(urls.get("get_base_info") % "4")
        if base_info.get("result") != "0":
            return
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        for i in range(5, 7):
            tmp = self.myreq(urls.get("get_base_info") % str(i))
            if tmp.get("result") != "0":
                return
            for t in tmp.get("skill"):
                base_info["skill"].append(t)
        for t in base_info.get("skill"):
            t["need_goods_num"] = int(t.get("updateGoodsNum"))
        base_info.get("skill").sort(key=itemgetter("need_goods_num"))
        for weapon in [w for w in base_info.get("skill") if
                       w.get("successRate") == u"必成" and w.get("need_goods_num") <= int(
                           base_info.get("updateGoodsHave")) + can_exchange_num.get(
                           base_info.get("updateGoodsName")).get("can_exchange_num")]:
            for i in range(0, weapon.get("need_goods_num") - int(base_info.get("updateGoodsHave"))):
                tmp = self.myreq(
                    urls.get("exchange") % can_exchange_num.get(base_info.get("updateGoodsName")).get("type"))
                if tmp.get("result") != "0":
                    return
            tmp = self.myreq(urls.get("upgrade") % weapon.get("baseId"))
            if tmp.get("result") != "0":
                return

    # 五行升级
    def element(self):
        urls = dict()
        urls["get_element_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=element&subtype=0"
        urls["get_element_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=element&elementId=%s&subtype=1"
        urls["upgrade_element"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=element&elementId=%s&stoneNum=%s&subtype=2"
        urls["get_stone_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=element&subtype=3"
        urls["upgrade_stone"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=element&stoneId=%s&upTimes=%s&subtype=4"
        element_info = self.myreq(urls.get("get_element_info"))
        if element_info.get("result") != "0" or len(element_info.get("picInfo")) == 0:
            return
        # 拿出等级最小的那个来升级
        for e in element_info.get("picInfo"):
            e["mylevel"] = int(e.get("eLevel"))
        element_info.get("picInfo").sort(key=itemgetter("mylevel", "eId"))
        element = self.myreq(urls.get("get_element_detail") % element_info.get("picInfo")[0].get("eId"))
        if element.get("result") != "0":
            return
        need_radio = 900  # 成功概率至少要达到85%
        # 计算需要多少个石头才能达到规定的概率
        need_stone_num = int(math.ceil((need_radio - int(element.get("upRadio"))) / int(element.get("stoneRadio"))))
        # 当需要的石头名称
        need_stone_name = element.get("stone")
        while int(element.get("achievment")) >= int(element.get("needAchievment")) and \
                need_stone_num <= int(element.get("stoneNum")) and \
                need_stone_name == element.get("stone"):
            tmp = self.myreq(urls.get("upgrade_element") % (element.get("eId"), str(need_stone_num)))
            if tmp.get("result") != "0":
                break
            element = self.myreq(urls.get("get_element_detail") % element.get("eId"))
            need_stone_num = int(math.ceil((need_radio - int(element.get("upRadio"))) / int(element.get("stoneRadio"))))
        # 升级石头
        stone_info = self.myreq(urls.get("get_stone_info"))
        if stone_info.get("result") != "0":
            return
        for stone in stone_info.get("stoneList"):
            if stone.get("stoneName") == need_stone_name:
                stone_id = stone.get("stoneId")
        for stone in stone_info.get("stoneList"):
            if stone.get("stoneId") > stone_id:
                continue
            upgrade_num = int(min(int(stone.get("ownUpNeedNum")) / int(stone.get("upNeedNum")),
                                  int(stone_info.get("achievment")) / int(stone.get("upNeedAcievement"))))
            if upgrade_num > 0:
                tmp = self.myreq(urls.get("upgrade_stone") % (stone.get("stoneId"), upgrade_num))
                break  # 只升级一次石头

    def pearl(self):
        urls = dict()
        urls["get_upgrade_pearl_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=composepearl&exchangetype=2001"
        urls["upgrade_pearl_piece"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=composepearl&exchangetype=%s"
        urls["upgrade_pearl"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=upgradepearls&pearl=%s"
        urls["get_weapon_pearl_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=viewpearl"
        urls["upgrade_weapon_pearl"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=inlaypearls&weapon=%s&pearl=%s&pos=%s"
        upgrade_ids = {"1": "2001",
                       "2": "2000",
                       "3": "2004",
                       "4": "2002",
                       "5": "2005",
                       "6": "2003",
                       "7": "2006"}
        type_min_id = {"1": "4007",
                       "2": "4017",
                       "3": "4027",
                       "4": "4037",
                       "5": "4047",
                       "6": "4057",
                       "7": "4067"}
        upgrade_level_need_num = {"1": 3,
                                  "2": 3,
                                  "3": 3,
                                  "4": 6,
                                  "5": 2,
                                  "6": 2,
                                  "7": 10000000}
        pearl_info = self.myreq(urls.get("get_upgrade_pearl_detail"))
        if pearl_info.get("result") != "0" and pearl_info.get("result") != "-100":
            return
        # 升级一次碎片
        for i in range(1, 8):
            while True:
                piece = [p for p in pearl_info.get("piece") if p.get("type") == str(i) and int(p.get("num")) >= 5]
                if len(piece) == 0:
                    break
                pearl_info = self.myreq(urls.get("upgrade_pearl_piece") % upgrade_ids.get(str(i)))
                if pearl_info.get("result") != "0":
                    return
        # 武器
        weapon_pearl_info = self.myreq(urls.get("get_weapon_pearl_detail"))
        if weapon_pearl_info.get("result") != "0":
            return
        # 升级武器的魂珠
        for weapon in weapon_pearl_info.get("info"):
            for pearl in weapon.get("pearl"):
                if pearl.get("level") == "7" or pearl.get("id") == "0":
                    continue
                if type_min_id.get(pearl.get("type")) > pearl.get("id"):
                    type_min_id[pearl.get("type")] = pearl.get("id")
                for p in pearl_info.get("info"):
                    if p.get("id") == str(int(pearl.get("id")) + 1) and int(p.get("num")) > 0:
                        tmp = self.myreq(
                            urls.get("upgrade_weapon_pearl") % (
                                weapon.get("id"), p.get("id"), str(int(pearl.get("pos")) - 1)))
                        p["num"] = str(int(p.get("num")) - 1)
                        if tmp.get("result") != "0":
                            return
                        else:
                            break
        # 升级魂珠
        for pearl in pearl_info.get("info"):
            while True:
                if int(pearl.get("id")) > int(type_min_id.get(pearl.get("type"))) or \
                        int(pearl.get("num")) < upgrade_level_need_num.get(pearl.get("level")):
                    break  # 数量不够，或者还不能升级
                tmp = self.myreq(urls.get("upgrade_pearl") % pearl.get("id"))
                pearl["num"] = str(int(pearl.get("num")) - upgrade_level_need_num.get(pearl.get("level")))
                if tmp.get("result") != "0":
                    return

    # 经脉
    def intfmerid(self):
        urls = dict()
        urls["get_xiangjie_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid"
        urls["get_chuangong_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid&sub=3"
        urls["chuangong"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid&master=9004&sub=4"
        urls["zhuru"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid&sub=8&merid=%s&id=%s&idx=%s&cult=%s"
        urls["shiqu"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid&sub=7"
        urls["hecheng"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=intfmerid&sub=2"
        chuangong_info = self.myreq(urls.get("get_chuangong_info"))
        if chuangong_info.get("result") != "0":
            return
        # 传功
        if chuangong_info.get("master") == "9004" and int(chuangong_info.get("cgf")) > 7:
            for i in range(1, 20):
                tmp = self.myreq(urls.get("chuangong"))
                if tmp.get("result") != "0" or tmp.get("next_master") != "9004":
                    break
        chuangong_info = self.myreq(urls.get("get_chuangong_info"))
        if chuangong_info.get("result") != "0" or len(chuangong_info.get("intf_array")) == 0:
            return
        xiangjie_info = self.myreq(urls.get("get_xiangjie_info"))
        if xiangjie_info.get("result") != "0":
            return
        if len(xiangjie_info.get("intf_array")) < int(xiangjie_info.get("slot_num")):
            # 还有空位拾取一次
            tmp = self.myreq(urls.get("shiqu"))
        while True:
            xiangjie_info = self.myreq(urls.get("get_xiangjie_info"))
            if xiangjie_info.get("result") != "0":
                return
            # 找出升级需要点数最少的那个
            min_cult = {"id": "1", "need_cult": 1000000}
            for ini in xiangjie_info.get("merid_array"):
                if ini.get("intfid") == "0":
                    continue
                if int(ini.get("max_cult")) - int(ini.get("cur_cult")) < min_cult.get("need_cult"):
                    min_cult = ini
                    min_cult["need_cult"] = int(ini.get("max_cult")) - int(ini.get("cur_cult"))
            have_num = len(xiangjie_info.get("intf_array"))
            zhuru_num = 0
            for idx, ini in enumerate(xiangjie_info.get("intf_array")):
                # 先判断下这个筋脉有没有注入，没有的话则找个空位注入
                if not any(i.get("intfid") == ini.get("intfid") for i in xiangjie_info.get("merid_array")):
                    empty = [x for x in xiangjie_info.get("merid_array") if
                             x.get("intfid") == "0" and x.get("intf_type") == ini.get("intf_type")]
                    if len(empty) > 0:
                        empty = empty[0]
                        tmp = self.myreq(urls.get("zhuru") % (
                            empty.get("id"), ini.get("intfid"), str(idx - zhuru_num), ini.get("cur_cult")))
                        zhuru_num = zhuru_num + 1
                        if tmp.get("result") != "0":
                            return
                        continue
                # 再看有没有等级已经注入了，但等级比这个小的
                low_same = [i for i in xiangjie_info.get("merid_array") if
                            i.get("intfid") == ini.get("intfid") and int(i.get("cur_cult")) < int(ini.get("cur_cult"))]
                if len(low_same) > 0:
                    low_same = low_same[0]
                    tmp = self.myreq(urls.get("zhuru") % (
                        low_same.get("id"), ini.get("intfid"), str(idx - zhuru_num), ini.get("cur_cult")))
                    zhuru_num = zhuru_num + 1
                    if tmp.get("result") != "0":
                        return
                    continue
                # 注入
                if int(ini.get("cur_cult")) <= int(min_cult.get("cur_cult")):
                    tmp = self.myreq(urls.get("zhuru") % (
                        min_cult.get("id"), ini.get("intfid"), str(idx - zhuru_num), ini.get("cur_cult")))
                    zhuru_num = zhuru_num + 1
                    if tmp.get("result") != "0":
                        return
                    continue
            # 还有多余的全部合并
            if have_num - zhuru_num > 1:
                tmp = self.myreq(urls.get("hecheng"))
                if tmp.get("result") != "0":
                    return
            # 拾取不到了就退出
            tmp = self.myreq(urls.get("shiqu"))
            if tmp.get("result") != "0":
                break

    # 天书助阵
    def formation(self):
        urls = dict()
        urls[
            "get_formation_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=formation&index=%s&type=1&formationtype=1"
        urls[
            "active_formation"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=formation&index=%s&type=2&formationtype=1&attrindex=%s&formationid=%s"
        urls[
            "upgrade_formation"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=formation&formationtype=1&attrindex=%s&times=%s&index=%s&type=3&formationid=%s"
        consume_yueli_num = 40  # 升级一次消耗阅历
        consume_tianshu_num = 1  # 升级一次消耗天数
        get_exp_upgrade_one_time = 30  # 升级一次获得的经验
        active_consume_yueli_num = 200  # 激活需要消耗的阅历
        formation_info = self.myreq(urls.get("get_formation_detail") % "0")
        if formation_info.get("result") != "0" or formation_info.get("in_act_time") != "1" or formation_info.get(
                "isactivity") != "1":
            return
        # 先统一升级到5级
        for idx, f in enumerate(formation_info.get("formation")):
            if f.get("lock") != "1":
                continue
            formation = self.myreq(urls.get("get_formation_detail") % str(idx))
            if formation.get("result") != "0":
                return
            if any(int(ff.get("curpower")) < int(ff.get("power")) for ff in formation.get("mercenary")):
                continue  # 没有达到战力要求
            aidx = 0
            while aidx < len(formation.get("attrinfo")):
                attr = formation.get("attrinfo")[aidx]
                if attr.get("level") == "0":
                    # 先激活
                    tmp = self.myreq(urls.get("active_formation") % (str(idx), str(aidx), f.get("id")))
                    if tmp.get("result") != "0":
                        return
                    formation = tmp
                    continue
                if int(attr.get("level")) >= 5:
                    aidx = aidx + 1
                    continue  # 大于5级了就跳过
                upgrade_need_time = int(math.ceil(
                    (float(attr.get("exp")) - float(attr.get("curexp"))) / get_exp_upgrade_one_time))
                upgrade_time = min(int(float(formation.get("consumeitemnum")) / consume_tianshu_num),
                                   int(float(formation.get("yueli")) / consume_yueli_num), upgrade_need_time)
                if upgrade_time == 0:
                    return  # 没有天数或者阅历了
                elif upgrade_need_time != upgrade_time:
                    aidx = aidx + 1
                    continue
                tmp = self.myreq(
                    urls.get("upgrade_formation") % (str(aidx), str(upgrade_time), str(idx), f.get("id")))
                if tmp.get("result") != "0":
                    return
                formation = tmp
        # 所有已激活的都到了5级了，再逐个升级
        formation_info = self.myreq(urls.get("get_formation_detail") % "0")
        if formation_info.get("result") != "0" or formation_info.get("in_act_time") != "1" or formation_info.get(
                "isactivity") != "1":
            return
        for aidx, attr in enumerate(formation_info.get("attrinfo")):
            attr["aidx"] = aidx
            attr["idx"] = 0
            attr["id"] = formation_info.get("formation")[0].get("id")
            if attr.get("level") == "0" or attr.get("level") == "10":
                attr["exp"] = "1000000000000000"
            attr["need_exp"] = int(attr.get("exp")) - int(attr.get("curexp"))
        for idx in range(1, len(formation_info.get("formation"))):
            tmp = self.myreq(urls.get("get_formation_detail") % "0")
            if tmp.get("result") != "0":
                return
            for aidx, attr in enumerate(tmp.get("attrinfo")):
                attr["aidx"] = aidx
                attr["idx"] = idx
                attr["id"] = formation_info.get("formation")[idx].get("id")
                if attr.get("level") == "0" or attr.get("level") == "10":
                    attr["exp"] = "1000000000000000"
                attr["need_exp"] = int(attr.get("exp")) - int(attr.get("curexp"))
            formation_info.get("attrinfo").extend(tmp.get("attrinfo"))
        # 排序找出升级需要经验最少的一个
        formation_info.get("attrinfo").sort(key=itemgetter("need_exp"))
        attr = formation_info.get("attrinfo")[0]
        if attr.get("level") == "10":
            return
        upgrade_need_time = math.ceil(
            (int(attr.get("exp")) - int(attr.get("curexp"))) / get_exp_upgrade_one_time)
        upgrade_time = min(int(int(formation_info.get("consumeitemnum")) / consume_tianshu_num),
                           int(int(formation_info.get("yueli")) / consume_yueli_num), upgrade_need_time)
        if upgrade_time == 0 or upgrade_need_time != upgrade_time:
            return  # 没有天数或者阅历了
        tmp = self.myreq(
            urls.get("upgrade_formation") % (
                str(attr.get("aidx")), str(upgrade_time), str(attr.get("idx")), attr.get("id")))

    # 铭刻
    def inscription(self):
        urls = dict()
        urls[
            "get_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=inscription&type_id=%s&attr_id=%s&subtype=0&weapon_idx=%s"
        urls[
            "active"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=inscription&type_id=%s&attr_id=%s&subtype=1&weapon_idx=%s"
        urls[
            "upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=inscription&type_id=%s&attr_id=%s&subtype=2&times=%s&weapon_idx=%s"
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=14"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=2&type=%s&times=%s"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"铭刻" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 4
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["id"] = exc.get("type")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        # 将所有的属性构建成字典，如果有可以激活的，将在构建过程中直接激活
        max_type_id = 100
        type_id = 0
        goods_list = dict()
        attr_list = list()
        while type_id <= max_type_id:
            max_weapon_idx = 100
            weapon_idx = 0
            while weapon_idx <= max_weapon_idx:
                max_attr_idx = 100
                attr_idx = 0
                while attr_idx <= max_attr_idx:
                    tmp = self.myreq(urls.get("get_detail") % (str(type_id), str(attr_idx), str(weapon_idx)))
                    if tmp.get("result") != "0":
                        return
                    attr = dict()
                    attr["attr_idx"] = str(attr_idx)
                    attr["type_id"] = str(type_id)
                    attr["weapon_idx"] = str(weapon_idx)
                    attr["goods_name"] = tmp.get("goods_name")
                    attr["goods_consume"] = tmp.get("goods_consume")
                    attr["bless"] = tmp.get("bless")
                    attr["bless_limit"] = tmp.get("bless_limit")
                    attr["upgrade_need_bless"] = int(tmp.get("bless_limit")) - int(tmp.get("bless"))
                    attr["require_weapon_level"] = tmp.get("attr_list")[attr_idx].get("require")
                    attr["level"] = tmp.get("attr_list")[attr_idx].get("level")
                    attr["name"] = tmp.get("attr_list")[attr_idx].get("name")
                    attr["skill_name"] = tmp.get("skill_name")
                    attr["weapon_name"] = tmp.get("weapon_list")[weapon_idx].get("weapon_name")
                    attr["weapon_level"] = tmp.get("weapon_list")[weapon_idx].get("level")
                    if attr["weapon_level"] == "-1":
                        break  # 没有该武器，跳过
                    if attr["level"] == "-1" and attr["require_weapon_level"] <= attr["weapon_level"]:
                        # 需要激活
                        tmp = self.myreq(urls.get("active") % (str(type_id), str(attr_idx), str(weapon_idx)))
                        if tmp.get("result") != "0":
                            return
                        continue
                    if attr["level"] == "-1" and attr["require_weapon_level"] > attr["weapon_level"]:
                        break  # 无法激活及之后的属性
                    attr_list.append(attr)
                    goods_list[attr.get("goods_name")] = int(tmp.get("goods_have"))
                    if attr_idx == 0:
                        max_attr_idx = len(tmp.get("attr_list")) - 1
                    attr_idx = attr_idx + 1
                if weapon_idx == 0:
                    max_weapon_idx = len(tmp.get("weapon_list")) - 1
                weapon_idx = weapon_idx + 1
            if type_id == 0:
                max_type_id = len(tmp.get("insc_list")) - 1
            type_id = type_id + 1
        # 排序
        attr_list.sort(key=itemgetter("upgrade_need_bless"))
        for attr in attr_list:
            need_upgrade_time = int(math.ceil(float(attr.get("upgrade_need_bless")) / float(get_bless_when_fail))) + 1
            can_upgrade_time = int(goods_list.get(attr.get("goods_name")) / int(attr.get("goods_consume")))
            if can_upgrade_time < need_upgrade_time and (need_upgrade_time - can_upgrade_time) * int(
                    attr.get("goods_consume")) > can_exchange_num.get(attr.get("goods_name")).get("can_exchange_num"):
                continue
            for i in range(0, (need_upgrade_time - can_upgrade_time) * int(attr.get("goods_consume"))):
                tmp = self.myreq(urls.get("exchange") % (can_exchange_num.get(
                    attr.get("goods_name")).get("id"), "1"))
                if tmp.get("result") != "0":
                    return
            for i in range(1, need_upgrade_time + 1):
                tmp = self.myreq(
                    urls.get("upgrade") % (attr.get("type_id"), attr.get("attr_idx"), "1", attr.get("weapon_idx")))
                if tmp.get("result") != "0":
                    return
                if tmp.get("msg").find(u"失败") != -1:
                    continue
                return

    # 星盘
    def astrolabe(self):
        urls = dict()
        urls["get_astrolabe_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=index"
        urls["active"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=activate&star=%s"
        urls[
            "upgrade_directly"] = "https://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=upgradeinsocket&star=%s&socket=%s"
        urls["get_exchange1_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=13"
        urls["exchange1"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=%s&subtype=2"
        urls["insert"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=insert&star=%s&socket=%s&gem=%s"
        urls["get_exchange2_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=wlmz&op=view_exchange"
        urls["exchange2"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=wlmz&op=exchange&type_id=%s"
        urls["get_upgrade_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=viewupgrade&gem_type=%s"
        urls["upgrade"] = "https://fight.pet.qq.com/cgi-bin/petpk?cmd=astrolabe&op=upgrade&gem=%s"
        exchange_info = self.myreq(urls.get("get_exchange1_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        exchange_info = self.myreq(urls.get("get_exchange2_info"))
        if exchange_info.get("result") != "0":
            return
        for exc in exchange_info.get("exchange_goods_info"):
            e = dict()
            e["name"] = exc.get("goods_name")
            e["type"] = exc.get("type_id")
            e["id"] = exc.get("goods_id")
            e["can_exchange_num"] = int(int(exchange_info.get("points")) / int(exc.get("need_points"))) * int(
                exc.get("goods_num"))
            can_exchange_num[e.get("name")] = e
        astrolabe_info = self.myreq(urls.get("get_astrolabe_info"))
        if astrolabe_info.get("result") != "0":
            return
        # 激活
        for star in astrolabe_info.get("stars"):
            if star.get("activated") != "1":
                if int(star.get("required_skill_num")) <= int(astrolabe_info.get("skill_num")):
                    tmp = self.myreq(urls.get("active") % star.get("id"))
        astrolabe_info = self.myreq(urls.get("get_astrolabe_info"))
        if astrolabe_info.get("result") != "0":
            return
        gems = dict()
        for i in range(1, 9):
            upgrade_info = self.myreq(urls.get("get_upgrade_info") % str(i))
            if upgrade_info.get("result") != "0":
                return
            for gem in upgrade_info.get("gems"):
                gems[gem.get("id")] = gem.get("name")
        min_gem = dict()
        # 把空的填上
        for star in astrolabe_info.get("stars"):
            if star.get("activated") != "1":
                continue
            for idx in range(0, 2):
                s = star.get("sockets")[idx]
                if s.get("gem") != "0":
                    min_gem[gems.get(s.get("gem"))[2:5]] = min(min_gem.get(gems.get(s.get("gem"))[2:5], u"8级"),
                                                               gems.get(s.get("gem"))[0:2])
                    continue
                # 应该填什么石头
                if star.get("name").startswith(u"天"):
                    if any(gems.get(ss.get("gem"), "none").endswith(u"玛瑙石") for ss in star.get("sockets")):
                        gem = u"1级日曜石"
                    else:
                        gem = u"1级玛瑙石"
                else:
                    if any(gems.get(ss.get("gem"), "none").endswith(u"翡翠石") for ss in star.get("sockets")):
                        gem = u"1级月光石"
                    else:
                        gem = u"1级翡翠石"
                min_gem[gem[2:5]] = min(min_gem.get(gem[2:5], u"8级"), gem[0:2])
                # 背包里面有的话直接升级
                if any(goods.get("name") == gem for goods in self.mypackage):
                    self.myreq(urls.get("insert") % (star.get("id"), str(idx), can_exchange_num.get(gem).get("id")))
                    return
                # 背包没有则兑换
                if can_exchange_num.get(gem).get("can_exchange_num") >= 1:
                    self.myreq(urls.get("exchange1") % (can_exchange_num.get(gem).get("type"), "1"))
                    self.myreq(urls.get("insert") % (star.get("id"), str(idx), can_exchange_num.get(gem).get("id")))
                    return
            s = star.get("sockets")[2]
            if s.get("gem") != "0":
                min_gem[gems.get(s.get("gem"))[2:5]] = min(min_gem.get(gems.get(s.get("gem"))[2:5], u"8级"),
                                                           gems.get(s.get("gem"))[0:2])
                continue
            # 应该填什么石头
            if star.get("name").startswith(u"天"):
                gem = u"1级狂暴石"
            else:
                gem = u"1级神愈石"
            min_gem[gem[2:5]] = min(min_gem.get(gem[2:5], u"8级"), gem[0:2])
            # 背包里面有的话直接填
            if any(goods.get("name") == gem for goods in self.mypackage):
                tmp = self.myreq(urls.get("insert") % (star.get("id"), str(2), can_exchange_num.get(gem).get("id")))
                return
            # 背包没有则兑换
            if can_exchange_num.get(gem).get("can_exchange_num") >= 1:
                self.myreq(urls.get("exchange2") % can_exchange_num.get(gem).get("type"))
                self.myreq(urls.get("insert") % (star.get("id"), str(2), can_exchange_num.get(gem).get("id")))
                return
        upgrade_cost_detail = dict()
        # 升级石头
        for i in range(1, 9):
            upgrade_info = self.myreq(urls.get("get_upgrade_info") % str(i))
            if upgrade_info.get("result") != "0":
                return
            gem = upgrade_info.get("gems")[1].get("name")[2:5]
            for j in range(1, len(upgrade_info.get("gems"))):
                jj = upgrade_info.get("gems")[j]
                detail = dict()
                detail["name"] = jj.get("name")
                detail["id"] = jj.get("id")
                detail["upgrade_cost"] = int(jj.get("upgrade_cost"))
                detail["upgrade_directly_cost"] = int(jj.get("upgrade_cost")) - 1
                if j == 1:
                    detail["upgrade_cost_base"] = int(jj.get("upgrade_cost"))
                    detail["upgrade_directly_cost_base"] = int(jj.get("upgrade_cost")) - 1
                    detail["base_name"] = jj.get("name")
                    detail["had_base_number"] = int(jj.get("num"))
                else:
                    detail["upgrade_cost_base"] = int(jj.get("upgrade_cost")) * upgrade_cost_detail.get(
                        upgrade_info.get("gems")[j - 1].get("name")).get("upgrade_cost_base")
                    detail["upgrade_directly_cost_base"] = (int(jj.get("upgrade_cost")) - 1) * upgrade_cost_detail.get(
                        upgrade_info.get("gems")[j - 1].get("name")).get("upgrade_cost_base")
                    detail["base_name"] = upgrade_cost_detail.get(
                        upgrade_info.get("gems")[j - 1].get("name")).get("base_name")
                    detail["had_base_number"] = int(jj.get("num")) * detail.get("upgrade_cost_base") / detail.get(
                        "upgrade_cost") + upgrade_cost_detail.get(upgrade_info.get("gems")[j - 1].get("name")).get(
                        "had_base_number")
                detail["had_num"] = int(jj.get("num"))
                detail["upgrade_directly_still_need_base_num"] = detail.get("upgrade_directly_cost_base") - detail.get(
                    "had_base_number")
                upgrade_cost_detail[jj.get("name")] = detail
                if jj.get("name")[0:2] >= min_gem.get(gem):
                    continue
                if int(jj.get("num")) < int(jj.get("upgrade_cost")):
                    continue
                self.myreq(urls.get("upgrade") % jj.get("id"))
                return
        astrolabe_info = self.myreq(urls.get("get_astrolabe_info"))
        if astrolabe_info.get("result") != "0":
            return
        sockets = list()
        for star in astrolabe_info.get("stars"):
            if star.get("activated") != "1":
                continue
            for sidx in range(0, len(star.get("sockets"))):
                socket = star.get("sockets")[sidx]
                if socket.get("gem") == "0":
                    continue
                s = dict()
                s["star_id"] = star.get("id")
                s["star_name"] = star.get("name")
                s["socket_index"] = sidx
                s["upgrade_need_name"] = \
                    [one for one in upgrade_cost_detail if upgrade_cost_detail.get(one).get("id") == socket.get("gem")][
                        0]
                s["upgrade_need_base_name"] = upgrade_cost_detail.get(s.get("upgrade_need_name")).get("base_name")
                s["upgrade_need_base_num"] = upgrade_cost_detail.get(s.get("upgrade_need_name")).get(
                    "upgrade_directly_still_need_base_num")
                s["had_num"] = upgrade_cost_detail.get(s.get("upgrade_need_name")).get("had_num")
                s["upgrade_need_num"] = upgrade_cost_detail.get(s.get("upgrade_need_name")).get("upgrade_directly_cost")
                if s.get("upgrade_need_name")[0:2] > min_gem.get(s.get("upgrade_need_name")[2:5]):
                    continue
                sockets.append(s)
        if len(sockets) == 0:
            return
        sockets.sort(key=itemgetter("upgrade_need_base_num", "star_id", "socket_index"))
        if sockets[0].get("upgrade_need_base_num") <= 0:
            socket = sockets[0]
            if socket.get("had_num") >= socket.get("upgrade_need_num"):
                tmp = self.myreq(urls.get("upgrade_directly") % (socket.get("star_id"), socket.get("socket_index")))
            return
        for socket in sockets:
            if not socket.get("upgrade_need_name").endswith(u"狂暴石") and not socket.get("upgrade_need_name").endswith(
                    u"神愈石"):
                continue
            if can_exchange_num.get(socket.get("upgrade_need_base_name")).get("can_exchange_num") >= 1:
                tmp = self.myreq(
                    urls.get("exchange2") % can_exchange_num.get(socket.get("upgrade_need_base_name")).get("type"))
            break
        for socket in sockets:
            if socket.get("upgrade_need_name").endswith(u"狂暴石") or socket.get("upgrade_need_name").endswith(u"神愈石"):
                continue
            if can_exchange_num.get(socket.get("upgrade_need_base_name")).get("can_exchange_num") >= 1:
                tmp = self.myreq(urls.get("exchange1") % (
                    can_exchange_num.get(socket.get("upgrade_need_base_name")).get("type"), "1"))
            break

    # 专精
    def weapon_specialize(self):
        urls = dict()
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=8"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=weapon_specialize&type_id=%s&op=0"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=weapon_specialize&type_id=%s&op=1"
        urls["get_storage_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=weapon_specialize&storage_id=%s&op=3"
        urls["upgrade_storage"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=weapon_specialize&storage_id=%s&op=4"
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"专精" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 6  # 四阶五星前6点，其他5点
        base_info = list()
        storage_info = list()
        for type_id in range(0, 4):
            tmp = self.myreq(urls.get("get_base_info") % str(type_id))
            b = dict()
            b["type_id"] = str(type_id)
            b["bless"] = int(tmp.get("bless"))
            b["bless_limit"] = int(tmp.get("bless_limit"))
            b["level"] = int(tmp.get("level"))
            b["name"] = tmp.get("name")[0:2]
            if b.get("name") <= u"四阶" and b.get("level") <= 5:
                b["get_bless_when_fail"] = 6
            else:
                b["get_bless_when_fail"] = 5
            b["goods_have"] = int(tmp.get("update_goods_have"))
            b["goods_name"] = tmp.get("update_goods_name")
            b["goods_needs"] = int(tmp.get("update_goods_needs"))
            b["still_need_goods_num"] = int(math.ceil(
                float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
                "goods_needs") - b.get("goods_have")
            base_info.append(b)
            for storage in tmp.get("storages"):
                if storage.get("active_info") != "":
                    continue
                tmp = self.myreq(urls.get("get_storage_info") % storage.get("storage_id"))
                if tmp.get("result") != "0":
                    return
                s = dict()
                s["storage_id"] = storage.get("storage_id")
                s["bless_limit"] = int(tmp.get("bless_limit"))
                s["bless"] = int(tmp.get("bless"))
                s["goods_have"] = int(tmp.get("update_goods_have"))
                s["goods_name"] = tmp.get("update_goods_name")
                s["goods_needs"] = int(tmp.get("update_goods_needs"))
                s["get_bless_when_fail"] = 4
                s["still_need_goods_num"] = int(math.ceil(
                    float(s.get("bless_limit") - s.get("bless")) / float(s.get("get_bless_when_fail"))) + 1) * s.get(
                    "goods_needs") - s.get("goods_have")
                storage_info.append(s)
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = base_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("type_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"成功") != -1:
                        return  # 升级成功
        storage_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = storage_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade_storage") % min_one.get("storage_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"成功") != -1:
                        return  # 升级成功

    # 神魔录
    def ancient_god(self):
        urls = dict()
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=19"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=ancient_god&id=%s&op=1"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=ancient_god&id=%s&times=1&op=3"
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"神魔录" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 4  # 五阶五星前4点，其他2点
        base_info = list()
        for i in range(1, 5):
            tmp = self.myreq(urls.get("get_base_info") % str(i))
            if tmp.get("result") != "0":
                return
            b = dict()
            b["bless"] = int(tmp.get("bless"))
            b["blessLimit"] = int(tmp.get("blessLimit"))
            b["goodsConsume"] = int(tmp.get("goodsConsume"))
            b["goodsHave"] = int(tmp.get("goodsHave"))
            b["goodsName"] = tmp.get("goodsName")
            b["stage"] = tmp.get("stage")
            b["id"] = str(i)
            if tmp.get("stage") < u"5阶5级":
                b["bless_get_when_fail"] = 4
            else:
                b["bless_get_when_fail"] = 2
            b["still_need_goods_num"] = int(int(math.ceil(
                float(b.get("blessLimit") - b.get("bless")) / float(b.get("bless_get_when_fail")))) + 1) * b.get(
                "goodsConsume") - b.get("goodsHave")
            base_info.append(b)
        base_info.sort(key=itemgetter("still_need_goods_num", "id"))
        min_one = base_info[0]
        while True:
            if min_one.get("goodsHave") >= min_one.get("goodsConsume"):
                tmp = self.myreq(urls.get("upgrade") % min_one.get("id"))
                min_one["goodsHave"] = min_one.get("goodsHave") - min_one.get("goodsConsume")
                if tmp.get("result") != "0":
                    return
                if tmp.get("msg").find(u"成功") != -1:
                    break
            else:
                if can_exchange_num.get(min_one.get("goodsName")).get("can_exchange_num") >= min_one.get(
                        "goodsConsume") - min_one.get("goodsHave"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goodsName")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goodsHave"] = min_one.get("goodsHave") + 1
                    can_exchange_num.get(min_one.get("goodsName"))["can_exchange_num"] = can_exchange_num.get(
                        min_one.get("goodsName")).get("can_exchange_num") - 1
                else:
                    break

    # 礼物
    def gift(self):
        urls = dict()
        urls["send"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchangegifts&op=send&recipient=%s"
        urls["send_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchangegifts&op=query"
        urls["rec_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchangegifts&op=msg"
        urls["rec"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchangegifts&op=receive&id=%s"
        qqs = ["1417650155", "409966172", "3326703801", "1129426277"]
        send_info = self.myreq(urls.get("send_info"))
        if send_info.get("result") != "0":
            return
        for qq in qqs:
            if self.myqq == qq:
                continue
            for s in send_info.get("friends_info"):
                if s.get("can_send") == "2":
                    continue
                if qq != s.get("uin"):
                    continue
                tmp = self.myreq(urls.get("send") % qq)
        rec_info = self.myreq(urls.get("rec_info"))
        if rec_info.get("result") != "0":
            return
        already_rec = list()
        for r in rec_info.get("notifications"):
            if r.get("uin") in already_rec:
                continue
            tmp = self.myreq(urls.get("rec") % r.get("id"))
            already_rec.append(r.get("uin"))

    # 奥义
    def skillEnhance(self):
        urls = dict()
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=17"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=skillEnhance&op=0"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=skillEnhance&op=1"
        urls["get_storage_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=skillEnhance&storageId=%s&op=3"
        urls["upgrade_storage"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=skillEnhance&storageId=%s&op=4"
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"技能奥义" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 4  # 五阶五星前4点，其他2点
        base_info = list()
        storage_info = list()
        tmp = self.myreq(urls.get("get_base_info"))
        if tmp.get("result") != "0":
            return
        b = dict()
        b["bless"] = int(tmp.get("bless"))
        b["bless_limit"] = int(tmp.get("blessLimit"))
        b["level"] = int(tmp.get("level"))
        b["star"] = int(tmp.get("star"))
        if b.get("star") <= 5 and b.get("level") % 5 - 1 <= 5:
            b["get_bless_when_fail"] = 4
        else:
            b["get_bless_when_fail"] = 2
        b["goods_have"] = int(tmp.get("updateGoodsHave"))
        b["goods_name"] = tmp.get("updateGoodsName")
        b["goods_needs"] = int(tmp.get("updateGoodsCosume"))
        b["still_need_goods_num"] = int(math.ceil(
            float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
            "goods_needs") - b.get("goods_have")
        base_info.append(b)
        for storage in tmp.get("storage"):
            if storage.get("skillName") == u"未激活":
                continue
            tmp = self.myreq(urls.get("get_storage_info") % storage.get("storage_id"))
            if tmp.get("result") != "0":
                return
            s = dict()
            s["storage_id"] = storage.get("storage_id")
            s["bless_limit"] = int(tmp.get("bless_limit"))
            s["bless"] = int(tmp.get("bless"))
            s["goods_have"] = int(tmp.get("update_goods_have"))
            s["goods_name"] = tmp.get("update_goods_name")
            s["goods_needs"] = int(tmp.get("update_goods_needs"))
            s["get_bless_when_fail"] = 4
            s["still_need_goods_num"] = int(math.ceil(
                float(s.get("bless_limit") - s.get("bless")) / float(s.get("get_bless_when_fail"))) + 1) * s.get(
                "goods_needs") - s.get("goods_have")
            storage_info.append(s)
        if len(base_info) == 0:
            return
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = base_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"成功") != -1:
                        return  # 升级成功
        storage_info.sort(key=itemgetter("still_need_goods_num"))
        if len(storage_info) == 0:
            return
        min_one = storage_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade_storage") % min_one.get("storage_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"成功") != -1:
                        return  # 升级成功

    # 门派武器技能
    def sect_trump(self):
        urls = dict()
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=16"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_trump&subtype=0"
        urls["get_base_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_trump&trump_id=%s&subtype=1"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_trump&trump_id=%s&times=1&subtype=2"
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"门派" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 4
        base_info = list()
        tmp_base_info = self.myreq(urls.get("get_base_info"))
        if tmp_base_info.get("result") != "0":
            return
        for one in tmp_base_info.get("trumps"):
            if one.get("level") == "-1":
                continue
            b = dict()
            tmp = self.myreq(urls.get("get_base_detail") % one.get("id"))
            if tmp.get("result") != "0":
                return
            b["bless"] = int(tmp.get("bless"))
            b["trump_id"] = tmp.get("trump_id")
            b["bless_limit"] = int(tmp.get("bless_limit"))
            b["level"] = int(tmp.get("level"))
            b["max_level"] = int(tmp.get("max_level"))
            if b.get("level") >= b.get("max_level"):
                continue
            b["get_bless_when_fail"] = 4
            b["goods_have"] = int(tmp.get("consume_desc").split("*")[1].split("/")[1])
            b["goods_name"] = tmp.get("consume_desc").split("*")[0]
            b["goods_needs"] = int(tmp.get("consume_desc").split("*")[1].split("/")[0])
            b["still_need_goods_num"] = int(math.ceil(
                float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
                "goods_needs") - b.get("goods_have")
            base_info.append(b)
        if len(base_info) == 0:
            return
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = base_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("trump_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"成功") != -1:
                        return  # 升级成功

    # 门派上层心法
    def sect_art(self):
        urls = dict()
        urls["get_exchange_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&subtype=16"
        urls["exchange"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=exchange&type=%s&times=1&subtype=2"
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_sect_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_art&subtype=0&sect_id=%s"
        urls["get_base_detail"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_art&subtype=1&art_id=%s"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=sect_art&times=1&subtype=2&art_id=%s"
        exchange_info = self.myreq(urls.get("get_exchange_info"))
        if exchange_info.get("result") != "0":
            return
        can_exchange_num = dict()
        for exc in exchange_info.get("items"):
            e = dict()
            e["name"] = exc.get("name")
            e["type"] = exc.get("type")
            e["id"] = exc.get("id")
            e["can_exchange_num"] = int(
                int(exchange_info.get("values").get(exc.get("needs_id"))) / int(exc.get("needs_num"))) * int(
                exc.get("num"))
            can_exchange_num[e.get("name")] = e
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(u"门派" != active.get("name") for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 1
        sect_info = self.myreq(urls.get("get_sect_info"))
        if sect_info.get("result") != "0":
            return
        base_info = list()
        tmp_base_info = self.myreq(urls.get("get_base_info") % sect_info.get("sect"))
        if tmp_base_info.get("result") != "0":
            return
        for one in tmp_base_info.get("arts"):
            if one.get("desc").find(u"基础") != -1:
                continue
            b = dict()
            tmp = self.myreq(urls.get("get_base_detail") % one.get("id"))
            if tmp.get("result") != "0":
                return
            b["bless"] = int(tmp.get("exp"))
            b["art_id"] = tmp.get("art_id")
            b["bless_limit"] = int(tmp.get("exp_limit"))
            b["level"] = int(tmp.get("level"))
            b["max_level"] = int(tmp.get("max_level"))
            if b.get("level") >= b.get("max_level"):
                continue
            b["get_bless_when_fail"] = 1
            b["goods_have"] = int(tmp.get("consume_desc").split("*")[1].split("/")[1])
            b["goods_name"] = tmp.get("consume_desc").split("*")[0]
            b["goods_needs"] = int(tmp.get("consume_desc").split("*")[1].split("/")[0])
            b["still_need_goods_num"] = int(math.ceil(
                float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
                "goods_needs") - b.get("goods_have")
            base_info.append(b)
        if len(base_info) == 0:
            return
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = base_info[0]
        if min_one.get("still_need_goods_num") <= can_exchange_num.get(min_one.get("goods_name")).get(
                "can_exchange_num") + min_one.get("goods_have"):
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    tmp = self.myreq(urls.get("exchange") % can_exchange_num.get(min_one.get("goods_name")).get("type"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") + 1
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("art_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"升级了") != -1:
                        return  # 升级成功


    # 兵法
    def brofight(self):
        urls = dict()
        urls["get_active_list"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=view&kind=5&selfuin=%s"
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=brofight&subtype=5"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=brofight&skill_base_id=%s&subtype=4"
        tmp = self.myreq(urls.get("get_active_list") % self.myqq)
        if tmp.get("result") != "0":
            return
        if all(active.get("name").find(u"兵法") == -1 for active in tmp.get("act_array")):
            get_bless_when_fail = 2  # 不再活动时间范围内
            return
        else:
            get_bless_when_fail = 1
        base_info = list()
        tmp_base_info = self.myreq(urls.get("get_base_info"))
        if tmp_base_info.get("result") != "0":
            return
        for tmp in tmp_base_info.get("skills"):
            b = dict()
            b["bless"] = int(tmp.get("progress"))
            b["base_id"] = tmp.get("base_id")
            b["bless_limit"] = 100
            b["level"] = int(tmp.get("level"))
            b["get_bless_when_fail"] = 1
            if tmp.get("base_id").startswith("25"):
                b["goods_have"] = int(tmp_base_info.get("art_of_war_count"))
                b["goods_name"] = u"孙子兵法"
            else:
                b["goods_have"] = int(tmp_base_info.get("wumu_yishu_count"))
                b["goods_name"] = u"武穆遗书"
            b["goods_needs"] = int(tmp.get("cost"))
            b["still_need_goods_num"] = int(math.ceil(
                float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
                "goods_needs") - b.get("goods_have")
            base_info.append(b)
        if len(base_info) == 0:
            return
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = [b for b in base_info if b.get("base_id").startswith("25")]
        if len(min_one) > 0:
            min_one = min_one[0]
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    break
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("base_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"升级了") != -1:
                        break  # 升级成功
        min_one = [b for b in base_info if not b.get("base_id").startswith("25")]
        if len(min_one) > 0:
            min_one = min_one[0]
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    break
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("base_id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"升级了") != -1:
                        break  # 升级成功

    # 帮派修炼
    def factiontrain(self):
        urls = dict()
        urls["get_base_info"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=factiontrain&type=1"
        urls["upgrade"] = "http://fight.pet.qq.com/cgi-bin/petpk?cmd=factiontrain&type=2&id=%s&times=1"
        base_info = list()
        tmp_base_info = self.myreq(urls.get("get_base_info"))
        if tmp_base_info.get("result") != "0":
            return
        for tmp in tmp_base_info.get("array"):
            b = dict()
            b["bless"] = int(tmp.get("cur_lvl_exp").split("/")[0])
            b["id"] = tmp.get("id")
            b["bless_limit"] = int(tmp.get("cur_lvl_exp").split("/")[1])
            b["level"] = int(tmp.get("level"))
            b["get_bless_when_fail"] = 20
            b["goods_have"] = int(tmp_base_info.get("new_contrib"))
            b["goods_needs"] = int(tmp.get("sub_banggong"))
            b["still_need_goods_num"] = int(math.ceil(
                float(b.get("bless_limit") - b.get("bless")) / float(b.get("get_bless_when_fail"))) + 1) * b.get(
                "goods_needs") - b.get("goods_have")
            base_info.append(b)
        if len(base_info) == 0:
            return
        base_info.sort(key=itemgetter("still_need_goods_num"))
        min_one = base_info
        if len(min_one) > 0:
            min_one = min_one[0]
            while True:
                if min_one.get("goods_have") < min_one.get("goods_needs"):
                    break
                else:
                    tmp = self.myreq(urls.get("upgrade") % min_one.get("id"))
                    if tmp.get("result") != "0":
                        return
                    min_one["goods_have"] = min_one.get("goods_have") - min_one.get("goods_needs")
                    if tmp.get("msg").find(u"升级了") != -1:
                        break  # 升级成功