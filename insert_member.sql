-- 查询用户member表 所有数据--
SELECT * FROM tcl_college_test.member;

-- 1. 向member表中插入一条新数据, memberid = member_notification_settings.id --
INSERT INTO tcl_college_test.member(id,OpenId,DepartmentId,NAME,Score,Enabled,MemberType,MemberTypeModifiedTime,Gender,MemberId)
SELECT '975bd4f2-baff-4aa9-8588-4323e6f10000','owc6iuGL-fouV7erLYDGhbqIN0000',0,'zhao01',0,1,1,MemberTypeModifiedTime,Gender,MemberId 
FROM tcl_college_test.member WHERE id='975bd4f2-baff-4aa9-8588-4323e6f1b675';

--查询插入的数据--
SELECT * FROM tcl_college_test.member where id = '975bd4f2-baff-4aa9-8588-4323e6f10000'


-- 查询member 信息设置表 --
select * from tcl_college_test.member_notification_settings; 

-- 2. 向member信息设置表中插入一条新数据，id = member.memberid --
INSERT INTO tcl_college_test.member_notification_settings
(`Id`,
`MemberId`,
`CourseStartWeChat`,
`CourseStartStation`,
`CourseBuyWeChat`,
`CourseBuyStation`,
`CourseReleaseStation`,
`CourseReleaseWeChat`,
`CourseEnrollStation`,
`CourseEnrollWeChat`,
`CourseLecturerApplyStation`,
`CourseLecturerApplyWeChat`,
`CourseCourseEvaluateStation`,
`CourseCourseEvaluateWeChat`,
`CreatorId`,
`CreatorName`,
`CreatedTime`,
`ModifierId`,
`ModifierName`,
`ModifiedTime`,
`LecturerSubscribeStation`,
`LecturerSubscribeWeChat`)
select
'82d060bd-710a-46bf-9be0-cf2711e50000',
'975bd4f2-baff-4aa9-8588-4323e6f10000',
`CourseStartWeChat`,
`CourseStartStation`,
`CourseBuyWeChat`,
`CourseBuyStation`,
`CourseReleaseStation`,
`CourseReleaseWeChat`,
`CourseEnrollStation`,
`CourseEnrollWeChat`,
`CourseLecturerApplyStation`,
`CourseLecturerApplyWeChat`,
`CourseCourseEvaluateStation`,
`CourseCourseEvaluateWeChat`,
`CreatorId`,
`CreatorName`,
`CreatedTime`,
`ModifierId`,
`ModifierName`,
`ModifiedTime`,
`LecturerSubscribeStation`,
`LecturerSubscribeWeChat`
from tcl_college_test.member_notification_settings
where id ='82d060bd-710a-46bf-9be0-cf2711e5f38c';

--查询插入的数据--
select * from tcl_college_test.member_notification_settings where id = '82d060bd-710a-46bf-9be0-cf2711e50000'

-- 3. 将member.MemberId = member_notification_settings.id  --
update tcl_college_test.member set MemberId = '82d060bd-710a-46bf-9be0-cf2711e50000' where id = '975bd4f2-baff-4aa9-8588-4323e6f10000';