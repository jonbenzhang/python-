CREATE TABLE `作废cz02` ( 
`ccz201` string  COMMENT '充值交易流水号（由平台的序列生成）',
`kkb101` string  COMMENT '医疗机构编号',
`ccz101` string  COMMENT '充值订单记录流水号=cz01.ccz101',
`ccz202` string  COMMENT '交易类型（1：付款 ，2：退款）',
`ccz102` double  COMMENT '充值金额，单位：元',
`ccz108` string  COMMENT '充值类型（01：就诊卡充值，02：住院预交金充值）',
`ccz106` string  COMMENT '支付方式｛00全部用医保支付、42微信线上支付、52支付宝线上支付、62 银联线上支付｝【原来叫：充值终端类型（01微信、02支付宝 03 云闪付）】',
`aae036` timestamp  COMMENT '交易时间',
PRIMARY KEY (`ccz201`)
) COMMENT '线上充值交易流水表' stored as kudu;

CREATE TABLE `作废gh02` ( 
`ggh201` string  COMMENT '挂号交易流水号（由平台的序列生成）',
`ggh101` string  COMMENT '平台的挂号编码=gh01.ggh101',
`ggh105` string  COMMENT '支付方式｛00全部用医保支付、42微信线上支付、52支付宝线上支付、62 银联线上支付｝【原来叫：自费金额支付方式{4微信5支付宝6云闪付7全部用医保支付}】',
`kkb909` double  COMMENT '挂号费用',
`aae036` timestamp  COMMENT '交易时间',
`ggh202` string  COMMENT '交易类型：1付款；2退款',
`kkb101` string  COMMENT '医疗机构编码',
PRIMARY KEY (`ggh201`)
) COMMENT '线上预约挂号流水表' stored as kudu;

CREATE TABLE `作废online_trade_summary` ( 
`trade_summary_id` string  COMMENT '线上交易流水号[医疗机构编码+yyyymmddhh24miss+seq-a-trade)',
`trade_id_merchant` string  COMMENT '商户送给平台的订单号',
`kkb101` string  COMMENT '机构ID',
`baz061` string  COMMENT '社保卡SID',
`aaz500` string  COMMENT '社保卡号',
`order_status` string  COMMENT '订单状态：0未支付，1已支付，2已退单',
`trade_status` string  COMMENT '交易状态｛00:自费未支付，医保未结算、10：自费已支付，医保未结算、11 自费已支付，医保已结算、20自费已退费，医保未结算、22自费已退费，医保已退费，30订单已关单,0x纯自费未支付；1x纯自费已支付；x0纯医保未支付；x1纯医保已支付}',
`trade_id_yb` string  COMMENT 'HIS交易流水号【数港原来的注释不对，为：HIS医保结算流水号（MSGID发送方交易流水号）】',
`recipe_no` string  COMMENT '处方单号',
`fee_total` double  COMMENT '总费用',
`fee_coordination` double  COMMENT '医保统筹支付金额',
`fee_personal_account` double  COMMENT '医保个人账户支付金额',
`fee_personal_wallet` double  COMMENT '自费支付金额',
`fee_other` double  COMMENT '医保其他支付金额',
`pay_type` string  COMMENT '支付方式｛00全部用医保支付、42微信线上支付、52支付宝线上支付、62 银联线上支付｝',
`trade_id_pay_pt` string  COMMENT '平台支付流水号【医疗机构编码+当前毫秒数】',
`trade_id_pay_td` string  COMMENT '第三方支付结算流水号',
`trade_id_refund_pt` string  COMMENT '平台退款流水号【医疗机构编码+当前毫秒数】',
`aae036` timestamp  COMMENT '生成时间',
`gmt_modified` timestamp  COMMENT '更新时间',
`card_type` string  COMMENT '卡片类型｛1:就诊卡，3：社保卡｝',
PRIMARY KEY (`trade_summary_id`)
) COMMENT '线上缴费结算(数港目前不支持线上退费)' stored as kudu;

CREATE TABLE `作废rs01` ( 
`rss001` string  COMMENT '刷新流水号',
`kkb101` string  COMMENT '医疗机构id',
`kkb702` string  COMMENT '医疗机构具体科室标志',
`kkb703` string  COMMENT '医疗机构具体科室名称',
`kkb802` string  COMMENT '医生标志',
`kkb803` string  COMMENT '医生',
`kkb903` string  COMMENT '出诊日期',
`aae036` timestamp  COMMENT '上次刷新时间',
PRIMARY KEY (`rss001`)
) COMMENT '排班更新【作废】' stored as kudu;

CREATE TABLE `作废sys_log` ( 
`id` bigint ,
`username` string  COMMENT '用户名',
`operation` string  COMMENT '用户操作',
`method` string  COMMENT '请求方法',
`params` string  COMMENT '请求参数',
`time` bigint  COMMENT '执行时长(毫秒)',
`ip` string  COMMENT 'IP地址',
`create_date` timestamp  COMMENT '创建时间',
PRIMARY KEY (`id`)
) COMMENT '系统日志' stored as kudu;

CREATE TABLE `作废va01` ( 
`vva001` string  COMMENT '验证码流水号',
`vva002` string  COMMENT '验证码',
`vva003` timestamp  COMMENT '生成时间',
`vva004` timestamp  COMMENT '失效时间',
`bae017` string  COMMENT '接收手机号码',
`vva005` timestamp  COMMENT '验证码验证时间',
`vva006` string  COMMENT '是否验证通过',
`vva008` string  COMMENT '接收验证码',
`ddv102` string  COMMENT '读卡器号',
`ddv103` string  COMMENT 'psam卡号',
`kkb101` string  COMMENT '医疗机构id',
`vva007` string  COMMENT '短信发送方（1银行、2银联，3平台)',
PRIMARY KEY (`vva001`)
) COMMENT '验证码信息' stored as kudu;

CREATE TABLE `线下as01` ( 
`baz061` string  COMMENT '社保卡sid',
`aae135` string  COMMENT '身份证号 ',
`aac003` string  COMMENT '姓名     ',
`aac004` string  COMMENT '性别     ',
`aac005` string  COMMENT '民族     ',
`aac006` timestamp  COMMENT '出生日期 ',
`aac010` string  COMMENT '通讯地址 ',
`bae017` string  COMMENT '手机号码 ',
`aab004` string  COMMENT '单位名称 ',
`aae036` timestamp  COMMENT '更新时间',
PRIMARY KEY (`baz061`)
) COMMENT '社保卡持卡人信息（社保卡金融账户签约时插入、随后查询也用）' stored as kudu;

CREATE TABLE `线下ba01` ( 
`bba101` string  COMMENT '银行机构id		',
`aad108` string  COMMENT '银行类别',
`bba102` string  COMMENT '银行名称       ',
`bba103` string  COMMENT '银行联系人     ',
`bba104` string  COMMENT '银行联系方式   ',
`bba105` string  COMMENT '银行通讯地址   ',
`aae036` timestamp  COMMENT '更新时间       ',
PRIMARY KEY (`bba101`)
) COMMENT '？与社保卡金融功能签约的银行信息' stored as kudu;

CREATE TABLE `线下ba06` ( 
`bba101` string  COMMENT '可签约银行记录ID',
`bba102` string  COMMENT '银行名称',
`bba602` string  COMMENT '银行图标',
PRIMARY KEY (`bba101`)
) COMMENT '？可签约银行表' stored as kudu;

CREATE TABLE `线下kb02` ( 
`kkb201` string  COMMENT '医疗机构签约id		',
`kkb101` string  COMMENT '医疗机构id            ',
`bba101` string  COMMENT '银行id                ',
`kkb202` string  COMMENT '医院在银联的商户号      ',
`kkb203` string  COMMENT '对应收单银行名称      ',
`kkb204` string  COMMENT '对应收单银行帐户      ',
`kkb205` double  COMMENT '单笔金额上限          ',
`kkb206` double  COMMENT '单笔金额下限          ',
`kkb207` double  COMMENT '单笔退货交易上限      ',
`kkb208` double  COMMENT '日累计正交易金额上限  ',
`kkb209` double  COMMENT '日累计退货交易上限    ',
`kkb210` string  COMMENT '商户fallback标志      ',
`kkb211` string  COMMENT '商户交易状态          ',
`kkb212` timestamp  COMMENT '受理开始时间          ',
`kkb213` timestamp  COMMENT '受理终止时间          ',
`kkb214` string  COMMENT '商户交易权限位图      ',
`kkb215` string  COMMENT '协议状态(1有效，0无效)',
`kkb216` string  COMMENT '工行证书ID|转出账号名称',
`kkb217` string  COMMENT '集团号|行内医院编码|集团客户号',
`kkb218` string  COMMENT '归属银行编号(工行)',
`kkb219` string  COMMENT '转出账号',
`kkb220` string  COMMENT '转出账号中文名称',
`kkb403` string  COMMENT '签约类型（代收：f_daishuo;代付：f_daifu）',
`aae036` timestamp  COMMENT '更新时间              ',
PRIMARY KEY (`kkb201`)
) COMMENT '线下各家医疗机构与银行或者银联的签约信息（关联之后患者用社保卡金融账户的钱才能到医院账户）' stored as kudu;

CREATE TABLE `线下sg01` ( 
`ssg101` string  COMMENT '持卡人签约信息id',
`baz061` string  COMMENT 'sid ',
`aaz500` string  COMMENT '社保卡号 ',
`aae010` string  COMMENT '银行账号 ',
`aad108` string  COMMENT '银行账号所属银行类别',
`ssg102` string  COMMENT '是否签约银行 ',
`ssg103` string  COMMENT '是否签约银联 ',
`ssg104` string  COMMENT '签约方式（1电签，2面签,3,微信签约）',
`ssg105` string  COMMENT '办理材料存储位置',
`aae036` timestamp  COMMENT '更新时间',
PRIMARY KEY (`ssg101`)
) COMMENT '持卡人社保卡金融账户签约信息' stored as kudu;

CREATE TABLE `线下sg02` ( 
`ssg201` string  COMMENT '持卡人签约日志id					',
`ssg202` string  COMMENT '操作类型：1新增，3修改，2取消签约  ',
`ssg101` string  COMMENT '持卡人签约信息id                   ',
`baz061` string  COMMENT 'sid                                ',
`aaz500` string  COMMENT '社保卡号                           ',
`aae010` string  COMMENT '银行账号                           ',
`ssg102` string  COMMENT '是否签约银行                       ',
`ssg103` string  COMMENT '是否签约银联                       ',
`ssg104` string  COMMENT '签约方式（1电签，2面签,3,微信签约）',
`ssg105` string  COMMENT '办理材料存储位置',
`kkb101` string  COMMENT '医疗机构id                         ',
`ddv102` string  COMMENT '读卡器号                           ',
`ddv103` string  COMMENT 'psam卡号                           ',
`vva001` string  COMMENT '验证码流水号                       ',
`aae011` string  COMMENT '经办人                             ',
`aae036` timestamp  COMMENT '经办时间                           ',
PRIMARY KEY (`ssg201`)
) COMMENT '持卡人社保卡金融账户签约信息日志' stored as kudu;

CREATE TABLE `线下ta01` ( 
`tta101` string  COMMENT '平台交易订单号															',
`aaa027` string  COMMENT '统筹区划                                                                  ',
`kkb101` string  COMMENT '医疗机构id                                                                ',
`tta103` string  COMMENT '门诊号                                                                    ',
`tta104` string  COMMENT '结算类型：11普通门诊15慢性病21住院                                           ',
`tta105` string  COMMENT '单据号                                                                    ',
`tta106` timestamp  COMMENT '结算时间                                                                  ',
`tta107` string  COMMENT '个人编号                                                                  ',
`aaz500` string  COMMENT '社保卡号                                                                  ',
`aac003` string  COMMENT '姓名                                                                      ',
`tta108` double  COMMENT '银行卡支付金额                                                            ',
`aae010` string  COMMENT '银行账号                                       ',
`tta119` double  COMMENT '渠道清算金额                                                            ',
`tta109` string  COMMENT '其他费用                                                                  ',
`ddv102` string  COMMENT '读卡器号                                                                  ',
`ddv103` string  COMMENT 'psam卡号                                                                  ',
`aad108` string  COMMENT '银行类别                                        ',
`bba101` string  COMMENT '银行id                                    ',
`kkb202` string  COMMENT '商户号，为退费时提供方便                                                  ',
`tta111` string  COMMENT '交易当前状态:0-金融交易进行中，1-金融代收成功，2-金融代收失败，3-金融退费成功，4金融退费失败',
`tta112` string  COMMENT '医保经办人编号                                                            ',
`tta113` string  COMMENT '医保经办人姓名                                                            ',
`aae036` timestamp  COMMENT '更新日期                                                                  ',
`tta114` string  COMMENT '医保上报的银行结算流水号，便于医保对账                                    ',
`tta115` string  COMMENT '医保上报的险种类型，便于医保对账',
`tta116` string  COMMENT '持卡人在该机构HIS系统内关联的就诊卡号',
`tta117` string  COMMENT '此次结算PC的IP地址',
`tta118` string  COMMENT '此次结算PC的MAC地址',
`baz061` string  COMMENT '持卡人的sid，为后续统计某一个人的所有交易记录提供便利                     ',
`tta001` string  COMMENT '是否需要反交易处理，0和null：无需进行反交易，1：需进行反交易处理，且未处理或处理失败 ，2 :进行了反交易，自动处理成功或人工退费成功                                   ',
PRIMARY KEY (`tta101`)
) COMMENT '线下社保卡金融账户历次交易信息' stored as kudu;

CREATE TABLE `视图用途说明sys_view` ( 
`viewName` string  COMMENT '视图名称',
`viewRemark` string  COMMENT '视图说明',
`createuser` string  COMMENT '创建者',
`createdate` timestamp  COMMENT '创建日期',
`viewGroup` string  COMMENT '逻辑分组',
PRIMARY KEY (`viewName`)
) stored as kudu;

CREATE TABLE `address_info` ( 
`ID` string ,
`RECEIPT_PERSON` string  COMMENT '收件人',
`CONTACT` string  COMMENT '收件人电话',
`PROVINCE` string  COMMENT '地址省份',
`CITY` string  COMMENT '地址城市',
`DISTRICT` string  COMMENT '地址区域',
`SITE` string  COMMENT '详细地址',
`IS_DEFAULT` string  COMMENT '是否是默认地址',
`PERSON_ID` string  COMMENT '用户Id（userid）',
PRIMARY KEY (`ID`)
) COMMENT '收货地址' stored as kudu;

CREATE TABLE `au_dict_prop` ( 
`id` string  COMMENT '主键ID',
`prop_key` string  COMMENT '属性值',
`prop_value` string  COMMENT '属性名称',
`type_id` string  COMMENT '所属类型ID',
`description` string  COMMENT '属性描述',
`enabled` bigint  COMMENT '是否可用',
`show_order` string  COMMENT '排序',
`create_date` timestamp  COMMENT '创建时间',
`modify_date` timestamp  COMMENT '修改时间',
`create_user_name` string  COMMENT '创建人',
`modify_user` string  COMMENT '修改人',
`create_user_id` bigint ,
`create_time` timestamp ,
`jgid` string ,
PRIMARY KEY (`id`)
) COMMENT '数据字典属性表' stored as kudu;

CREATE TABLE `au_dict_type` ( 
`idseq` string  COMMENT '主键',
`type_id` string  COMMENT '类型主键ID',
`type_name` string  COMMENT '类型名称',
`dict_type` string  COMMENT '字典类型',
`description` string  COMMENT '类型描述',
`enabled` bigint  COMMENT '是否可用0否1是',
`create_date` timestamp  COMMENT '创建时间',
`modify_date` timestamp  COMMENT '修改时间',
`create_user_name` string  COMMENT '创建人',
`modify_user` string  COMMENT '修改人',
`create_user_id` bigint  COMMENT '创建者ID',
`create_time` timestamp  COMMENT '创建时间',
`jgid` string ,
PRIMARY KEY (`idseq`)
) COMMENT '数据字典类型表' stored as kudu;

