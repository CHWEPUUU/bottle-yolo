<template>
  <div>
    <span style="color: #409EFF">你好：{{username}}</span>

    <el-link :underline="false" @click="clear()" style="padding:0px 0px 0px 10px"><i class="el-icon-error"></i>退出</el-link>

    <!-- 弹窗 -->
    <DialogAddStu></DialogAddStu>
    <DialogAddCou></DialogAddCou>     
  </div>
</template>

<script>
import DialogAddStu from './DialogAddStu.vue'
import DialogAddCou from './DialogAddCou.vue'
export default {
  name: 'WelHeader',
  data() {
    return{
      username:sessionStorage.getItem('username')
    }
  },
  components: {
    DialogAddStu,
    DialogAddCou
  },
  methods: {
    showDialog1() {
      this.$bus.$emit('dialogFormVisible1',true)
    },
    showDialog2() {
      this.$bus.$emit('dialogFormVisible2',true)
    },
    clear() {
      sessionStorage.clear();
      window.location.href = '/';
    }
  }
}
</script>

<style lang="scss" scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
</style>