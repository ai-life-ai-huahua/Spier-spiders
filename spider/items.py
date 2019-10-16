# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime





class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # type = scrapy.Field()
    # # 视频图片URL
    video_image_url = scrapy.Field()
    # 标题
    Title = scrapy.Field()
    keyno = scrapy.Field()
    # 内容描述
    Description = scrapy.Field()
    # 微信html
    html = scrapy.Field()
    # 命令行传入的uid
    uid = scrapy.Field()
    # 博主创建文章的时间
    release_time = scrapy.Field()
    # 平台类型
    PyInfoType = scrapy.Field()
    # 抓取类型(url爬取、自增爬取)
    CatchType = scrapy.Field()
    # 抓取url
    CatchUrl = scrapy.Field()
    Content = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    Imgs = scrapy.Field()













    #法人代码
    legalCode = scrapy.Field()

    #法定代表人姓名
    legalRepresent  =scrapy.Field()

    # 注册地-省
    registerProvince = scrapy.Field()

    #注册地-市
    registerCity = scrapy.Field()
    #法人机构类别
    legalType = scrapy.Field()
    #法人机构地址
    legalUnitAddress = scrapy.Field()

    #注册资本
    regCapital = scrapy.Field()

    #
    regUnit = scrapy.Field()

    #注册资本币种
    regCapCurrency = scrapy.Field()

    #联系人电话
    legalContactPhone = scrapy.Field()

    #邮箱（页面上没有）
    legalEmail = scrapy.Field()

    attachmentSetCode = scrapy.Field()

    basicAccountName = scrapy.Field()

    basicAccountNo = scrapy.Field()

    basicBank = scrapy.Field()

    basicBranchBank = scrapy.Field()


    bidderCodeType = scrapy.Field()

    creditRate = scrapy.Field()

    legalContactAddress = scrapy.Field()

    legalIndustry = scrapy.Field()

    legalName = scrapy.Field()

    legalRole = scrapy.Field()

    legalStatus = scrapy.Field()

    legalWeb = scrapy.Field()

    legalZipCode = scrapy.Field()

    licenseNo = scrapy.Field()

    #时间没转换
    dataTimestamp = scrapy.Field()

    # 时间没转换
    licenseEndDate = scrapy.Field()

    localTaxCertEndDate = scrapy.Field()

    #时间没转换
    localTaxCertNo = scrapy.Field()

    organCertEndDate = scrapy.Field()

    organNo = scrapy.Field()

    platfromCode = scrapy.Field()

    pubServicePlatCode = scrapy.Field()

    regionCode = scrapy.Field()

    rowguid = scrapy.Field()

    representPhone = scrapy.Field()

    taxCertEndDate = scrapy.Field()

    taxCertNo = scrapy.Field()

    danWeiGuid = scrapy.Field()
    danWeiType = scrapy.Field()
    type = scrapy.Field()


# class SpiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     #发布时间
#     publishTime = scrapy.Field()
#     #文章
#     article = scrapy.Field()
#     #标题
#     title = scrapy.Field()
#     #行政处罚决定书文号
#     articledministrativePenaltyDecisionNo = scrapy.Field()
#     #处罚名称
#     nameOfPenalty = scrapy.Field()
#     #处罚事由
#     theCauseOfThePunishment = scrapy.Field()
#     #处罚类别
#     typesOfPenalties = scrapy.Field()
#     #处罚依据
#     theBasisOfThePenalty = scrapy.Field()
#     #行政相对人名称
#     nameOfAdministrativeCounterpart = scrapy.Field()
#     #统一社会信用代码
#     unifiedSocialCreditCode = scrapy.Field()
#     #组织机构代码
#     organizationCode = scrapy.Field()
#     #工商登记码
#     businessRegistrationCode = scrapy.Field()
#     #税务登记号
#     taxRegistrationNumber = scrapy.Field()
#     #居民身份证号
#     residentIDNumber = scrapy.Field()
#     #法定代表人姓名
#     nameOfLegalRepresentative = scrapy.Field()
#     #处罚结果
#     resultsOfPenalties = scrapy.Field()
#     #处罚决定日期
#     penaltyDecisionDate = scrapy.Field()
#     #公示截止期
#     publicityDeadline = scrapy.Field()
#     #处罚机关
#     penaltyOrgans = scrapy.Field()
#     #当前状态
#     currentState = scrapy.Field()
#     #地方编码
#     localCoding = scrapy.Field()
#     #数据更新时间戳
#     dataUpdateTimestamp = scrapy.Field()
#     type = scrapy.Field()