CREATE TABLE `br01` ( 
`BBR101` bigint  COMMENT '提醒人员id',
`KKB101` bigint  COMMENT '医疗机构编码（kb01.kkb101）',
`KKB104` string  COMMENT '医疗机构名称',
`KKB701` bigint  COMMENT '科室平台id(kb07.KKB701)',
`KKB703` string  COMMENT '科室名称(kb07.KKB703)',
`KKB801` bigint  COMMENT '医生平台id(kb08.KKB801)',
`KKB803` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`BBR101`)
) COMMENT '提醒人员表' stored as kudu;

CREATE TABLE `br02` ( 
`BBR201` bigint  COMMENT '自增主键id',
`BBR202` string  COMMENT '需提醒的业务类型代码（au_dict_prop.prop_key）',
`BBR101` bigint  COMMENT '业务提醒人员id（br01.bbr101）',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`BBR201`)
) COMMENT '业务提醒人员关系表' stored as kudu;

CREATE TABLE `cm01` ( 
`KKB101` bigint  COMMENT '医疗机构编码（开方机构id）',
`CCM101` bigint  COMMENT '药品id（开方药品目录）',
`KKB104` string  COMMENT '医疗机构名称(开放机构）',
`CCM102` string  COMMENT '药品通用名',
`CCM103` string  COMMENT '通用名拼音简码',
`CCM104` string  COMMENT '药品商品名',
`CCM105` string  COMMENT '商品名拼音简码',
`CCM106` string  COMMENT '规格',
`CCM107` string  COMMENT '剂型',
`CCM108` string  COMMENT '毒理名称',
`CCM109` string  COMMENT '包装单位',
`CCM110` double  COMMENT '剂量',
`CCM111` string  COMMENT '剂量单位',
`CCM112` string  COMMENT '是否草药(0否1是)',
`CCM113` string  COMMENT '是否OTC(0否1是)',
`CCM114` string  COMMENT '是否药品(0否1是)',
`CCM115` string  COMMENT '是否有效(0否1是)',
`CCO101` timestamp  COMMENT '修改时间',
PRIMARY KEY (`CCM101`,`KKB101`)
) COMMENT '开方药品目录表（平台目录）' stored as kudu;

CREATE TABLE `cm02` ( 
`DDR401` bigint  COMMENT '划价药店/药房编码kb01.KKB101',
`CCM201` bigint  COMMENT '药品id（划价药品目录）',
`DDR402` string  COMMENT '划价药店/药房名称kb01.KKB104',
`CCM202` bigint  COMMENT '药店药品id',
`CCM203` string  COMMENT '药品通用名',
`CCM204` string  COMMENT '通用名拼音简码',
`CCM205` string  COMMENT '药品商品名',
`CCM206` string  COMMENT '商品名拼音简码',
`CCM207` string  COMMENT '规格',
`CCM208` string  COMMENT '剂型',
`CCM209` string  COMMENT '毒理名称',
`CCM212` string  COMMENT '包装单位',
`CCM213` string  COMMENT '生产厂家',
`CCM214` double  COMMENT '单价',
`CCM215` string  COMMENT '医保目录编码',
`CCM220` string  COMMENT '医保目录名称',
`CCM216` string  COMMENT '是否草药(0否1是)',
`CCM217` string  COMMENT '是否OTC(0否1是)',
`CCM218` string  COMMENT '是否药品(0否1是)',
`CCM219` string  COMMENT '是否有效(0否1是)',
`CCM221` string  COMMENT '药品图片地址',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '修改时间',
PRIMARY KEY (`CCM201`,`DDR401`)
) COMMENT '药店划价药品目录' stored as kudu;

CREATE TABLE `cm03` ( 
`KKB101` bigint  COMMENT '医疗机构编码',
`CCM301` bigint  COMMENT '用法代码',
`KKB104` string  COMMENT '医疗机构名称',
`CCM302` string  COMMENT '用法名称',
`CCM403` string  COMMENT '顺序号',
`CCM304` string  COMMENT '是否有效(0否1是)',
`CCO101` timestamp  COMMENT '修改时间',
`CCM305` string  COMMENT '拼音简码',
PRIMARY KEY (`CCM301`,`KKB101`)
) COMMENT '用药用法目录（平台目录）' stored as kudu;

CREATE TABLE `cm04` ( 
`KKB101` bigint  COMMENT '医疗机构编码（平台id）',
`CCM401` bigint  COMMENT '使用频率代码',
`KKB104` string  COMMENT '医疗机构名称(平台名称）',
`CCM402` string  COMMENT '使用频率名称',
`CCM403` string  COMMENT '顺序号',
`CCM404` string  COMMENT '是否有效(0否1是)',
`CCO101` timestamp  COMMENT '修改时间',
`CCM405` string  COMMENT '拼音简码',
PRIMARY KEY (`CCM401`,`KKB101`)
) COMMENT '用药频率目录（平台目录）' stored as kudu;

CREATE TABLE `cm05` ( 
`CCM501` bigint  COMMENT '发货地址id',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR402` string  COMMENT '划价药店/药房名称',
`CCM502` string  COMMENT '发货地址',
`CCM503` string  COMMENT '经度',
`CCM504` string  COMMENT '纬度',
`CCM505` string  COMMENT '是否有效（0否1是）',
`CCO106` bigint  COMMENT '操作员ID（patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCM501`)
) COMMENT '药店发货地址表' stored as kudu;

CREATE TABLE `cm06` ( 
`CCM601` bigint  COMMENT '药店发货人id',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR402` string  COMMENT '划价药店/药房名称',
`CCM602` string  COMMENT '药店发货人姓名',
`CCM603` string  COMMENT '药店发货人身份证号',
`CCM604` string  COMMENT '药店发货人手机号',
`CCM605` string  COMMENT '是否有效（0否1是）',
`CCO106` bigint  COMMENT '操作员ID（patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCM601`)
) COMMENT '药店发货人信息表' stored as kudu;

CREATE TABLE `cm07` ( 
`CCM701` bigint  COMMENT '委托配送单位id',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR402` string  COMMENT '划价药店/药房名称',
`CCM702` string  COMMENT '委托配送单位',
`CCM703` string  COMMENT '是否有效（0否1是）',
`CCO106` bigint  COMMENT '操作员ID（patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCM701`)
) COMMENT '委托配送单位表\r\n' stored as kudu;

CREATE TABLE `cm08` ( 
`KKB101` string  COMMENT '医疗机构id',
`AKC515` string  COMMENT '医疗机构收费项目编码',
`AKC223` string  COMMENT '医疗机构收费项目名称',
`AKA066` string  COMMENT '助记码',
`AKA090` string  COMMENT '医保项目编码',
`CCO101` timestamp  COMMENT '更改时间',
`CCO106` bigint  COMMENT '操作员id(sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.user_name)',
`isvalid` string  COMMENT '是否有效，0否1是',
PRIMARY KEY (`KKB101`,`AKC515`)
) COMMENT '机构诊疗项目表（平台目录）' stored as kudu;

CREATE TABLE `cm09` ( 
`CCM901` bigint  COMMENT '协定项目id',
`KKB101` bigint  COMMENT '医疗机构编码（kb01.kkb101）',
`KKB104` string  COMMENT '医疗机构名称（kb01.kkb104）',
`CCM902` string  COMMENT 'his项目id',
`CCM903` string  COMMENT '拼音编码',
`CCM904` string  COMMENT '拼音编码全拼',
`CCM905` string  COMMENT '数字编码',
`CCM906` string  COMMENT '协定项目名称',
`CCM907` string  COMMENT '单位',
`CCM908` double  COMMENT '单价',
`CCM909` string  COMMENT '是否停用(0正常 1停用)',
`CCM910` timestamp  COMMENT '停用时间',
`CCM911` bigint  COMMENT '停用操作员代码',
`CCM912` string  COMMENT '停用操作员名称',
`CCO101` timestamp  COMMENT '创建时间',
`CCO106` bigint  COMMENT '创建操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '创建操作员姓名(sys_user.user_name)',
PRIMARY KEY (`CCM901`)
) COMMENT '协定项目表（预约检查）' stored as kudu;

CREATE TABLE `contact_info` ( 
`user_id` bigint  COMMENT '用户id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '姓名patients.patientname',
`sex` string  COMMENT '性别',
`CCO104` string  COMMENT '身份证号(patients.idcardno)',
`handphone` string  COMMENT '手机号',
`medicaretypecode` string  COMMENT '个人身份代码',
`medicaretypename` string  COMMENT '个人身份名称',
`birthday` timestamp  COMMENT '出生日期',
`relationship` string  COMMENT '关系（参考字典表typeid=jtgx，注意：注册时存储为‘本人’）',
`is_default` string  COMMENT '是否为默认就诊人(0否1是)',
`areaid` bigint  COMMENT '区划代码',
`areaname` string  COMMENT '区划名称',
`address` string  COMMENT '家庭地址',
`CCO101` timestamp  COMMENT '创建时间(patients.create_time)',
`isvalid` string  COMMENT '1表示有效，0表示无效',
PRIMARY KEY (`user_id`,`CCO108`)
) COMMENT '就诊人信息表' stored as kudu;

CREATE TABLE `contact_info_card` ( 
`ID` bigint  COMMENT '自增ID',
`user_id` bigint  COMMENT '用户id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO112` string  COMMENT '卡片类型｛1:就诊卡，2:居民身份证，3：社保卡，4：银行卡（未用），5：病人id（未用），6：居民健康卡，7：积分卡（未用），8：条码（未用），9其它介质卡（未用）｝',
`CCO113` string  COMMENT '卡号',
`CCO105` string  COMMENT '姓名(patients.patientname)',
`KKB101` bigint  COMMENT '医疗机构id(原orgid)',
`KKB104` string  COMMENT '医疗机构名称(原orgname)',
`CCO101` timestamp  COMMENT '创建时间(patients.create_time)',
`sid` string  COMMENT '社保卡sid',
PRIMARY KEY (`ID`)
) COMMENT '就诊卡信息表' stored as kudu;

CREATE TABLE `cx01` ( 
`CCX101` bigint  COMMENT 'ID（自增id）',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`CCX102` string  COMMENT '手机号',
`CCX103` string  COMMENT '身份证号',
`CCX104` timestamp  COMMENT '最新登陆时间',
`CCX105` string  COMMENT '企业编码',
`CCX106` bigint  COMMENT '企业id',
`CCX107` string  COMMENT '熙康token',
`CCX108` bigint  COMMENT '机构id',
`CCX109` string  COMMENT '熙康userName',
`CCX110` string  COMMENT '是否为新用户',
`CCX111` bigint  COMMENT '熙康userId',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCX101`)
) COMMENT '登录记录表' stored as kudu;

CREATE TABLE `cx02` ( 
`CCX201` bigint  COMMENT '自增id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname',
`CCX202` bigint  COMMENT '订单id',
`CCX203` string  COMMENT '订单编号',
`CCX204` string  COMMENT '服务地址ID',
`CCX205` string  COMMENT '支付方式(type统一为1，为微信支付)',
`CCX206` bigint  COMMENT '规格id',
`CCX207` bigint  COMMENT '购买数量',
`CCX208` double  COMMENT '订单实际总价',
`CCX209` bigint  COMMENT '优惠券ID(实际为couponUserId)',
`CCX210` bigint  COMMENT '项目参与活动的id',
`CCX211` string  COMMENT '是否紧急上门',
`CCX212` double  COMMENT '紧急上门费用',
`CCX213` string  COMMENT '是否共享优惠券',
`CCX214` bigint  COMMENT 'addActivityId',
`CCX215` string  COMMENT '支付状态(0待支付 1已支付 2已取消 3支付失败)',
`CCX216` timestamp  COMMENT '操作时间',
`CCX217` bigint  COMMENT '项目id',
`CCX218` string  COMMENT '项目名字',
`CCX219` bigint  COMMENT '项目所属机构id',
`CCX220` string  COMMENT '机构名称',
`CCX221` double  COMMENT '项目原价',
`CCX222` bigint  COMMENT '购买次数',
`CCX223` double  COMMENT '订单原价',
`CCX224` double  COMMENT '订单优惠券价格',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCX201`)
) COMMENT '订单记录表' stored as kudu;

CREATE TABLE `cx03` ( 
`CCX301` bigint  COMMENT '自增ID',
`CCX302` bigint  COMMENT '联系人ID',
`CCX303` timestamp  COMMENT '预定开始时间',
`CCX304` timestamp  COMMENT '预定结束时间',
`CCX305` bigint  COMMENT '护理人id',
`CCX306` bigint  COMMENT '服务项目id',
`CCX202` bigint  COMMENT '订单id',
`CCX307` string  COMMENT '支付类型(type统一为1，为微信支付)',
`CCX308` bigint  COMMENT '规格id',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCX301`)
) COMMENT '预约记录表' stored as kudu;

CREATE TABLE `cx04` ( 
`CCX401` bigint  COMMENT '自增ID',
`CCX202` bigint  COMMENT '订单id',
`CCX203` string  COMMENT '订单编号',
`CCX108` bigint  COMMENT '机构id',
`CCX402` string  COMMENT '退款原因',
`CCX403` double  COMMENT '退款金额',
`CCX404` string  COMMENT '退款类型（订单类型）',
`CCX405` timestamp  COMMENT '申请退款时间',
`CCX406` string  COMMENT '机构联系电话',
`CCX407` bigint  COMMENT '剩余预约次数',
PRIMARY KEY (`CCX401`)
) COMMENT '退款记录表' stored as kudu;

CREATE TABLE `cx05` ( 
`CCX501` bigint  COMMENT '自增ID',
`CCX301` bigint  COMMENT '预约记录ID',
`CCX502` bigint  COMMENT '服务申请记录信息Id',
`CCX503` string  COMMENT '名称',
`CCX504` string  COMMENT '申请记录类型',
`CCX505` string  COMMENT '是否必填',
`CCX506` string  COMMENT '顺序',
`CCX507` string  COMMENT '值',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`CCX501`)
) COMMENT '服务申请记录信息表' stored as kudu;

CREATE TABLE `cz01` ( 
`CCZ101` bigint  COMMENT '订单号id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO112` string  COMMENT '卡类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`CCZ102` double  COMMENT '业务金额（正票为充值金额，退票为退的金额）',
`CCZ103` double  COMMENT '可退金额（正票为可退金额,负票为0）',
`CCZ104` double  COMMENT '业务后账户余额（正票被退不更新）',
`CCZ105` string  COMMENT '票据类型：-1负票1正票',
`CCZ106` string  COMMENT '被退状态：0未退1已全退2部分退',
`CCZ107` bigint  COMMENT '正/末次退票购药订单id',
`CCZ108` string  COMMENT '支付状态:0未支付1已支付2支付退款成功3已取消',
`CCZ109` string  COMMENT 'his充值状态:0未充值1充值成功2充值退款成功',
`CCZ110` string  COMMENT 'HIS收据号(调接口获取)',
`CCZ111` string  COMMENT '支付方式｛42微信线上支付、52支付宝线上支付、62 银联线上支付',
`KKB912` string  COMMENT '平台生成付款订单号',
`YYG209` string  COMMENT '第三方线上支付平台订单号',
`YYG210` string  COMMENT '平台生成的退款订单号',
`CCO106` bigint  COMMENT '操作员ID（patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间（充值时间）',
PRIMARY KEY (`CCZ101`)
) COMMENT '线上充值订单记录表（门诊充值）' stored as kudu;

