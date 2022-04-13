# -*- coding: utf-8 -*-
# DATE : 2021/8/31

import pymysql

db_params = {'host': 'localhost', 'user': 'root', 'passwd': '123456', 'port': 3306, 'db': 'sixlens_company', 'charset': 'utf8mb4'}
conn = pymysql.connect(**db_params)
cursor = conn.cursor()

name_db = "yaopin_2022_03_18"


sql_createTb = """CREATE TABLE if not exists {} (
                 id INT NOT NULL AUTO_INCREMENT,
                 companys                VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '公司名称',
                 registerkind                VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '注册类型',
                 createdate                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '创建日期',
                 acceptidCODE                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '代码',
                 acceptid                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT 'id',
                 drgnamecn                VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '药品名称',
                 drugtype                VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '药品类型',
                 applytype                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '申请类型',
                 ROW_ID                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '序号',
                 PRIMARY KEY(id)
                 ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '国家药品监督管理局药品数据' ROW_FORMAT = Dynamic;
                 """.format(name_db)
cursor.execute(sql_createTb)

# sql_createTb = """CREATE TABLE if not exists {} (
#                  id INT NOT NULL AUTO_INCREMENT,
#                  companys                VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '图片名称',
#                  createdate                VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '图片名称',
#                  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
#                  PRIMARY KEY(id),
#                  INDEX `img_name`(`img_name`) USING BTREE
#                  ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '国家药品监督管理局药品数据' ROW_FORMAT = Dynamic;
#                  """.format(name_db)
# cursor.execute(sql_createTb)