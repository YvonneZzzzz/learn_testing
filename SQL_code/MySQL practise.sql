--这后边就是注释
/*
这里是注释
这里是第二行注释
*/

--建议关键字大写

------

--当你决定不想执行某条命令时
\c		--取消它

--显示有哪些数据库
SHOW DATABASES;

--使用连接某个数据库
USE edrain01;

--查看你正在使用的是那一个数据库
SELECT DATABASE();

--查看使用的数据库中有哪些表
SHOW TABLES;

--查看表结构
DESCRIBE employee;

--查看表的数据结构
SHOW CREATE TABLE department;

--查看表中字段的信息
SHOW FULL COLUMNS FROM department;

--查看索引(如果表有索引的话)
SHOW INDEX FROM employee;


--退出
QUIT
EXIT


------

--创建数据库(注意DARABA后面没有S)
CREATE DATABASE edrain01;

--创建表
CREATE TABLE test
(
id int(10),
name char(20),
phone int(12)
);

--在表格中插入数据
INSERT INTO employee(id,name,phone) VALUES(01,'Tom',110110110);
INSERT INTO employee VALUES(02,'Jack',119119119);
INSERT INTO employee(id,name) VALUES(04,'Rose');

--检索单个列
SELECT id 
FROM employee;

--检索多个列
SELECT id, name, phone 
FROM employee;

--检索所有列
SELECT * 
FROM employee;
-- * 叫做通配符

--检索去重
--使用DISTINCT关键字
SELECT DISTINCT * 
FROM employee;

--限制只显示结果中的前2行
SELECT * FROM employee LIMIT 2;

--查看某个表的指定列
SELECT id,name FROM employee;

--数学符号条件(=,<,>,>=,<=)
SELECT id,name FROM employee WHERE id>2;
SELECT id,name,phone FROM employee WHERE name='Tom';
SELECT id,name FROM employee WHERE id<2 OR id>3;
SELECT name,age FROM employee WHERE age>25 AND age<30;

-- IN 和 NOT IN 筛选“在” 或 “不在”某个范围内的结果
SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt IN ('dpt3','dpt4');
SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt NOT IN ('dpt1','dpt3');

------
--通配符
--SQL中的通配符是 _ 和 % 
-- % 代表不定个未指定字符。
SELECT id, name 
FROM employee 
WHERE name LIKE '%om%';

--下划线_通配符
-- _ 代表一个未指定字符
SELECT id, name 
FROM employee 
WHERE name LIKE '__m';

--用CONTAINS进行搜索
SELECT id,name 
FROM employee 
WHERE CONTAINS(id,'1');
/*CONTAINS搜索通常比LIKE更快，表越大越如此
CONTAINS 中可以使用*通配符：CONTAINS(note_text, '"anvil*"');
表示匹配任何以anvil开始的词*/

--通配符使用技巧
--不要过度使用通配符，如果能够用其他操作符达到相同的目的，就用其他操作符
--尽量不要把通配符放在搜索模式的开始处，因为这样是搜索最慢的
--仔细注意通配符的位置。如果放错地方，可能不会返回想要的数据

------

--对结果进行排序
--ORDER BY 语句 升序排列 ASC；
SELECT name 
FROM employee 
ORDER BY name;
--会以字母顺序排序

--按照多个列排序
SELECT id, phone, name 
FROM employee 
ORDER BY phone, name;
--先按电话排序，后按名称排序

--降序排列 DESC
SELECT id, phone, name 
FROM employee 
ORDER BY phone DESC;
--会以电话降序排列

------

--SQL 内置函数和计算
Count()	--返回某列的行数
Sum()   --返回某列值的和
Avg()	--返回某列的平均值
Max()   --返回某列的最大值
Min()   --返回某列的最小值

--Count()函数  --返回表中行的数目或者复合特定条件的行的数目
--包括了NULL行
--能够使用Count(*)对表中的行数目进行计数
SELECT COUNT(cust_email) AS num_cust FROM customers;
SELECT COUNT(*) FROM employee;
--选取具有电子邮件的客户计数,计数值在以num_cust命名的列中返回
--如果指定列名，则指定列的值为空的行被Count()函数忽略，但是如果Count()函数中用的星号(*),则不忽略

--Sum()用来返回指定列值的和
SELECT Sum(item_price * quantity) AS total_price
FROM prderitems
WHERE order_num = 20005;
--利用标准的算术操作符，所有聚集函数都可以用来执行多个列上的计算

--Avg()函数  --Avg()忽略列值为NULL的行
SELECT Avg(prod_price) AS avg_price
FROM products
WHERE vend_id = 1003;

--Max()函数  --返回指定列中的最大值
--Max()函数忽略列值为NULL的行
--如果对于非数值数据使用Max()，在用于文本数据时，如果数据按照相应的列排序，则Max()返回最后一行

