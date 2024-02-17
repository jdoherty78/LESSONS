import random as rd
from datetime import datetime as dt
################################################
#### GENERATES TIMESTAMPS FOR ORDERS TABLE #####
################################################
rd.seed(129)
order_list = []
for i in range(400):
    year = rd.randint(2020, 2023)
    month = rd.randint(1, 6)
    day = rd.randint(1, 28)
    hour = rd.randint(0, 5)
    minute = rd.randint(0, 30)
    second = rd.randint(0, 30)

    # print(year, month, day, hour, minute, second)
    order_dt = dt(year, month, day, 
                     hour, minute, second)

    order_list.append(order_dt)
    
timestamp_orders = [int(dt.timestamp(order_list[o]))
                 for o in range(len(order_list))]

timestamp_orders_list = [(timestamp_orders[i], i+ 1) for i in range(len(timestamp_orders))]

order_date_id_list = [(1646446516, 8),
 (1647742769, 11),
 (1612833436, 14),
 (1609553525, 16),
 (1650589932, 18),
 (1674180738, 20),
 (1687925422, 26),
 (1647655640, 27),
 (1623812410, 29),
 (1587004158, 32),
 (1679702549, 36),
 (1616728157, 37),
 (1621646711, 38),
 (1651807325, 41),
 (1683154829, 42),
 (1623294721, 43),
 (1585267697, 46),
 (1579915350, 47),
 (1618528698, 49),
 (1622599748, 50),
 (1679533981, 55),
 (1614828191, 63),
 (1687656017, 66),
 (1647494475, 68),
 (1617405080, 71),
 (1621552328, 72),
 (1678580067, 73),
 (1610420769, 74),
 (1622156765, 79),
 (1588817826, 82),
 (1650161884, 84),
 (1679192604, 86),
 (1674782962, 87),
 (1613185627, 93),
 (1590550229, 96),
 (1623377657, 97),
 (1647303025, 98),
 (1679974089, 101),
 (1610770470, 104),
 (1650244512, 109),
 (1622952004, 111),
 (1614216150, 120),
 (1684710430, 124),
 (1610849164, 125),
 (1585013416, 136),
 (1649391439, 137),
 (1686784581, 138),
 (1614654064, 139),
 (1679110094, 142),
 (1616461886, 145),
 (1611014537, 149),
 (1588638181, 157),
 (1588644854, 158),
 (1614211823, 160),
 (1592539861, 161),
 (1623888804, 162),
 (1649207786, 165),
 (1579046719, 171),
 (1621393768, 175),
 (1586487733, 178),
 (1680833461, 183),
 (1687306229, 189),
 (1682550794, 197),
 (1655428213, 202),
 (1616044769, 206),
 (1647666783, 207),
 (1620097626, 211),
 (1673493731, 215),
 (1677647188, 216),
 (1676437562, 217),
 (1615781583, 221),
 (1613020879, 227),
 (1645834937, 240),
 (1649984910, 242),
 (1578709163, 245),
 (1686093930, 246),
 (1621211295, 253),
 (1653618008, 258),
 (1615696211, 260),
 (1641441787, 268),
 (1680739387, 271),
 (1610504655, 272),
 (1583107328, 279),
 (1656036976, 286),
 (1685579364, 287),
 (1675307647, 300),
 (1578788646, 301),
 (1642385603, 304),
 (1642299501, 312),
 (1585704365, 314),
 (1678155505, 320),
 (1649988498, 325),
 (1616130624, 333),
 (1652232489, 335),
 (1620357555, 337),
 (1587349627, 338),
 (1583816905, 341),
 (1583029163, 344),
 (1673152214, 346),
 (1589253741, 352),
 (1589336821, 356),
 (1646269281, 363),
 (1615341721, 364),
 (1590459627, 368),
 (1672801500, 375),
 (1646705833, 376),
 (1581567507, 380),
 (1646439499, 382),
 (1621033575, 387),
 (1684034893, 391),
 (1673583013, 392),
 (1588892482, 395),
 (1584411846, 396),
 (1584321906, 398)]


################################################
#### GENERATES TIMESTAMPS FOR REVIEWS TABLE #####
################################################
# rd.seed(127)
rev_dt_list = []
for i in range(len(order_date_id_list)):
    rd_month = rd.randint(1, 6)
    rd_hour = rd.randint(0, 5)
    rd_minute = rd.randint(0, 30)
    rd_second = rd.randint(0, 30)

    order_date = dt.fromtimestamp(order_date_id_list[i][0])
    year_r = order_date.year

    ### MONTH ###
    month_r = order_date.month
    if month_r <= 6:
        month_r = order_date.month + rd_month

    ### DAY ###
    day_r = order_date.day
    if day_r <= 14:
        rd_day = rd.randint(2, 14)
        day_r = order_date.day + rd_day
        
    ### HOUR ###
    hour_r = order_date.hour
    if hour_r <= 12:
        rd_hour = rd.randint(1, 11)
        hour_r = order_date.hour + rd_hour
        
    ### MINUTES ###
    minute_r = order_date.minute
    if minute_r <= 30:
        rd_minute = rd.randint(0, 29)
        minute_r = order_date.minute + rd_minute
        
    ### SECONDS ###
    second_r = order_date.second
    if second_r <= 30:
        rd_second = rd.randint(0, 29)
        second_r = order_date.second + rd_second

    # print(year, month, day, hour, minute, second)
    rev_dt = dt(year_r, month_r, day_r, 
                     hour_r, minute_r, second_r)

    rev_dt_list.append(rev_dt)
    
timestamp_reviews = [int(dt.timestamp(rev_dt_list[r]))
                 for r in range(len(rev_dt_list))]

timestamp_reviews_list = [(timestamp_reviews[i], order_date_id_list[i][1]) for i in range(len(timestamp_reviews))]