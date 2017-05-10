自动摘要提取工具
--------
安装步骤
------
pip install flask

pip install snownlp

python summary-service.py

测试接口例子
------
curl -i -H "Content-Type: application/json" -X POST -d '{"text":"欧洲央行行长德拉吉今日在荷兰众议院发表讲话时指出，欧洲央行的政策显然利大于弊，欧元区明显在改善，下行风险已经进一步消失"}' http://127.0.0.1:5000/api/v1.0/summary