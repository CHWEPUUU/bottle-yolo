<template>
  <el-aside  width="250px" style="background-color: rgb(22, 38, 65)">
    <!-- 菜单 -->
    <el-menu background-color="rgb(22, 38, 65)"
            text-color="#fff">
      <!-- 添加图片 -->       
      <img src="../assets/logo.png" class="img">

      <el-menu-item index="1" @click="profile()"><i class="el-icon-user-solid"></i><span slot="title">个人资料</span></el-menu-item>
      <el-menu-item index="2" @click="users()" v-if="role"><i class="el-icon-s-custom"></i><span slot="title">用户</span></el-menu-item>
      <el-menu-item index="3" @click="modelInfo()"><i class="el-icon-info"></i><span slot="title">模型</span></el-menu-item>
      <el-menu-item index="4" @click="download()"><i class="el-icon-download"></i><span slot="title">下载</span></el-menu-item>
      <el-menu-item index="5" @click="home()"><i class="el-icon-s-home"></i><span slot="title">主页</span></el-menu-item>
     
    </el-menu>
  </el-aside>
</template>

<script>
export default {
  name: 'WelAside',
  data(){
    return {
      role: false
    }
  },
  methods: {
    profile(){
      this.$router.push({path:'/profile'})
    },
    users(){
      this.$router.push({path:'/users'})
    },
    modelInfo(){
      this.$router.push({path:'/modelInfo'})
    },
    download(){
      this.$router.push({path:'/download'})
    },
    home(){
      this.$router.push({path:'/home'})
    }
  },

	mounted(){
    if(sessionStorage.getItem('role') === "ADMIN"){
      this.role = true
    }
  },
}
</script>

<style lang="scss" scoped>
  //子菜单元素选择  
  // .el-menu-item.is-active {
  //   background-color: #134668 !important;
  // }
  //子菜单元素悬停
  .el-menu-item:hover {
    background-color: #141414 !important;
  }

  .img{
    background-color: rgb(78, 1, 7);
    width: 100%;
    height: 100%;
  }

</style>