CREATE TABLE `cz02` ( 
`CCZ201` bigint  COMMENT '门诊处方结算订单id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO112` string  COMMENT '卡类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`CCZ202` string  COMMENT 'his挂号单号',
`CCZ203` string  COMMENT 'his处方单号',
`CCZ204` timestamp  COMMENT 'his开单时间',
`CCZ205` double  COMMENT 'his处方费用',
`CCZ206` string  COMMENT 'his开单科室',
`CCZ207` string  COMMENT 'his开单医生',
`CCZ208` string  COMMENT 'his处方类别 0自费  1医保',
`CCZ209` string  COMMENT 'his交易流水号（his预结算返回）',
`CCZ210` string  COMMENT 'his结算ID（his结算返回）',
`CCZ211` string  COMMENT '票据类型：-1负票1正票',
`CCZ212` string  COMMENT '被退状态：0未退1已全退2部分退',
`CCZ213` bigint  COMMENT '正/末次退票购药订单id',
`CCZ214` string  COMMENT '结算状态：0未结算1已结算2已退结算3已取消',
`CCZ215` string  COMMENT '支付状态：两位，第一位代表自费（说明：0代表未支付1代表已经支付2代表已退款x代表未使用）第二位代表医保（说明：0代表未支付1代表已经支付2代表已退款x代表未使用）00:自费未支付，医保未结算、10：自费已支付，医保未结算、11 自费已支付，医保已结算、20自费已退费，医保未结算、22自费已退费，医保已退费，0x纯自费未支付；1x纯自费已支付；2x纯自费已退款；x0纯医保未支付；x1纯医保已支付，x2纯医保已退款，xx不需要挂号费；',
`CCZ216` string  COMMENT '支付方式：00全医保42微信52支付宝62云闪付（区分自费流程的支付方式）',
`CCZ217` double  COMMENT '订单费用',
`CCZ218` string  COMMENT '平台生成付款订单号',
`CCZ219` string  COMMENT '第三方线上支付平台订单号',
`CCZ220` string  COMMENT '平台生成的退款订单号',
`CCZ221` double  COMMENT '总订单费用',
`CCZ222` double  COMMENT '医保统筹支付金额',
`CCZ223` double  COMMENT '医保个人账户支付金额',
`CCZ224` double  COMMENT '自费支付金额',
`CCZ225` double  COMMENT '医保其他支付金额',
`CCZ226` string  COMMENT '社保卡SID',
`CCZ227` timestamp  COMMENT '支付时间',
`CCO106` bigint  COMMENT '操作员ID（patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间（结算时间）',
PRIMARY KEY (`CCZ201`)
) COMMENT '门诊处方结算订单记录表' stored as kudu;

CREATE TABLE `cz03` ( 
`CCZ301` bigint  COMMENT '门诊处方结算订单明细id',
`CCZ201` bigint  COMMENT '门诊处方结算订单id',
`CCZ202` string  COMMENT 'his挂号单号',
`CCZ203` string  COMMENT 'his处方单号',
`CCZ302` string  COMMENT '费用类别名称',
`CCZ303` string  COMMENT '费用名称',
`CCZ304` string  COMMENT '费用编码',
`CCZ305` string  COMMENT '规格',
`CCZ306` string  COMMENT '单位',
`CCZ307` double  COMMENT '数量',
`CCZ308` double  COMMENT '单价',
`CCZ309` double  COMMENT '金额',
`CCZ310` string  COMMENT '备注',
PRIMARY KEY (`CCZ301`)
) COMMENT '门诊处方结算订单明细表' stored as kudu;

CREATE TABLE `cz04` ( 
`CCZ401` bigint  COMMENT '订单号ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO112` string  COMMENT '卡类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(PATIENTS.PATIENTID)',
`CCO105` string  COMMENT '患者姓名(PATIENTS.PATIENTNAME)',
`CCZ402` string  COMMENT '患者手机号码',
`CCZ403` string  COMMENT '病区编码',
`CCZ404` string  COMMENT '病区名称',
`CCZ405` string  COMMENT '科室名称',
`CCZ406` string  COMMENT '医生姓名',
`CCZ407` double  COMMENT '已交预交金额',
`CCZ408` double  COMMENT '总费用',
`CCZ409` double  COMMENT '业务金额（正票为充值金额，退票为退的金额）',
`CCZ410` double  COMMENT '可退金额（正票为可退金额,负票为0）',
`CCZ411` double  COMMENT '业务后账户余额（正票被退不更新）',
`CCZ412` string  COMMENT '票据类型：-1负票1正票',
`CCZ413` string  COMMENT '被退状态：0未退1已全退2部分退',
`CCZ414` bigint  COMMENT '正/末次退票购药订单ID',
`CCZ415` string  COMMENT '支付状态:0未支付1已支付2支付退款成功3已取消',
`CCZ416` string  COMMENT 'HIS充值状态:0未充值1充值成功2充值退款成功',
`CCZ417` string  COMMENT 'HIS住院押金充值流水号(调接口获取)',
`CCZ418` string  COMMENT '支付方式｛42微信线上支付、52支付宝线上支付、62 银联线上支付',
`CCZ419` string  COMMENT '住院号',
`KKB912` string  COMMENT '平台生成付款订单号',
`YYG209` string  COMMENT '第三方线上支付平台订单号',
`YYG210` string  COMMENT '平台生成的退款订单号',
`CCO106` bigint  COMMENT '操作员ID（PATIENTS_LOGIN.USER_ID)',
`CCO107` string  COMMENT '操作员姓名(PATIENTS_LOGIN.PATIENTNAME)',
`CCO101` timestamp  COMMENT '创建时间（充值时间）',
`CCZ420` bigint  COMMENT 'HIS操作员id',
`CCZ421` string  COMMENT 'HIS操作员姓名',
`CCZ422` timestamp  COMMENT 'HIS退费时间',
`CCZ423` string  COMMENT 'HIS住院交预交金单据号',
PRIMARY KEY (`CCZ401`)
) COMMENT '线上充值订单记录表（住院缴费预交金充值）' stored as kudu;

CREATE TABLE `dj01` ( 
`DDJ101` bigint  COMMENT '主键id',
`KKB101` bigint  COMMENT '医疗机构id（kb01.kkb101）',
`DDJ102` string  COMMENT '对接账号（dddl+企业名称简拼+对接人手机号码）',
`DDJ104` string  COMMENT '企业信息（例如：企业名称|企业对接人姓名|企业对接人手机号码）',
`DDJ103` string  COMMENT '对接密码（对接账号转base64后MD5值）',
`DDJ105` string  COMMENT '内部调用url(二次报销)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`DDJ101`)
) COMMENT '对接单点登录平台账号密码专用表' stored as kudu;

