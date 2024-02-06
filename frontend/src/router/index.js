// 该文件专门用于创建整个应用的路由器
//npm i vue-router@3
import VueRouter from 'vue-router'
//引入组件
import StudentList from '../pages/StudentList'
import CourseList from '../pages/CourseList'
import StudentInfo from '../pages/StudentInfo'
import Home from '../pages/Home'
import Manage from '../pages/Manage'
import Login from '../pages/Login'
import CourseInfo from '../pages/CourseInfo'
import Profile from '../pages/PersonalProfile'
import Users from '../pages/Users'
import Download from '../pages/Download'
import ModelInfo from '../pages/ModelInfo'

//创建并暴露一个路由器
const router = new VueRouter({
	//没有#号
	mode:'history',
	routes:[
		{
			//先进入登录页
			path:'/',
			component:Login
		},
		{
			//欢迎页 主容器 导航栏
			path:'/home',
			component:Home,
		},
		{
			//欢迎页 主容器 导航栏
			path:'/Manage',
			component:Manage,
			//包含副容器 显示区
			children:[
				{
					path:'/profile',
					component:Profile,
				},
				//多级路由用name指定
				{
					path:'/users',
					component:Users,
				},
				{
					path:'/modelInfo',
					component:ModelInfo
				},			
				{
					path:'/download',
					component:Download
				}		
			]
		},
				
	]
})

//全局路由守卫
router.beforeEach((to,from,next) =>{
	//默认进入登录页
	if(to.path === '/')
		next()
	//判断是否登录
	else{
		//如果登录 放行
		if(sessionStorage.getItem('state') == 'true')
			next()
		//否则进入登录页
		else
			next("/")	
	}	
})

export default router

