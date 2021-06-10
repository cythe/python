#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# base logic
#
# 思路1： 对patch中的每个hunt与上游patch做对比，查看是否有应用的
#            缺点： 需要处理 应用了之后又撤销了的情况
#
# 思路2： 对patch中的每个hunt与当前状态作对比看是否应用
