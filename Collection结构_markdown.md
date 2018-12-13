#  结构说明

## √ 学校

[**CollectionName:SS_School**](#SS_School)

```javascript
{
    SchoolId : string //"rucode" 学校组织代码
    SchoolName : string //"学校名称"
    SchoolStatus：int  //"学校状态" 1 ??        2??
    SchoolArea：String  //"学校区域"
    SchoolCity：String  // "学校城市"
    SchoolStartDateTime：datetime  //"学校开始时间" ISODate("2018-04-01 15:30:00")
    SchoolEndDateTime：datetime  //"学校结束时间" ISODate("2018-04-01 15:30:00")
    Proposer：String   //"提议者"
    AttendenceType: int // ??
    FaceRecognition : int //"是否开通人脸识别"
    VideoCall：int  //"是否开通视频通话"
    createddatetime : datetime  //"创建时间" ISODate("2018-04-01 15:30:00")
    scheduledStartTime: string //班牌定时开机时间
    scheduledStopTime: string //班牌定时关机时间
}
```

## √ 校日程安排
[**CollectionName: SS_SchoolAgenda**](#SS_SchoolAgenda)

```javascript
{
    SemesterMid : string //关联的学期Mid
    AgendaType : int     //日程类型  1正常  2放假  3补课  4其它 0为月份信息
    AgendaDateTime : date//日程日期  ISODate("2018-04-01 15:30:00")
    AgendaMonth : string  //年月"2018-09"
    AgendaMakeUpDate : date  //补哪一天课的日期
    AgendaComment : string  //日程备注
}
```

## √ 角色

[**CollectionName:SS_Role**](#SS_Role)

```javascript
//角色(0: 超级管理员,1: 普通管理员)
{
    RoleId : int //1
    RoleName : string //'管理员'
}
```

## √ 用户


[**CollectionName: SS_User**](#SS_User)


```javascript
{
     Rucode : string //组织代码,
     Role : int //0、超级管理员，1、 管理员 2 、教师 3 、学生
     UserName : string //用户名学号
     UserCode : string // 用户手机号码''
     Passwd : string //密码'' 后台自动加密生成的密码
     CreatedTime : datetime //创建时间''
     lastlogindatetime : Date //最后登录时间''
     StudentMid : array //学生关联Mid"" 
     TeacherMid : array //教师 Mid""，
     Permission : int // 1普通老师权限，2在线上课 ，3 1+2 同时拥有普通老师和在线上课权限 ??没有使用该字段
}
```

## √ 科目信息表

[**CollectionName: SS_Subject**](#SS_Subject)

```javascript
{
    Rucode : string //"3401006" 学校组织编码
    SubJect_Name : int // "数学"
    SubJect_Status : int // 科目状态，默认为1
    SubJect_Created_Time : datetime //"2017-07-29 17:00:00"
    HeFeiSync： int //跟合肥数据库同步
}
```

## √ 教室信息表

[**CollectionName: SS_ClassRoom**](#SS_ClassRoom)

```javascript
{
    Rucode : string //学校的组织代码
    Class_Room_Uid : string //教室的账号 编号 Uid
    Class_Room_Password : string // 教室对应的登录密码 初始welcome
    Class_Room_Name : string //教室名称
    Class_Room_Adreess : string //学校楼栋地址
    Class_Room_Type : string //教室类型   普通教室、多媒体教室 等
    Class_Room_Number : int //200 班级容纳人数
    LoginStatus : int //0 未登录 1 登录 2 离线 创建班级的时候无该字段
    BanPaiDeviceId : string // 教室绑定班牌的设备 Id 创建班级的时候无该字段
    Class_Room_Created_Time : datetime//ISODate("2018-04-01 15:30:00")
}
```

## √ 教师部门

[**CollectionName:SS_TeacherDeparment**](#SS_TeacherDeparment)

```javascript
{
    TeacherDeparmentName:String, // "部门名称"
    Rucode: String, // "组织编码"
    ParentMid: String, // "父级部门MID"
    CreateDateTime: String //部门创建时间 ISODate("2017-11-10T15:49:58.902+0000");
}
```

## √ 教研组

[**CollectionName:SS_TeacherGroup**](#SS_TeacherGroup)

```javascript
{
    TeacherGroupName：String, // "教研组名称"，
    TeacherGroupSubject：String, // "教研组科目"
    TeacherGroupDesc: String, // "教研组描述"
    Rucode：String //"学校组织代码"
    CreateDateTime：String // "教研组创建时间" ISODate("2017-11-10T15:49:58.902+0000");
}
```

## √ 教师表

[**CollectionName:SS_Teacher**](#SS_Teacher)

```javascript
{
    Rucode : string //"3408076" //学校组代码
    TeacherID : string //"30621020102" //教师编号
    TeacherName : string //"史妮娜" //教师姓名
    TeacherPhone : string //"15395118889" //教师手机号码
    TeacherRole : array [ 
        {
            Teacher_Grade : [], //管理年级，除校长和班主任外，必须设置该字段
            Teacher_Role: NumberInt(5),//角色 1 校长、2.年级组长、3.学科组长、4.班主任、5.授课老师
            Teacher_Subject: "语文"
            isSubject: boolean, //默认是false,管理年级设置后变为true
            isGrade: boolean //默认为false,管理年级设置后变为true
        },
    ],
    DepartmentMid : string // 学校部门 Mid,
    GroupMid : string //学校教研组 Mid,
    CreatedTiDateme : datetime  //ISODate("2017-11-10T15:58:03.181+0000") 创建时间
}
```

## √ 学生分组
[**CollectionName: SS_StudentGroup**](#SS_StudentGroup)

```javascript
{
    RuCode : string // 学校组织代码"3401006"
    StudentGroup_Enrollment_Year : string // 学生入学年份 "2017年"
    StudentGroup_GradeName : string // 年级段 "高中" G "高中" C "初中"  X "小学"
    StudentGroup_StudentCount : int // 分组学生数 ？创建分组添加学生后仍然为0，但是页面显示正常
    StudentGroup_Name : string //学生分组自定义名称
    SS_StudentGroup_Created_Time : datetime //学生分组创建时间 ISODate("2018-04-01 15:30:00")
}
```

## √ 学生表
[**CollectionName:SS_Student**](#SS_Student)

```javascript

{
    Rucode : string //"3408076"//学校组织代码
    StudentID : string //"40621020101" //学生学号
    StudentName : string // "李明洁" //学生姓名
    StudentPhone : string //"13300000187" //手机号码
    StudentCardId :  string  // 学生身份证号码
    StudentSex : string //"男" //性别
    StudentGroupMid : string //入学年份分组 Mid 关联 SS_StudentGroup
    StudentClassMid : string //学生原班级 Mid 关联 SS_StudentClass 添加学生会新创建一个原班级
    ICCard1 : string //学生IC卡卡号
    Created_Time : datetime //ISODate("2017-11-10T15:49:58.902+0000");// 数据创建时间
}

```

## √ 学期表

[**CollectionName: SS_Semester**](#SS_Semester)

```javascript
{
    Rucode : string, //"3401006" 学校组织代码
    SemesterName: String, // 学期名称
    StartDateTime：datetime, //学期开始时间 ISODate("2018-04-01 15:30:00")
    EndDateTime：datetime, //学期结束时间 ISODate("2018-04-01 15:30:00")
    SemesterStatus：int, //学期状态  过期0, 正常1
    SemesterCreateDateTime：datetime, //学期创建时间 ISODate("2018-04-01 15:30:00")
}
```

## √ 学生原班级信息
[**CollectionName:SS_StudentClass**](#SS_StudentClass)

```javascript
{
    ClassName : string //"1班级",
    HeadTeacherMid : string //"1231221112",
    StudentCount : int //NumberInt(55),
    CreateDateTime : ISODate //ISODate("2017-11-10T15:58:03.173+0000"), 创建时间
    StudentGroupMid : string "",
    ClassRoomMid : string //绑定教室Mid  添加学生没有这个字段，分班后添加这个字段
}
```

## √ 选课任务
[**CollectionName:SS_Choose_Subject_Task**](#SS_Choose_Subject_Task)

```javascript
{
	Choose_Subject_Task_Name : string //"国行原封", //选课任务名称
    SemesterMid : string //关联学期 Mid 
    StudentGroupMid : string //选课关联的哪一入学年份组下的学生
   	Choose_Subject_Task_Enrollment_Year : string //"2017年", //入学年份 ??没有使用该字段?
   	Choose_Subject_Task_Grad : string //"G", //高中/初中   ??没有使用该字段？
	Rucode : string //"3408076", //组织代码
	Choose_Subject_Status : int //选课任务状态 0 新建学科任务并发布 4 完成选课 5 设置分班 2 发布分班结果
	Choose_Subject_CreatedTime : ISODate //ISODate("2018-03-13T11:08:42.457Z"), //任务创建时间
    **************************************
	Choose_Subject_Task_Subject : array [
		"物理",
		"化学",
		"生物",
		"政治",
		"历史",
		"地理"
	],  //选课任务涉及的选课科目
	Choose_Subject_Task_Type : int //1, //选课类型 1自由组合 2 套餐组合
	Choose_Subject_Task_StartDateTime : string //"2017-11-20 10:12:00",//选课开始时间
	Choose_Subject_Task_EndDateTime : string //"2017-12-07 17:12:00",//选课任务结束时间
	Choose_Subject_Task_Package :  array //[
	],//选课组合套餐列表
	Choose_Subject_Task_Desc : string //"",//选课任务描述
    ******************************************
	Choose_Subject_Split : object //{  //设置分班信息后出现该字段
		Student_Number : object //{
			ExecutiveCourses : object //{ //行政班设置信息
				num : int //55, //行政班设置人数
				scope : array [ //行政班人数范围
					50,
					60
				]
			},
			commonclass: {  //教学班设置信息
				num: 55,   //教学班设置人数
				scope: [  //教学班人数范围
					50,
					60
				]
			}
		},//选课任务分班设置信息
		EndObj : array //[], //学考结束科目列表
		ClassGroup : array //[],//班级分组，每组之间独立分班
		IsSplit : int //0,//是否拆分行政班级 0 拆 1 不拆
         Pattern: int,//0 分班模式  1 减少走班 0 减少资源
         Plan: int //0 分班方案  3 固3 2 固2走1 1 固1走2
	}
```

## √ 学生选课信息
[**CollectionName:SS_SeleCourseResult**](#SS_SeleCourseResult)

```javascript
{
    Rucode : string //"3408076" //组织代码
    UserStudent_ID : string //"3010000001" //学生学号
    UserStudent_Name : string //"艾珂" //学生姓名
    UserStudentMID : string //"5a055c20705deb3b32d3bbde" //学生Mid
    Class : string //"1班" //学生原班级Mid
    Choose_Subject_Task_ID : string //"5a055c56705deb3b31d3bcab" //选课任务Mid
    result : array
    [
        {
            Subject : string //"物理"//科目
            Status : int // 1 //是否选课
            SS_Class_Info : object //{ // 分班完成后，出现此字段， 若未完成，则无此字段
                Group_Name : string //分组名称
                Class_Name : string //选课教学班分班名称
            }
        }, //提交选课结果无该字段,划分教学班后添加该字段
         
        ****************************
        {
            Subject : string //"化学"
            Status : int //1 选中为1 未选中为0
        },
        {
            Subject : string //"生物"
            Status : int //1
        },
        {
            Subject : string //"政治"
            Status : int //0
        },
        {
            Subject : string //"历史"
            Status : int //0
        },
        {
            Subject : string //"地理"
            Status : int //0,
            EndStatus : int //学考科目结束标识, 1 为结束; 选考科目无此字段
        },
        *******************************************
         {
            Subject : string  //"" 每个学生的选课信息添加该字段
            Status : 3,
            SS_Class_Info: {
                Group_Name: //分组名称
                Class_Name: //选课分班后自动分配名称
                Class_CheifTeacher: //班主任Mid
                ClassRoomMid: //行政班绑定教室Mid
            }
        }
        *******************//划分行政班后添加该字段信息
    ]
}
```

## √ 排课任务表信息
[**CollectionName:SS_Arranging**](#SS_Arranging)

```javascript
{
	Rucode : string //"3408076", //学校组织代码
	Choose_Subject_Task_ID : string //"5a055c56705deb3b31d3bcab", //选课任务Mid
	SS_Arranging_Type : int //0, //排课类型 0 走班排课 1 普通排课
	StudentGroupMid : string ,//关联的学生入学年份分组Mid
	SemesterMid : string //"", //关联的学期分组 Mid
	SS_Arranging_Name : string //排课任务自定义名称
	SS_Arranging_Status : int //排课任务状态  0 新建排课任务 1 排课发布
	SS_Arranging_CreatedTime : datetiem //ISODate("2017-11-10T16:01:05.720Z"),
	Resource_Settings : array //[ //资源设置 分班后每个科目的行政班和教学班信息 在创建排课任务时添加该字段
		{
			Subject : string //"语文", //科目
			week_period : int //默认是0 一周多少课时
			Status : int //状态区别 3 行政课,  选学考类型 0 学考科目 1 选考科目
			Settings : array //[ //每个班级信息和教师老师设置，可以有多个
			{
					classname : string //"1班",//班级名称
					subjecttype : int //3, //科目类型 3 行政科目 1 选考科目 0 学考科目
					containExecutivecourses : array[ //行政科目为空，学考选考则表示学生来自哪个行政班                        "_id": string, // '一班'
                           'count': int  // ''
                      ]
					period : int//该科目课时数，默认为0
					teachername : string //"张合荣",//老师名称
					teacherMid : string //"5a055c0b705deb3b2fd3bb15", //老师MID
					classroomMid : string //"59e6d09b705deb72706503ae", //教室MID
					classroom : string //"1001"  //教室名称
			} //
			],
			ForAclass : { //连堂设置 
				weekcount : int //一周几次连堂 默认是0
				num : int //连堂课时数 默认是0
			},
			SeniorSettings : array [
                1,   //教案平齐
                1    //课时分散
            ]  //高级设置 默认2个1
		},
	],
	Basic_Setting : {  //排课基本设置
		week_days : 7, //一周上几天课
		AM : 4, //上午课时数
		PM : 4, //下午课时数
		TimeAbout : [ //具体每节课上课时间
			{
				starttime : "08:00",
				endtime : "08:40"
			}
		]
	},
    "Unfixedprogram" : null,
    "Rule_Settings" : [ //排课规则设置
        {
            "ClassName" : [ 
                "1班"    //针对哪个班级设置规则
            ],
            "Subject" : "语文",   //针对哪个科目设置规则
            "Teacher" : "语一",   //针对哪个教师设置规则
            "Arranging_time" : [ 
                9,    //针对哪个节次设置规则 从一到每周最大节次数
                3
            ],
            "RuleType" : 0  // 0 禁止排课  1 优先排课  3 单双周 4合班 5 走班时间 6 跨年级
        }
        {
            "RuleValue" : [ //单双周规则格式
                [ 
                    {
                        "Type" : 0,
                        "Subject" : "语文"
                    }, 
                    {
                        "Type" : 0,
                        "Subject" : "数学"
                    }
                ]
            ],
            "RuleType" : 3
        }, 
        { //走班时间规则格式
            "RuleValue" : [ 
                1,  //课程节次
                2, 
                3, 
            ],
            "RuleType" : 5
        },
        {  //跨年级排课规则格式
            "RuleValue" : [ 
                {
                    "TaskName" : "班牌1点4", //排课任务id
                    "Mid" : "5bea4926705deb72209dc925", // 排课任务Mid
                    "Grade" : "2018年"
                }
            ],
            "RuleType" : 6  
        }
    ]
}
```

## √ 课表结果信息
[**CollectionName:SS_ArrangingResult**](#SS_ArrangingResult)
```javascript
{
	SS_Arranging_Mid : string //"5a055cc1705deb3b32d3bca6",//排课任务Mid
	Lessons : int //4,//第几课节
	Lessons_Status : int //1,正式课时 ,0,待排区课
	schedule : array [ //该课节上课的所有班级列表
				{
					classname : string, //"历史选考2班",//分班名称
					publicclass : array, // ["1班","2班"],//所包含的行政班级
					subject : string, //"历史",//科目
					teacher :  string, //"5a055c0b705deb3b2fd3bb29", //讲课教师Mid
					studentlist : array, //["5a055c20705deb3b32d3bbe3"],//上课学生mid列表
					classroomMid : string, //"59e6d09b705deb72706503af" //教室Mid
                      Status: int, // 0 学考  1 选考 3 行政
                      is_sdw: int  // 0 不是单双周 1 单双周 
				},
			]
}
```

## √ 考勤表

[**CollectionName:SS_AttendenceLog**](#SS_AttendenceLog)

```javascript

{
    StudentMid : string // 考勤学生的Mid
    StudentGroupMid : string //"考勤学生的GroupMid"
    AttendenceType : int //1 .正常  2.迟到 3.请假 4.旷课
    Lessons : int // 课节号
    Subject : string // "语文" 课节科目
    PublicClass : string // "行政班级"
    PunchDateTime : datetime // ISODate("2017-11-10T15:58:03.173+0000")//打卡时间
    CreateDateTime : datetime //ISODate("2017-11-10T15:58:03.173+0000") //记录生成时间
}

```

## √ 学生请假任务表

[**CollectionName:SS_StudentsLeaveTask**](#SS_StudentsLeaveTask)

```javascript
{
    Rucode : string // "3408076"//学校组织代码
    StudentMid : string //请假学生的Mid
    PublicCLass : string // 行政班级名称
    LeaveType : int //请假类型 1.事假、2.病假、3.其它
    LeaveStartDate : string  //"2018-04-01" 请假起始日期
    LeaveEndDate : string //"2018-04-02"  请假结束日期
    LeaveStartLesson : int // 1  请假的起始课节数
    LeaveEndLesson : int //1  请假的结束课节数
    LackLessons : int //8  从起始请假课节到结束请假课节总共的课节数
    LeaveReason : string // "家中有事！" 请假原因
    LeaveCreateDateTime : datetime //ISODate("2018-03-31 15:30:00") 请假申请创建时间
    LeaveTaskStatus : int //请假任务状态 0.默认审批中、1.同意、2.拒绝、3.撤回
    LeaveTaskRefuseReason : string //拒绝原因
    LeaveToTeacherMid : string //向谁请假（班主任的Mid）
    LeaveOperatingDatetime : datetime // ISODate("2018-04-01 15:30:00")请假操作时间
}
```


## √ 调课表
[**CollectionName: SS_AdjustSchedule**](#SS_AdjustSchedule)
```javascript
{
    ASProposer : string	//提交调课申请的教师的Mid
    Rucode  : string //学校组织代码
    ASFromMid	:	string	//	Mid ?? 申请调动课时
    ASFromSchedule ： Array[ ??
        {
            "classname" :String //"数学1班",
            "publicclass" : Array[   
                "1班"
            ],
            "subject" : String //"数学",
            "teacher" : String //"5ad87b36705deb53d881f6cd",
            "studentlist" : Array [ //"5ad85e4c705deb4d3b98c2d1", 学生Mid 
            ],
            "classroomMid" : String// "5ad87cbc705deb53d881f6ef" 教室Mid
        }, 
    ]
    ASFromLessonNum:	int		//	申请调课课节数
    ASStartDateTime:	datetime //	申请调课开始时间
    ASEndDateTime	: datetime //	申请调课结束时间
    ASCreatedDateTime: 	datetime //	申请调课的创建时间
    ASReason 	:	int		//	调课原因（1公差 2病假 3事假 4其他）
    ASReasonDesc:	string 	//	原因描述
    ASMethod	:	int 	//	申请调课方式（1调课 2教务安排）
    ASToMid	:		string	//	申请调动到课时
    ASToLessonNum:	int		//	申请调课到课节数
    ASStatus	:	int		//	调课任务状态（0处理中 1通过 2拒绝 3撤回）
    ASHandleMethod:	int	//		教务人员处理方式（1调课2代管课3上其他课程）
    ASHandleDateTime datetime   //处理时间
    ASToTeacher :	Array	//	调课老师（调课老师，代管课老师Mid）[{"teacher":0},{"teacher":0}]
    ASOtherSubject :	string// 其他课程（自习,或者其他课程Mid）
    ASRefuseReason : string  //   拒绝原因
    ASToSchedule: Array [ ??
        {
            "classname" : String //"数学1班",
            "publicclass" : Array [ //行政班  
                "1班"
            ],
            "subject" : String //"数学",
            "teacher" : String //"5ad87b36705deb53d881f6cd", 教师Mid
            "studentlist" : Array [ //"5ad85e4c705deb4d3b98c2d1",学生Mid 
            ],
            "classroomMid" : String //"5ad87cbc705deb53d881f6ef" 教室Mid
        }, 
    ]
}
```

## √ 通知消息表
[**CollectionName:SS_NMessage**](#SS_NMessage)


```javascript
{
    NMName : string //"通知消息名称"
    NMType : int //0//通知消息类型，0.请假、1.调课、2.选课
    NMContent : sting //"2018-01-05  周一第一节课 ~ 2018-01-05  周一第一节课已经同意，请注意查看" 通知消息内容
    NMSender : string //"系统发送"
    NMFromTaskMid : string // 具体是哪个任务触发的通知的Mid
    NMSendToObject : string // 消息发送对象,当为 ClassRoomMid 时发送给你班牌终端，当为StudentGroupMid时发送给所有学生
    NMCreatedDateTime : datetime //ISODate("2017-11-10T15:58:03.173+0000")，
    NMIsReadList : array // 此列表为已读该消息的 Mid
    NMStatus : int // 0 未读，1已读
}
```

## √ 留言

[**CollectionName: SS_Leavemessage**](#SS_Leavemessage)

```javascript
{
    Rucode : string //学校的组织代码
    LeavemessageContent : string // 留言内容
    LeavemessageFromPhone:  string//留言手机号码
    LeavemessageToObj:string //留言给学生的Mid
    LeavemessageStatus:int // 0 未读 1 已读
    LeavemessageCreatedTime : datetime//'2017-07-29'
}
```

## √ 教师课时日志

[**CollectionName:SS_LessonsLog**](#SS_LessonsLog)
```javascript
{
    Rucode：String //学校组织代码
    TeacherMid : String //老师的Mid
    Lessons : int // 课时，对应课表中的课时
    LessonsDesc : string //"上午-第一节课",//课时描述
    Subject : string //"语文",
    ClassRoomMid : string //教室的Mid,
    ClassName : string //"语文一班",  //班级名称
    CreateDateTime : datetime //ISODate("2017-11-10T15:58:03.173+0000") 创建时间
}
```

## √ 临时课表记录

[**CollectionName:SS_AdjustResultLog**](#SS_AdjustResultLog)

```javascript

{
    SS_Arranging_Mid : string //排课任务Mid
    ScheduleDate : datetime //调整日期 ISODate("2018-04-25T00:00:00.000+0000")
    Lessons : int // NumberInt(19), //调整的课节数
    schedule : array // [
        {
            classname : string //"数学1班",
            publicclass : array // ["1班"],
            subject : string //"数学",
            teacher : "5ad87b36705deb53d881f6cd",
            studentlist : array //["5ad85e4c705deb4d3b98c31f"],
            classroomMid : string //"5ad87cbc705deb53d881f6ef"
        }
    ]
}

```


## √ 终端机表

[**CollectionName:SS_Terminal**](#SS_Terminal)

```javascript

{
    Rucode : string //学校的组织代码
    TerminalUid : string //终端机账号 编号 Uid
    TerminalPassword : string // 教室对应的登录密码
    TerminalName : string //教室名称
    TerminalStatus : int //0 未登录 1 登录 2 离线
    BanPaiDeviceId : string //？？教室绑定班牌的设备Id 是否有用？
    TerminalCreatedTime : datetime//ISODate("2017-11-10T15:58:03.173+0000") 创建时间
}
```

## √ 终端内容
[**CollectionName: SS_TerminalCMS**](#SS_TerminalCMS)

```javascript
{
    Rucode : string //学校的组织代码
    TerminalCMSTitle : string //终端机标题
    TerminalCMSContent : string //终端机内容
    TerminalCMSNotifyScope : {//[Roomuid] 通知对象
        "Grade" : "X", //通知年级
        "EnrollmentYear" : "2018年", // 入学年份
        "checkArry" : [ 
            {
                "Year" : "2018年",
                "Grade" : "X",
                "classname" : "1班(shhshhnhnans)",
                "classroomMid" : "5bdfdc29705deb191fcfe21a"
            }
        ]
    }
    TerminalCMSType:int //0 通知、1 新闻、 2 班级风采、 3 校园风采
    TerminalCMSAuthor:string //发布者
    TerminalCMSStatus:int //0未读 1 已读
    TerminalCMSIMG:array [// 图片阿里云 oss路径列表
          {
            "imgUrl" : "http://seven-schedule-dev.oss-cn-qingdao.aliyuncs.com/cms/3408076/2383acd8c2a6f885a4bf4ced4a23506b.png", //图片oss url
            "content" : ""
        }
    ]    
    TerminalCMSCreatedTime : datetime//ISODate("2017-11-10T15:58:03.173+0000") 创建时间
}
```

## √ 院校信息表

[**CollectionName:SS_UniversityInfo**](#SS_UniversityInfo)

```javascript
Area:String //院校所在地区 
Rucode:String //学校组织代码 
SchoolName:String //学校名称 
EnrolWebsite:String //学校招生链接 (未展示-招生网址)
BelongsTo:String  //学校隶属 
WebSite:String //学校网址 (目前展示-学校网址)
Category:String //院校所属分类(["体育","军事","农业","医药","工科","师范","政法","林业","民族","综合","艺术","语言","财经","其它"])
Address:String //学校地址 
Email:String //学校邮箱 
Tel: String //学校电话
Level: String //学校层次("本科","高职(专科),独立院校")
Tags:Array //院校特色 ("985","211","一流大学建设高校","一流学科建设高校")
LogoUrl:String //图标链接 
```

## √ 科目限制表

[**CollectionName:SS_SubjectScope**](#SS_SubjectScope)

```javascript
Rucode:String //学校组织代码 
SchoolName:String //学校名称 
Level: String //'本科' 专业层次
ProfessionalType: String //专业(类)名称
Scope: Array //选考科目要求
ScoprStatus: Int //选考科目规则 0 不限 1 选一门即可报考 2 两门都选可报考 3 三门都选可报考
ScopeArea: Array[ //科目限制地区及年份
        {
            "Province" : "浙江省",
            "ScopeTime" : "2019"
        }
      ]
ProfessionalName: Array  // 类中所含专业
```

## √ 生涯规划问题表

[**CollectionName: SS_CareerQuestions**](#SS_CareerQuestions)

```javascript
CareerType: String //本题性格类型 ( 社会型(S),现实型(R),企业型(E),艺术型(A),常规型(C),研究型(I))
Question: String  // 测试题 
Yes : Int //本题选是时得分 0 否  1 是
```

## √ 热门专业表

[**CollectionName:SS_HotProfessional**](#SS_HotProfessional)

```javascript
Ranking: String  // 本类别中排名 
Name: String   // 专业名 
Professional: String // 专业类别 
TotalAttention: Int // 关注热度 
```

## √ 职业生涯测试报告表

[**CollectionName:SS_CareerReport**](#SS_CareerReport)

```javascript
StudentMid: String //学生Mid 
datetime: Date //创建时间 
CharaterType: String //"IAR" 性格类型 
CharacterValue: Array //性格能力数值 
    [ 
            {
                "careerType" : "社会型(S)", 
                "score" : 3, //测试得分
                "max" : 10  //雷达图的最大值
            }, 
            {
                "careerType" : "现实型(R)",
                "score" : 6,
                "max" : 10
            }, 
            {
                "careerType" : "企业型(E)",
                "score" : 6,
                "max" : 10
            }, 
            {
                "careerType" : "艺术型(A)",
                "score" : 6,
                "max" : 10
            }, 
            {
                "careerType" : "常规型(C)",
                "score" : 2,
                "max" : 10
            }, 
            {
                "careerType" : "研究型(I)",
                "score" : 7,
                "max" : 10
            }
    ]
DataFromArea: String //数据来源省份 
schoolCount: Int //可选院校数量 
SubjectInterest: Array [ // 学科兴趣排名 (考生生源地如果是浙江则有"技术"课程)
        "历史", 
        "地理", 
        "政治", 
        "物理", 
        "生物", 
        "化学"]
```

