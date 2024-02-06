<template>
  <div>
    <span>修改用户名</span>
    <div class="username">
        <el-input v-model="change_username"></el-input>        
    </div>

    <span>更改密码</span>
    <div class="passwd">
     <el-input v-model="passwd" show-password></el-input>        
    </div>
    <div style="padding-bottom: 25px">如果您不想更改密码，请保持为空</div>

    <el-button type="primary" @click="update()">保存</el-button>
  </div>
</template>

<script>
export default {
    name: 'Profile',
    data() {
        return {
            username: sessionStorage.getItem('username'),
            change_username:sessionStorage.getItem('username'),
            passwd: sessionStorage.getItem('passwd'),
            // change_passwd:''
        }
    },
    methods: {
        update() {
            this.$axios.post('/updateProfile', {
                username:this.username,
                change_username:this.change_username,
                passwd:this.passwd,
            }).then(response => {
                console.log(response.data)
                this.$router.push({path:'/'})
                sessionStorage.setItem('state',false)
                },error => {
                console.log(error.message)
            })     
        }
    },
}
</script>

<style lang="scss" scoped>
    .username {
        width: 200px;
        padding-bottom: 25px;
    }
    .passwd {
         width: 400px;
    }
</style>