CREATE TABLE `do01` ( 
`DDO101` bigint  COMMENT '配送单id',
`DDO102` string  COMMENT '配送状态（0未发货1已发货2已签收）',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR402` string  COMMENT '划价药店/药房名称',
`CCM601` bigint  COMMENT '药店发货人id',
`CCM602` string  COMMENT '药店发货人姓名',
`CCM603` string  COMMENT '药店发货人身份证号',
`CCM604` string  COMMENT '药店发货人手机号',
`CCM501` bigint  COMMENT '发货地址id仓储点id',
`CCM502` string  COMMENT '发货地址(仓储点地址）',
`CCM503` string  COMMENT '发货经度',
`CCM504` string  COMMENT '发货纬度',
`DDO103` timestamp  COMMENT '发货时间',
`CCM701` bigint  COMMENT '委托配送单位id',
`CCM702` string  COMMENT '委托配送单位',
`DDO104` double  COMMENT '委托配送费',
`DDO105` string  COMMENT '委托配送备注',
`OOR101` bigint  COMMENT '购药订单id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`RECEIPT_PERSON` string  COMMENT '收件人',
`CONTACT` string  COMMENT '收件人电话address_info.CONTACT',
`PROVINCE` string  COMMENT '地址省份address_info.PROVINCE',
`CITY` string  COMMENT '地址城市address_info.CITY',
`DISTRICT` string  COMMENT '地址区域address_info.DISTRICT',
`SITE` string  COMMENT '详细地址address_info.SITE',
`DDO106` timestamp  COMMENT '签收时间',
PRIMARY KEY (`DDO101`)
) COMMENT '购药配送单表\r\n' stored as kudu;

CREATE TABLE `do02` ( 
`HHA401` bigint  COMMENT '评价id',
`DDO101` bigint  COMMENT '配送单id',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR402` string  COMMENT '划价药店/药房名称',
`OOR101` bigint  COMMENT '购药订单id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`HHA402` string  COMMENT '评价级别',
`HHA403` string  COMMENT '评价内容',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HHA401`)
) COMMENT '购药评价表' stored as kudu;

CREATE TABLE `doctor_audit` ( 
`id` bigint  COMMENT '自增id',
`userid` bigint  COMMENT '医生id(sys_user.user_id)',
`auditstatus` string  COMMENT '审核状态（0未审核，1待审核，2已审核）',
PRIMARY KEY (`id`)
) stored as kudu;

CREATE TABLE `dr01` ( 
`DDR101` bigint  COMMENT '处方ID（平台序号）',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)开方医生id',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)开方医生姓名',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO110` bigint  COMMENT 'HIS科室id/小屋id(kb07.KKB702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`OOT201` bigint  COMMENT '在线问诊订单id(门诊号）',
`CCO112` string  COMMENT '卡片类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`DDR102` string  COMMENT '性别',
`DDR103` string  COMMENT '年龄',
`DDR104` string  COMMENT '处方来源1在线开方2上传处方3慢性病购药4云购药',
`DDR105` timestamp  COMMENT '开方时间',
`DDR106` bigint  COMMENT '主诊断代码(病种编码）',
`DDR107` string  COMMENT '主诊断名称(病种名称）',
`DDR108` string  COMMENT '诊断描述',
`DDR110` string  COMMENT '结算状态0未结算1已结算2已退结算',
`DDR125` timestamp  COMMENT '已结算时间',
`DDR126` timestamp  COMMENT '已退结算时间',
`DDR111` string  COMMENT '医疗类别',
`DDR128` string  COMMENT '医疗类别名称',
`DDR112` string  COMMENT '医师审方状态（0未审1通过、2不通过）',
`DDR113` string  COMMENT '处方审计状态（0未审1通过、2不通过）',
`DDR114` string  COMMENT '药师审方状态（0未审1通过、2不通过）',
`DDR115` bigint  COMMENT '处方核对药剂师id',
`DDR116` string  COMMENT '处方核对药剂师姓名',
`DDR117` bigint  COMMENT '处方调配药剂师id',
`DDR118` string  COMMENT '处方调配药剂师姓名',
`DDR119` bigint  COMMENT '签章药师id',
`DDR120` string  COMMENT '签章药师姓名',
`DDR121` bigint  COMMENT '签章医师id',
`DDR122` string  COMMENT '签章医师姓名（CA）',
`DDR123` string  COMMENT '处方锁定（0正常1锁定）',
`DDR127` timestamp  COMMENT '处方锁定时间',
`DDR124` string  COMMENT '处方类别0西药1中成药2中药饮片3医药',
`DDR129` string  COMMENT '是否已重开处方(0未重开 1已重开)',
`CCO106` bigint  COMMENT '问诊账号（patients_login.user_id)',
`CCO107` string  COMMENT '问诊姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`DDR101`)
) COMMENT '处方表' stored as kudu;

CREATE TABLE `dr02` ( 
`DDR201` bigint  COMMENT '处方明细ID',
`DDR101` bigint  COMMENT '处方ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCM101` bigint  COMMENT '药品id（开方药品目录）',
`CCM102` string  COMMENT '药品通用名',
`CCM104` string  COMMENT '药品商品名',
`CCM106` string  COMMENT '规格',
`CCM107` string  COMMENT '剂型',
`CCM108` string  COMMENT '毒理名称',
`CCM109` string  COMMENT '包装单位（出库单位）',
`CCM110` double  COMMENT '剂量',
`CCM111` string  COMMENT '剂量单位',
`DDR202` double  COMMENT '次剂量(单次用量)',
`CCM301` bigint  COMMENT '用法代码',
`CCM302` string  COMMENT '用法名称',
`CCM401` bigint  COMMENT '使用频率代码',
`CCM402` string  COMMENT '使用频率名称',
`DDR203` string  COMMENT '用药天数',
`DDR204` string  COMMENT '数量（出库单位数量）',
`DDR205` string  COMMENT '单付数量',
`DDR206` string  COMMENT '付数',
`DDR207` string  COMMENT '备注',
`CCO106` bigint  COMMENT '问诊账号（patients_login.user_id)',
`CCO107` string  COMMENT '问诊姓名(patients_login.patientname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`DDR201`)
) COMMENT '处方药品表\r\n' stored as kudu;

CREATE TABLE `dr03` ( 
`DDR301` bigint  COMMENT '审核id',
`DDR101` bigint  COMMENT '处方ID',
`DDR302` string  COMMENT '审核状态（0未审、1通过、2不通过）',
`DDR303` string  COMMENT '审核意见',
`DDR304` string  COMMENT '审核类型（1医师审方、2处方审计、3药师审方）',
`DDR401` bigint  COMMENT '划价药店/药房编码/医师审方机构',
`DDR402` string  COMMENT '划价药店/药房名称/医师审方机构',
`DDR305` bigint  COMMENT '审核人id',
`DDR306` string  COMMENT '审核姓名',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '创建时间（审核时间）',
PRIMARY KEY (`DDR301`)
) COMMENT '处方审核表' stored as kudu;

CREATE TABLE `dr04` ( 
`DDR101` bigint  COMMENT '处方ID',
`DDR401` bigint  COMMENT '划价药店/药房编码',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO110` bigint  COMMENT 'HIS科室id/小屋id(kb07.KKB702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`OOT201` bigint  COMMENT '在线问诊订单id（门诊号）',
`CCO112` string  COMMENT '卡片类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`DDR102` string  COMMENT '性别',
`DDR103` string  COMMENT '年龄',
`DDR124` string  COMMENT '处方类别0西药1中成药2中药饮片',
`DDR106` bigint  COMMENT '主诊断代码(病种编码）',
`DDR107` string  COMMENT '主诊断名称(病种名称）',
`DDR109` string  COMMENT '划价状态0药店划价中1审核未通过无法划价2无库存无法划价',
`DDR402` string  COMMENT '划价药店/药房名称',
`DDR403` string  COMMENT '划价员id',
`DDR404` string  COMMENT '划价员姓名',
`DDR405` timestamp  COMMENT '划价时间',
`DDR301` bigint  COMMENT '审核id(药师审方)',
`CCO106` bigint  COMMENT '问诊账号（patients_login.user_id)，由py创建且不可修改',
`CCO107` string  COMMENT '问诊姓名(patients_login.patientname)，由py创建且不可修改',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`DDR401`,`DDR101`)
) COMMENT '药店/药房划价表\r\n' stored as kudu;

CREATE TABLE `dr05` ( 
`DDR401` bigint  COMMENT '划价药店/药房编码',
`DDR101` bigint  COMMENT '处方ID',
`DDR201` bigint  COMMENT '处方明细ID',
`DDR402` string  COMMENT '划价药店/药房名称',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCM101` bigint  COMMENT '药品id（开方药品目录）',
`CCM102` string  COMMENT '药品通用名',
`CCM104` string  COMMENT '药品商品名',
`CCM106` string  COMMENT '规格',
`CCM107` string  COMMENT '剂型',
`CCM109` string  COMMENT '包装单位',
`DDR204` string  COMMENT '数量（总量）',
`DDR205` string  COMMENT '单付数量',
`DDR206` string  COMMENT '付数',
`DDR207` string  COMMENT '备注',
`CCM201` bigint  COMMENT '药品id（划价药品目录）平台码',
`CCM202` bigint  COMMENT '药店药品id',
`CCM203` string  COMMENT '药品通用名',
`CCM205` string  COMMENT '药品商品名',
`CCM207` string  COMMENT '规格',
`CCM208` string  COMMENT '剂型',
`CCM209` string  COMMENT '毒理名称',
`CCM212` string  COMMENT '包装单位',
`CCM213` string  COMMENT '生产厂家',
`CCM214` double  COMMENT '单价',
`CCM215` string  COMMENT '医保目录编码',
`CCM220` string  COMMENT '医保目录名称',
`DDR502` string  COMMENT '划价药店开药数量(现用于人社app慢性病购药)',
PRIMARY KEY (`DDR401`,`DDR101`,`DDR201`)
) COMMENT '处方药品划价表' stored as kudu;

CREATE TABLE `dy01` ( 
`ddy101` bigint  COMMENT '角色ID',
`ddy102` string  COMMENT '角色名称',
`ddy103` string  COMMENT '是否管理员 0否 1是',
`ddy104` string  COMMENT 'vue首页名称',
`ddy105` string  COMMENT 'vue个人名称',
`isvalid` string  COMMENT '是否有效(0否1是)',
`cco106` string  COMMENT '操作员id',
`cco107` string  COMMENT '操作员姓名',
`cco101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`ddy101`)
) COMMENT '医生移动端角色表' stored as kudu;

CREATE TABLE `dy02` ( 
`kkb101` bigint  COMMENT '医疗机构id',
`deptype` string  COMMENT '类型：1科室 2小屋',
`cco109` bigint  COMMENT '科室小屋id/小屋id(kb07.kkb701/health_room.roomid)',
`user_id` bigint  COMMENT '医生ID',
`ddy101` bigint  COMMENT '角色ID',
`kkb104` string  COMMENT '医疗机构名称(原orgname)',
`cco111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`kkb801` bigint  COMMENT '医生编号',
`realname` string  COMMENT '医生真实姓名',
`cco106` string  COMMENT '操作员id',
`cco107` string  COMMENT '操作员姓名',
`cco101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`kkb101`,`cco109`,`user_id`,`ddy101`,`deptype`)
) COMMENT '医生移动端角色关联表' stored as kudu;

CREATE TABLE `eb01` ( 
`EEB101` bigint  COMMENT '记录id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`EEB102` string  COMMENT '允许二次报销单位编码',
`CCO101` timestamp  COMMENT '更新日期',
PRIMARY KEY (`EEB101`)
) stored as kudu;

CREATE TABLE `fl01` ( 
`log_id` string  COMMENT '日志ID',
`imgurl` string  COMMENT '图片在fastdfs中的存储位置',
`createtime` timestamp  COMMENT '图片保存时间',
PRIMARY KEY (`log_id`)
) COMMENT 'fastdfs服务器中图片地址日志（可被删除的图片）' stored as kudu;

CREATE TABLE `fw01` ( 
`ffw101` bigint  COMMENT '服务id',
`ffw102` string  COMMENT '服务名称',
`ffw103` string  COMMENT '英文服务名',
`ffw104` string  COMMENT '业务路由',
PRIMARY KEY (`ffw101`)
) stored as kudu;

CREATE TABLE `fw02` ( 
`ffw201` bigint  COMMENT '主键',
`ffw101` bigint  COMMENT '服务id(fw01.ffw101)',
`ffw102` string  COMMENT '服务名称(fw01.ffw102)',
`areaid` string  COMMENT '城市编号sys_area.areaid',
`areaname` string  COMMENT '行政区名称(sys_area.areaname)',
`isvalid` string  COMMENT '是否有效（0否，1是）',
`ffw103` string  COMMENT '英文服务名',
`ffw104` string  COMMENT '业务路由',
PRIMARY KEY (`ffw201`)
) stored as kudu;

CREATE TABLE `gh01` ( 
`GGH101` string  COMMENT '预约编号（由平台的序列生成）',
`KKB101` string  COMMENT '医疗机构编码',
`KKB902` string  COMMENT '排班ID',
`GGH102` string  COMMENT '预约单号？程序里写死了1',
`KKB602` string  COMMENT '科室分类ID',
`KKB603` string  COMMENT '科室分类名称',
`KKB702` string  COMMENT '科室ID',
`KKB703` string  COMMENT '科室名称',
`KKB802` string  COMMENT '医生ID',
`KKB803` string  COMMENT '医生名称',
`KKB804` string  COMMENT '职称ID',
`KKB805` string  COMMENT '职称名称',
`KKB806` string  COMMENT '级别ID',
`KKB807` string  COMMENT '级别名称',
`AAC003` string  COMMENT '患者姓名',
`AAZ500` string  COMMENT '就诊卡号：可以绑定社保卡、就诊卡等',
`BAZ061` string  COMMENT '社保卡SID',
`idcard` string  COMMENT '身份证号',
`BAE017` string  COMMENT '联系方式',
`KKB903` string  COMMENT '预约就诊日期',
`KKB905` string  COMMENT '午别(S上午/X下午/Y夜间) ',
`KKB910` string  COMMENT '可挂号时间(如果HIS号源给的是时间点则此字段保存的就是这个时间点,如果HIS号源给的是时间段则此字段为结束时间)',
`KKB911` string  COMMENT '开始时间(如果HIS号源给的是时间点则此字段为空,如果HIS号源给的是时间段则此字段为开始时间)',
`GGH103` string  COMMENT '预约单状态：0预约未成功1预约成功2退号3已取消',
`GGH104` string  COMMENT '支付状态｛00:自费未支付，医保未结算、10：自费已支付，医保未结算、11 自费已支付，医保已结算、20自费已退费，医保未结算、22自费已退费，医保已退费，30订单已关单，0x纯自费未支付；1x纯自费已支付；2x纯自费已退款；x0纯医保未支付；x1纯医保已支付，x2纯医保已退款，xx不需要挂号费；  }',
`GGH105` string  COMMENT '支付方式｛00全部用医保支付、42微信线上支付、52支付宝线上支付、62 银联线上支付｝【原来叫：自费金额支付方式{4微信5支付宝6云闪付7全部用医保支付}】',
`KKB909` double  COMMENT '挂号费用',
`AAE036` timestamp  COMMENT '更新时间',
`KKB809` string  COMMENT 'HIS交易流水号',
`AAE011` string  COMMENT '操作人',
`KKB912` string  COMMENT '平台生成的付款订单号',
`KKB913` string  COMMENT '第三方线上支付平台订单号',
`KKB914` string  COMMENT '平台生成的退款订单号',
`fee_total` double  COMMENT '总挂号费用',
`fee_coordination` double  COMMENT '医保统筹支付金额',
`fee_personal_account` double  COMMENT '医保个人账户支付金额',
`fee_personal_wallet` double  COMMENT '自费支付金额=总挂号费-医保统筹-医保账户支付-医保其他支付金额',
`fee_other` double  COMMENT '医保其他支付金额',
`reg_id` string  COMMENT 'HIS的锁号流水号 ',
`card_type` string  COMMENT '卡片类型',
`reg_recipt_id` string  COMMENT 'his挂号单号',
`CCO114` string  COMMENT '结算类型（1医保 0自费）',
`GGH106` string  COMMENT '自费退号流水表主键id(trade_flow_wechat.trade_flow_id/trade_flow_alipay.trade_flow_id/trade_flow_union.trade_flow_id)',
PRIMARY KEY (`GGH101`)
) COMMENT '线上预约挂号订单表' stored as kudu;

CREATE TABLE `gy01` ( 
`GGY101` bigint  COMMENT 'ID（自增id）',
`CCO108` bigint  COMMENT '患者id（patientid）',
`CCO105` string  COMMENT '患者姓名',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`KKB601` string  COMMENT '科室分类编号',
`KKB603` string  COMMENT '科室分类名称',
`KKB607` string  COMMENT '分类映射',
`GGY102` string  COMMENT '咨询状态（0待咨询 1咨询中 2咨询完 3已取消）',
`GGY103` timestamp  COMMENT '发起咨询时间',
`GGY104` timestamp  COMMENT '医生接受咨询时间',
`GGY105` timestamp  COMMENT '医生结束咨询时间',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`GGY106` timestamp  COMMENT '问卷时间',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`GGY101`)
) stored as kudu;

CREATE TABLE `gz01` ( 
`GGZ101` bigint  COMMENT 'ID（自增id）',
`userId` bigint  COMMENT '医生用户id',
`GGZ102` string  COMMENT '工资卡号',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`GGZ101`)
) stored as kudu;

CREATE TABLE `gz02` ( 
`GGZ201` bigint  COMMENT 'ID（自增id）',
`GGZ245` string  COMMENT '工资卡号',
`GGZ202` string  COMMENT '单位内部人员编号',
`GGZ203` string  COMMENT '人员姓名',
`GGZ204` string  COMMENT '岗位工资',
`GGZ205` string  COMMENT '保留工资',
`GGZ206` string  COMMENT '年功工资',
`GGZ207` string  COMMENT '加班工资',
`GGZ208` string  COMMENT '夜班津贴',
`GGZ209` string  COMMENT '交通补贴',
`GGZ210` string  COMMENT '取暖补贴',
`GGZ211` string  COMMENT '暑假补贴',
`GGZ212` string  COMMENT '信访津贴',
`GGZ213` string  COMMENT '保健津贴',
`GGZ214` string  COMMENT '女工卫生费',
`GGZ215` string  COMMENT '生育津贴',
`GGZ216` string  COMMENT '工伤津贴',
`GGZ217` string  COMMENT '护龄津贴',
`GGZ218` string  COMMENT '教护百分之十工资',
`GGZ219` string  COMMENT '补发工资',
`GGZ220` string  COMMENT '绩效奖惩',
`GGZ221` string  COMMENT '院嘉奖嘉奖',
`GGZ222` string  COMMENT '全勤奖',
`GGZ223` string  COMMENT '生产奖',
`GGZ224` string  COMMENT '安全奖',
`GGZ225` string  COMMENT '节能奖',
`GGZ226` string  COMMENT '一次性奖',
`GGZ227` string  COMMENT '年功奖金',
`GGZ228` string  COMMENT '职称奖金',
`GGZ229` string  COMMENT '先进奖励',
`GGZ230` string  COMMENT '工资应发合计',
`GGZ231` string  COMMENT '养老保险',
`GGZ232` string  COMMENT '医疗保险',
`GGZ233` string  COMMENT '医疗保险补缴',
`GGZ234` string  COMMENT '失业保险',
`GGZ235` string  COMMENT '企业年金',
`GGZ236` string  COMMENT '住房公积金',
`GGZ237` string  COMMENT '房租费',
`GGZ238` string  COMMENT '电费',
`GGZ239` string  COMMENT '电话费',
`GGZ240` string  COMMENT '工会会费',
`GGZ241` string  COMMENT '扣款合计',
`GGZ242` string  COMMENT '税金合计',
`GGZ243` string  COMMENT '实发合计',
`GGZ244` string  COMMENT '工资时间',
`GGZ246` string  COMMENT '手机号',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`GGZ201`)
) stored as kudu;

CREATE TABLE `gz03` ( 
`GGZ301` bigint  COMMENT 'ID（自增id）',
`GGZ302` string  COMMENT '工资时间',
`CCO106` bigint  COMMENT '操作员id(sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.user_name)',
`CCO101` timestamp ,
PRIMARY KEY (`GGZ301`)
) stored as kudu;

CREATE TABLE `ha01` ( 
`HHA101` bigint  COMMENT '活动id',
`HHA102` string  COMMENT '类型0健康活动1健康资讯',
`HHA103` string  COMMENT '活动主题',
`CCO101` timestamp  COMMENT '创建时间',
`HHA104` string  COMMENT '活动状态0未提交1已提交2医生撤销3管理员撤销4结束',
`HHA105` string  COMMENT '审核状态0未审核1通过2未通过',
`HHA106` string  COMMENT '限制人数',
`HHA107` timestamp  COMMENT '活动举办时间',
`HHA108` string  COMMENT '活动举办地点',
`CCO102` bigint  COMMENT '医师id',
`CCO103` string  COMMENT '医师姓名',
`HHA109` timestamp  COMMENT '报名截止日期',
`HHA110` string  COMMENT '活动内容简介',
`HHA111` string  COMMENT '审核不通过原因',
`isvalid` string  COMMENT '是否有效：0否1是',
PRIMARY KEY (`HHA101`)
) COMMENT '健康活动表' stored as kudu;

CREATE TABLE `ha02` ( 
`HHA201` bigint  COMMENT '文件id',
`HHA101` bigint  COMMENT '活动id',
`HHA202` string  COMMENT '文件名称',
`HHA203` string  COMMENT '文件类型(0图片; 1文件; 2视频;)',
`HHA204` string  COMMENT '文件扩展名',
`HHA205` string  COMMENT '文件上传服务器的存储路径',
`HHA206` string  COMMENT '文件内容简介(作废)',
`HHA207` string  COMMENT '文件权限（0不可下载，1可下载）',
`HHA208` timestamp  COMMENT '上传时间',
`HHA209` string  COMMENT '审核状态0未通过1已通过',
`HHA210` string  COMMENT '审核描述（可记录未通过原因）',
`HHA211` bigint  COMMENT '审核人ID',
`HHA212` string  COMMENT '审核人姓名',
`HHA213` string  COMMENT '下载次数',
PRIMARY KEY (`HHA201`)
) COMMENT '健康活动资料表' stored as kudu;

CREATE TABLE `ha03` ( 
`HHA301` bigint  COMMENT '预约id',
`HHA101` bigint  COMMENT '活动id',
`CCO104` string  COMMENT 'user_id',
`CCO105` string  COMMENT '患者姓名',
`HHA302` string  COMMENT '预约状态，0：未预约 1：已预约 2：取消预约',
`HHA303` string  COMMENT '取消预约原因',
`HHA304` timestamp  COMMENT '预约时间',
`HHA305` string  COMMENT '签到状态，0：未签到 1：已签到',
`HHA306` timestamp  COMMENT '签到时间',
PRIMARY KEY (`HHA301`)
) COMMENT '健康活动预约表' stored as kudu;

CREATE TABLE `ha04` ( 
`HHA401` bigint  COMMENT '评价id',
`HHA101` bigint  COMMENT '活动id',
`CCO104` string  COMMENT 'user_id',
`CCO105` string  COMMENT '患者姓名',
`HHA402` string  COMMENT '评价级别',
`HHA403` string  COMMENT '评价内容',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HHA401`)
) COMMENT '健康活动评价表' stored as kudu;

CREATE TABLE `ha05` ( 
`HHA501` bigint  COMMENT '健康资讯id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`HHA502` string  COMMENT '类别（0文字图片类1视频类）',
`HHA503` string  COMMENT '专题',
`HHA504` string  COMMENT '专题描述（此字段废弃）',
`HHA104` string  COMMENT '活动状态0未提交1已提交2已作废3管理员下架4结束',
`HHA105` string  COMMENT '审核状态0未审核1通过2未通过3',
`HHA210` string  COMMENT '审核描述（可记录未通过原因）',
`HHA211` string  COMMENT '审核人ID（sys_user.user_id）',
`HHA212` string  COMMENT '审核人姓名（sys_user.realname）',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
`HHA505` string  COMMENT '专题配图名称',
`HHA506` string  COMMENT '专题配图扩展名',
`HHA507` string  COMMENT '专题配图上传服务器的存储路径',
`isvalid` string  COMMENT '是否有效：0否1是',
`isout` string  COMMENT '0或者null是内部链接，1是外部链接',
`outurl` string  COMMENT '外部链接url',
`HHA508` string  COMMENT '健康资讯可看人员类型：1患者2医生',
PRIMARY KEY (`HHA501`)
) COMMENT '健康资讯表' stored as kudu;

CREATE TABLE `ha06` ( 
`HHA601` bigint  COMMENT '健康资讯详情id',
`HHA501` bigint  COMMENT '健康资讯id',
`HHA602` string  COMMENT '类型（1详情描述及配图）',
`HHA603` string  COMMENT '资讯描述',
`HHA604` string  COMMENT '资讯描述配图名称',
`HHA605` string  COMMENT '配图文件扩展名',
`HHA606` string  COMMENT '配图上传服务器的存储路径',
`HHA607` string  COMMENT '配图说明（图下说明）',
`HHA105` string  COMMENT '审核状态0未通过1已通过',
`HHA210` string  COMMENT '审核描述（可记录未通过原因）',
`HHA211` string  COMMENT '审核人ID（sys_user.user_id）',
`HHA212` string  COMMENT '审核人姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HHA601`)
) COMMENT '健康资讯详情表' stored as kudu;

CREATE TABLE `ha07` ( 
`HHA501` bigint  COMMENT '健康资讯id',
`CCO106` bigint  COMMENT '关注者id(patients_login.user_id)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HHA501`,`CCO106`)
) COMMENT '健康资讯关注表' stored as kudu;

CREATE TABLE `ha08` ( 
`HHA801` bigint  COMMENT '系统公告id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`HHA802` string  COMMENT '类别（0文字图片类1视频类）',
`HHA803` string  COMMENT '公告标题',
`HHA104` string  COMMENT '公告状态0未提交1已提交2已作废3管理员下架',
`HHA105` string  COMMENT '审核状态0未审核1通过2未通过',
`HHA210` string  COMMENT '审核描述（可记录未通过原因）',
`HHA211` string  COMMENT '审核人ID（sys_user.user_id）',
`HHA212` string  COMMENT '审核人姓名（sys_user.realname）',
`HHA213` timestamp  COMMENT '审核时间(通过时为发布公告时间) ',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
`HHA805` string  COMMENT '公告配图名称',
`HHA806` string  COMMENT '公告配图扩展名',
`HHA807` string  COMMENT '公告配图上传服务器的存储路径',
`HHA808` string  COMMENT '用途类型：0平台，1体检',
`isvalid` string  COMMENT '是否有效：0否1是',
PRIMARY KEY (`HHA801`)
) COMMENT '系统公告表' stored as kudu;

