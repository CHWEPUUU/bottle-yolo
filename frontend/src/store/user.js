//引入Vue
import Vue from 'vue'
//引入路由
import VueRouter from 'vue-router'
import router from '../router'
Vue.use(VueRouter)

export default {
    namespaced:true,
    //响应组件中的动作 迎宾业务逻辑
    actions:{
        login(context,value){
            //登录
            Vue.prototype.$axios.post('/login',{
                username: value.username,
                password: value.password,
                guest: value.guest
            }).then(
                response => {
                    if(response.data.includes( "successful")){
                        //先存放再重定位
                        sessionStorage.setItem('state',true)
                        sessionStorage.setItem('username',value.username)
                        sessionStorage.setItem('passwd',value.password)
                        sessionStorage.setItem('role',response.data.split("/")[1])

                        context.commit('LOGIN',value.username)

                        router.push("/home").catch(()=>{})  
                    }else if(response.data === "failed"){
                        Vue.prototype.$message.error('您输入的账号或密码错误，请重新输入！');
                    }else if(response.data === "banned"){
                        Vue.prototype.$message.error('该账号被禁用，请联系管理员！');
                    }else if(response.data === "guest"){
                        window.location.href = 'http://localhost:7860'
                    }
                },
                error => {
                    console.log(error.message)
                }
            )
        },          
        
    },
    //操作数据
    mutations:{
        LOGIN(state,value){
            state.username = value
            // state.password = value.password
        } 
    },
    //存储数据
    state:{
        username:'',
        password:'',       
    },
    //加工数据
    getters:{
        
    }
}