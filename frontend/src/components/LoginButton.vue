<template>
    <div>
        <el-button type="success" @click="form.guest = 'guest';login(form)" style="margin-left: -45px">以游客身份浏览</el-button>  
        <el-button type="primary" @click="form.guest = '';login(form)" >登录</el-button>    
    </div>
  
</template>

<script>
import {mapActions} from 'vuex'
export default {
    name: "LoginButton",
    data() {
        return {
            form: {
                username: '',
                password: '',
                guest:''
            },   
        }
    }, 
 
    methods: {
        ...mapActions('user',['login']),

    },   
    mounted() {
        //挂载前先获取数据
        this.$bus.$on('loginInfo',(data)=>{
            this.form = data    
		})
    }

}
</script>

<style lang="scss" scoped>

</style>