CREATE TABLE `ha09` ( 
`HHA901` bigint  COMMENT '系统公告详情id',
`HHA801` bigint  COMMENT '系统公告id',
`HHA902` string  COMMENT '类型（1详情描述及配图）',
`HHA903` string  COMMENT '公告描述',
`HHA904` string  COMMENT '公告描述配图名称',
`HHA905` string  COMMENT '配图文件扩展名',
`HHA906` string  COMMENT '配图上传服务器的存储路径',
`HHA907` string  COMMENT '配图说明（图下说明）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HHA901`)
) COMMENT '系统公告详情表' stored as kudu;

CREATE TABLE `ha10` ( 
`HA1001` bigint  COMMENT '系统公告id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`HA1002` string  COMMENT '类别（0文字图片类1视频类）',
`HA1003` string  COMMENT '公告标题',
`HHA104` string  COMMENT '公告状态0未提交1已提交2已作废3管理员下架',
`HHA105` string  COMMENT '审核状态0未审核1通过2未通过',
`HHA210` string  COMMENT '审核描述（可记录未通过原因）',
`HHA211` string  COMMENT '审核人ID（sys_user.user_id）',
`HHA212` string  COMMENT '审核人姓名（sys_user.realname）',
`HHA213` timestamp  COMMENT '审核时间(通过时为发布公告时间) ',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
`HA1005` string  COMMENT '公告配图名称',
`HA1006` string  COMMENT '公告配图扩展名',
`HA1007` string  COMMENT '公告配图上传服务器的存储路径',
`HA1008` string  COMMENT '签署部门',
`HA1009` string  COMMENT '签署人',
`isvalid` string  COMMENT '是否有效：0否1是',
PRIMARY KEY (`HA1001`)
) COMMENT '医生系统公告表' stored as kudu;

CREATE TABLE `ha11` ( 
`HA1101` bigint  COMMENT '系统公告详情id',
`HA1001` bigint  COMMENT '系统公告id',
`HA1102` string  COMMENT '类型（1详情描述及配图）',
`HA1103` string  COMMENT '公告描述',
`HA1104` string  COMMENT '公告描述配图名称',
`HA1105` string  COMMENT '配图文件扩展名',
`HA1106` string  COMMENT '配图上传服务器的存储路径',
`HA1107` string  COMMENT '配图说明（图下说明）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HA1101`)
) COMMENT '医生系统公告详情表' stored as kudu;

CREATE TABLE `ha12` ( 
`HA1201` bigint  COMMENT '资讯id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '发布人id(kb08.KKB801)',
`CCO103` string  COMMENT '发布人姓名(kb08.KKB803)',
`HA1202` string  COMMENT '类型（au_dict_prop.prop_key）',
`HA1203` string  COMMENT '类型名称（au_dict_prop.prop_value）',
`HA1204` string  COMMENT '专题',
`HA1205` string  COMMENT '专题配图上传服务器的存储路径',
`HA1206` string  COMMENT '0内部链接，1外部链接',
`HA1207` string  COMMENT '内容',
`HA1208` string  COMMENT '外部链接url',
`HA1209` string  COMMENT '活动状态：0未提交1已提交2已作废3管理员下架4结束',
`HA1210` string  COMMENT '审核状态：0未审核1审核通过2未通过审核',
`HA1211` string  COMMENT '审核人ID（sys_user.user_id）',
`HA1212` string  COMMENT '审核人姓名（sys_user.realname）',
`HA1213` string  COMMENT '审核未通过原因',
`HA1214` string  COMMENT '是否有效：0否1是',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`HA1201`)
) stored as kudu;

CREATE TABLE `he01` ( 
`HHE101` bigint  COMMENT '测评项目id',
`HHE102` string  COMMENT '测评项目名称',
`HHE103` string  COMMENT '分类id（1健康2职场3情感4社交5情绪管理6医学评测）',
`HHE108` string  COMMENT '分类名称',
`HHE104` string  COMMENT '文件名称',
`HHE105` string  COMMENT '文件扩展名',
`HHE106` string  COMMENT '文件上传服务器的存储路径',
`HHE107` string  COMMENT '测评项目介绍',
`CCO101` timestamp  COMMENT '创建时间',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`HHE109` string  COMMENT '0无效1有效',
`HHE110` bigint  COMMENT '排序号',
PRIMARY KEY (`HHE101`)
) COMMENT '测评项目表' stored as kudu;

CREATE TABLE `he02` ( 
`HHE201` bigint  COMMENT '自增id',
`HHE101` bigint  COMMENT '测评项目id',
`HHE102` string  COMMENT '测评项目名称',
`HHE202` bigint  COMMENT '题目id',
`HHE203` string  COMMENT '题目名称（问题）',
`HHE204` string  COMMENT '答案id',
`HHE205` string  COMMENT '答案名称',
`HHE206` double  COMMENT '答案分值',
`HHE207` string  COMMENT '答案说明',
`CCO101` timestamp  COMMENT '创建时间',
`CCO106` bigint  COMMENT '操作员id',
`CCO107` string  COMMENT '操作员姓名',
`HHE208` string  COMMENT '0题目无效1题目有效',
PRIMARY KEY (`HHE201`)
) COMMENT '测评项目题目表' stored as kudu;

CREATE TABLE `he03` ( 
`HHE301` bigint  COMMENT '自增id',
`HHE101` bigint  COMMENT '测评项目id',
`HHE102` string  COMMENT '测评项目名称',
`HHE302` bigint  COMMENT '测评结果id',
`HHE303` string  COMMENT '测评结果名称',
`HHE304` bigint  COMMENT '测评结果分值（起始值）',
`HHE305` bigint  COMMENT '测评结果分值（终止值）',
`HHE306` string  COMMENT '测评结果说明',
`HHE307` string  COMMENT '测评寄语',
`CCO101` timestamp  COMMENT '创建时间',
`CCO106` bigint  COMMENT '操作员id',
`CCO107` string  COMMENT '操作员姓名',
PRIMARY KEY (`HHE301`)
) COMMENT '测评项目结果表' stored as kudu;

CREATE TABLE `he04` ( 
`HHE401` bigint  COMMENT '自增id',
`HHE101` bigint  COMMENT '测评项目id',
`HHE102` string  COMMENT '测评项目名称',
`HHE103` string  COMMENT '分类（1健康2职场3情感4社交5情绪管理6医学评测）',
`HHE404` double  COMMENT '测评结果分值',
`HHE302` bigint  COMMENT '测评结果id',
`HHE306` string  COMMENT '测评结果说明',
`HHE307` string  COMMENT '测评寄语',
`CCO101` timestamp  COMMENT '创建时间',
`CCO106` bigint  COMMENT '操作员id',
`CCO107` string  COMMENT '操作员姓名',
PRIMARY KEY (`HHE401`)
) COMMENT '患者健康测评表' stored as kudu;

CREATE TABLE `he05` ( 
`HHE501` bigint  COMMENT '自增id',
`HHE401` bigint  COMMENT '患者健康测评自增id',
`HHE202` bigint  COMMENT '题目id',
`HHE203` string  COMMENT '题目名称（问题）',
`HHE204` string  COMMENT '答案id',
`HHE205` string  COMMENT '答案名称',
`HHE206` double  COMMENT '答案分值',
`HHE207` string  COMMENT '答案说明',
`CCO101` timestamp  COMMENT '创建时间',
`HHE201` bigint  COMMENT '题目自增id',
PRIMARY KEY (`HHE501`)
) COMMENT '患者答题结果表' stored as kudu;

CREATE TABLE `health_room` ( 
`roomid` bigint  COMMENT '健康小屋id',
`roomname` string  COMMENT '小屋名称',
`orgid` bigint  COMMENT '所属机构代码（kb01.kkb101）',
`mchorgid` bigint  COMMENT '所属商户机构代码(作废)',
`isvalid` string  COMMENT '是否有效0否1是',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
`introduction` string  COMMENT '健康小屋简介',
`address` string  COMMENT '健康小屋所在位置',
`remark` string  COMMENT '备注',
PRIMARY KEY (`roomid`)
) COMMENT '健康小屋表' stored as kudu;

CREATE TABLE `health_room_doctor` ( 
`id` bigint  COMMENT '自增ID',
`userid` bigint  COMMENT '用户ID',
`realname` string  COMMENT '用户名称，目前是医生',
`roomid` bigint  COMMENT '健康小屋ID=health_room.roomid',
`orgid` bigint  COMMENT '机构代码',
`KKB801` bigint  COMMENT '医生编号',
`create_time` timestamp  COMMENT '修改时间',
PRIMARY KEY (`id`)
) COMMENT '健康小屋成员表' stored as kudu;

CREATE TABLE `hj01` ( 
`HHJ101` bigint  COMMENT '记录id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`KKB602` string  COMMENT '科室代码（kb09.kkb702）',
`KKB603` string  COMMENT '科室名称',
`HHJ102` string  COMMENT '拉取号源方式：0job自动拉取 1手动拉取',
`HHJ103` string  COMMENT '号源日期',
`HHJ104` timestamp  COMMENT '末次拉取号源开始时间',
`HHJ105` timestamp  COMMENT '末次拉取号源结束时间',
`HHJ106` string  COMMENT '末次拉取号源状态： 0进行中1成功2失败',
`HHJ107` string  COMMENT '末次失败原因',
`HHJ108` string  COMMENT '拉取成功次数',
`HHJ109` string  COMMENT '拉取失败次数',
`CCO106` bigint  COMMENT '手动拉取号源操作员id(sys_user.user_id)',
`CCO107` string  COMMENT '手动拉取号源操作员姓名(sys_user.user_name)',
PRIMARY KEY (`HHJ101`)
) COMMENT '拉取医院号源记录表' stored as kudu;

CREATE TABLE `hj02` ( 
`HHJ201` bigint  COMMENT '记录id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`HHJ202` string  COMMENT '拉取方式：0 job自动拉取 1 手动拉取',
`HHJ204` timestamp  COMMENT '拉取开始时间',
`HHJ205` timestamp  COMMENT '拉取结束时间',
`HHJ206` string  COMMENT '拉取状态：1成功2失败',
`HHJ207` string  COMMENT '失败原因',
`HHJ210` string  COMMENT '拉取数据源：1项目目录2科室信息3医生信息',
`CCO106` bigint  COMMENT '手动拉取操作员id(sys_user.user_id)',
`CCO107` string  COMMENT '手动拉取操作员姓名(sys_user.user_name)',
PRIMARY KEY (`HHJ201`)
) stored as kudu;

CREATE TABLE `hot_dept` ( 
`hdp101` bigint ,
`hdp102` bigint  COMMENT '热门科室id',
`hdp103` string  COMMENT '热门科室名称',
`hdp104` string  COMMENT '热门科室图片',
`hdp105` string  COMMENT '热门科室状态0-使用，1-禁用',
`hdp106` string  COMMENT '热门科室排序',
`CCO106` bigint  COMMENT '创建操作员ID',
`CCO107` string ,
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`hdp101`)
) stored as kudu;

CREATE TABLE `im01` ( 
`IIM101` string  COMMENT '登录融云的用户ID=MD5(KKB101+CCO102+CCO109+hlwyl00)',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO110` bigint  COMMENT 'HIS科室id/小屋id(kb07.KKB702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`IIM102` string  COMMENT '末次用户登录融云返回的token',
`IIM103` timestamp  COMMENT '末次登录日期',
`IIM104` string  COMMENT '末次登录的设备（浏览器指纹）',
`CCO106` bigint  COMMENT '操作员id(sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
PRIMARY KEY (`IIM101`)
) COMMENT '医生注册表(融云即时通讯用户)' stored as kudu;

CREATE TABLE `im02` ( 
`IIM201` string  COMMENT '患者登录融云的ID=MD5(CCO108+CCO105+hlwyl01)',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`IIM202` string  COMMENT '末次患者登录融云返回的token',
`IIM203` timestamp  COMMENT '末次患者登录日期',
`IIM204` string  COMMENT '末次患者登录的设备（浏览器指纹）',
`CCO106` bigint  COMMENT '操作员id(patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名(patients_login.patientname)',
PRIMARY KEY (`IIM201`)
) COMMENT '终端注册表(融云即时通讯用户)' stored as kudu;

CREATE TABLE `ir01` ( 
`IIR101` bigint  COMMENT '递增id',
`IIR102` string  COMMENT '检查报告单id',
`IIR103` string  COMMENT '检查报告单类型(DR:DR,CT:CT,MRI:MRI)',
`IIR104` string  COMMENT '门诊号/住院号',
`IIR105` string  COMMENT '门诊住院类型(01:门诊，02:住院)',
`IIR106` string  COMMENT '临床诊断',
`IIR107` string  COMMENT '临床病史',
`IIR108` string  COMMENT '患者姓名',
`IIR109` string  COMMENT '性别（1:男,2:女,9:其他）',
`IIR110` string  COMMENT '出生日期',
`IIR111` string  COMMENT '身份证号',
`IIR112` string  COMMENT '手机号',
`IIR113` string  COMMENT '社会保障卡',
`IIR114` string  COMMENT '居民健康卡',
`IIR115` string  COMMENT '家庭地址',
`IIR116` string  COMMENT '申请单号',
`IIR117` timestamp  COMMENT '申请时间',
`IIR118` string  COMMENT '申请科室',
`IIR119` string  COMMENT '申请医生',
`IIR120` double  COMMENT '费用',
`IIR121` string  COMMENT '执行科室',
`IIR122` string  COMMENT '执行医生',
`IIR123` timestamp  COMMENT '检查时间',
`IIR124` string  COMMENT '检查项目',
`IIR125` string  COMMENT '检查部位',
`IIR126` string  COMMENT '检查方法名称（如：平扫、增强）',
`IIR127` string  COMMENT '设备类型(DR:DR,CT:CT,MRI:MRI)',
`IIR128` string  COMMENT '报告医生',
`IIR129` string  COMMENT '影像表现',
`IIR130` string  COMMENT '检查结论',
`IIR131` string  COMMENT '诊断医生建议',
`orgcode` string  COMMENT '检查机构注册id（kb01.orgcode）',
`KKB101` bigint  COMMENT '检查机构id（kb01.kkb101）',
`KKB104` string  COMMENT '检查机构名称（kb01.kkb104）',
`CCO106` string  COMMENT '创建操作员ID（his系统操作员代码)',
`CCO107` string  COMMENT '创建操作员姓名(his系统操作员名称)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`IIR101`)
) COMMENT '检查报告表' stored as kudu;

CREATE TABLE `ir02` ( 
`IIR201` bigint  COMMENT '递增id',
`KKB101` bigint  COMMENT '检查机构id（kb01.kkb101）',
`IIR102` string  COMMENT '检查报告单id（ir01.iir102）',
`IIR202` string  COMMENT '系列序号',
`IIR203` string  COMMENT '系列内顺序号',
`IIR204` string  COMMENT '影像文件id',
`IIR205` string  COMMENT '影像文件名称',
`IIR206` string  COMMENT '影像文件后缀',
`IIR207` string  COMMENT '影像文件上传服务器的存储路径',
`CCO106` string  COMMENT '创建操作员ID（his系统操作员代码)',
`CCO107` string  COMMENT '创建操作员姓名(his系统操作员名称)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`IIR201`)
) COMMENT '影像文件表' stored as kudu;

CREATE TABLE `jk03` ( 
`JJK301` bigint  COMMENT '记录id',
`CCO108` bigint  COMMENT '患者id',
`CCO105` string  COMMENT '患者姓名',
`JJK302` string  COMMENT '餐别代码：1、早餐，2、午餐，3、晚餐，4、夜宵，5、其他',
`JJK303` string  COMMENT '饮食记录文字信息',
`CCO101` timestamp  COMMENT '上传时间',
PRIMARY KEY (`JJK301`)
) COMMENT '饮食信息表' stored as kudu;

CREATE TABLE `jk04` ( 
`JJK401` bigint  COMMENT '自增id',
`CCO108` bigint  COMMENT '患者ID(patients.patiendid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`JJK402` string  COMMENT '时间段选择：1早间用药、2中午用药、3晚间用药、4其他时段、5当日用药',
`JJK403` string  COMMENT '用药记录（json格式：{“info”:[{“name”: "双黄莲口服液", “num”: 500,”unit“:0}，{“name”: "双黄莲口服液", “num”: 500,”unit“:0}]}）',
`CCO101` timestamp  COMMENT '数据采集时间',
PRIMARY KEY (`JJK401`)
) COMMENT '用药信息表' stored as kudu;

CREATE TABLE `jk05` ( 
`JJK501` bigint  COMMENT '签约id',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`KKB101` bigint  COMMENT '签约机构代码',
`KKB104` string  COMMENT '签约机构名称',
`CCO102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.kkb701/health_room.roomid)',
`CCO110` string  COMMENT 'his科室id/小屋id(kb07.kkb702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.kkb703/health_room.roomname)',
`JJK502` string  COMMENT '病情文字描述',
`JJK503` string  COMMENT '签约状态:0待审核、1已签约、2拒绝签约、3解约',
`JJK504` timestamp  COMMENT '审核时间',
`JJK505` timestamp  COMMENT '解约时间',
`JJK506` string  COMMENT '解约原因',
`JJK507` string  COMMENT '拒绝签约原因',
`CCO101` timestamp  COMMENT '创建时间（申请时间）',
`CCO106` bigint  COMMENT '操作员id(sys_user.user_id/patients_login.user_id)',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname/patients_login.patientname）',
PRIMARY KEY (`JJK501`)
) COMMENT '健康管理签约表' stored as kudu;

