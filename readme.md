## 逻辑表达式化简

化简的基本思路：
1. 计算逻辑表达式的真值表
2. 基于真值表，优先找到含有变量较小的质蕴涵
3. 对第二部找到的所有质蕴涵，从含有较多变量的质蕴涵开始，从列表中删除非最大的质蕴涵
4. 将质蕴涵用或连接

运行test.py可查看测试用例
运行main.py可输入任何变量数在13位以内的逻辑表达式，程序会输出该表达式的真值表和最简逻辑表达式（非唯一）。输入规范参考test.py
若要将真值表作为输入，可将真值表储存为一维列表，并通过该列表初始化logical_function类
若要操作更多的变量，可先运行_generate_implicant.py