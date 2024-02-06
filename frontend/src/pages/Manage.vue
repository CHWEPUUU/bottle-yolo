<template>
  <el-container style="height: 800px; border: 1px solid #eee">
    <!-- 左侧 -->
    <WelAside></WelAside>

    <el-container>
      <el-header height="55px" style="text-align: right; font-size: 25px; background-color:rgb(22, 38, 65)">
        <!-- 头部 -->
        <WelHeader></WelHeader>    
      </el-header>    
      <el-main>
          <!-- 主容器内容 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import WelAside from '../components/WelAside.vue'
import WelHeader from '../components/WelHeader.vue'
export default {
  name:'manage',
  data() {
      return {}
  },
  components:{
    WelAside,
    WelHeader
  }
};
</script>

<style lang="scss">
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  //子菜单悬停
  .el-submenu .el-submenu__title:hover{
    background-color: #04121d !important;
    color: #ffd04b !important;
  }

</style>