CREATE TABLE `jk06` ( 
`JJK601` bigint  COMMENT '文件id',
`JJK501` bigint  COMMENT '签约id',
`JJK602` string  COMMENT '文件名称',
`JJK603` string  COMMENT '文件类型(0文本; 1图片; )',
`JJK604` string  COMMENT '资料类型(0处方; 1检查报告; 2其它材料) 默认为2',
`JJK605` string  COMMENT '文件扩展名',
`JJK606` string  COMMENT '文件上传服务器的存储路径',
`JJK607` timestamp  COMMENT '上传时间',
PRIMARY KEY (`JJK601`)
) COMMENT '健康管理签约附件表' stored as kudu;

CREATE TABLE `jk07` ( 
`JJK701` bigint  COMMENT '资讯id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`JJK702` string  COMMENT '标题',
`JJK901` bigint  COMMENT '标题分类',
`JJK703` string  COMMENT '资讯状态：0、未发布，1、已发布',
`JJK704` string  COMMENT '封面配图名称',
`JJK705` string  COMMENT '封面配图扩展名',
`JJK706` string  COMMENT '封面配图上传服务器的存储路径',
`JJK707` string  COMMENT '浏览数量',
`CCO106` bigint  COMMENT '操作员ID(sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '上传时间',
`JJK708` string  COMMENT '推送人群',
PRIMARY KEY (`JJK701`)
) COMMENT '康养知识主题表' stored as kudu;

CREATE TABLE `jk08` ( 
`JJK801` bigint  COMMENT '健康资讯详情id',
`JJK701` bigint  COMMENT '资讯id',
`JJK802` string  COMMENT '类型（1文字及图片2文字及视频）',
`JJK803` string  COMMENT '资讯描述',
`JJK804` string  COMMENT '资讯描述配图或视频名称',
`JJK805` string  COMMENT '配图或视频文件扩展名',
`JJK806` string  COMMENT '配图或视频上传服务器的存储路径',
`JJK807` string  COMMENT '配图或视频说明（图下说明）',
`JJK808` string  COMMENT '段落序号',
PRIMARY KEY (`JJK801`)
) COMMENT '康养知识详情表' stored as kudu;

CREATE TABLE `jk09` ( 
`JJK901` bigint  COMMENT '分类id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`JJK902` string  COMMENT '分类名称',
`JJK903` bigint  COMMENT '排序值',
`CCO106` bigint  COMMENT '操作员ID(sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJK901`)
) COMMENT '康养知识主题分类表' stored as kudu;

CREATE TABLE `jk10` ( 
`JJK101` bigint  COMMENT '主键ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`KKB701` string  COMMENT '医院具体科室编号（平台）',
`KKB703` string  COMMENT '医疗机构具体科室名称(deptname)',
`JJK102` string  COMMENT '病史',
`JJK103` string  COMMENT '诊断',
`JJK104` string  COMMENT '医嘱-概述',
`JJK105` string  COMMENT '医嘱-用药建议',
`JJK106` string  COMMENT '医嘱-饮食指导',
`JJK107` string  COMMENT '医嘱-运动指导',
`JJK108` string  COMMENT '医嘱-测量指导',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJK101`)
) COMMENT '监测指导信息表' stored as kudu;

CREATE TABLE `jk11` ( 
`JJK111` bigint  COMMENT '主键ID',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`JJK112` string  COMMENT '检测类型',
`JJK113` timestamp  COMMENT '起始时间',
`JJK114` timestamp  COMMENT '终止时间',
`JJK115` bigint  COMMENT '提醒次数',
PRIMARY KEY (`JJK111`)
) COMMENT '健康管理时间提醒设置' stored as kudu;

CREATE TABLE `jk13` ( 
`JJK131` bigint  COMMENT '附件id',
`JJK301` bigint  COMMENT '饮食信息表id',
`JJK132` string  COMMENT '上传图片地址',
PRIMARY KEY (`JJK131`)
) COMMENT '饮食信息附件表' stored as kudu;

CREATE TABLE `jk14` ( 
`JJK141` bigint  COMMENT '附件id',
`JJK401` bigint  COMMENT '用药信息表id',
`JJK142` string  COMMENT '上传图片地址',
PRIMARY KEY (`JJK141`)
) COMMENT '用药信息附件表' stored as kudu;

CREATE TABLE `jk15` ( 
`JJK151` bigint  COMMENT '主键ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.kkb701/health_room.roomid)',
`CCO110` string  COMMENT 'his科室id/小屋id(kb07.kkb702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.kkb703/health_room.roomname)',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`CCO112` string  COMMENT '卡类型',
`CCO113` string  COMMENT '卡号',
`JJK152` string  COMMENT '续方描述',
`JJK153` string  COMMENT '患者上传的原始处方图片地址',
`JJK154` bigint  COMMENT '上传的处方记录ID',
`JJK155` string  COMMENT '上传的处方记录来源类别（1在线问诊dr01; 2慢病管理jk16）',
`JJK156` string  COMMENT '续方状态(0申请续方;1医生完成开方;2 医生取消开方； 3医生拒绝续方；4患者取消续方；5慢病解约后失效状态； )',
`JJK157` string  COMMENT '医生取消/拒绝原因',
`JJK158` timestamp  COMMENT '医生操作时间',
`JJK161` bigint  COMMENT '本次续方时医生开具的处方',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
`JJK159` string  COMMENT '用于记录医生开方类别，JJK161字段状态（1在线问诊dr01, 2慢病管理jk16）',
PRIMARY KEY (`JJK151`)
) COMMENT '续方记录表' stored as kudu;

CREATE TABLE `jk16` ( 
`JJK161` bigint  COMMENT '处方ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO110` string  COMMENT 'HIS科室id/小屋id(kb07.KKB702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`CCO112` string  COMMENT '卡类型',
`CCO113` string  COMMENT '卡号',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname)',
`JJK162` string  COMMENT '性别',
`JJK163` string  COMMENT '年龄',
`JJK164` string  COMMENT '处方来源1在线开方2上传处方',
`JJK165` timestamp  COMMENT '开方时间',
`JJK166` bigint  COMMENT '主诊断代码',
`JJK167` string  COMMENT '主诊断名称',
`JJK168` string  COMMENT '诊断描述',
`JJK169` string  COMMENT '结算状态0未结算1已结算2已退结算',
`JJK170` timestamp  COMMENT '已结算时间',
`JJK171` timestamp  COMMENT '已退结算时间',
`JJK172` string  COMMENT '医疗类别名称',
`JJK173` string  COMMENT '医疗类别',
`JJK174` string  COMMENT '医师审方状态（0未审1通过、2不通过）',
`JJK175` string  COMMENT '处方审计状态（0未审1通过、2不通过）',
`JJK176` string  COMMENT '药师审方状态（0未审1通过、2不通过）',
`JJK177` bigint  COMMENT '处方核对药剂师id',
`JJK178` string  COMMENT '处方核对药剂师姓名',
`JJK179` bigint  COMMENT '处方调配药剂师id',
`JJK180` string  COMMENT '处方调配药剂师姓名',
`JJK181` string  COMMENT '签章药师id',
`JJK182` string  COMMENT '签章药师姓名',
`JJK183` string  COMMENT '签章医师id',
`JJK184` string  COMMENT '签章医师姓名',
`JJK185` string  COMMENT '处方锁定（0正常1锁定）',
`JJK186` timestamp  COMMENT '处方锁定时间',
`JJK187` string  COMMENT '处方类别0西药1中成药2中药饮片',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJK161`)
) COMMENT '续方管理处方信息' stored as kudu;

CREATE TABLE `jk19` ( 
`JJK191` bigint  COMMENT '处方明细ID',
`JJK161` bigint  COMMENT '处方ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCM101` bigint  COMMENT '药品id（开方药品目录）',
`CCM102` string  COMMENT '药品通用名',
`CCM104` string  COMMENT '药品商品名',
`CCM106` string  COMMENT '规格',
`CCM107` string  COMMENT '剂型',
`CCM108` string  COMMENT '毒理名称',
`CCM109` string  COMMENT '包装单位',
`CCM110` string  COMMENT '剂量',
`CCM111` string  COMMENT '剂量单位',
`JJK192` string  COMMENT '次剂量',
`CCM301` bigint  COMMENT '用法代码',
`CCM302` string  COMMENT '用法名称',
`CCM401` bigint  COMMENT '使用频率代码',
`CCM402` string  COMMENT '使用频率名称',
`JJK193` string  COMMENT '用药天数',
`JJK194` string  COMMENT '数量',
`JJK195` string  COMMENT '单付数量',
`JJK196` string  COMMENT '付数',
`JJK197` string  COMMENT '备注',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJK191`)
) COMMENT '续方管理处方药品信息' stored as kudu;

CREATE TABLE `jk21` ( 
`JJK211` bigint  COMMENT '审核id',
`JJK161` bigint  COMMENT '处方ID',
`JJK212` string  COMMENT '审核状态（0未审、1通过、2不通过）',
`JJK213` string  COMMENT '审核意见',
`JJK214` string  COMMENT '审核类型（1医师审方、2处方审计、3药师审方）',
`JJK215` bigint  COMMENT '审核人id',
`JJK216` string  COMMENT '审核姓名',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.realname)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJK211`)
) COMMENT '处方审核表' stored as kudu;

CREATE TABLE `jk22` ( 
`JJK221` bigint  COMMENT '自增ID',
`CCO108` bigint  COMMENT '患者ID(patients.patientid)',
`CCO105` string  COMMENT '患者姓名(patients.patientname',
`KKB101` bigint  COMMENT '签约机构代码',
`KKB104` string  COMMENT '签约机构名称',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.kkb701/health_room.roomid)',
`CCO110` string  COMMENT 'his科室id/小屋id(kb07.kkb702/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.kkb703/health_room.roomname)',
`CCO102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`JJK222` string  COMMENT '所属慢病代码',
PRIMARY KEY (`JJK221`)
) COMMENT '患者慢病信息表' stored as kudu;

CREATE TABLE `jk23` ( 
`JJK231` bigint  COMMENT '自增ID',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`JJK232` string  COMMENT '签约标志(0不允许签约；1允许签约)',
`JJK233` string  COMMENT '在线问诊标志(0不允许在线问诊；1允许在线问诊)',
PRIMARY KEY (`JJK231`)
) COMMENT '可签约医生关系表' stored as kudu;

CREATE TABLE `jr01` ( 
`JJR101` string  COMMENT '分类id',
`JJR102` string  COMMENT '父级分类id',
`JJR103` string  COMMENT '父级分类名称',
`JJR104` string  COMMENT '分类名称',
`CCO106` bigint  COMMENT '创建操作员ID',
`CCO107` string  COMMENT '创建操作员姓名',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJR101`)
) COMMENT '健康宣传分类表' stored as kudu;

CREATE TABLE `jr02` ( 
`JJR201` bigint  COMMENT '宣传资讯id',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB104` string  COMMENT '医疗机构名称',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801 作废)',
`CCO103` string  COMMENT '发布人姓名',
`JJR101` string  COMMENT '分类id',
`JJR104` string  COMMENT '分类名称',
`JJR202` string  COMMENT '类别（0文字图片类1视频类）',
`JJR203` string  COMMENT '专题',
`JJR204` string  COMMENT '专题描述（此字段废弃）',
`JJR205` string  COMMENT '专题配图名称',
`JJR206` string  COMMENT '专题配图扩展名',
`JJR207` string  COMMENT '专题配图上传服务器的存储路径',
`JJR208` string  COMMENT '状态0未提交1已提交2已撤销3管理员下架4结束',
`JJR209` string  COMMENT '审核状态0未审核1通过2未通过3',
`JJR210` string  COMMENT '审核描述（可记录未通过原因）',
`JJR211` string  COMMENT '审核人ID（sys_user.user_id）',
`JJR212` string  COMMENT '审核人姓名（sys_user.realname）',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
`isvalid` string  COMMENT '是否有效：0否1是',
PRIMARY KEY (`JJR201`)
) COMMENT '健康中国行宣传资讯表' stored as kudu;

CREATE TABLE `jr03` ( 
`JJR301` bigint  COMMENT '健康中国行宣传资讯详情id',
`JJR201` bigint  COMMENT '宣传资讯id',
`JJR302` string  COMMENT '类型（1详情描述及配图）',
`JJR303` string  COMMENT '资讯描述',
`JJR304` string  COMMENT '资讯描述配图名称',
`JJR305` string  COMMENT '配图文件扩展名',
`JJR306` string  COMMENT '配图上传服务器的存储路径',
`JJR307` string  COMMENT '配图说明（图下说明）',
`JJR209` string  COMMENT '审核状态0未通过1已通过',
`JJR210` string  COMMENT '审核描述（可记录未通过原因）',
`JJR211` string  COMMENT '审核人ID（sys_user.user_id）',
`JJR212` string  COMMENT '审核人姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJR301`)
) COMMENT '健康中国行宣传资讯详情表' stored as kudu;

CREATE TABLE `jr04` ( 
`JJR201` bigint  COMMENT '宣传资讯id',
`CCO106` bigint  COMMENT '关注者id(patients_login.user_id)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJR201`,`CCO106`)
) COMMENT '健康中国行宣传资讯关注表' stored as kudu;

