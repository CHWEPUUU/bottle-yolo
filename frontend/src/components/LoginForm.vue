<template>
  <div>
    <div class="form">
        <el-form label-position="top" label-width="80px" :model="form"
                :rules="rules">
            <div class="login-title">账号</div>
            <!-- prop用于规则rules -->
            <el-form-item class="item" prop="username">
                <el-input v-model="form.username" placeholder="请输入姓名" @blur="sendInfo()"></el-input>
            </el-form-item>
            <div class="login-title">密码</div>
            <el-form-item class="item" prop="password">
                <!-- 失去焦点把数据发给LoginButton组件 -->
                <el-input v-model="form.password" placeholder="请输入学号" show-password
                        @blur="sendInfo()"></el-input>
            </el-form-item>
        </el-form>

        <LoginButton class="btn"></LoginButton>
    </div> 
  </div>
</template>

<script>
import LoginButton from './LoginButton.vue'

export default {
    name: "LoginForm",
    components: {
        LoginButton
    },
    data() {
        return {
            form: {
                username: 'admin',
                password: '123',
            },
            //表单验证，需要在 el-form-item 元素中增加 prop 属性
            rules: {
                username: [
                    {required: true, message: '账号不可为空', trigger: 'blur'}
                ],
                password: [
                    {required: true, message: '密码不可为空', trigger: 'blur'}
                ]
            }
        }
    },
    methods: {
        //全局事件总线
        sendInfo() {
            this.$bus.$emit('loginInfo',this.form)
        }
    }
}
</script>

<style lang="scss" scoped>
    .form{
        width: 350px;
        height: 350px;
        margin: 0 auto;
        text-align: center;
        border: #1a52c0 3px solid;
        border-radius: 10px;
        margin-top: 10%;
        box-shadow: 0 0 25px #909399;
        
        .login-title{
            text-align: center;
            font-size: 25px;
            margin-top: 5%;
            margin-bottom: 4%;
        } 
        
        .item {
            width: 200px;
            margin: 0 auto;
            margin-bottom: 10%;        
        }

        .btn{
            width: 150px;
            height: 40px;
        }
    }

</style>