# 关于：
>1、原项目地址: https://github.com/Nriver/Episode-ReName
>
>2、适配群晖Download Station
>
>3、协议: https://github.com/Nriver/Episode-ReName/blob/main/LICENSE
----

# 配置
## 关键字段
>1、编辑schedule.py字段,修改为你的环境
>
>downloadpath = "/volume4/download/2222-incomplete/dl_tmp/bangumi"
>warepath = "/volume1/homes/xinjiawei/bangumi/new_bangumi"
>renamescript = "/volume4/download/2222-incomplete/dl_tmp/EpisodeReName.py"
>renamedelay = 1
>badstr = '@|DAV'
>
## 解释
>临时下载目录: {downloadpath}')
>本地或挂载的目标仓库目录: {warepath}')
>主程序EpisodeReName.py路径: {renamescript}')
>重命名延时,防止拥塞,单位为秒: {badstr}')
>跳过的目录关键词,使用|分割: {renamedelay}')
----

# 安装使用,这里略写,详细请参考博客: [定制符合我de环境的,第三代自动追番一体化](https://blog.jiawei.xin/?p=1019)
## 第一步: 安装依赖

>1、安装pip
>
>2、安装依赖
>
----

## 第二步: 配置群晖的定时任务

>1、root权限运行
>
>2、设置半个小时运行一次
>
>3、设置运行命令
----
