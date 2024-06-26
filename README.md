# 目录结构

### 目录结构说明

```
├── common	                                         # 公共层
├── API                                                  # API
├── requirements.txt                                     # 项目用到的第三方库
├── README.md		                                 # 说明文档
├── reports                                              # 测试报告
├── data                                                 # 测试数据
│     ├── asset_detection                                # 资产测绘                        
│         ├── asset_allocation                           # 资产配置
│         ├── asset_discovery                            # 资产发现
│         ├── asset_management                           # 资产管理
│         ├── asset_scan                                 # 资产扫描
│         ├── asset_topology                             # 资产拓扑
│     ├── flow_analysis                                  # 流量分析
│         ├── application_flow                           # 应用流量
│         ├── behavior_auditing                          # 行为审计
│         ├── flow_statistics                            # 流量统计
│         ├── key_behavior                               # 关键行为
│         ├── link_details                               # 链路详情
│     ├── security_configuration                         # 安全配置
│         ├── alarm_configuration                        # 告警配置
│         ├── Association_analysis                       # 关联分析
│         ├── Baseline_strategy                          # 基线策略
│         ├── exception_management                       # 例外管理
│         ├── Intrusion_Strategy                         # 入侵策略
│         ├── Key_behavior_strategy                      # 关键行为策略
│         ├── Resource_library                           # 资源库
│         ├── Safety_margin                              # 安全域
│         ├── Virus_configuration                        # 病毒配置
│         ├── Weak_password_configuration                # 弱口令配置
│     ├── statistical_statement                          # 统计报表
│         ├── report_template                            # 报表模版
│         ├── statement_record                           # 报表记录
│     ├── system_management                              # 系统管理
│         ├── authority_management                       # 权限管理
│         ├── condition_monitoring                       # 状态监测
│         ├── data_management                            # 数据管理
│         ├── data_separation                            # 数据分离
│         ├── engine_management                          # 引擎管理
│         ├── network_settings                           # 网络设置
│         ├── outgoing_data                              # 数据外发
│         ├── policy_backup                              # 策略备份
│         ├── system_information                         # 系统信息
│         ├── system_log                                 # 系统日志
│         ├── system_settings                            # 系统设置
│         ├── tool_box                                   # 工具箱
│     ├── threat_dection                                 # 威胁检测
│         ├── anomaly_warning                            # 异常预警
│         ├── intrusion_detection                        # 入侵检测
│         ├── security_zone_alarm                        # 安全域告警
│         ├── virus_detection                            # 病毒检测
│         ├── workbench                                  # 工作台
│     ├── vulnerability                                  # 脆弱性
│         ├── asset_weakness                             # 资产弱点
│         ├── dangerous_port                             # 危险端口
│         ├── weak_password                              # 弱口令
├── decorators
├── lib                     #工控协议功能码信息
├── log                     #日志文件
├── testcases               #测试用例
├── upload                  #上传证书
├── utils                   #工具类
│   ├── lib_config          #加载配置信息
|   ├── logger              #日志记录器
│   ├── random_data         #生成随机字符
├── config.yml              #文件的全局配置信息
├── conftest.py             # 装饰器文件
├── pytest.ini              #pytest框架配置信息
└── run.py                  # 工程入口执行脚本 


```