CREATE TABLE `jtys_contract` ( 
`contractid` bigint  COMMENT '签约ID',
`patientid` bigint  COMMENT '患者ID',
`cco105` string  COMMENT '患者姓名（patients.patientname）',
`orgid` bigint  COMMENT '签约机构代码',
`teamid` bigint  COMMENT '签约团队代码',
`teamname` string  COMMENT '签约团队名称',
`checkstate` string  COMMENT '签约状态:0待审核、1审核通过、2审核不通过、3解约',
`create_time` timestamp  COMMENT '创建时间',
`cco102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`cco103` string  COMMENT '医生姓名(kb08.KKB803)',
`remark` string  COMMENT '签约备注',
`checkremark` string  COMMENT '审核备注',
`paytimes` string  COMMENT '总计费次数',
`payid` bigint  COMMENT '末次结算ID',
`paytime` timestamp ,
`payamount` double  COMMENT '末次支付金额',
`begindate` timestamp ,
`yeartimes` string  COMMENT '签约n年',
`enddate` timestamp ,
`drawtime` timestamp  COMMENT '解约时间',
`drawcode` bigint  COMMENT '解约代码',
`drawreason` string  COMMENT '解约原因',
`otherdrawreason` string  COMMENT '其他解约原因',
`signtype` string  COMMENT '签约方式：0医生端签约，1患者端签约',
`cco106` bigint  COMMENT '操作员id（sys_user.user_id/patients_login.user_id）',
`cco107` string  COMMENT '操作员姓名（sys_user.realname/patients_login.patientname）',
`orgname` string  COMMENT '签约机构名称',
PRIMARY KEY (`contractid`)
) COMMENT '签约' stored as kudu;

CREATE TABLE `jtys_contract_exec` ( 
`execid` bigint  COMMENT '执行ID',
`payid` bigint  COMMENT '结算ID',
`detailid` bigint  COMMENT '结算明细ID',
`contractid` bigint  COMMENT '签约者ID',
`patientid` bigint  COMMENT '患者ID',
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`itemid` bigint  COMMENT '服务项目ID',
`itemname` string  COMMENT '服务项目名称',
`price` double  COMMENT '单价',
`itemtype` string  COMMENT '项目分类id',
`itemtypename` string  COMMENT '项目分类名称',
`servicecontent` string  COMMENT '服务内容',
`yeartimes` string  COMMENT '年服务次数:0不限',
`yeartimesinfo` string  COMMENT '年服务次数说明',
`servicecontentmemo` string  COMMENT '服务内容解释',
`ispay` string  COMMENT '是否免付0否1是',
`payinfo` string  COMMENT '免付说明',
`areaid` bigint  COMMENT '区划代码',
`orgid` bigint  COMMENT '签约机构代码',
`teamid` bigint  COMMENT '签约团队代码',
`teamname` string ,
`billtype` bigint  COMMENT '票据类型1正票-1退票',
`user_id` bigint  COMMENT '执行操作员ID',
`username` string  COMMENT '执行操作员工号',
`realname` string  COMMENT '执行操作员姓名',
`extime` timestamp  COMMENT '执行时间',
`serviceTypeCode` bigint  COMMENT '服务方式代码',
`serviceTypeName` string  COMMENT '服务方式名称',
`otherServiceName` string  COMMENT '其他服务方式',
`serviceRemark` string  COMMENT '服务情况说明',
PRIMARY KEY (`execid`)
) COMMENT '签约执行单' stored as kudu;

CREATE TABLE `jtys_contractitem` ( 
`contractid` bigint  COMMENT '签约者ID',
`packageid` bigint  COMMENT '服务包ID',
`itemid` bigint  COMMENT '服务项目ID',
`packagename` string  COMMENT '服务包名称',
`itemname` string  COMMENT '服务项目名称',
`price` double  COMMENT '单价',
`itemtype` string  COMMENT '项目分类id',
`itemtypename` string  COMMENT '项目分类名称',
`servicecontent` string  COMMENT '服务内容',
`yeartimes` string  COMMENT '年服务次数:0不限',
`yeartimesinfo` string  COMMENT '年服务次数说明',
`servicecontentmemo` string  COMMENT '服务内容解释',
`ispay` string  COMMENT '是否免付0否1是',
`payinfo` string  COMMENT '免付说明',
`areaid` bigint  COMMENT '区划代码',
`orgid` bigint  COMMENT '签约机构代码',
`teamid` bigint  COMMENT '签约团队代码',
`isselected` string  COMMENT '与签约者未选择的服务包一并返回,用于变更服务包,此标志告知前台0签约者未选择1签约者已选择',
PRIMARY KEY (`contractid`,`packageid`,`itemid`)
) COMMENT '签约者服务包及服务项目' stored as kudu;

CREATE TABLE `jtys_package_item` ( 
`itemid` bigint  COMMENT '项目id',
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`itemno` string  COMMENT '项目编码（官方的编码）',
`itemname` string  COMMENT '项目名称',
`itemtype` string  COMMENT '项目分类id',
`itemtypename` string  COMMENT '项目分类名称',
`servicecontent` string  COMMENT '服务内容',
`yeartimes` string  COMMENT '年服务次数:0不限',
`yeartimesinfo` string  COMMENT '年服务次数说明',
`servicecontentmemo` string  COMMENT '服务内容解释',
`price` double  COMMENT '价格',
`ispay` string  COMMENT '是否免付0否1是',
`payinfo` string  COMMENT '免付说明',
`orgid` string  COMMENT '所属机构id',
`areaid` string  COMMENT '所属行政区划id',
`isvalid` string  COMMENT '是否有效0否1是',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
PRIMARY KEY (`itemid`)
) COMMENT '家庭医生服务项目' stored as kudu;

CREATE TABLE `jtys_package_item_offical` ( 
`itemid` bigint  COMMENT '项目id',
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`itemno` string  COMMENT '项目编码（官方的编码）',
`itemname` string  COMMENT '项目名称',
`itemtype` string  COMMENT '项目分类id',
`itemtypename` string  COMMENT '项目分类名称',
`servicecontent` string  COMMENT '服务内容',
`yeartimes` string  COMMENT '年服务次数:0不限',
`yeartimesinfo` string  COMMENT '年服务次数说明',
`servicecontentmemo` string  COMMENT '服务内容解释',
`price` double  COMMENT '价格',
`ispay` string  COMMENT '是否免付0否1是',
`payinfo` string  COMMENT '免付说明',
`orgid` string  COMMENT '所属机构id',
`areaid` string  COMMENT '所属行政区划id',
`isvalid` string  COMMENT '是否有效0否1是',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
PRIMARY KEY (`itemid`)
) COMMENT '家庭医生服务项目(通用目录)' stored as kudu;

CREATE TABLE `jtys_pay` ( 
`payid` bigint  COMMENT '结算ID',
`contractid` bigint  COMMENT '签约ID',
`patientid` bigint  COMMENT '患者ID',
`areaid` string  COMMENT '区划代码',
`areaname` string  COMMENT '区划名称',
`orgid` bigint  COMMENT '签约机构代码',
`teamid` bigint  COMMENT '签约团队代码',
`teamname` string  COMMENT '签约团队名称',
`create_time` timestamp  COMMENT '结算时间',
`user_id` bigint  COMMENT '结算操作员ID',
`username` string  COMMENT '结算操作员工号',
`realname` string  COMMENT '结算操作员姓名',
`shouldpay` double  COMMENT '应付金额',
`amount` double  COMMENT '结算金额',
`remark` string  COMMENT '结算备注',
`isstriked` string  COMMENT '被冲标志0未被冲1已被冲',
`redbillflag` bigint  COMMENT '票据类型1正票-1退票',
`strikedpayid` bigint  COMMENT '被退的结算ID',
`isagainpay` string  COMMENT '是否续费0否1是',
PRIMARY KEY (`payid`)
) COMMENT '签约结算单' stored as kudu;

CREATE TABLE `jtys_pay_detail` ( 
`payid` bigint  COMMENT '结算ID',
`detailid` string  COMMENT '某次结算的序列号从1开始',
`patientid` bigint  COMMENT '患者ID',
`contractid` bigint  COMMENT '签约者ID',
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`itemid` bigint  COMMENT '服务项目ID',
`itemname` string  COMMENT '服务项目名称',
`price` double  COMMENT '单价',
`itemtype` string  COMMENT '项目分类id',
`itemtypename` string  COMMENT '项目分类名称',
`servicecontent` string  COMMENT '服务内容',
`yeartimes` string  COMMENT '年服务次数:0不限',
`yeartimesinfo` string  COMMENT '年服务次数说明',
`servicecontentmemo` string  COMMENT '服务内容解释',
`ispay` string  COMMENT '是否免付0否1是',
`payinfo` string  COMMENT '免付说明',
`areaid` bigint  COMMENT '区划代码',
`orgid` bigint  COMMENT '签约机构代码',
`teamid` bigint  COMMENT '签约团队代码',
`teamname` string  COMMENT '签约团队名称',
`billtype` bigint  COMMENT '票据类型1正票-1退票',
`extimes` string  COMMENT '已执行次数',
PRIMARY KEY (`payid`,`detailid`)
) COMMENT '签约结算明细' stored as kudu;

CREATE TABLE `jtys_pay_type` ( 
`payid` bigint  COMMENT '结算ID',
`detailid` string  COMMENT '某次结算的序列号从1开始',
`paytypeid` bigint  COMMENT '支付类型ID',
`paytypename` string  COMMENT '支付类型名称',
`amount` double  COMMENT '支付金额',
`user_id` bigint  COMMENT '收费员ID',
`username` string  COMMENT '收费员代码',
`realname` string  COMMENT '收费员姓名',
`orgid` bigint  COMMENT '机构ID',
PRIMARY KEY (`payid`,`detailid`)
) COMMENT '签约结算类型表' stored as kudu;

CREATE TABLE `jtys_servicepackage` ( 
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`orgid` bigint  COMMENT '机构ID',
`areaid` string  COMMENT '区域编码',
`isvalid` string  COMMENT '是否有效0否1是',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
PRIMARY KEY (`packageid`)
) COMMENT '家庭医生服务包' stored as kudu;

CREATE TABLE `jtys_servicepackage_official` ( 
`packageid` bigint  COMMENT '服务包ID',
`packagename` string  COMMENT '服务包名称',
`orgid` bigint  COMMENT '机构ID',
`areaid` string  COMMENT '区域编码',
`isvalid` string  COMMENT '是否有效0否1是',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
PRIMARY KEY (`packageid`)
) COMMENT '家庭医生服务包(通用目录)' stored as kudu;

CREATE TABLE `jtys_serviceteam` ( 
`teamid` bigint  COMMENT '服务团队id',
`teamname` string  COMMENT '服务团队名称',
`orgid` bigint  COMMENT '所属机构id',
`areaid` bigint  COMMENT '所属行政区划id',
`status` string  COMMENT '是否有效0否1是',
`remark` string  COMMENT '备注',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者姓名',
PRIMARY KEY (`teamid`)
) COMMENT '服务团队管理' stored as kudu;

CREATE TABLE `jtys_team_user` ( 
`id` bigint  COMMENT '自增ID',
`cco102` bigint  COMMENT '平台医生id(kb08.KKB801)',
`cco103` string  COMMENT '医生姓名(kb08.KKB803)',
`teamid` bigint  COMMENT '服务团队id',
`orgid` bigint  COMMENT '机构代码',
`cco106` bigint  COMMENT '操作员id（sys_user.user_id）',
`cco107` string  COMMENT '操作员姓名（sys_user.realname）',
`create_time` timestamp  COMMENT '修改时间',
PRIMARY KEY (`id`)
) COMMENT '团队医生表' stored as kudu;

CREATE TABLE `jy01` ( 
`JJY101` bigint  COMMENT '预约检查关联机构id',
`JJY102` bigint  COMMENT '申请机构平台id（kb01.kkb101）',
`JJY103` string  COMMENT '申请机构HIS代码',
`JJY104` string  COMMENT '申请机构名称',
`JJY105` bigint  COMMENT '检查机构平台id（kb01.kkb101）',
`JJY106` string  COMMENT '检查机构HIS代码',
`JJY107` string  COMMENT '检查机构名称',
`CCO106` bigint  COMMENT '操作员ID（sys_user.user_id)',
`CCO107` string  COMMENT '操作员姓名(sys_user.user_name)',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJY101`)
) COMMENT '预约检查机构关联表' stored as kudu;

CREATE TABLE `jy02` ( 
`JJY201` bigint  COMMENT '排班id',
`KKB101` bigint  COMMENT '医疗机构编码（kb01.kkb101）',
`KKB104` string  COMMENT '医疗机构名称',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`JJY202` string  COMMENT '状态（0未发布 1已发布）',
`JJY203` string  COMMENT '职称id',
`JJY204` string  COMMENT '职称名称',
`JJY205` string  COMMENT '专家级别id',
`JJY206` string  COMMENT '级别名称',
`JJY207` string  COMMENT '出诊日期',
`JJY208` string  COMMENT '星期数（1-7）',
`JJY209` string  COMMENT '午别（上午/下午/夜间）',
`JJY210` string  COMMENT '出诊级别id(01：普通门诊，02：专家门诊)',
`JJY211` string  COMMENT '出诊级别名称(普通号、专家号)',
`JJY212` string  COMMENT '号源数',
`JJY213` string  COMMENT '可预约号源数',
`JJY214` string  COMMENT '看诊开始时间',
`JJY215` string  COMMENT '看诊结束时间',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
`CCO101` timestamp  COMMENT '创建时间',
PRIMARY KEY (`JJY201`)
) COMMENT '检查机构排班表' stored as kudu;

