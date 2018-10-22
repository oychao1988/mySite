from manage import db


class LagouRecruit(db.Document):
    # 指定集合名称
    meta = {'collection': 'lagouRecruit',
            'ordering': ['-createTime'],
            'strict': False,
            }

    category = db.StringField()  # 工作类别
    category_url = db.StringField()  # 类别url

    adWord = db.StringField()
    appShow = db.StringField()  # 手机端显示
    approve = db.StringField()  # 同意
    businessZones = db.StringField()  # 商业区域
    city = db.StringField()  # 城市
    companyFullName = db.StringField()  # 公司全称
    companyId = db.StringField()  # 公司ID
    companyLabelList = db.StringField()  # 公司标签列表
    companyLogo = db.StringField()  # 公司logo
    companyShortName = db.StringField()  # 公司简称
    companySize = db.StringField()  # 公司规模
    createTime = db.StringField()  # 发布时间
    deliver = db.StringField()
    district = db.StringField()  # 地区
    education = db.StringField()  # 学历
    explain = db.StringField()
    financeStage = db.StringField()  # 融资阶段
    firstType = db.StringField()  # 工作类型1
    formatCreateTime = db.StringField()
    gradeDescription = db.StringField()
    hitags = db.StringField()
    imState = db.StringField()
    industryField = db.StringField()
    industryLables = db.StringField()
    isSchoolJob = db.StringField()
    jobNature = db.StringField()
    lastLogin = db.StringField()
    linestaion = db.StringField()
    latitude = db.StringField()  # 纬度
    longitude = db.StringField()  # 经度
    pcShow = db.StringField()  # PC端显示
    plus = db.StringField()
    positionAdvantage = db.StringField()  # 职位优势
    positionId = db.StringField()  # 职位编号
    positionLables = db.StringField()  # 职位标签
    positionName = db.StringField()  # 职位名称
    promotionScoreExplain = db.StringField()
    publisherId = db.StringField()
    resumeProcessDay = db.StringField()
    resumeProcessRate = db.StringField()
    salary = db.StringField()  # 薪资
    score = db.StringField()
    secondType = db.StringField()  # 工作类型2
    skillLables = db.StringField()  # 技能标签
    stationname = db.StringField()  # 站点名称
    subwayline = db.StringField()  # 地铁线路
    thirdType = db.StringField()  # 工作类型3
    workYear = db.StringField()  # 工作年限
    description = db.StringField()  # 职位描述

    def __str__(self):
        description = """companyFullName\t:%s,
                         createTime\t:%s,
                         positionName\t:%s,
                         salary\t:%s,
                         businessZones\t:%s
                      """ % (self.companyFullName, self.createTime, self.positionName, self.salary, self.businessZones)
        return description