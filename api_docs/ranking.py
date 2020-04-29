# coding=utf-8
"""
API-DOCS FOR RANKING APP
"""

"""
    @api {POST} /ranking/client_score/  上传客户端分值
    @apiVersion         1.0.0
    @apiName            create_client_score
    @apiGroup           Ranking
    @apiDescription     描述: 上传客户端分值
    @apiPermission      None
    
    @apiParam {String}  client_name      客户端名称
    @apiParam {Integer} score            客户端分值

    @apiSuccess {statue_code}    状态码         201：创建成功， 400：创建失败
    @apiSuccess {Integer}        id            主键ID
    @apiSuccess {String}         client_name   客户端姓名
    @apiSuccess {Integer}        score         分数
    @apiSuccess {Integer}        create_time   创建时间
    
    @apiSuccessExample {json} 成功返回示例:
      HTTP/1.1 201 CREATED
        {
            "id": 24,
            "client_name": "客户端7",
            "score": 100,
            "create_time": "2020-04-29T16:12:12.321899Z"
        }

    @apiError    status_code  400    错误的请求参数
    @apiErrorExample {json} 失败返回示例:
      HTTP/1.1 400 BAD REQUEST
        {
            "score": [
                "客户端分值范围：0-10000000！"
            ]
        }
        
      HTTP/1.1 400 BAD REQUEST
        {
            "score": [
                "A valid integer is required."
            ]
        }
"""

"""
    @api {GET} /ranking/ranking_list/?my_client_name=客户端1&start=3&end=10  获取排行榜
    @apiVersion         1.0.0
    @apiName            get_ranking_list
    @apiGroup           Ranking
    @apiDescription     描述: 获取排行榜
    @apiPermission      None

    @apiParam {Integer}  start               查询开始区间（可为空）
    @apiParam {Integer}  end                 查询结束区间（可为空）
    @apiParam {String}   my_client_name      当前客户端

    @apiSuccess {statue_code}    状态码         200：请求成功， 400：请求失败
    @apiSuccess {Integer}        id            主键ID
    @apiSuccess {String}         client_name   客户端姓名
    @apiSuccess {Integer}        score         分数

    @apiSuccessExample {json} 成功返回示例:
      HTTP/1.1 200 OK
        [
            {
                "id": 1,
                "client_name": "客户端3",
                "score": 10000000
            },
            {
                "id": 5,
                "client_name": "客户端4",
                "score": 89892
            },
            ......
            # 最后一条数据为当前客户端分值
            {
                "id": 4,
                "client_name": "客户端6",
                "score": 8989
            }
        ]

    @apiError    status_code  400    错误的请求参数
    @apiErrorExample {json} 失败返回示例:
      HTTP/1.1 400 BAD REQUEST
        {
            "my_client_name": [
                "This field is required."
            ]
        }
        
      HTTP/1.1 400 BAD REQUEST
        {
            "my_client_name": [
                "客户端名称有误！"
            ]
        }
        
      HTTP/1.1 400 BAD REQUEST
        {
            "start": [
                "A valid integer is required."
            ]
        }
"""
