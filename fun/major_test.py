from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017, username="admin", password="123456")

# 指定数据库和集合
db = client.school
collection = db.test

col = collection.find_one({}, {'_id': 0})
li = collection.find_one({'type': '理科'}, {'_id': 0})
li_ls = list(li['batch'].keys())

wen = collection.find_one({'type': '文科'}, {'_id': 0})
wen_ls = list(wen['batch'].keys())

new = {
    'type': '理科',
    'batch': {
        '西南石油大学': [['本科一批A段', 552, 14898], ['本科一批B段', 480, 42972]],
        '西华大学': [['本科一批B段', 508, 30280], ['本科二批A段', 467, 49693]],
        '重庆理工大学': [['本科二批A段', 475, 45517]],
        '成都信息工程大学': [['本科一批B段', 486, 40012]],
        '山东师范大学': [['本科一批B段', 480, 42972]],
        '海南师范大学': [['本科一批B段', 480, 42972], ['本科二批A段', 479, 43455]],
        '海南医科大学': [['本科一批B段', 495, 35885], ['本科二批A段', 441, 64867], ['本科二批A段', 398, 93042]],
        '琼台师范学院': [['本科二批B段', 413, 83195]],
        '海南热带海洋学院': [['本科二批B段', 413, 83195]],
        '清华大学': [['本科一批A段', 674, 84]],
        '北京大学': [['本科一批A段', 679, 55]],
        '浙江大学': [['本科一批A段', 657, 335]],
        '上海交通大学': [['本科一批A段', 660, 271]],
        '复旦大学': [['本科一批A段', 659, 293]],
        '南京大学': [['本科一批A段', 653, 442]],
        '中国科学技术大学': [['本科一批A段', 654, 414]],
        '华中科技大学': [['本科一批A段', 623, 2102]],
        '武汉大学': [['本科一批A段', 604, 4131]],
        '西安交通大学': [['本科一批A段', 634, 1282]],
        '中山大学': [['本科一批A段', 616, 2754]],
        '北京航空航天大学': [['本科一批A段', 647, 646], ['本科一批A1段', 591, 6076]],
        '东南大学': [['本科一批A段', 631, 1484]],
        '北京理工大学': [['本科一批A段', 637, 1102], ['本科一批A1段', 582, 7750]],
        '四川大学': [['本科一批A段', 583, 7561]],
        '哈尔滨工业大学': [['本科一批A段', 634, 1282]],
        '北京协和医学院': [['本科一批A段', 582, 7750]],
        '同济大学': [['本科一批A段', 610, 3403]],
        '中国人民大学': [['本科一批A段', 651, 504]],
        '北京师范大学': [['本科一批A段', 615, 2864], ['本科一批A段', 603, 4299]],
        '天津大学': [['本科一批A段', 611, 3316]],
        '南开大学': [['本科一批A段', 626, 1846]],
        '山东大学': [['本科一批A段', 579, 8356]],
        '西北工业大学': [['本科一批A段', 623, 2102]],
        '厦门大学': [['本科一批A段', 611, 3316]],
        '中南大学': [['本科一批A段', 597, 5122], ['本科一批A1段', 573, 9627]],
        '吉林大学': [['本科一批A段', 577, 8769], ['本科一批A1段', 552, 14898]],
        '中国农业大学': [['本科一批A段', 595, 5441], ['本科一批A1段', 543, 17615]],
        '大连理工大学': [['本科一批A段', 607, 3757], ['本科一批A1段', 573, 9627]],
        '华东师范大学': [['本科一批A段', 604, 4131]],
        '华南理工大学': [['本科一批A段', 603, 4299]],
        '电子科技大学': [['本科一批A段', 620, 2371], ['本科一批A段', 623, 2102]],
        '湖南大学': [['本科一批A段', 575, 9199]],
        '重庆大学': [['本科一批A段', 592, 5926]],
        '北京科技大学': [['本科一批A段', 592, 5926]],
        '上海财经大学': [['本科一批A段', 591, 6076]],
        '南京航空航天大学': [['本科一批A段', 596, 5288]],
        '南京理工大学': [['本科一批A段', 589, 6423]],
        '兰州大学': [['本科一批A段', 566, 11268]],
        '东北大学': [['本科一批A段', 576, 8981], ['本科一批A1段', 539, 18800]],
        '首都医科大学': [['本科一批A段', 577, 8769]],
        '西安电子科技大学': [['本科一批A段', 611, 3316], ['本科一批A1段', 571, 10071]],
        '北京交通大学': [['本科一批A段', 594, 5609], ['本科一批A段', 551, 15192]],
        '苏州大学': [['本科一批A段', 583, 7561]],
        '华东理工大学': [['本科一批A段', 589, 6423], ['本科一批A1段', 544, 17284]],
        '中央财经大学': [['本科一批A段', 568, 10768]],
        '哈尔滨工程大学': [['本科一批A段', 589, 6423], ['本科一批A1段', 556, 13766]],
        '东北师范大学': [['本科一批A段', 521, 25146]],
        '南方医科大学': [['本科一批A段', 566, 11268]],
        '华中农业大学': [['本科一批A段', 524, 24047]],
        '中国石油大学（北京）': [['本科一批A段', 580, 8162]],
        '南京农业大学': [['本科一批A段', 550, 15459]],
        '郑州大学': [['本科一批A段', 554, 14332]],
        '暨南大学': [['本科一批A段', 560, 12721]],
        '哈尔滨医科大学': [['本科一批A段', 553, 14608], ['本科二批A段', 456, 55767]],
        '南京师范大学': [['本科一批A段', 552, 14898]],
        '武汉理工大学': [['本科一批A段', 558, 13252], ['本科一批A1段', 535, 20092]],
        '中国矿业大学': [['本科一批A段', 558, 13252], ['本科一批A1段', 513, 28176]],
        '对外经济贸易大学': [['本科一批A段', 600, 4707]],
        '中国医科大学': [['本科一批A段', 581, 7951], ['本科一批A1段', 507, 30713]],
        '中国政法大学': [['本科一批A段', 564, 11735]],
        '江南大学': [['本科一批A段', 564, 11735], ['本科一批A1段', 539, 18800]],
        '天津医科大学': [['本科一批A段', 558, 13252]],
        '上海大学': [['本科一批A段', 586, 6961], ['本科一批A1段', 549, 15751]],
        '中国海洋大学': [['本科一批A段', 577, 8769], ['本科一批A1段', 541, 18179]],
        '华中师范大学': [['本科一批A段', 518, 26277]],
        '西南交通大学': [['本科一批A段', 567, 11013], ['本科一批A1段', 540, 18480]],
        '中国石油大学（华东）': [['本科一批A段', 567, 11013]],
        '中国地质大学（武汉）': [['本科一批A段', 564, 11735], ['本科一批A1段', 541, 18179]],
        '陕西师范大学': [['本科一批A段', 551, 15192]],
        '北京邮电大学': [['本科一批A段', 619, 2465], ['本科一批A段', 586, 6961]],
        '浙江工业大学': [['本科一批B段', 480, 42972]],
        '河海大学': [['本科一批A段', 572, 9840]],
        '北京工业大学': [['本科一批A段', 577, 8769], ['本科一批A1段', 557, 13511]],
        '西北大学': [['本科一批A段', 569, 10521], ['本科一批A1段', 551, 15192]],
        '北京化工大学': [['本科一批A段', 573, 9627], ['本科一批A1段', 531, 21492]],
        '西南大学': [['本科一批A段', 553, 14608], ['本科一批A段', 540, 18480], ['本科一批A1段', 533, 20792]],
        '云南大学': [['本科一批A段', 550, 15459], ['本科一批A1段', 507, 30713]],
        '西南财经大学': [['本科一批A段', 577, 8769]],
        '南昌大学': [['本科一批A段', 551, 15192], ['本科一批A1段', 557, 13511]],
        '中南财经政法大学': [['本科一批A段', 535, 20092]],
        '深圳大学': [['本科一批A段', 573, 9627], ['本科一批A1段', 530, 21853]],
        '西北农林科技大学': [['本科一批A段', 561, 12487], ['本科一批A1段', 511, 29000]],
        '北京外国语大学': [['本科一批A段', 528, 22574]],
        '中国地质大学（北京）': [['本科一批A段', 553, 14608]],
        '华北电力大学': [['本科一批A段', 565, 11485]],
        '东华大学': [['本科一批A段', 555, 14031]],
        '中国矿业大学（北京）': [['本科一批A段', 560, 12721]],
        '宁波大学': [['本科一批A段', 560, 12721], ['本科一批B段', 520, 25525]],
        '华南师范大学': [['本科一批A段', 552, 14898]],
        '江苏大学': [['本科一批A段', 549, 15751]],
        '福州大学': [['本科一批A段', 553, 14608], ['本科一批A1段', 545, 16951]],
        '扬州大学': [['本科一批B段', 497, 35020]],
        '合肥工业大学': [['本科一批A段', 568, 10768], ['本科一批A1段', 523, 24390]],
        '北京中医药大学': [['本科一批A段', 558, 13252], ['本科二批A段', 480, 42972]],
        '北京林业大学': [['本科一批A段', 542, 17900], ['本科一批A1段', 517, 26634]],
        '中国传媒大学': [['本科一批A段', 561, 12487], ['本科一批A1段', 514, 27801]],
        '南京邮电大学': [['本科一批A段', 585, 7166]],
        '湖南师范大学': [['本科一批A段', 555, 14031]],
        '重庆医科大学': [['本科一批A段', 611, 3316], ['本科一批B段', 537, 19443]],
        '福建师范大学': [['本科一批B段', 480, 42972], ['本科二批A段', 477, 44449]],
        '浙江师范大学': [['本科一批B段', 495, 35885]],
        '南京工业大学': [['本科一批B段', 480, 42972]],
        '广西大学': [['本科一批A段', 528, 22574]],
        '首都师范大学': [['本科一批A段', 586, 6961], ['本科一批B段', 481, 42458]],
        '长安大学': [['本科一批A段', 573, 9627], ['本科一批A1段', 526, 23276]],
        '南京林业大学': [['本科一批B段', 499, 34103]],
        '华南农业大学': [['本科一批A段', 532, 21143], ['本科一批A1段', 508, 30280]],
        '上海中医药大学': [['本科一批A段', 576, 8981], ['本科一批B段', 516, 27028]],
        '安徽大学': [['本科一批A段', 559, 12970], ['本科一批A1段', 523, 24390]],
        '贵州大学': [['本科一批A段', 531, 21492], ['本科一批A1段', 494, 36323]],
        '上海外国语大学': [['本科一批A段', 569, 10521]],
        '杭州电子科技大学': [['本科一批B段', 534, 20448]],
        '广州医科大学': [['本科一批A段', 587, 6768], ['本科一批B段', 504, 31988]],
        '广州大学': [['本科一批B段', 501, 33237]],
        '河南大学': [['本科一批A段', 535, 20092]],
        '东北财经大学': [['本科一批A段', 557, 13511], ['本科一批A1段', 505, 31571]],
        '广东工业大学': [['本科一批B段', 523, 24390]],
        '山西大学': [['本科一批A段', 508, 30280], ['本科一批B段', 495, 35885]],
        '湘潭大学': [['本科一批A段', 550, 15459]],
        '中国药科大学': [['本科一批A段', 573, 9627]],
        '南京信息工程大学': [['本科一批A段', 564, 11735]],
        '中央民族大学': [['本科一批A段', 573, 9627], ['本科一批A1段', 544, 17284]],
        '海南大学': [['本科一批A段', 537, 19443], ['本科一批A1段', 503, 32398]],
        '浙江理工大学': [['本科一批B段', 480, 42972]],
        '上海理工大学': [['本科一批B段', 541, 18179]],
        '太原理工大学': [['本科一批A段', 531, 21492], ['本科一批B段', 505, 31571], ['本科一批A1段', 503, 32398]],
        '河北工业大学': [['本科一批A段', 564, 11735], ['本科一批A1段', 514, 27801]],
        '青岛大学': [['本科一批B段', 500, 33668]],
        '大连海事大学': [['本科一批A段', 564, 11735], ['本科一批A1段', 523, 24390]],
        '燕山大学': [['本科一批A段', 543, 17615], ['本科一批A1段', 495, 35885]],
        '东北林业大学': [['本科一批A段', 539, 18800], ['本科一批A1段', 514, 27801]],
        '宁波诺丁汉大学': [['本科一批A1段', 532, 21143]],
        '西安建筑科技大学': [['本科一批B段', 502, 32801]],
        '昆明理工大学': [['本科一批B段', 485, 40511], ['本科二批A段', 475, 45517]],
        '内蒙古大学': [['本科一批A段', 517, 26634]],
        '江西师范大学': [['本科一批B段', 480, 42972]],
        '西安理工大学': [['本科一批B段', 517, 26634]],
        '上海师范大学': [['本科一批B段', 486, 40012]],
        '大连医科大学': [['本科一批A段', 598, 4993], ['本科一批B段', 543, 17615]],
        '杭州师范大学': [['本科一批B段', 497, 35020]],
        '东北农业大学': [['本科一批A段', 532, 21143], ['本科一批A1段', 498, 34541]],
        '河北医科大学': [['本科一批A段', 597, 5122], ['本科一批B段', 541, 18179], ['本科二批A段', 474, 45991]],
        '武汉科技大学': [['本科一批B段', 480, 42972]],
        '山东科技大学': [['本科一批B段', 482, 41988]],
        '陕西科技大学': [['本科一批A段', 535, 20092], ['本科一批A1段', 498, 34541]],
        '福建农林大学': [['本科一批B段', 493, 36771], ['本科二批A段', 454, 56966], ['本科二批B段', 446, 61687]],
        '江西财经大学': [['本科一批B段', 502, 32801]],
        '长沙理工大学': [['本科一批B段', 498, 34541]],
        '河北大学': [['本科一批B段', 480, 42972]],
        '宁夏大学': [['本科一批A段', 523, 24390]],
        '新疆大学': [['本科一批A段', 515, 27417]],
        '辽宁大学': [['本科一批A段', 562, 12240], ['本科一批A1段', 530, 21853]],
        '温州大学': [['本科一批B段', 500, 33668]],
        '湖北大学': [['本科一批B段', 509, 29887]],
        '四川农业大学': [['本科一批A段', 535, 20092]],
        '长春理工大学': [['本科一批B段', 492, 37264]],
        '浙江工商大学': [['本科一批B段', 480, 42972]],
        '石河子大学': [['本科一批A段', 511, 29000]],
        '中国计量大学': [['本科一批B段', 524, 24047]],
        '天津工业大学': [['本科一批A段', 535, 20092], ['本科一批B段', 486, 40012]],
        '南京中医药大学': [['本科一批A段', 556, 13766]],
        '江苏科技大学': [['本科一批B段', 486, 40012]],
        '首都经济贸易大学': [['本科一批B段', 505, 31571]],
        '天津师范大学': [['本科一批B段', 485, 40511], ['本科二批A段', 485, 40511]],
        '齐鲁工业大学': [['本科一批B段', 511, 29000], ['本科二批A段', 463, 51865]],
        '北京语言大学': [['本科一批A段', 539, 18800]],
        '江苏师范大学': [['本科二批A段', 458, 54639]],
        '山东农业大学': [['本科二批A段', 434, 69199]],
        '上海海洋大学': [['本科一批A段', 520, 25525]],
        '福建医科大学': [['本科一批B段', 551, 15192], ['本科二批A段', 457, 55187]],
        '湖北工业大学': [['本科一批B段', 499, 34103]],
        '浙江农林大学': [['本科一批B段', 491, 37698]],
        '华东政法大学': [['本科一批A段', 570, 10291]],
        '河南农业大学': [['本科二批A段', 458, 54639]],
        '常州大学': [['本科一批B段', 497, 35020]],
        '西交利物浦大学': [['本科一批A1段', 537, 19443]],
        '沈阳农业大学': [['本科一批A段', 497, 35020], ['本科一批A1段', 495, 35885]],
        '河南师范大学': [['本科一批B段', 480, 42972]],
        '重庆邮电大学': [['本科一批B段', 492, 37264]],
        '广州中医药大学': [['本科一批A段', 573, 9627], ['本科一批B段', 509, 29887]],
        '安徽农业大学': [['本科一批B段', 486, 40012], ['本科二批A段', 442, 64210]],
        '成都理工大学': [['本科一批A段', 547, 16357], ['本科一批B段', 497, 35020], ['本科二批A段', 474, 45991]],
        '安徽医科大学': [['本科二批A段', 474, 45991]],
        '广西师范大学': [['本科二批A段', 444, 62900]],
        '黑龙江大学': [['本科一批B段', 499, 34103], ['本科二批A段', 461, 52938]],
        '上海体育大学': [['本科二批A段', 469, 48526]],
        '西南政法大学': [['本科一批A段', 573, 9627]],
        '北京建筑大学': [['本科一批B段', 480, 42972]],
        '武汉工程大学': [['本科一批B段', 480, 42972]],
        '南通大学': [['本科一批B段', 509, 29887], ['本科二批A段', 442, 64210]],
        '浙江中医药大学': [['本科一批B段', 528, 22574], ['本科二批A段', 458, 54639]],
        '河北师范大学': [['本科一批B段', 480, 42972], ['本科二批A段', 463, 51865]],
        '广西医科大学': [['本科一批A段', 546, 16663]],
        '天津科技大学': [['本科一批B段', 493, 36771]],
        '青岛科技大学': [['本科一批B段', 492, 37264], ['本科二批A段', 474, 45991]],
        '华侨大学': [['本科一批B段', 480, 42972]],
        '广东外语外贸大学': [['本科一批A段', 538, 19136]],
        '河南科技大学': [['本科二批A段', 460, 53488]],
        '延边大学': [['本科一批A段', 527, 22898], ['本科一批A1段', 493, 36771]],
        '山西医科大学': [['本科一批A段', 584, 7372], ['本科一批B段', 480, 42972], ['本科二批A段', 460, 53488]],
        '汕头大学': [['本科一批B段', 501, 33237]],
        '武汉纺织大学': [['本科二批A段', 475, 45517]],
        '南京财经大学': [['本科一批B段', 515, 27417]],
        '天津中医药大学': [['本科一批A段', 557, 13511], ['本科一批B段', 514, 27801]],
        '江西理工大学': [['本科一批B段', 487, 39532]],
        '西安科技大学': [['本科一批B段', 480, 42972]],
        '集美大学': [['本科一批B段', 497, 35020]],
        '西北师范大学': [['本科一批B段', 480, 42972], ['本科二批B段', 430, 71869], ['本科二批A段', 420, 78503]],
        '湖南农业大学': [['本科一批B段', 494, 36323], ['本科二批A段', 445, 62278]],
        '青海大学': [['本科一批A段', 528, 22574]],
        '成都中医药大学': [['本科一批B段', 545, 16951]],
        '辽宁师范大学': [['本科二批A段', 474, 45991], ['本科二批B段', 415, 81821]],
        '浙江财经大学': [['本科一批B段', 489, 38606]],
        '上海海事大学': [['本科一批B段', 521, 25146]],
        '吉林农业大学': [['本科二批A段', 421, 77851]],
        '上海对外经贸大学': [['本科一批B段', 522, 24767]],
        '曲阜师范大学': [['本科一批B段', 480, 42972]],
        '三峡大学': [['本科一批B段', 488, 39088]],
        '深圳北理莫斯科大学': [['本科一批A1段', 525, 23678]],
        '华东交通大学': [['本科一批B段', 501, 33237], ['本科二批A段', 467, 49693]],
        '济南大学': [['本科一批B段', 494, 36323]],
        '中北大学': [['本科一批A段', 497, 35020], ['本科一批B段', 488, 39088], ['本科一批B段', 480, 42972]],
        '山东财经大学': [['本科二批A段', 454, 56966]],
        '南昌航空大学': [['本科一批B段', 515, 27417], ['本科二批B段', 469, 48526], ['本科二批A段', 466, 50253]],
        '天津理工大学': [['本科一批B段', 480, 42972], ['本科二批A段', 471, 47470], ['本科二批B段', 447, 61036]],
        '湖南科技大学': [['本科一批B段', 487, 39532]],
        '安徽工业大学': [['本科一批B段', 486, 40012], ['本科二批A段', 452, 58154]],
        '长江大学': [['本科一批B段', 494, 36323]],
        '兰州理工大学': [['本科一批B段', 492, 37264], ['本科二批A段', 435, 68610]],
        '重庆交通大学': [['本科一批B段', 480, 42972]],
        '沈阳工业大学': [['本科一批B段', 482, 41988]],
        '烟台大学': [['本科一批B段', 492, 37264]],
        '山东理工大学': [['本科二批A段', 457, 55187]],
        '安徽理工大学': [['本科一批B段', 491, 37698]],
        '西藏大学': [['本科二批A段', 451, 58754]],
        '上海电力大学': [['本科一批B段', 523, 24390]],
        '北京工商大学': [['本科一批B段', 512, 28598]],
        '河北农业大学': [['本科二批A段', 440, 65475], ['本科二批B段', 401, 91074]],
        '北方工业大学': [['本科一批B段', 497, 35020]],
        '西安邮电大学': [['本科一批B段', 549, 15751], ['本科二批A段', 499, 34103]],
        '四川师范大学': [['本科一批B段', 480, 42972]],
        '云南师范大学': [['本科二批A段', 460, 53488], ['本科二批B段', 448, 60464]],
        '南华大学': [['本科一批B段', 501, 33237]],
        '江西农业大学': [['本科二批A段', 428, 73161]],
        '山东第一医科大学': [['本科一批B段', 526, 23276], ['本科二批A段', 461, 52938]],
        '河南理工大学': [['本科二批A段', 461, 52938]],
        '苏州科技大学': [['本科一批B段', 496, 35433]],
        '内蒙古农业大学': [['本科二批A段', 424, 75806]],
        '北京信息科技大学': [['本科一批B段', 543, 17615]],
        '兰州交通大学': [['本科二批A段', 474, 45991]],
        '北京师范大学-香港浸会大学联合国际学院': [['本科一批A1段', 518, 26277]],
        '南京审计大学': [['本科一批B段', 519, 25896]],
        '河南工业大学': [['本科一批B段', 484, 41000], ['本科二批A段', 459, 54084], ['本科二批B段', 401, 91074]],
        '天津财经大学': [['本科一批B段', 496, 35433]],
        '青岛理工大学': [['本科一批B段', 494, 36323]],
        '大连工业大学': [['本科二批A段', 459, 54084], ['本科二批B段', 455, 56376]],
        '徐州医科大学': [['本科一批B段', 562, 12240]],
        '沈阳航空航天大学': [['本科一批B段', 502, 32801], ['本科二批A段', 465, 50775]],
        '沈阳药科大学': [['本科一批B段', 525, 23678]],
        '沈阳建筑大学': [['本科一批B段', 487, 39532]],
        '重庆师范大学': [['本科一批B段', 491, 37698], ['本科二批A段', 456, 55767]],
        '中南民族大学': [['本科一批B段', 497, 35020]],
        '青岛农业大学': [['本科二批A段', 448, 60464]],
        '北京体育大学': [['本科一批A段', 528, 22574]],
        '山西农业大学': [['本科一批A段', 481, 42458], ['本科一批B段', 480, 42972], ['本科二批A段', 433, 69833],
                         ['本科二批B段', 414, 82501]],
        '西安工业大学': [['本科一批B段', 527, 22898], ['本科二批A段', 474, 45991]],
        '湖州师范学院': [['本科二批B段', 449, 59901]],
        '东北石油大学': [['本科一批A段', 511, 29000]],
        '佛山大学': [['本科二批A段', 429, 72498]],
        '嘉兴大学': [['本科二批B段', 453, 57570]],
        '浙江海洋大学': [['本科二批A段', 456, 55767]],
        '西南科技大学': [['本科一批B段', 488, 39088]],
        '石家庄铁道大学': [['本科一批B段', 491, 37698]],
        '青海师范大学': [['本科二批A段', 436, 67959]],
        '上海工程技术大学': [['本科二批A段', 462, 52379]],
        '河北科技大学': [['本科一批B段', 490, 38134], ['本科二批A段', 454, 56966], ['本科二批B段', 411, 84577]],
        '安徽财经大学': [['本科一批B段', 480, 42972]],
        '中南林业科技大学': [['本科一批B段', 480, 42972]],
        '桂林电子科技大学': [['本科一批B段', 492, 37264]],
        '哈尔滨理工大学': [['本科二批A段', 473, 46479]],
        '成都大学': [['本科二批B段', 461, 52938]],
        '甘肃农业大学': [['本科二批A段', 430, 71869]],
        '东莞理工学院': [['本科一批B段', 495, 35885], ['本科二批A段', 472, 46978]],
        '鲁东大学': [['本科二批A段', 426, 74522]],
        '浙江科技大学': [['本科二批A段', 467, 49693], ['本科二批B段', 431, 71186]],
        '内蒙古师范大学': [['本科二批A段', 444, 62900]],
        '沈阳化工大学': [['本科二批A段', 450, 59324]],
        '聊城大学': [['本科二批A段', 462, 52379]],
        '西南医科大学': [['本科一批B段', 537, 19443], ['本科二批A段', 459, 54084]],
        '山东建筑大学': [['本科二批A段', 460, 53488], ['本科二批B段', 426, 74522]],
        '宁夏医科大学': [['本科一批B段', 535, 20092], ['本科二批A段', 452, 58154]],
        '东华理工大学': [['本科一批B段', 506, 31121], ['本科二批A段', 469, 48526]],
        '山东中医药大学': [['本科二批A段', 463, 51865]],
        '哈尔滨师范大学': [['本科二批A段', 428, 73161]],
        '武汉轻工大学': [['本科二批A段', 460, 53488], ['本科二批B段', 424, 75806]],
        '赣南师范大学': [['本科二批A段', 432, 70526]],
        '北京第二外国语学院': [['本科一批A段', 535, 20092]],
        '长春工业大学': [['本科二批B段', 453, 57570], ['本科二批A段', 425, 75187]],
        '西北政法大学': [['本科一批B段', 533, 20792]],
        '渤海大学': [['本科二批A段', 462, 52379], ['本科二批B段', 405, 88482]],
        '华北水利水电大学': [['本科一批B段', 494, 36323]],
        '上海应用技术大学': [['本科一批B段', 497, 35020], ['本科二批A段', 470, 48047]],
        '西安石油大学': [['本科一批B段', 480, 42972]],
        '温州肯恩大学': [['本科一批A1段', 516, 27028]],
        '山西师范大学': [['本科一批B段', 480, 42972], ['本科二批A段', 399, 92380]],
        '郑州轻工业大学': [['本科二批A段', 461, 52938], ['本科二批B段', 454, 56966]],
        '东北电力大学': [['本科二批B段', 478, 43947], ['本科二批A段', 470, 48047]],
        '滨州医学院': [['本科二批A段', 465, 50775]],
        '贵州师范大学': [['本科二批A段', 443, 63520]],
        '大连大学': [['本科二批A段', 455, 56376]],
        '辽宁石油化工大学': [['本科二批A段', 454, 56966], ['本科二批B段', 441, 64867]],
        '西华师范大学': [['本科二批A段', 409, 85872]],
        '新疆医科大学': [['本科一批B段', 575, 9199], ['本科二批A段', 457, 55187]],
        '北京农学院': [['本科二批A段', 459, 54084]],
        '南京工程学院': [['本科二批A段', 470, 48047]],
        '安徽工程大学': [['本科二批A段', 415, 81821]],
        '沈阳师范大学': [['本科二批B段', 443, 63520], ['本科二批A段', 431, 71186]],
        '湖南中医药大学': [['本科一批B段', 519, 25896], ['本科二批A段', 461, 52938]],
        '大连交通大学': [['本科一批B段', 499, 34103], ['本科二批A段', 476, 44986], ['本科二批B段', 436, 67959]],
        '河南中医药大学': [['本科二批A段', 458, 54639]],
        '新乡医学院': [['本科一批B段', 528, 22574]],
        '西安工程大学': [['本科一批B段', 509, 29887]],
        '桂林理工大学': [['本科一批B段', 480, 42972], ['本科二批A段', 448, 60464]],
        '江汉大学': [['本科一批B段', 505, 31571]],
        '上海政法学院': [['本科一批B段', 510, 29440]],
        '沈阳理工大学': [['本科一批B段', 497, 35020], ['本科二批A段', 473, 46479]],
        '安徽建筑大学': [['本科一批B段', 480, 42972], ['本科二批A段', 438, 66720]],
        '湖南工业大学': [['本科一批B段', 488, 39088]],
        '绍兴文理学院': [['本科二批A段', 476, 44986]],
        '厦门理工学院': [['本科二批A段', 465, 50775], ['本科二批B段', 458, 54639]],
        '辽宁工程技术大学': [['本科一批B段', 480, 42972]],
        '北京印刷学院': [['本科一批B段', 481, 42458]],
        '内蒙古工业大学': [['本科二批A段', 400, 91697]],
        '昆明医科大学': [['本科一批B段', 550, 15459], ['本科二批A段', 465, 50775], ['本科二批B段', 442, 64210]],
        '北京石油化工学院': [['本科二批A段', 450, 59324]],
        '华北理工大学': [['本科一批B段', 483, 41494]],
        '延安大学': [['本科二批A段', 449, 59901]],
        '中国民航大学': [['本科一批B段', 523, 24390]],
        '黑龙江八一农垦大学': [['本科二批A段', 439, 66078]],
        '中原工学院': [['本科二批A段', 462, 52379]],
        '辽宁科技大学': [['本科一批B段', 487, 39532], ['本科二批A段', 416, 81123]],
        '西南民族大学': [['本科一批B段', 481, 42458]],
        '沈阳大学': [['本科二批A段', 440, 65475]],
        '辽宁中医药大学': [['本科二批A段', 454, 56966]],
        '北华大学': [['本科二批A段', 462, 52379], ['本科二批B段', 418, 79807]],
        '新疆农业大学': [['本科二批A段', 428, 73161], ['本科二批B段', 396, 94352]],
        '北京联合大学': [['本科一批B段', 507, 30713], ['本科二批A段', 465, 50775], ['本科二批B段', 431, 71186]],
        '山西财经大学': [['本科一批A段', 511, 29000], ['本科一批B段', 480, 42972], ['本科二批A段', 430, 71869],
                         ['本科一批B段', 480, 42972]],
        '闽江学院': [['本科二批B段', 424, 75806]],
        '遵义医科大学': [['本科一批B段', 534, 20448], ['本科二批A段', 470, 48047]],
        '辽宁工业大学': [['本科二批A段', 469, 48526], ['本科二批B段', 442, 64210]],
        '湖北医药学院': [['本科二批A段', 435, 68610]],
        '宁波工程学院': [['本科二批A段', 455, 56376], ['本科二批B段', 430, 71869]],
        '河北工程大学': [['本科一批B段', 494, 36323], ['本科二批B段', 419, 79161], ['本科二批A段', 419, 79161]],
        '云南农业大学': [['本科二批A段', 435, 68610], ['本科二批B段', 411, 84577]],
        '太原科技大学': [['本科一批B段', 480, 42972], ['本科二批A段', 438, 66720]],
        '吉首大学': [['本科二批A段', 435, 68610]],
        '重庆科技大学': [['本科二批B段', 440, 65475]],
        '广东海洋大学': [['本科二批A段', 443, 63520]],
        '大连海洋大学': [['本科二批A段', 451, 58754], ['本科二批B段', 436, 67959]],
        '内蒙古医科大学': [['本科二批A段', 472, 46978]],
        '淮阴工学院': [['本科二批B段', 413, 83195]],
        '内蒙古科技大学': [['本科二批A段', 438, 66720]],
        '山东第二医科大学': [['本科二批A段', 461, 52938]],
        '台州学院': [['本科二批B段', 448, 60464]],
        '重庆工商大学': [['本科一批B段', 490, 38134]],
        '黑龙江中医药大学': [['本科一批A段', 558, 13252], ['本科一批B段', 498, 34541], ['本科二批A段', 443, 63520]],
        '塔里木大学': [['本科二批A段', 406, 87825]],
        '湖南理工学院': [['本科二批A段', 459, 54084]],
        '大理大学': [['本科一批B段', 507, 30713], ['本科二批B段', 434, 69199]],
        '景德镇陶瓷大学': [['本科二批A段', 462, 52379]],
        '新疆师范大学': [['本科二批A段', 443, 63520]],
        '贵州医科大学': [['本科一批B段', 539, 18800], ['本科二批A段', 466, 50253]],
        '吉林财经大学': [['本科一批B段', 480, 42972], ['本科二批A段', 463, 51865]],
        '四川外国语大学': [['本科一批B段', 480, 42972]],
        '吉林师范大学': [['本科二批A段', 436, 67959], ['本科二批B段', 416, 81123]],
        '广东医科大学': [['本科一批B段', 529, 22220]],
        '河北经贸大学': [['本科二批A段', 443, 63520]],
        '长春师范大学': [['本科二批B段', 451, 58754], ['本科二批A段', 442, 64210]],
        '大连外国语大学': [['本科一批B段', 480, 42972]],
        '西南林业大学': [['本科二批A段', 435, 68610]],
        '长江师范学院': [['本科二批A段', 421, 77851]],
        '盐城师范学院': [['本科二批A段', 459, 54084]],
        '江苏理工学院': [['本科二批A段', 460, 53488]],
        '闽南师范大学': [['本科二批B段', 398, 93042]],
        '广东财经大学': [['本科一批B段', 516, 27028]],
        '淮阴师范学院': [['本科二批A段', 438, 66720]],
        '福建理工大学': [['本科二批A段', 464, 51307]],
        '江西中医药大学': [['本科一批B段', 512, 28598]],
        '河北地质大学': [['本科二批A段', 450, 59324]],
        '淮北师范大学': [['本科二批A段', 447, 61036]],
        '南宁师范大学': [['本科二批A段', 411, 84577]],
        '河南财经政法大学': [['本科一批B段', 511, 29000]],
        '西安外国语大学': [['本科一批B段', 480, 42972]],
        '常州工学院': [['本科二批A段', 468, 49114]],
        '北京物资学院': [['本科二批A段', 457, 55187]],
        '锦州医科大学': [['本科二批A段', 483, 41494]],
        '上海第二工业大学': [['本科二批A段', 459, 54084]],
        '长春中医药大学': [['本科一批B段', 519, 25896], ['本科二批A段', 456, 55767], ['本科二批B段', 422, 77168]],
        '天津城建大学': [['本科二批A段', 461, 52938], ['本科二批B段', 402, 90411]],
        '广东技术师范大学': [['本科二批A段', 460, 53488]],
        '上海电机学院': [['本科一批B段', 503, 32398], ['本科二批A段', 469, 48526], ['本科二批B段', 449, 59901]],
        '徐州工程学院': [['本科二批A段', 458, 54639]],
        '湖北师范大学': [['本科二批A段', 449, 59901]],
        '江苏海洋大学': [['本科一批B段', 494, 36323]],
        '广西中医药大学': [['本科二批A段', 440, 65475]],
        '首都体育学院': [['本科二批A段', 442, 64210]],
        '吉林建筑大学': [['本科二批A段', 442, 64210], ['本科二批B段', 419, 79161]],
        '湖北中医药大学': [['本科二批A段', 444, 62900]],
        '安庆师范大学': [['本科二批B段', 419, 79161]],
        '长沙学院': [['本科二批B段', 421, 77851]],
        '南昌工程学院': [['本科二批A段', 462, 52379]],
        '山东交通学院': [['本科二批A段', 464, 51307], ['本科二批B段', 423, 76497]],
        '五邑大学': [['本科二批A段', 463, 51865]],
        '河南科技学院': [['本科二批A段', 429, 72498]],
        '江西科技师范大学': [['本科二批A段', 441, 64867]],
        '桂林医学院': [['本科二批A段', 472, 46978]],
        '井冈山大学': [['本科二批A段', 441, 64867]],
        '重庆文理学院': [['本科二批A段', 438, 66720], ['本科二批B段', 418, 79807]],
        '湖南第一师范学院': [['本科二批B段', 437, 67346]],
        '陕西理工大学': [['本科一批B段', 520, 25525], ['本科二批A段', 461, 52938], ['本科二批B段', 437, 67346]],
        '洛阳师范学院': [['本科二批B段', 417, 80481]],
        '天津职业技术师范大学': [['本科一批B段', 498, 34541], ['本科二批B段', 446, 61687], ['本科二批A段', 432, 70526]],
        '仲恺农业工程学院': [['本科二批A段', 453, 57570]],
        '衡阳师范学院': [['本科二批B段', 407, 87224]],
        '临沂大学': [['本科二批A段', 474, 45991]],
        '天津农学院': [['本科二批A段', 459, 54084]],
        '南京晓庄学院': [['本科二批A段', 472, 46978]],
        '黄冈师范学院': [['本科二批B段', 412, 83884]],
        '天津外国语大学': [['本科一批B段', 482, 41988], ['本科二批A段', 471, 47470]],
        '四川轻化工大学': [['本科二批A段', 471, 47470]],
        '长春大学': [['本科二批A段', 439, 66078], ['本科二批B段', 426, 74522]],
        '长春工程学院': [['本科二批A段', 446, 61687], ['本科二批B段', 415, 81821]],
        '无锡学院': [['本科二批B段', 463, 51865]],
        '安徽科技学院': [['本科二批B段', 396, 94352]],
        '金陵科技学院': [['本科二批B段', 447, 61036]],
        '岭南师范学院': [['本科二批A段', 413, 83195]],
        '西藏农牧学院': [['本科二批A段', 405, 88482]],
        '贵州民族大学': [['本科二批A段', 396, 94352]],
        '衢州学院': [['本科二批B段', 428, 73161]],
        '浙江传媒学院': [['本科二批A段', 446, 61687]],
        '湖北第二师范学院': [['本科二批A段', 470, 48047]],
        '齐齐哈尔大学': [['本科二批A段', 423, 76497]],
        '福建中医药大学': [['本科二批A段', 466, 50253]],
        '合肥师范学院': [['本科二批A段', 466, 50253]],
        '绵阳师范学院': [['本科二批A段', 408, 86561]],
        '上海立信会计金融学院': [['本科一批B段', 507, 30713], ['本科二批A段', 462, 52379]],
        '广西科技大学': [['本科二批B段', 423, 76497], ['本科二批A段', 416, 81123]],
        '攀枝花学院': [['本科二批B段', 431, 71186]],
        '榆林学院': [['本科二批B段', 405, 88482]],
        '湖南工商大学': [['本科一批B段', 480, 42972], ['本科二批A段', 463, 51865]],
        '内江师范学院': [['本科二批B段', 396, 94352]],
        '广东药科大学': [['本科二批A段', 462, 52379]],
        '湖北汽车工业学院': [['本科二批A段', 471, 47470], ['本科二批B段', 446, 61687]],
        '山东航空学院': [['本科二批B段', 436, 67959]],
        '沈阳医学院': [['本科二批A段', 445, 62278]],
        '泰山学院': [['本科二批B段', 416, 81123]],
        '湖北文理学院': [['本科二批B段', 403, 89802]],
        '三明学院': [['本科二批B段', 411, 84577]],
        '重庆三峡学院': [['本科二批A段', 460, 53488]],
        '丽水学院': [['本科二批B段', 432, 70526]],
        '潍坊学院': [['本科二批B段', 407, 87224]],
        '云南民族大学': [['本科二批A段', 455, 56376]],
        '泉州师范学院': [['本科二批A段', 441, 64867]],
        '黑龙江科技大学': [['本科二批A段', 436, 67959]],
        '广西民族大学': [['本科二批A段', 396, 94352]],
        '防灾科技学院': [['本科二批B段', 433, 69833]],
        '西安文理学院': [['本科二批A段', 472, 46978]],
        '天津商业大学': [['本科一批B段', 484, 41000], ['本科二批A段', 475, 45517]],
        '湖北科技学院': [['本科二批B段', 422, 77168]],
        '杭州医学院': [['本科二批A段', 469, 48526]],
        '宝鸡文理学院': [['本科二批A段', 454, 56966]],
        '龙岩学院': [['本科二批B段', 401, 91074]],
        '南阳师范学院': [['本科二批B段', 419, 79161]],
        '大连民族大学': [['本科二批A段', 459, 54084]],
        '湖南文理学院': [['本科二批A段', 451, 58754]],
        '通化师范学院': [['本科二批A段', 418, 79807], ['本科二批B段', 396, 94352]],
        '湘南学院': [['本科二批B段', 454, 56966]],
        '北方民族大学': [['本科二批B段', 448, 60464], ['本科二批A段', 428, 73161]],
        '广东石油化工学院': [['本科二批B段', 427, 73824]],
        '陕西中医药大学': [['本科一批B段', 517, 26634]],
        '北华航天工业学院': [['本科二批B段', 453, 57570]],
        '怀化学院': [['本科二批B段', 419, 79161]],
        '佳木斯大学': [['本科二批A段', 432, 70526]],
        '中国人民警察大学': [['本科一批B段', 490, 38134]],
        '河北科技师范学院': [['本科二批A段', 410, 85217]],
        '渭南师范学院': [['本科二批A段', 431, 71186]],
        '湖北经济学院': [['本科二批A段', 443, 63520]],
        '阜阳师范大学': [['本科二批A段', 404, 89127]],
        '德州学院': [['本科二批B段', 414, 82501]],
        '玉林师范学院': [['本科二批A段', 418, 79807]],
        '川北医学院': [['本科一批B段', 526, 23276]],
        '云南财经大学': [['本科二批A段', 439, 66078]],
        '济宁医学院': [['本科二批A段', 483, 41494]],
        '南阳理工学院': [['本科二批A段', 459, 54084], ['本科二批B段', 400, 91697]],
        '曲靖师范学院': [['本科二批A段', 421, 77851]],
        '莆田学院': [['本科二批B段', 428, 73161]],
        '西安财经大学': [['本科二批A段', 474, 45991], ['本科二批B段', 452, 58154]],
        '枣庄学院': [['本科二批B段', 428, 73161]],
        '湖北理工学院': [['本科二批B段', 421, 77851]],
        '郑州航空工业管理学院': [['本科二批A段', 412, 83884]],
        '湖南城市学院': [['本科二批B段', 396, 94352]],
        '湖南工程学院': [['本科二批A段', 430, 71869]],
        '湖南科技学院': [['本科二批B段', 416, 81123]],
        '西藏民族大学': [['本科二批A段', 471, 47470]],
        '广东第二师范学院': [['本科二批A段', 436, 67959]],
        '中国劳动关系学院': [['本科二批A段', 442, 64210]],
        '太原师范学院': [['本科一批B段', 480, 42972], ['本科二批A段', 422, 77168]],
        '周口师范学院': [['本科二批B段', 396, 94352]],
        '贵州财经大学': [['本科二批A段', 430, 71869]],
        '北部湾大学': [['本科二批B段', 413, 83195]],
        '浙江水利水电学院': [['本科二批B段', 443, 63520]],
        '肇庆学院': [['本科二批B段', 411, 84577]],
        '西北民族大学': [['本科二批A段', 452, 58154]],
        '韩山师范学院': [['本科二批A段', 438, 66720]],
        '宿迁学院': [['本科二批B段', 410, 85217]],
        '河南城建学院': [['本科二批A段', 422, 77168]],
        '中国民用航空飞行学院': [['本科一批B段', 490, 38134]],
        '咸阳师范学院': [['本科二批A段', 468, 49114]],
        '黑龙江工程学院': [['本科二批A段', 402, 90411]],
        '安阳师范学院': [['本科二批B段', 396, 94352]],
        '唐山师范学院': [['本科二批B段', 402, 90411]],
        '齐鲁师范学院': [['本科二批A段', 447, 61036]],
        '成都师范学院': [['本科二批A段', 468, 49114]],
        '河南工程学院': [['本科二批B段', 414, 82501]],
        '哈尔滨商业大学': [['本科一批B段', 480, 42972], ['本科二批A段', 438, 66720]],
        '哈尔滨学院': [['本科二批B段', 409, 85872]],
        '上饶师范学院': [['本科二批A段', 419, 79161]],
        '贵州理工学院': [['本科二批B段', 404, 89127]],
        '牡丹江师范学院': [['本科二批A段', 411, 84577]],
        '昆明学院': [['本科二批B段', 411, 84577]],
        '武汉体育学院': [['本科二批A段', 454, 56966]],
        '浙江外国语学院': [['本科二批A段', 423, 76497]],
        '宜宾学院': [['本科二批B段', 435, 68610]],
        '山东工商学院': [['本科二批A段', 450, 59324], ['本科二批B段', 414, 82501]],
        '重庆第二师范学院': [['本科二批A段', 439, 66078]],
        '河北中医药大学': [['本科一批B段', 512, 28598]],
        '商丘师范学院': [['本科二批B段', 396, 94352]],
        '湖南人文科技学院': [['本科二批A段', 399, 92380], ['本科二批B段', 399, 92380]],
        '黄淮学院': [['本科二批B段', 398, 93042]],
        '长治学院': [['本科二批A段', 420, 78503], ['本科二批B段', 396, 94352]],
        '湖北工程学院': [['本科二批B段', 408, 86561]],
        '平顶山学院': [['本科二批B段', 412, 83884]],
        '内蒙古民族大学': [['本科二批A段', 436, 67959]],
        '温州理工学院': [['本科二批B段', 451, 58754]],
        '遵义师范学院': [['本科二批B段', 396, 94352]],
        '沈阳体育学院': [['本科二批A段', 421, 77851]],
        '内蒙古财经大学': [['本科二批A段', 445, 62278]],
        '宜春学院': [['本科二批B段', 405, 88482]],
        '天水师范学院': [['本科二批A段', 418, 79807]],
        '营口理工学院': [['本科二批B段', 417, 80481]],
        '商洛学院': [['本科二批B段', 406, 87825]],
        '兰州石化职业技术大学': [['本科二批B段', 400, 91697]],
        '上海健康医学院': [['本科一批B段', 526, 23276], ['本科二批A段', 466, 50253]],
        '中华女子学院': [['本科二批A段', 449, 59901]],
        '宁德师范学院': [['本科二批B段', 411, 84577]],
        '邵阳学院': [['本科二批B段', 433, 69833]],
        '洛阳理工学院': [['本科二批B段', 430, 71869]],
        '玉溪师范学院': [['本科二批A段', 419, 79161]],
        '成都工业学院': [['本科二批B段', 456, 55767]],
        '安阳工学院': [['本科二批A段', 446, 61687], ['本科二批B段', 417, 80481]],
        '赣南医科大学': [['本科一批B段', 516, 27028], ['本科二批A段', 438, 66720]],
        '四川旅游学院': [['本科二批B段', 413, 83195]],
        '九江学院': [['本科二批B段', 406, 87825]],
        '鞍山师范学院': [['本科二批A段', 439, 66078]],
        '承德医学院': [['本科二批A段', 470, 48047]],
        '内蒙古科技大学包头师范学院': [['本科二批A段', 428, 73161]],
        '成都医学院': [['本科一批B段', 527, 22898]],
        '赤峰学院': [['本科二批B段', 401, 91074]],
        '淮南师范学院': [['本科二批B段', 412, 83884]],
        '湖南工学院': [['本科二批B段', 426, 74522]],
        '贺州学院': [['本科二批B段', 396, 94352]],
        '吉林化工学院': [['本科二批A段', 442, 64210]],
        '河西学院': [['本科二批B段', 398, 93042]],
        '云南中医药大学': [['本科二批A段', 459, 54084]],
        '南昌师范学院': [['本科二批B段', 400, 91697]],
        '许昌学院': [['本科二批B段', 418, 79807]],
        '吉林农业科技学院': [['本科二批B段', 408, 86561]],
        '河北建筑工程学院': [['本科二批A段', 431, 71186]],
        '天津体育学院': [['本科二批A段', 425, 75187]],
        '河南牧业经济学院': [['本科二批B段', 408, 86561]],
        '宁夏师范大学': [['本科二批A段', 441, 64867]],
        '陇东学院': [['本科二批B段', 403, 89802]],
        '武夷学院': [['本科二批B段', 397, 93720]],
        '运城学院': [['本科二批A段', 412, 83884], ['本科二批B段', 399, 92380]],
        '安康学院': [['本科二批B段', 408, 86561]],
        '宿州学院': [['本科二批B段', 404, 89127]],
        '上海商学院': [['本科二批A段', 442, 64210]],
        '山东管理学院': [['本科二批B段', 416, 81123]],
        '泰州学院': [['本科二批A段', 453, 57570]],
        '喀什大学': [['本科二批A段', 414, 82501]],
        '辽东学院': [['本科二批B段', 403, 89802]],
        '辽宁科技学院': [['本科二批B段', 414, 82501]],
        '红河学院': [['本科二批B段', 400, 91697]],
        '湖州学院': [['本科二批B段', 449, 59901]],
        '山东青年政治学院': [['本科二批B段', 435, 68610]],
        '六盘水师范学院': [['本科二批B段', 405, 88482]],
        '梧州学院': [['本科二批B段', 396, 94352]],
        '甘肃政法大学': [['本科二批A段', 454, 56966]],
        '呼伦贝尔学院': [['本科二批B段', 401, 91074]],
        '湖北民族大学': [['本科二批A段', 458, 54639]],
        '河北民族师范学院': [['本科二批B段', 410, 85217]],
        '兰州城市学院': [['本科二批A段', 423, 76497]],
        '兰州工业学院': [['本科二批B段', 421, 77851]],
        '郑州工程技术学院': [['本科二批B段', 430, 71869]],
        '山西中医药大学': [['本科一批A段', 549, 15751], ['本科一批B段', 499, 34103], ['本科二批A段', 443, 63520]],
        '福建技术师范学院': [['本科二批B段', 411, 84577]],
        '广东金融学院': [['本科二批A段', 485, 40511]],
        '大庆师范学院': [['本科二批B段', 401, 91074]],
        '萍乡学院': [['本科二批B段', 403, 89802]],
        '南京特殊教育师范学院': [['本科二批B段', 399, 92380]],
        '郑州师范学院': [['本科二批B段', 423, 76497]],
        '长沙师范学院': [['本科二批B段', 442, 64210]],
        '赣南科技学院': [['本科二批B段', 413, 83195]],
        '桂林航天工业学院': [['本科二批B段', 432, 70526]],
        '晋中学院': [['本科二批A段', 411, 84577], ['本科二批B段', 396, 94352]],
        '新疆财经大学': [['本科二批A段', 424, 75806]],
        '邯郸学院': [['本科二批B段', 411, 84577]],
        '河北环境工程学院': [['本科二批B段', 398, 93042]],
        '内蒙古科技大学包头医学院': [['本科二批A段', 472, 46978]],
        '楚雄师范学院': [['本科二批B段', 401, 91074]],
        '白城师范学院': [['本科二批A段', 417, 80481]],
        '华北科技学院': [['本科二批A段', 457, 55187]],
        '太原工业学院': [['本科二批A段', 437, 67346]],
        '右江民族医学院': [['本科二批A段', 470, 48047]],
        '保定学院': [['本科二批B段', 396, 94352]],
        '忻州师范学院': [['本科二批A段', 414, 82501], ['本科二批B段', 396, 94352]],
        '蚌埠学院': [['本科二批B段', 444, 62900]],
        '广州航海学院': [['本科二批B段', 424, 75806]],
        '青海民族大学': [['本科二批B段', 396, 94352]],
        '山西大同大学': [['本科一批B段', 484, 41000], ['本科二批A段', 428, 73161], ['本科二批B段', 398, 93042]],
        '兴义民族师范学院': [['本科二批B段', 406, 87825]],
        '四川文理学院': [['本科二批B段', 401, 91074]],
        '西安医学院': [['本科二批B段', 438, 66720]],
        '鄂尔多斯应用技术学院': [['本科二批B段', 418, 79807]],
        '广西民族师范学院': [['本科二批B段', 399, 92380]],
        '天津中德应用技术大学': [['本科二批B段', 435, 68610]],
        '绥化学院': [['本科二批A段', 422, 77168]],
        '河南工学院': [['本科二批B段', 434, 69199]],
        '苏州城市学院': [['本科二批B段', 465, 50775]],
        '新余学院': [['本科二批B段', 417, 80481]],
        '亳州学院': [['本科二批B段', 396, 94352]],
        '吉林工程技术师范学院': [['本科二批A段', 424, 75806]],
        '河套学院': [['本科二批B段', 407, 87224]],
        '黑河学院': [['本科二批B段', 397, 93720]],
        '厦门医学院': [['本科二批A段', 473, 46479]],
        '吕梁学院': [['本科二批A段', 412, 83884], ['本科二批B段', 396, 94352]],
        '荆楚理工学院': [['本科二批B段', 408, 86561]],
        '山西能源学院': [['本科二批A段', 425, 75187], ['本科二批B段', 396, 94352]],
        '南京工业职业技术大学': [['本科二批B段', 447, 61036]],
        '石家庄学院': [['本科二批B段', 412, 83884]],
        '福建江夏学院': [['本科二批B段', 409, 85872]],
        '兰州文理学院': [['本科二批B段', 403, 89802]],
        '新疆工程学院': [['本科二批B段', 402, 90411]],
        '牡丹江医学院': [['本科二批A段', 471, 47470]],
        '张家口学院': [['本科二批B段', 414, 82501]],
        '黔南民族师范学院': [['本科二批A段', 404, 89127]],
        '保山学院': [['本科二批B段', 405, 88482]],
        '赣东学院': [['本科二批B段', 404, 89127]],
        '山西工程技术学院': [['本科二批A段', 409, 85872], ['本科二批B段', 396, 94352]],
        '西安体育学院': [['本科二批A段', 433, 69833]],
        '河北北方学院': [['本科二批A段', 477, 44449]],
        '兰州财经大学': [['本科二批A段', 437, 67346], ['本科二批B段', 423, 76497]],
        '河北水利电力学院': [['本科二批B段', 409, 85872]],
        '山东政法学院': [['本科二批A段', 462, 52379]],
        '西安航空学院': [['本科二批B段', 437, 67346]],
        '新乡学院': [['本科二批B段', 408, 86561]],
        '河北金融学院': [['本科二批B段', 396, 94352]],
        '齐齐哈尔医学院': [['本科二批B段', 412, 83884]],
        '黑龙江工业学院': [['本科二批B段', 398, 93042]],
        '昌吉学院': [['本科二批B段', 396, 94352]],
        '太原学院': [['本科二批A段', 414, 82501], ['本科二批B段', 396, 94352]],
        '甘肃民族师范学院': [['本科二批B段', 405, 88482]],
        '山东石油化工学院': [['本科二批B段', 439, 66078]],
        '唐山学院': [['本科二批B段', 430, 71869]],
        '河北工业职业技术大学': [['本科二批B段', 410, 85217]],
        '邢台学院': [['本科二批B段', 407, 87224]],
        '昭通学院': [['本科二批B段', 419, 79161]],
        '沧州师范学院': [['本科二批B段', 415, 81821]],
        '廊坊师范学院': [['本科二批A段', 421, 77851]],
        '山西工程科技职业大学': [['本科二批B段', 396, 94352]],
        '沈阳工程学院': [['本科二批B段', 440, 65475]],
        '湖南财政经济学院': [['本科二批B段', 430, 71869]],
        '河北科技工程职业技术大学': [['本科二批B段', 406, 87825]],
        '河北石油职业技术大学': [['本科二批B段', 405, 88482]],
        '新疆政法学院': [['本科二批B段', 399, 92380]],
        '广西农业职业技术大学': [['本科二批B段', 414, 82501]],
        '山西科技学院': [['本科二批B段', 402, 90411]],
        '长治医学院': [['本科一批B段', 507, 30713], ['本科二批A段', 434, 69199], ['本科二批B段', 406, 87825]],
        '福建商学院': [['本科二批B段', 424, 75806]],
        '甘肃医学院': [['本科二批B段', 436, 67959]],
        '广西财经学院': [['本科二批A段', 456, 55767]],
        '广西警察学院': [['本科二批A段', 414, 82501]],
        '桂林旅游学院': [['本科二批A段', 416, 81123]],
        '哈尔滨金融学院': [['本科二批A段', 439, 66078]],
        '河南财政金融学院': [['本科二批B段', 424, 75806]],
        '呼和浩特民族学院': [['本科二批B段', 413, 83195]],
        '湖南警察学院': [['本科二批B段', 403, 89802]],
        '湖南女子学院': [['本科二批B段', 431, 71186]],
        '湖南医药学院': [['本科二批B段', 454, 56966]],
        '吉林工商学院': [['本科二批A段', 414, 82501]],
        '吉林警察学院': [['本科二批B段', 414, 82501]],
        '吉林医药学院': [['本科二批A段', 447, 61036], ['本科二批B段', 407, 87224]],
        '嘉兴南湖学院': [['本科二批B段', 432, 70526]],
        '兰州资源环境职业技术大学': [['本科二批B段', 396, 94352]],
        '南昌医学院': [['本科二批B段', 449, 59901]],
        '山西警察学院': [['本科二批B段', 407, 87224]],
        '武汉商学院': [['本科二批B段', 461, 52938]],
        '新疆科技学院': [['本科二批B段', 400, 91697]],
        '云南警官学院': [['本科二批A段', 446, 61687]],
        '中国人民解放军国防科技大学': [['提前一批本科', 604, 4131], ['提前一批本科', 601, 4585],
                                       ['提前一批本科', 592, 5926]],
        '山东大学（威海）': [['本科一批A段', 594, 5609], ['本科一批A1段', 566, 11268]],
        '东北大学秦皇岛分校': [['本科一批A段', 575, 9199], ['本科一批A1段', 560, 12721]],
        '华北电力大学保定校区': [['本科一批A段', 564, 11735]],
        '哈尔滨工业大学（威海）': [['本科一批A段', 607, 3757]],
        '中国人民解放军空军军医大学': [['本科一批A段', 588, 6588]],
        '北京服装学院': [['本科二批A段', 445, 62278]],
        '北京大学医学部': [['本科一批A段', 658, 311]],
        '山西医科大学汾阳学院': [['本科一批B段', 510, 29440], ['本科二批A段', 422, 77168]],
        '上海交通大学医学院': [['本科一批A段', 665, 181]],
        '深圳技术大学': [['本科一批B段', 528, 22574]],
        '山西工学院': [['本科二批B段', 399, 92380]],
        '河北传媒学院': [['本科二批B段', 396, 94352]],
        '吉林外国语大学': [['本科二批B段', 396, 94352]],
        '山西传媒学院': [['本科二批A段', 406, 87825]],
        '中国石油大学（北京）克拉玛依校区': [['本科一批A段', 530, 21853]],
        '四川美术学院': [['本科二批A段', 458, 54639]],
        '广西艺术学院': [['本科二批A段', 423, 76497]],
        '山西应用科技学院': [['本科二批B段', 396, 94352]],
        '中国人民大学（苏州校区）': [['本科一批A段', 611, 3316]],
        '山西工商学院': [['本科二批B段', 396, 94352]],
        '大连理工大学盘锦校区': [['本科一批A段', 571, 10071], ['本科一批A1段', 533, 20792]],
        '复旦大学上海医学院': [['本科一批A段', 666, 169]],
        '合肥工业大学宣城校区': [['本科一批A段', 557, 13511]],
        '浙江大学医学院': [['本科一批A段', 639, 996]]
    }
}

# collection.replace_one(li, new)

print(li_ls)
print(wen_ls)