CREATE TABLE `jy03` ( 
`JJY301` bigint  COMMENT '排班模板id',
`JJY302` string  COMMENT '模板名称',
`KKB101` bigint  COMMENT '医疗机构编码(kb01.kkb101)',
`KKB104` string  COMMENT '医疗机构名称',
`CCO109` bigint  COMMENT '平台科室id/小屋id(kb07.KKB701/health_room.roomid)',
`CCO111` string  COMMENT '科室名称/小屋名称(kb07.KKB703/health_room.roomname)',
`CCO102` bigint  COMMENT '医生id(kb08.KKB801)',
`CCO103` string  COMMENT '医生姓名(kb08.KKB803)',
`JJY303` string  COMMENT '状态（0无效 1有效）',
`JJY203` string  COMMENT '职称id',
`JJY204` string  COMMENT '职称名称',
`JJY205` string  COMMENT '专家级别id',
`JJY206` string  COMMENT '级别名称',
`JJY209` string  COMMENT '午别（上午/下午/夜间）',
`JJY210` string  COMMENT '出诊级别id(01：普通门诊，02：专家门诊)',
`JJY211` string  COMMENT '出诊级别名称(普通号、专家号)',
`JJY212` string  COMMENT '号源数',
`JJY214` string  COMMENT '看诊开始时间',
`JJY215` string  COMMENT '看诊结束时间',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO101` timestamp  COMMENT '创建时间',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname）',
PRIMARY KEY (`JJY301`)
) COMMENT '检查机构排班模板表' stored as kudu;

CREATE TABLE `jy04` ( 
`JJY401` bigint  COMMENT '预约检查单id',
`JJY402` string  COMMENT '患者在当前机构的治疗类型(0门诊)',
`JJY403` string  COMMENT '门诊流水号',
`CCO108` string  COMMENT '患者ID（手录或his传）',
`CCO105` string  COMMENT '患者姓名',
`JJY404` string  COMMENT '性别',
`JJY405` string  COMMENT '年龄',
`JJY406` string  COMMENT '民族',
`JJY407` string  COMMENT '婚姻状况',
`JJY408` string  COMMENT '手机号码',
`JJY409` string  COMMENT '身份证号',
`JJY410` string  COMMENT '初步诊断',
`JJY411` bigint  COMMENT '申请机构平台id（kb01.kkb101',
`JJY412` string  COMMENT '申请机构HIS代码',
`JJY413` string  COMMENT '申请机构名称',
`JJY414` bigint  COMMENT '申请科室id(kb07.kkb701)',
`JJY461` string  COMMENT '申请科室his代码',
`JJY415` string  COMMENT '申请科室名称',
`JJY416` bigint  COMMENT '申请医师id(kb08.KKB801)',
`JJY462` string  COMMENT '申请医生his代码',
`JJY417` string  COMMENT '申请医生姓名(kb08.KKB803)',
`JJY418` string  COMMENT '申请方医生联系方式',
`JJY419` string  COMMENT '检查单状态（0未提交 1已提交)',
`JJY420` bigint  COMMENT '检查机构平台id（kb01.kkb101',
`JJY421` string  COMMENT '检查机构HIS代码',
`JJY422` string  COMMENT '检查机构名称',
`JJY423` bigint  COMMENT '检查科室id(kb07.kkb701)',
`JJY463` string  COMMENT '检查科室his代码',
`JJY424` string  COMMENT '检查科室名称',
`JJY425` bigint  COMMENT '检查医生id(kb08.KKB801)',
`JJY464` string  COMMENT '检查医生his代码',
`JJY426` string  COMMENT '检查医生名称',
`JJY427` string  COMMENT '检查医生联系方式',
`JJY428` string  COMMENT '检查状态(0未检查 1已检查)',
`JJY453` timestamp  COMMENT '完成检查的时间',
`JJY446` bigint  COMMENT '检查操作员id(sys_user.user_id或HIS传)',
`JJY447` string  COMMENT '检查操作员名称(sys_user.user_name或HIS传)',
`JJY201` bigint  COMMENT '排班id',
`JJY203` string  COMMENT '职称id',
`JJY204` string  COMMENT '职称名称',
`JJY205` string  COMMENT '专家级别id',
`JJY206` string  COMMENT '级别名称',
`JJY207` string  COMMENT '出诊日期',
`JJY209` string  COMMENT '午别（S上午/X下午/Y夜间',
`JJY214` string  COMMENT '看诊开始时间',
`JJY215` string  COMMENT '看诊结束时间',
`JJY429` string  COMMENT '收费类型（0未收费 1app收费 2HIS收费 3web收费）',
`JJY448` bigint  COMMENT '收费操作员id（HIS方）或者缴费操作员id(app方，patients_login.user_id）',
`JJY449` string  COMMENT '收费操作员名称(HIS方)或者缴费操作员名称(app方，patients_login.username）',
`JJY430` string  COMMENT '检查报告状态（0未生成 1已生成）',
`JJY454` timestamp  COMMENT 'HIS生成检查报告的时间',
`JJY450` bigint  COMMENT '报告生成操作员id（his传）',
`JJY451` string  COMMENT '报告生成操作员名称',
`JJY452` string  COMMENT '结算类型（0自费 1医保）',
`JJY431` string  COMMENT '卡类型',
`JJY432` string  COMMENT '卡号',
`JJY433` string  COMMENT '结算状态：0未结算（初始值）1结算中2已结算3已取消',
`JJY434` string  COMMENT '支付状态：两位，第一位代表自费（说明：0代表未支付1代表已经支付2代表已退款x代表未使用）第二位代表医保（说明：0代表未支付1代表已经支付2代表已退款x代表未使用）',
`JJY435` string  COMMENT '支付方式：00全医保42微信52支付宝62云闪付（区分自费流程的支付方式）',
`JJY455` timestamp  COMMENT '支付时间',
`JJY436` double  COMMENT '订单费用',
`JJY437` string  COMMENT '平台生成付款订单号',
`JJY438` string  COMMENT '第三方线上支付平台订单号',
`JJY439` string  COMMENT '平台生成的退款订单号',
`JJY440` double  COMMENT '总订单费用',
`JJY441` double  COMMENT '医保统筹支付金额',
`JJY442` double  COMMENT '医保个人账户支付金额',
`JJY443` double  COMMENT '自费支付金额',
`JJY444` double  COMMENT '医保其他支付金额',
`JJY445` string  COMMENT '社保卡SID',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id',
`CCO107` string  COMMENT '操作员姓名（sys_user.realname',
`CCO101` timestamp  COMMENT '创建时间',
`JJY456` string  COMMENT '0未发送1已发送2已作废',
`JJY457` string  COMMENT '病种名称（主诊）',
`JJY458` string  COMMENT 'icd10码（主诊）',
`JJY459` string  COMMENT '病种名称（次诊）',
`JJY460` string  COMMENT 'icd10码（次诊）',
`JJY465` string  COMMENT '医疗类别：00自费11普通门诊13慢性病14急诊抢救',
PRIMARY KEY (`JJY401`)
) COMMENT '预约检查单表\r\n' stored as kudu;

CREATE TABLE `jy05` ( 
`JJY501` bigint  COMMENT '预约单附件id',
`JJY401` bigint  COMMENT '预约检查单id',
`JJY502` string  COMMENT '文件名称',
`JJY503` string  COMMENT '文件后缀',
`JJY504` string  COMMENT '文件类型（0图片资料1文件资料）',
`JJY505` string  COMMENT '文件在服务器中的存储路径',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.user_name）',
`CCO101` timestamp ,
PRIMARY KEY (`JJY501`)
) COMMENT '预约检查单附件表' stored as kudu;

CREATE TABLE `jy06` ( 
`JJY601` bigint  COMMENT '预约检查项目id',
`JJY401` bigint  COMMENT '预约检查id',
`JJY420` bigint  COMMENT '检查机构平台id（kb01.kkb101）',
`JJY422` string  COMMENT '检查机构平台名称',
`CCM901` bigint  COMMENT '协定项目id',
`CCM902` string  COMMENT 'his项目id',
`CCM903` string  COMMENT '拼音编码',
`CCM904` string  COMMENT '拼音编码全拼',
`CCM905` string  COMMENT '数字编码',
`CCM906` string  COMMENT '协定项目名称',
`CCM907` string  COMMENT '单位',
`CCM908` double  COMMENT '单价',
`CCO106` bigint  COMMENT '操作员id（sys_user.user_id）',
`CCO107` string  COMMENT '操作员姓名（sys_user.user_name）',
`CCO101` timestamp ,
`JJY602` string  COMMENT 'HIS接收申请单流水号',
PRIMARY KEY (`JJY601`)
) COMMENT '预约检查项目表' stored as kudu;

CREATE TABLE `kb01` ( 
`kkb101` bigint  COMMENT '医疗机构id(原orgid)',
`orgcode` string  COMMENT '机构代码，可以是HIS的机构编码',
`kkb104` string  COMMENT '医疗机构名称(原orgname)',
`aaa027` string  COMMENT '统筹区划(原areaid)',
`areaname` string  COMMENT '所属区划名称',
`isvalid` string  COMMENT '是否有效0否1是',
`signprotocolhead` string  COMMENT '家庭医生签约协议抬头',
`signprotocol` string  COMMENT '家庭医生签约协议',
`kkb106` string  COMMENT '联系电话',
`orgnameprint` string  COMMENT '机构名称用于打印(甲方)',
`create_user_id` bigint  COMMENT '创建者ID',
`create_user_name` string  COMMENT '创建者姓名',
`aae036` timestamp  COMMENT '更新时间(create_time)',
`mediatype` string  COMMENT '协同门诊：机构开通的多媒体协同类型:1文字、2音频、3视频，可以多选（按英文逗号分隔符保存）',
`kkb112` string  COMMENT '医疗机构描述信息(introduction)',
`kkb107` string  COMMENT '通讯地址',
`kkb111` string  COMMENT '医疗机构等级(levelname)',
`capitaltype` string  COMMENT '医院投资性质',
`kkb121` string  COMMENT '机构类型',
`weburl` string  COMMENT '医院公网网址',
`longitude` string  COMMENT '医院地理位置的经度',
`latitude` string  COMMENT '医院地理位置的纬度',
`kkb120` string  COMMENT '医疗机构logo路径',
`kkb103` string  COMMENT '职工医保定点编号，医保中心分配的',
`kkb105` string  COMMENT '联系人',
`kkb108` string  COMMENT '是否从HIS拉取号源，如果拉取则维护的值与机构编码相同',
`kkb109` string  COMMENT '接入式医院接口实现类名，接入式医院his业务必须维护为appointOnline',
`kkb110` string  COMMENT '微信子商户号',
`kkb113` string  COMMENT '支付宝merchantID',
`kkb114` string  COMMENT '支付宝token',
`kkb115` timestamp ,
`kkb116` string  COMMENT '支付宝AppID（作废，佳宇说没用）',
`kkb117` string  COMMENT '支付宝MD5私钥（作废，佳宇说没用）',
`kkb118` string  COMMENT '乘车路线',
`aae011` string  COMMENT '经办人',
`kkb122` string  COMMENT '医疗机构接口服务URL地址（平台调用HIS线上webservices的地址，作废）',
`kkb123` string  COMMENT '云闪付线上商户号',
`kkb124` string  COMMENT '云闪付扫码商户号',
`orgtype` string  COMMENT '机构属性（0：管理机构，1：入驻平台的社区【一级及以下】，2：对接平台的医院【二级及以上】，3：既是平台入驻的机构又是平台对接的机构【20190520作废】，4：对接平台的药店，5：支付平台）\r\n说明：\r\n1、维护平台人员的时候用0和非0区分\r\n2、线上开方的时候向属性为1、4的推送处方',
`hospitalpic` string  COMMENT '医院图片',
`kkb125` string  COMMENT '是否运维机构，0否1是',
`isunionpay` string  COMMENT '是否开通银联支付，0否1是',
`iswechat` string  COMMENT '是否开通微信支付，0否1是',
`isalipay` string  COMMENT '是否开通支付宝支付，0否1是',
`kkb126` string  COMMENT '机构是否开通医保，0否1是',
`kkb127` string  COMMENT '机构星级',
`kkb128` bigint  COMMENT '自定义排序',
`kkb129` string  COMMENT '是否开通二次报销，0否1是',
`kkb130` string  COMMENT '医护到家是否对接his，0否1是',
`kkb131` string  COMMENT '挂号不结算转HIS（非小屋）：0否1是',
`kkb132` string  COMMENT '1.仅支持线上app，2仅支持线下pda，3支持线上app和线下pda',
`kkb133` string  COMMENT '机构进行二次报销的授权码',
`kkb134` string  COMMENT '是否可拉取当日号源(0否 1是)',
`kkb135` string  COMMENT '是否接入在线问诊（控制在患者端的机构列表显示）(0否 1是)',
`kkb136` string  COMMENT '是否接入预约挂号（控制在患者端的机构列表显示）(0否 1是)',
`kkb137` string  COMMENT '接入药店类型(0独立自营 1唐人连锁)',
`kkb138` string  COMMENT '居民医保定点编号，医保中心分配的',
`kkb139` string  COMMENT '腾讯位置服务key，用于获取公网IP接口使用（官网地址：https://lbs.qq.com/）',
`kkb140` string ,
PRIMARY KEY (`kkb101`)
) COMMENT '组织机构表(原sys_org)' stored as kudu;

CREATE TABLE `kb06` ( 
`KKB601` string  COMMENT '科室分类编号',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB602` string  COMMENT '科室分类代码，来自HIS(-为手动新增的分类，与his无关)',
`KKB603` string  COMMENT '科室分类名称',
`kkb604` string ,
`kkb605` string  COMMENT '排序',
`KKB606` string  COMMENT '图片地址',
`KKB607` string  COMMENT '分类映射',
`KKB608` string  COMMENT '是否接入在线问诊（控制在患者端的列表显示）(0否 1是)',
PRIMARY KEY (`KKB601`)
) COMMENT '科室分类信息' stored as kudu;

CREATE TABLE `kb07` ( 
`KKB701` string  COMMENT '医院具体科室编号（平台）',
`KKB101` string  COMMENT '医疗机构编码(orgid)',
`KKB601` string  COMMENT '科室分类编号=kb06.kkb601',
`KKB602` string  COMMENT '科室分类ID',
`KKB603` string  COMMENT '科室分类名称',
`KKB702` string  COMMENT '医疗机构具体科室ID(deptid)',
`KKB703` string  COMMENT '医疗机构具体科室名称(deptname)',
`KKB704` string  COMMENT '具体科室的描述信息',
`KKB705` string  COMMENT 'HIS科室排序id',
`create_time` timestamp  COMMENT '创建时间',
`create_user_id` bigint  COMMENT '创建者id',
`create_user_name` string  COMMENT '创建者名称',
`istransferdept` string  COMMENT '是否为双向转诊科室0否1是',
`isteamworkdept` string  COMMENT '是否为协同门诊科室0否1是',
`address` string  COMMENT '科室所在位置',
`remark` string  COMMENT '备注',
`isvalid` string  COMMENT '是否有效0否1是',
`KKB706` string  COMMENT '科室排序（用于在线问诊处科室列表显示）',
`KKB707` string  COMMENT '是否在线问诊科室0否1是',
`KKB708` string  COMMENT '科室图片地址',
PRIMARY KEY (`KKB701`)
) COMMENT '科室表(sys_dept)' stored as kudu;

CREATE TABLE `kb08` ( 
`KKB801` bigint  COMMENT '医生编号',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB802` string  COMMENT 'HIS的医生编码',
`KKB803` string  COMMENT '医生名称',
`KKB804` string  COMMENT '职称代码',
`KKB805` string  COMMENT '职称',
`KKB806` string  COMMENT '职称级别',
`KKB807` string  COMMENT '级别',
`KKB808` string  COMMENT '医生介绍',
`KKB809` string  COMMENT '医生性别',
`KKB810` string  COMMENT '医生照片base64',
`KKB811` string  COMMENT '卫健委指定专家，0：未指定，1：专家',
`KKB812` bigint  COMMENT '自定义排序',
`user_id` bigint  COMMENT '医生对应的登录ID=sys_user.user_id 通过HIS接口过来的医生数据也让其带着手机号用于向sys_user表中产生数据',
`goodat` string  COMMENT '擅长',
`remark` string  COMMENT '备注',
`realnameauthkey` string  COMMENT '注册方式,例如：手机号，邮箱',
`realnameauthvalue` string  COMMENT '注册方式内容,例如:13812348888，zs@163.com',
`iscooperation` string  COMMENT '是否协同医生(协同门诊) ',
`isonline` string  COMMENT '在线状态：0离线，1在线，2接诊中',
`istreatmenting` string  COMMENT '是否正在接诊(协同门诊)',
`employeetype` string  COMMENT '员工类型：键值取自au_dict_type.typeid=employeetype',
`ismanager` string  COMMENT '是否管理员 0：普通用户，1：机构管理员，2：平台管理员',
`aaa027` string  COMMENT '区划代码',
`areaname` string  COMMENT '区划名称',
`status` bigint  COMMENT '状态  0：禁用   1：正常',
`kkb104` string  COMMENT '医疗机构名称(原orgname)',
`inquiringfee` double  COMMENT '咨询费（作废 姚丙清20190327 应该是当初给网上购药加的）',
`doctorcertificate` string  COMMENT '执业医师证',
`druggistcertificate` string  COMMENT '执业药师证',
`roomregisterfee` double  COMMENT '小屋医生预约挂号费',
`roomonlineinquiryfee` double  COMMENT '小屋医生在线问诊费',
`idcardno` string  COMMENT '医生身份证号',
`KKB813` string  COMMENT '人员资质（医生、药师等）',
`KKB814` double  COMMENT '挂号费（用于慢性病购药，可医保报销）',
`kkb815` string ,
PRIMARY KEY (`KKB801`,`KKB101`)
) COMMENT '医生表' stored as kudu;

CREATE TABLE `kb08_cm08` ( 
`KKB101` string  COMMENT '医疗机构id',
`KKB801` bigint  COMMENT '医生编号',
`feetype` string  COMMENT '费类型：0预约挂号费，1在线问诊费，2，慢性病购药挂号费',
`AKC515` string  COMMENT '医疗机构收费项目编码',
PRIMARY KEY (`KKB101`,`KKB801`,`feetype`)
) COMMENT '机构医生诊疗项目表' stored as kudu;

CREATE TABLE `kb09` ( 
`KKB901` string  COMMENT '平台排班编号（由平台的序列生成）',
`KKB101` bigint  COMMENT '医疗机构编码',
`KKB902` string  COMMENT 'HIS排班ID',
`KKB602` string  COMMENT '科室分类ID',
`KKB603` string  COMMENT '科室分类名称',
`KKB702` string  COMMENT '医疗机构具体科室ID',
`KKB703` string  COMMENT '医疗机构具体科室名称',
`KKB802` string  COMMENT '医生ID',
`KKB803` string  COMMENT '医生名称',
`KKB804` string  COMMENT '职称ID',
`KKB805` string  COMMENT '职称名称',
`KKB806` string  COMMENT '级别ID',
`KKB807` string  COMMENT '级别名称',
`KKB903` string  COMMENT '出诊日期',
`KKB904` string  COMMENT '星期数（1-7）',
`KKB905` string  COMMENT '午别（S上午/X下午/Y夜间）',
`KKB910` string  COMMENT '可挂号时间(如果HIS号源给的是时间点则此字段保存的就是这个时间点,如果HIS号源给的是时间段则此字段为结束时间)',
`KKB911` string  COMMENT '开始时间(如果HIS号源给的是时间点则此字段为空,如果HIS号源给的是时间段则此字段为开始时间)',
`KKB906` string  COMMENT '出诊级别ID',
`KKB907` string  COMMENT '出诊级别名称（例如普通门诊、专家门诊）',
`KKB908` string  COMMENT '可预约数量',
`KKB909` double  COMMENT '挂号费用',
`AAE011` string  COMMENT '操作员',
`AAE036` timestamp  COMMENT '更新时间',
`type` string  COMMENT '号源类别（0为HIS自己排，1为平台为HIS提供排班功能）',
PRIMARY KEY (`KKB901`)
) COMMENT 'HIS预约挂号排班信息，此表数据来源机构二选一：1、定时任务从HIS读取2、直接在平台上排班' stored as kudu;

CREATE TABLE `lucky_done_user` ( 
`OPENID` string ,
`FATHERVID` string ,
`PHONE` string ,
`ORDER_NUM` string ,
`SEND` double ,
`FATHER_VID` string ,
`LOTTERY` string ,
`LOTTERY_PLUS` string ,
`NICKNAME` string ,
`STATE` string ,
PRIMARY KEY (`OPENID`)
) stored as kudu;

