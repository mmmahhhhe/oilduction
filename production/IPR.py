# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:14:48 2020

@author: 舒晋
"""

import numpy as np


class IPR:
    
    def vogel_1point ( self , pwf_test , qo_test , pr_ave , pwf_pre ) :
        # TODO 增加数据检验
        assert pwf_test < pr_ave, '测试压力应小于地层静压'
        
        #产能预测
        qo_max = qo_test / ( 1 - 0.2 * pwf_test / pr_ave - 0.8 * ( pwf_test / pr_ave ) ** 2 )
        qo_pre = ( 1 - 0.2 * pwf_pre / pr_ave - 0.8 * ( pwf_pre / pr_ave ) ** 2 ) *qo_max
        return qo_pre
    
    def vogel_2point ( self , pwf_test1 , qo_test1 , pwf_test2 , qo_test2 , pwf_pre ) :
        # TODO 增加数据检验
        #计算油藏平均压力
        q1 = qo_test1
        q2 = qo_test2
        pwf1 = pwf_test1
        pwf2 = pwf_test2
        A = q1 / q2 - 1
        B = 0.2 * ( q1 / q2 * pwf2 - pwf1 )
        C = 0.8 * ( q1 / q2 * pwf2 ** 2 - pwf1 ** 2 )
        pr_ave1 = ( B + np.sqrt ( B ** 2 + 4 * A * C ) ) / 2 * A
        pr_ave2 = ( B - np.sqrt ( B ** 2 + 4 * A * C ) ) / 2 * A
        pr_ave = max ( pr_ave1 , pr_ave2 )
        #产能预测
        qo_max = qo_test1 / ( 1 - 0.2 * pwf_test1 / pr_ave - 0.8 * ( pwf_test1 / pr_ave ) ** 2 )
        qo_pre = ( 1 - 0.2 * pwf_pre / pr_ave - 0.8 * ( pwf_pre / pr_ave ) ** 2 ) * qo_max
        return qo_pre
                
if __name__=='__main__':
    # demo
    
    pwf_test = 20
    qo_test = 40
    pr_ave = 30
    pwf_pre1 = 15
    IPR = IPR ()
    qo = IPR.vogel_1point ( pwf_test , qo_test , pr_ave , pwf_pre1 )
    print ( ' The prediction of qo is : ' , qo )
    
    pwf_test1 = 15
    pwf_test2 = 20
    qo_test1 = 40
    qo_test2 = 20
    pwf_pre2 = 18
    qo = IPR.vogel_2point ( pwf_test1 , qo_test1 , pwf_test2 , qo_test2 , pwf_pre2 )
    print ( ' The prediction of qo is : ' , qo )
    
    