--Min()函数  --和上一条类比
--如果对于非数值数据，返回最前面的行

--计算出salary的最大、最小值
--使用AS关键词可以给值重命名
SELECT MAX(salary) AS max_salary,MIN(salary) FROM employee;

------

--子查询
/*
想要知道名为 "Tom" 的员工所在部门做了几个工程。
员工信息储存在 employee 表中，但工程信息储存在project 表中。
*/
SELECT of_dpt,COUNT(proj_name) AS count_project FROM project 
WHERE of_dpt IN 
(SELECT in_dpt FROM employee WHERE name='Tom');

![image.png](https://upload-images.jianshu.io/upload_images/1683050-154abba3e8378e22.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

--连接查询
/*
在处理多个表时，子查询只有在结果来自一个表时才有用。
但如果需要显示两个表或多个表中的数据，这时就必须使用连接 (join) 操作。
连接的基本思想是把两个或多个表当作一个新的表来操作
*/
SELECT id,name,people_num
FROM employee,department
WHERE employee.in_dpt = department.dpt_name
ORDER BY id;
--另一个连接语句格式是使用 JOIN ON 语法
SELECT id,name,people_num
FROM employee JOIN department
ON employee.in_dpt = department.dpt_name
ORDER BY id;
/*
查询出的是，各员工所在部门的人数，
其中员工的 id 和 name 来自 employee 表，people_num 来自 department 表：
*/
------

###修改和删除
- 数据库操作
- 数据表操作
- 更新和删除数据

--重命名一张表
RENAME TABLE 原名 TO 新名字;
ALTER TABLE 原名 RENAME 新名;
ALTER TABLE 原名 RENAME TO 新名;

--删除一张表,数据结构会被删除了
DROP TABLE 表名字;

--增加一列
ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;
ALTER TABLE 表名字 ADD 列名字 数据类型 约束;
约束默认值为2，eg:
ALTER TABLE employee ADD price INT(8) DEFAULT 2;
--如果想放在第一列的位置 FIRST
ALTER TABLE employee ADD test INT(10) DEFAULT 11 FIRST;
--新增的列加在某位置的后面 AFTER
ALTER TABLE employee ADD test INT(10) DEFAULT 8 AFTER price;

--删除一列
ALTER TABLE 表名字 DROP COLUMN 列名字;
ALTER TABLE 表名字 DROP 列名字;

--重命名一列
ALTER TABLE 表名字 CHANGE 原列名 新列名 数据类型 约束;
eg:
ALTER TABLE employee CHANGE price jiage INT(8) DEFAULT 2;

--改变数据类型
ALTER TABLE 表名字 MODIFY 列名字 新数据类型;
/*修改数据类型必须小心，因为这可能会导致数据丢失。
在尝试修改数据类型之前，请慎重考虑*/

--修改表中某个值
UPDATE 表名字 SET 列1=值1,列2=值2 WHERE 条件;
eg:
UPDATE employee SET name='EDRAINtest',phone=1888666 WHERE name='Tom';
UPDATE 表名字 SET 列1=REPLACE(列1,'原值','新值') WHERE 条件;
UPDATE employee SET name = REPLACE(name,'Rose','33') WHERE id=3;
UPDATE employee SET name = REPLACE(name,'Rose','wahh');

--删除一行记录
DELETE FROM 表名字 WHERE 条件;
eg：
DELETE FROM employee WHERE name='Rose';
/*删除表中的一行数据，也必须加上WHERE条件，否则整列的数据都会被删除。*/

------
###索引、视图，导入和导出，备份和恢复
- 索引
- 视图
- 导入和导出
- 备份和恢复

--显示表中有哪些索引
SHOW INDEX FROM 表名字
eg:
SHOW INDEX FROM employee;

--在表中添加索引值
ALTER TABLE 表名字 ADD INDEX 索引名 (列名);
CREATE INDEX 索引名 ON 表名字 (列名);
eg：
--在employee表的id列上建立名为idx_id的索引
ALTER TABLE employee ADD INDEX idx_id (id);  
--在employee表的name列上建立名为idx_name的索引
CREATE INDEX idx_name ON employee (name);   

--创建视图
CREATE VIEW 视图名(列a,列b,列c) AS SELECT 列1,列2,列3 FROM 表名字;
CREATE VIEW v_emp (v_name,v_age,v_phone) AS SELECT name,age,phone FROM employee;

--导入
LOAD DATA INFILE '文件路径和文件名' INTO TABLE 表名字;
--将文件中的数据导入到employee表中
LOAD DATA INFILE '/tmp/SQL6/in.txt' INTO TABLE employee;
--如果用Windows中的编辑器（使用\r\n做为行的结束符）创建文件，应使用：
LOAD DATA INFILE '文件路径' INTO TABLE employee LINES 
TERMINATED BY '\r\n';
--在运行OS X的苹果电脑上，应使用行结束符\r

--导出
SELECT * INTO OUTFILE '导出生成的文件路径和文件名' FROM 表名字;
--将整个employee表的数据导出到　/tmp　目录下
SELECT * INTO OUTFILE '/tmp/out.txt' FROM employee;

--备份
mysqldump -u root 数据库名>备份文件名;  --备份整个数据库
mysqldump -u root 数据库名 表名字>备份文件名;  --备份整个表
eg:
mysqldump -u root mysql_shiyan > bak.sql;

--第一种恢复数据库的方法
source /tmp/SQL6/MySQL-06.sql
--另一种恢复数据库的方法
--先使用命令新建一个空的数据库 test：
mysql -u root          --因为在上一步已经退出了MySQL，现在需要重新登录
CREATE DATABASE test;  --新建一个名为test的数据库
mysql -u root test < bak.sql --刚才备份的 bak.sql 恢复到 test 数据库：

/*
	1. 索引：可以加快查询速度
	2. 视图：是一种虚拟存在的表
	3. 导入：从文件中导入数据到表
	4. 导出：从表中导出到文件中
	5. 备份：mysqldump 备份数据库到文件
	6. 恢复：从文件恢复数据库
*/

------
--查询MySQL版本号
SELECT VERSION();
--查询当前日期
CURRENT_DATE;
--查询当前时间
SELECT NOW();
--查询当前用户
SELECT user();

--简单计算功能
SELECT SIN(PI()/4),(4+1)*5;

--查询表中的名称或类型
DESCRIBE department;
--查看表的数据结构
SHOW CREATE TABLE department;
--查看表中字段的信息
SHOW FULL COLUMNS FROM department;

--更新需要修改的值
UPDATE 表名字 SET 更新的地方 WHERE 条件;
eg:
UPDATE pet SET birth = '1989-08-31' WHERE name = 'Bowser';

--日期计算
--函数TIMESTAMPDIFF()计算当前日期的年和出生日期之间的差
--函数CURDATE()是计算当前的日期
SELECT name, birth, CURDATE(), 
TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age 
FROM pet;
--(YEAR(CURDATE())-YEAR(birth))也可以计算当前日期的年和出生日期之间的差
SELECT name, birth, CURDATE(), 
(YEAR(CURDATE())-YEAR(birth)) 
- (RIGHT(CURDATE(),5)<RIGHT(birth,5)) AS age  
FROM pet;
/*
此处，YEAR()提取日期的年部分，RIGHT()提取日期最右面5个字符的MM-DD (月份和日期)部分。
MM-DD值的表达式部分的值一般为1或0，如果CURDATE()的年比birth的年早，则年份应减去1。
整个表达式看起来有些难懂，使用age来使输出的列标记更有意义。
*/

--NULL值操作
/*
概念上，NULL意味着“没有值”或“未知值”，并且它被看作使与众不同的值。
为了测试NULL，你不能使用算术比较操作符例如=、<或!=
*/
SELECT 1 = NULL, 1 <> NULL, 1 < NULL, 1 > NULL;
/*
很显然你不能通过这些得到有意义的结果，因为任何使用算数比较操作符对NULL进行比较的结果都是NULL。
因此使用IS NULL和IS NOT NULL操作符：
*/
SELECT 1 IS NULL, 1 IS NOT NULL;
--在MySQL中，0或NULL意味着假而其它值意味着真。布尔运算的默认真值是1。

--使用“^”和“$”匹配名字的开始和结尾，和5个“.”实例在两者之间：
SELECT * FROM pet WHERE name REGEXP '^.....$';
--使用“{n}”重复n次操作符,重写前面的查询
SELECT * FROM pet WHERE name REGEXP '^.{5}$';

--COUNT(*)计算和GROUP BY分组以各种形式分类你的数据
--查看每种动物的数量：
SELECT species, COUNT(*) FROM pet GROUP BY species;
--按种类和性别组合分类的动物数量：
SELECT species, sex, COUNT(*) FROM pet GROUP BY species, sex;
------

--寻找列的最大值
SELECT MAX(article) as article FROM shop;

--查询某列最大值所在的行
SELECT article, dealer, price 
FROM shop 
WHERE price=(SELECT MAX(price) FROM shop);

--对所有行进行价格的降序排列，然后使用MySQL特定的LIMIT子句显示其中一行
SELECT article, dealer, price 
FROM shop 
ORDER BY price DESC 
LIMIT 1;

--按组显示列的最大值
SELECT article, MAX(price) AS price 
FROM shop 
GROUP BY article;

--使用用户变量
SELECT @min_price:=MIN(price),@max_price:=MAX(price) FROM shop;
SELECT * FROM shop WHERE price=@min_price OR price=@max_price;

-- 使用AUTO_INCREMENT语句
-- 在定义列属性的时候添加AUTO_INCREMENT语句可以使得每条记录都能被唯一标识：
CREATE TABLE animals (
id MEDIUMINT NOT NULL AUTO_INCREMENT,
name CHAR(30) NOT NULL,
PRIMARY KEY (id)
);
INSERT INTO animals (name) VALUES ('dog'),('cat'),('penguin'),('lax'),('whale'),('ostrich');
SELECT * FROM animals;
-- 要想AUTO_INCREMENT语句生成的起始值不是1，可以通过CREATE TABLE或ALTER TABLE来设置该值
ALTER TABLE animals AUTO_INCREMENT = 100;

------
--使用外键
/*  在连接两个表的时候并不需要外键约束。
对于除InnoDB表以外的表，可以使用REFERENCES tbl_name(col_name)语句定义将它的列设置为外键，
但是该语句并没有实际的作用，只是作为备注来提醒你现在正在定义的列指向另外一个表的列。 */
CREATE TABLE person (
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
name CHAR(60) NOT NULL,
PRIMARY KEY (id)
);
--
CREATE TABLE shirt (
id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
style ENUM('t-shirt', 'polo', 'dress') NOT NULL,
color ENUM('red', 'blue', 'orange', 'white', 'black') NOT NULL,
owner SMALLINT UNSIGNED NOT NULL REFERENCES person(id),
PRIMARY KEY (id)
);
--
INSERT INTO person VALUES (NULL, 'Antonio Paz');
--
SELECT @last := LAST_INSERT_ID();
--
INSERT INTO shirt VALUES
(NULL, 'polo', 'blue', @last),
(NULL, 'dress', 'white', @last),
(NULL, 't-shirt', 'blue', @last);
--
INSERT INTO person VALUES (NULL, 'Lilliana Angelovska');
--
SELECT @last := LAST_INSERT_ID();
--
INSERT INTO shirt VALUES
(NULL, 'dress', 'orange', @last),
(NULL, 'polo', 'red', @last),
(NULL, 'dress', 'blue', @last),
(NULL, 't-shirt', 'white', @last);

--查看表的数据结构
SHOW CREATE TABLE shirt;
SHOW CREATE TABLE shirt\G
DESCRIBE shirt;

--使用两个关键字进行搜索
-- 这里面的test_table可以是任何一个表，关键词也是类似
-- 充分利用OR连接两个关键字（AND也是一样的道理）
SELECT field1_index, field2_index FROM test_table 
WHERE field1_index = '1' OR  field2_index = '1';
eg：
SELECT id, name FROM employee 
WHERE id = '1' OR  name = 'Rose';

-- 计算每个月的访问量
-- 创建表
CREATE TABLE t1 (year YEAR(4), month INT(2) UNSIGNED ZEROFILL, day INT(2) UNSIGNED ZEROFILL);
INSERT INTO t1 VALUES(2000,1,1),(2000,1,20),(2000,1,30),(2000,2,2),(2000,2,23),(2000,2,23);
-- 使用BIT_COUNT函数计算每个月中某用户访问网页的天数：
SELECT year,month,BIT_COUNT(BIT_OR(1<<day)) AS days FROM t1 GROUP BY year,month;

------
--两张表格的内连接
select * from animals inner join employee on animals.id=employee.id;	#标准写法，on后面是带有限制条件的的“内连接”
select * from animals,employee where animals.id=employee.id;
--上面两种写法是一样的，“inner join”可以简写为“join”
--三张表格的内连接
SELECT * FROM animals INNER JOIN employee ON animals.id=employee.id INNER JOIN shirt ON animals.id=shirt.id;	
SELECT * FROM animals, employee, shirt WHERE animals.id=employee.id and animals.id=shirt.id;

--外连接：left join, right join
select * from animals left join employee on animals.id=employee.id;
select * from animals right join employee on animals.id=employee.id;
+-----+---------+------+------+-----------+-------+
| id  | name    | id   | name | phone     | jiage |
+-----+---------+------+------+-----------+-------+
|   3 | penguin |    3 | Rose |      NULL |    88 |
|   1 | dog     |    1 | Tom  | 110110110 |    88 |
|   4 | lax     |    4 | Rose |      NULL |    88 |
|   2 | cat     | NULL | NULL |      NULL |  NULL |
|   5 | whale   | NULL | NULL |      NULL |  NULL |
|   6 | ostrich | NULL | NULL |      NULL |  NULL |
| 100 | aaa     | NULL | NULL |      NULL |  NULL |
| 101 | bbb     | NULL | NULL |      NULL |  NULL |
+-----+---------+------+------+-----------+-------+

--联合查询
SELECT * FROM shirt UNION all SELECT * FROM employee;
